# Report contract

Deliver `FHIR-<Resource>-Chimney-Sweep-<date>.md` and the same stem `.docx`.
The builder reads JSON, validates required coverage and cross-references, and
renders one shared ordered content model into both formats. It does not conduct
the review or verify whether the evidence is true. Keep `review.json` and any
logs as working evidence; the two reports are the default user deliverables.

## Input

Run `build_report.py --example` to print a **synthetic** worked input. It is a
format demonstration, not FHIR evidence. Do not carry its findings into a report.
All prose fields are plain text (not Markdown or HTML). `replacement` can contain
multiline exact prose, XML, JSON, FSH, or a bounded owner decision when an exact
replacement cannot yet be supported. Do not include secrets or patient data.

The JSON object contains exactly these keys:

- `resource`, `fhir_version`, `package`, `build_url`, `source_revision`,
  `review_date` (YYYY-MM-DD), `scope`, `summary`, `recommendation` (strings).
  Use an explicit "Unavailable: <reason>" for unknown revision/package metadata.
- `limitations`: list of strings; empty only when no limitations were identified.
- `sources`: objects with `id`, `title`, `url`, `version`, `locator` strings.
  URLs must be HTTP(S), preferably exact official pages/anchors or immutable
  repository links. The locator identifies a section, element, or source line.
  Source entries for local-only evidence may link to its official upstream and
  explain the local snapshot in `version`/`locator`; do not fabricate a URL.
- `inventory`: objects with `area`, `artifact`, `status`, `note`, `source_ids`,
  `finding_ids`. Areas: `Documentation`, `Examples`, `Module`, `Cross-layer`.
  Status: `reviewed`, `not-reviewed`, `excluded`. The two ID fields are lists of
  strings. Include at least one row for each of the first three areas. If no
  module applies, make an excluded Module row with the search/rationale.
- `findings`: objects with `id`, `area`, `kind`, `priority`, `title`, `location`,
  `evidence`, `source_ids`, `proposed_change`, `replacement`, `rationale`,
  `validation`, `dependencies`, `decision`. All are strings except `source_ids`
  and `dependencies` (ID lists). `kind`: `Correction`, `Suggestion`, `Question`,
  `Missing example`. Priority: `P1`, `P2`, `P3`. P1 requires a Correction.
  Missing-example findings use Examples and describe scenario/minimum content
  in `replacement`. Cite evidence even for suggestions or coverage gaps.
- `checks`: objects with `name`, `status`, `details`. Include named checks
  `FHIR validator`, `Publisher`, `Terminology`, `Semantic review`, `DOCX visual QA`.
  Status: `passed`, `failed`, `not-run`, `not-applicable`. Give actual versions,
  commands, log locations, reviewed artifacts, or why unavailable in `details`.
  Set DOCX visual QA to not-run until rendering and inspection happen; update
  the JSON, regenerate both, and inspect the final DOCX before claiming passed.
- `acceptance`: list of actionable check strings for closing findings and
  reassessing the final pinned revision. These remain pending reviewer checks,
  not a claim that source changes were made.

Recommendation values:

- `Changes required` when demonstrated corrections remain.
- `No material inconsistencies identified` only within stated scope, with no
  corrections/questions or failed checks, a passed semantic review, and no
  unreviewed inventory entries.
  This wording is not "FHIR conformant" or "ready for publication".
- `Incomplete review` when material coverage or evidence is missing. Any
  not-reviewed inventory item requires this recommendation. Exclusions must be
  explicit and justified; do not use them to hide inaccessible in-scope content.

Empty findings are allowed. Do not create filler findings to complete sections.
All source/finding IDs must resolve and be unique; dependency cycles are rejected.
Inventory omissions, human evidence accuracy, and clinical validity still need
reviewer judgment; schema checks cannot establish completeness by themselves.

## Output layout

One consolidated report per resource, with: recommendation/build identity and
triage; scope and method; review inventory; documentation changes; example
changes; module changes; cross-layer changes; suggested missing examples;
verification performed; acceptance checklist; limitations and human decisions;
and sources. Findings use labeled paragraphs rather than enormous table cells.
Inventory uses compact comparable columns followed by evidence/notes. Finding
IDs and source IDs are identical in both files. Source URLs are clickable.

The Word design uses the compact-reference-guide page/type rhythm: Letter,
1-inch margins, Calibri 11 pt, 1.25 line spacing, blue real heading styles,
repeating table headers, and page numbers. Named overrides: title 23 pt navy;
code 9 pt Courier New/single-spaced; table and metadata 9 pt/1.10; source links
9 pt/1.10. This retains the earlier review's practical structure without making
its historical findings, exclusions, or "not ready" verdict universal rules.

## Rendering

Use an available host DOCX renderer and inspect every page. Portable fallback:

```sh
python /absolute/path/to/skill/scripts/render_report.py /absolute/path/to/report.docx --out-dir /absolute/path/to/new-qa-directory
```

This needs LibreOffice (`soffice`, or `--soffice /absolute/path/to/soffice`) and
Poppler's `pdftoppm`. It uses an isolated temporary LibreOffice profile, a fresh
output directory, a timeout, and argument lists rather than a shell. It renders
page PNGs but **does not visually inspect them**. Rendering logs and page images
are internal QA, not additional deliverables unless requested. In Codex use the
host's `render_docx.py` when supplied; the fallback supports Claude and other hosts.

If rendering tools are absent, structurally inspect the DOCX zip, headings,
links, table geometry, and Markdown/Word content parity; record visual QA as
not-run and disclose this on handoff. Do not install tools globally without
permission. Failures other than missing tools should be diagnosed, not treated
as a passed or waived render.
