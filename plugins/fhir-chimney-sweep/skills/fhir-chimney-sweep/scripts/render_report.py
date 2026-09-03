#!/usr/bin/env python3
"""Portable DOCX-to-PNG rendering; page images still require human inspection."""
import argparse
from pathlib import Path
import shutil
import subprocess
import tempfile


def render(source, out_dir, soffice=None):
    source, out_dir = Path(source).resolve(), Path(out_dir).resolve()
    if not source.is_file() or source.suffix.lower() != '.docx':
        raise ValueError('Input must be an existing DOCX file')
    office = soffice or shutil.which('soffice')
    poppler = shutil.which('pdftoppm')
    if not office or not poppler:
        raise FileNotFoundError('Rendering requires LibreOffice/soffice and Poppler/pdftoppm; visual QA was not performed')
    if out_dir.exists():
        raise FileExistsError('Choose a fresh QA directory to prevent stale page images')
    out_dir.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.sweep-render-', dir=out_dir.parent) as staging, tempfile.TemporaryDirectory(prefix='sweep-office-') as profile:
        stage = Path(staging)
        result = subprocess.run([str(office), '--headless', '-env:UserInstallation=' + Path(profile).as_uri(),
                                 '--convert-to', 'pdf', '--outdir', str(stage), str(source)],
                                capture_output=True, text=True, timeout=90)
        pdf = stage / (source.stem + '.pdf')
        if result.returncode or not pdf.is_file() or not pdf.stat().st_size:
            raise RuntimeError('LibreOffice conversion failed: ' + result.stderr + result.stdout)
        subprocess.run([poppler, '-png', '-r', '120', str(pdf), str(stage / 'page')],
                       capture_output=True, text=True, timeout=90, check=True)
        if not list(stage.glob('page-*.png')):
            raise RuntimeError('Rendering produced no page PNGs')
        if out_dir.exists():
            raise FileExistsError('QA directory was created during rendering; choose another directory')
        stage.rename(out_dir)
    return sorted(out_dir.glob('page-*.png'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('docx', type=Path)
    parser.add_argument('--out-dir', type=Path, required=True)
    parser.add_argument('--soffice', help='Path to a trusted LibreOffice executable')
    args = parser.parse_args()
    try:
        pages = render(args.docx, args.out_dir, args.soffice)
        print(f'Rendered {len(pages)} pages in {args.out_dir}. Inspect every page; rendering is not visual approval.')
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as exc:
        parser.exit(1, f'Render error: {exc}\n')


if __name__ == '__main__':
    main()
