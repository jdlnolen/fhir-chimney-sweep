import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile
from xml.etree import ElementTree as ET

from docx import Document

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "plugins/fhir-chimney-sweep/skills/fhir-chimney-sweep"
spec = importlib.util.spec_from_file_location("report", SKILL / "scripts/build_report.py")
report = importlib.util.module_from_spec(spec)
spec.loader.exec_module(report)


class ReportTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((SKILL / "assets/example-review.json").read_text())

    def test_example_and_real_docx_parity(self):
        with tempfile.TemporaryDirectory() as folder:
            md, docx = report.write_reports(self.data, Path(folder))
            self.assertIn("SYNTHETIC", md.read_text())
            with zipfile.ZipFile(docx) as z:
                root = ET.fromstring(z.read("word/document.xml"))
                ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
                actual = [e.text or "" for e in root.findall(".//w:t", ns)]
                self.assertEqual(actual, report.visible_texts(report.content_blocks(self.data)))
                self.assertIn(b"https://example.org", z.read("word/_rels/document.xml.rels"))
                self.assertTrue(root.findall(".//w:tblHeader", ns))
                for table in root.findall(".//w:tbl", ns):
                    widths = [int(e.attrib['{' + ns['w'] + '}w']) for e in table.findall("w:tblGrid/w:gridCol", ns)]
                    self.assertEqual(sum(widths), 9360)
                    self.assertEqual(table.find("w:tblPr/w:tblW", ns).attrib['{' + ns['w'] + '}w'], "9360")
                finding = next(p for p in Document(docx).paragraphs if p.text.startswith('EX-01 |'))
                self.assertEqual(finding.style.name, 'Heading 3')
            self.assertEqual(len(list(Path(folder).iterdir())), 2)

    def test_findings_are_grouped_by_classification_area_and_number(self):
        def finding(identifier, area, classification):
            item = copy.deepcopy(self.data['findings'][0])
            item['id'] = identifier
            item['area'] = area
            item['change_classification'] = classification
            item['dependencies'] = []
            return item

        self.data['findings'] = [
            finding('D10', 'Documentation', 'Minor fix'),
            self.data['findings'][1],
            finding('E03', 'Examples', 'Minor fix'),
            self.data['findings'][0],
            finding('D02', 'Documentation', 'Minor fix'),
        ]
        headings = [block for block in report.content_blocks(self.data) if block[0] in ('h1', 'h2', 'h3')]
        start = headings.index(('h1', 'Must fix (implementation or testing impact)'))
        self.assertEqual(headings[start:start + 10], [
            ('h1', 'Must fix (implementation or testing impact)'),
            ('h2', 'Examples findings'),
            ('h3', 'EX-01 | P1 | Correction: Required status is absent (synthetic)'),
            ('h1', 'Minor fix'),
            ('h2', 'Documentation findings'),
            ('h3', 'D02 | P1 | Correction: Required status is absent (synthetic)'),
            ('h3', 'D10 | P1 | Correction: Required status is absent (synthetic)'),
            ('h2', 'Examples findings'),
            ('h3', 'E03 | P1 | Correction: Required status is absent (synthetic)'),
            ('h1', 'Net new addition'),
        ])
        self.assertIn('#### EX-01 \\| P1 \\| Correction:', report.render_markdown(report.content_blocks(self.data)))

    def test_no_overwrite_or_partial_output(self):
        with tempfile.TemporaryDirectory() as folder:
            md, docx = report.write_reports(self.data, Path(folder))
            original = md.read_bytes(), docx.read_bytes()
            with self.assertRaises(FileExistsError):
                report.write_reports(self.data, Path(folder))
            self.assertEqual(original, (md.read_bytes(), docx.read_bytes()))

    def test_all_three_surfaces_required(self):
        self.data['inventory'] = [x for x in self.data['inventory'] if x['area'] != 'Module']
        with self.assertRaisesRegex(ValueError, 'Module'):
            report.validate_report(self.data)

    def test_unreviewed_cannot_be_complete(self):
        self.data['inventory'][0]['status'] = 'not-reviewed'
        with self.assertRaisesRegex(ValueError, 'Incomplete review'):
            report.validate_report(self.data)

    def test_no_clean_verdict_with_corrections(self):
        self.data['recommendation'] = 'No material inconsistencies identified'
        with self.assertRaisesRegex(ValueError, 'recommendation'):
            report.validate_report(self.data)

    def test_unknown_source_and_finding_ids(self):
        for field, entry in [('source_ids', 'unknown-source'), ('finding_ids', 'unknown-finding')]:
            data = copy.deepcopy(self.data)
            data['inventory'][0][field] = [entry]
            with self.assertRaisesRegex(ValueError, 'Unknown'):
                report.validate_report(data)

    def test_duplicate_ids_and_dependency_cycle(self):
        data = copy.deepcopy(self.data)
        data['findings'].append(data['findings'][0])
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            report.validate_report(data)
        self.data['findings'][0]['dependencies'] = [self.data['findings'][0]['id']]
        with self.assertRaisesRegex(ValueError, 'cycle'):
            report.validate_report(self.data)

    def test_suggestions_are_not_blockers(self):
        self.data['findings'][0]['kind'] = 'Suggestion'
        with self.assertRaisesRegex(ValueError, 'P1'):
            report.validate_report(self.data)

    def test_change_classification_is_validated(self):
        self.data['findings'][0]['change_classification'] = 'Critical'
        with self.assertRaisesRegex(ValueError, 'change classification'):
            report.validate_report(self.data)
        self.data = json.loads((SKILL / "assets/example-review.json").read_text())
        self.data['findings'][1]['change_classification'] = 'Minor fix'
        with self.assertRaisesRegex(ValueError, 'Net new'):
            report.validate_report(self.data)

    def test_safe_metadata_and_urls(self):
        for key, value in [('resource', '../escape'), ('review_date', '2026-02-30'), ('build_url', 'javascript:alert(1)')]:
            data = copy.deepcopy(self.data)
            data[key] = value
            with self.assertRaises(ValueError):
                report.validate_report(data)
        self.data['sources'][0]['url'] = 'file:///etc/passwd'
        with self.assertRaises(ValueError):
            report.validate_report(self.data)

    def test_checks_and_plain_text_escaping(self):
        self.data['summary'] = 'Literal *text* | <tag> [x] `x`'
        blocks = report.content_blocks(self.data)
        md = report.render_markdown(blocks)
        self.assertIn(r'\*text\*', md)
        self.assertIn('&lt;tag&gt;', md)
        self.data['checks'] = []
        with self.assertRaisesRegex(ValueError, 'checks'):
            report.validate_report(self.data)

    def test_empty_findings_do_not_manufacture_defects(self):
        self.data['findings'] = []
        for row in self.data['inventory']:
            row['finding_ids'] = []
        self.data['recommendation'] = 'No material inconsistencies identified'
        report.validate_report(self.data)
        self.assertIn('No findings recorded', report.render_markdown(report.content_blocks(self.data)))

    def test_all_required_finding_fields(self):
        for key in list(self.data['findings'][0]):
            data = copy.deepcopy(self.data)
            del data['findings'][0][key]
            with self.assertRaises(ValueError, msg=key):
                report.validate_report(data)

    def test_failed_check_prevents_clean_recommendation(self):
        self.data['findings'] = []
        for row in self.data['inventory']:
            row['finding_ids'] = []
        self.data['recommendation'] = 'No material inconsistencies identified'
        self.data['checks'][0]['status'] = 'failed'
        with self.assertRaises(ValueError):
            report.validate_report(self.data)

    def test_clean_recommendation_requires_semantic_review(self):
        self.data['findings'] = []
        for row in self.data['inventory']:
            row['finding_ids'] = []
        self.data['recommendation'] = 'No material inconsistencies identified'
        next(c for c in self.data['checks'] if c['name'] == 'Semantic review')['status'] = 'not-run'
        with self.assertRaises(ValueError):
            report.validate_report(self.data)

    def test_failed_pair_publish_rolls_back_only_own_output(self):
        with tempfile.TemporaryDirectory() as folder:
            import os
            original_link = os.link
            calls = []

            def racing_link(source, target):
                calls.append(target)
                if len(calls) == 2:
                    Path(target).write_bytes(b'other writer')
                original_link(source, target)

            with patch.object(report.os, 'link', side_effect=racing_link):
                with self.assertRaises(FileExistsError):
                    report.write_reports(self.data, Path(folder))
            self.assertFalse(calls[0].exists())
            self.assertEqual(calls[1].read_bytes(), b'other writer')


if __name__ == '__main__':
    unittest.main()
