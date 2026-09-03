# FHIR-chimney-sweep

A shared Codex and Claude Code plugin for **FHIR resource continuity reviews**.
For one resource, it checks:

1. Resource documentation (scope, usage, boundaries, and notes) against the
   resource structure and element definitions.
2. Examples for conformance issues, semantic consistency, narrative agreement,
   reference integrity, and useful coverage.
3. Relevant module or IG overview pages, including diagrams and workflow descriptions.

Every run produces **one Markdown report and one matching Word report** containing
the proposed changes, evidence, replacement wording or element-level edits,
optional readability suggestions, missing-example proposals, and acceptance checks.
The review does not edit FHIR source or submit tickets.

This is an independent community tool, not an official HL7 publication or
conformance certification. FHIR is a registered trademark of HL7 International.

## Sample report: Observation

See a completed whole-resource sweep in [Markdown](plugins/fhir-chimney-sweep/skills/fhir-chimney-sweep/references/sample-reports/observation-2026-09-03/FHIR-Observation-Chimney-Sweep-2026-09-03.md)
or download the matching [Word report](plugins/fhir-chimney-sweep/skills/fhir-chimney-sweep/references/sample-reports/observation-2026-09-03/FHIR-Observation-Chimney-Sweep-2026-09-03.docx).

The **September 3, 2026 Observation review** covers documentation, structure and
definitions, examples, and six relevant module pages. Its 54 findings comprise
34 corrections, 11 owner questions, three optional suggestions, and six
missing-example proposals. It demonstrates the inventory, evidence links,
proposed edits, decision gates, and acceptance checks included in both formats.

This is a **dated sample, not a current validation result or publication approval**.
It reviews `hl7.fhir.r6.core#6.0.0-ballot4` at source revision
`09dfb700767aa757dd405d56c62bf41c5007e0f0`; future sweeps must resolve their own
build and recheck the evidence. Formal FHIR validation, comprehensive terminology
validation, and a fresh Publisher build were not run. All 49 Word pages were
visually checked when the report was produced.

Both files are bundled inside the shared skill, so they travel with either
host's plugin installation. See the [sample notes](plugins/fhir-chimney-sweep/skills/fhir-chimney-sweep/references/sample-reports/observation-2026-09-03/README.md)
for provenance and limitations. The small synthetic `--example` fixture below
remains separate; it is for testing report generation, not a real-resource review.

## Install

### Codex

```sh
codex plugin marketplace add https://github.com/jdlnolen/fhir-chimney-sweep
codex plugin add fhir-chimney-sweep@fhir-chimney-sweep
```

Start a new task and use:

```text
Use $fhir-chimney-sweep to review Observation in the current FHIR build.
Produce the Markdown and Word reports in my chosen output directory.
```

### Claude Code

```text
/plugin marketplace add jdlnolen/fhir-chimney-sweep
/plugin install fhir-chimney-sweep@fhir-chimney-sweep
```

Start a new session and use:

```text
/fhir-chimney-sweep:fhir-chimney-sweep Observation in the current FHIR build
```

Both hosts load the same `SKILL.md`, review method, report contract, and Python
helpers. Names are lowercase for host identifiers; the display name is
**FHIR-chimney-sweep**. No MCP server, API key, hooks, or proprietary review
service is bundled. The host model and its tools perform the review.

Packaging references: [OpenAI plugins](https://developers.openai.com/plugins/build/plugins),
[Claude Code plugins](https://code.claude.com/docs/en/plugins-reference).

## Review scope

Specify a resource and optionally a FHIR version/build URL, repository revision,
domain restriction, or output directory. Without a release, the skill resolves
and records the current official CI build at invocation time. It verifies
relocations to incubators rather than assuming every resource remains in core.
There is no fixed OO-only list and no permanent DocumentReference exclusion.

Examples:

```text
Sweep DiagnosticReport in the current R6 build, including Diagnostics module guidance.
Sweep Specimen in FHIR R5; do not substitute current R6 definitions.
Sweep Transport in the current OO Incubator, including its workflow overview.
Sweep only laboratory-related Observation content and explicitly record that limitation.
```

The report distinguishes **corrections**, **suggestions**, **questions**, and
**missing examples**. Optional fields are not automatically required. Codes,
clinical values, element names, and intent are not invented to fill gaps.
Unresolved conflicts become owner decisions, not unsupported corrections.

## Report tooling

The compiler is a formatting and consistency helper, **not a FHIR validator**.
It validates required report fields, three-surface coverage dispositions,
source/finding IDs, dependency cycles, and recommendation consistency. It cannot
prove that an agent inventoried every artifact or interpreted evidence correctly.

Requirements: Python 3.10+ and `python-docx` 1.2.x. Use an available host document
runtime, or install into an isolated environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r plugins/fhir-chimney-sweep/requirements.txt
```

On Windows, use `.venv\Scripts\python.exe`. From a cloned repository:

```sh
.venv/bin/python plugins/fhir-chimney-sweep/skills/fhir-chimney-sweep/scripts/build_report.py --example
.venv/bin/python plugins/fhir-chimney-sweep/skills/fhir-chimney-sweep/scripts/build_report.py /path/to/review.json --check
.venv/bin/python plugins/fhir-chimney-sweep/skills/fhir-chimney-sweep/scripts/build_report.py /path/to/review.json --out-dir /path/to/reports
```

See the [report contract](plugins/fhir-chimney-sweep/skills/fhir-chimney-sweep/references/report-contract.md)
for the input fields. Existing output files are preserved unless `--overwrite`
is explicitly supplied. A shared content ID in both reports helps identify
matching revisions. Keep working JSON and downloaded evidence outside the FHIR
source checkout; only the two reports are default deliverables.

Word visual QA requires rendering and **inspection of every page**. Use the
host's document renderer, or the bundled fallback with LibreOffice and Poppler:

```sh
.venv/bin/python plugins/fhir-chimney-sweep/skills/fhir-chimney-sweep/scripts/render_report.py /path/to/report.docx --out-dir /path/to/new-qa-directory
```

If those tools are unavailable, the skill discloses the visual-QA limitation.
No source or private examples are uploaded to a public validator by this plugin.
Ordinary host model/tool data policies still apply when using an AI assistant.

## Development and contributions

```sh
.venv/bin/python -m unittest discover -s tests -v
claude plugin validate --strict .
claude plugin validate --strict plugins/fhir-chimney-sweep
```

Tests cover report contract failures, matching Word content, explicit table
geometry, links, overwrite protection, rendering error paths, and dual-host
package parity, plus the bundled sample's file integrity and matching content ID.
The synthetic fixture is labeled throughout and is not a real FHIR review.
Tests do not repeat or independently verify the sample's substantive findings.

Issues and pull requests are welcome; the repository owner controls merges
and releases. See [CONTRIBUTING.md](CONTRIBUTING.md). MIT licensed.
