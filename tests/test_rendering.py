import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'plugins/fhir-chimney-sweep/skills/fhir-chimney-sweep/scripts/render_report.py'
spec = importlib.util.spec_from_file_location('render', SCRIPT)
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


class RenderingTests(unittest.TestCase):
    def test_missing_tools_do_not_create_output(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / 'input.docx'
            source.touch()
            with patch.object(renderer.shutil, 'which', return_value=None):
                with self.assertRaises(FileNotFoundError):
                    renderer.render(source, root / 'qa')
            self.assertFalse((root / 'qa').exists())

    def test_timeout_leaves_retry_possible(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / 'input.docx'
            source.touch()
            with patch.object(renderer.shutil, 'which', return_value='/fake/tool'), patch.object(renderer.subprocess, 'run', side_effect=subprocess.TimeoutExpired('soffice', 90)):
                with self.assertRaises(subprocess.TimeoutExpired):
                    renderer.render(source, root / 'qa')
            self.assertFalse((root / 'qa').exists())

    def test_existing_qa_not_overwritten(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / 'input.docx'
            source.touch()
            (root / 'qa').mkdir()
            with patch.object(renderer.shutil, 'which', return_value='/fake/tool'):
                with self.assertRaises(FileExistsError):
                    renderer.render(source, root / 'qa')


if __name__ == '__main__':
    unittest.main()
