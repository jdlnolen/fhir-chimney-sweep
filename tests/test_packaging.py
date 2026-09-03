import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins/fhir-chimney-sweep'


class PackagingTests(unittest.TestCase):
    def test_two_native_manifests_share_payload(self):
        codex = json.loads((PLUGIN / '.codex-plugin/plugin.json').read_text())
        claude = json.loads((PLUGIN / '.claude-plugin/plugin.json').read_text())
        for key in ('name', 'version', 'repository', 'license'):
            self.assertEqual(codex[key], claude[key])
        self.assertEqual(codex['name'], PLUGIN.name)
        self.assertTrue((PLUGIN / codex['skills'] / 'fhir-chimney-sweep/SKILL.md').is_file())
        self.assertFalse((PLUGIN / '.mcp.json').exists())
        self.assertFalse((PLUGIN / 'hooks').exists())

    def test_marketplaces_resolve_inside_repository(self):
        for path in ('.agents/plugins/marketplace.json', '.claude-plugin/marketplace.json'):
            data = json.loads((ROOT / path).read_text())
            self.assertEqual(data['name'], 'fhir-chimney-sweep')
            self.assertEqual(len(data['plugins']), 1)
            entry = data['plugins'][0]
            source = entry['source']
            if isinstance(source, dict):
                self.assertEqual(source['source'], 'local')
                source = source['path']
                self.assertEqual(entry['policy']['installation'], 'AVAILABLE')
            self.assertEqual((ROOT / source).resolve(), PLUGIN.resolve())

    def test_packaged_references_are_self_contained(self):
        import re
        for path in (PLUGIN / 'skills').rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                dest = (path.parent / target).resolve()
                self.assertTrue(dest.is_relative_to(PLUGIN.resolve()), target)
                self.assertTrue(dest.is_file(), target)
        for path in PLUGIN.rglob('*'):
            self.assertFalse(path.is_symlink(), str(path))


if __name__ == '__main__':
    unittest.main()
