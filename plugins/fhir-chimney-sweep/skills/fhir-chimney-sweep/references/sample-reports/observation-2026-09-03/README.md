# Observation sample report

A completed FHIR-chimney-sweep review of the whole Observation resource, not
just laboratory examples. These are unchanged copies of the paired reports
delivered on September 3, 2026:

- [Read the Markdown report](FHIR-Observation-Chimney-Sweep-2026-09-03.md).
- [Download the Word report](FHIR-Observation-Chimney-Sweep-2026-09-03.docx).

## Provenance and scope

- Review date: **2026-09-03**.
- Build/package: **hl7.fhir.r6.core#6.0.0-ballot4**.
- Source revision: **09dfb700767aa757dd405d56c62bf41c5007e0f0**.
- Shared report content ID: **c87d13fc58ef7836**.
- Recommendation at review time: **Changes required**.
- Findings: **54** (34 corrections, 11 owner questions, three optional
  suggestions, and six missing-example proposals).

The review covers resource documentation, structure and definitions, mappings,
profiles, search and operation guidance; all 60 indexed example entries plus
the additional source-only and inline examples described in the report; and
six substantive modules. Its inventory distinguishes files, resource instances,
contained resources, and abbreviated fragments rather than treating those
counts as interchangeable.

The source was the official public FHIR CI build and its corresponding pinned
source revision. Example identities and clinical values discussed in the report
come from the cited public examples, not private patient records. This remains
an independent community review. FHIR and third-party terminology material
remain subject to their own attribution and licensing terms.

## How to use this sample

Use it to understand the report's organization and level of detail: coverage
inventory, prioritized findings, proposed changes, evidence, owner decisions,
missing examples, and publication acceptance checks. It is not a prescribed
report length, a template of findings to copy, or a current statement about FHIR.

Resolve the target build and inspect its sources for each new sweep. The sample
records a Ballot 5 banner / ballot4 package-metadata discrepancy; it does not
silently substitute a different version. Live CI links may now show different
content, so consult the pinned revision when interpreting this historical review.

## Verification and limitations

The original run parsed all 60 indexed JSON, XML, and Turtle files and performed
the targeted consistency checks described in the report. It did **not** run the
formal FHIR validator, comprehensive terminology-service validation, or a fresh
Publisher build. The semantic review found unresolved inconsistencies; it is
not clinical validation or publication sign-off.

Markdown/Word content parity was checked, and all **49 Word pages** were rendered
and visually inspected in the original run. The files are bundled unchanged;
the [SHA-256 checksums](SHA256SUMS) verify their identity. Repository tests check
packaging and integrity, not the correctness of the review's FHIR conclusions.

Only the two finished reports and these sample notes/checksums are included.
References in the reports to task-local capture logs, `static-qa.json`, working
JSON, or retained visual-QA artifacts describe the original run; those internal
files and downloaded evidence are not bundled. The separate synthetic
`build_report.py --example` fixture is still the compiler's test input.
