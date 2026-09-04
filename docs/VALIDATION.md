# Initial validation - 2026-09-03

Version: 0.1.0. These checks validate plugin packaging and report tooling, not
the accuracy of a completed clinical/FHIR resource review.

- 21 automated tests pass under Python 3.12 with python-docx 1.2.0.
- Both native plugin manifests have matching names, versions, repository and
  license, and load the same self-contained skill payload.
- Codex plugin manifest validator and skill validator pass.
- Claude Code strict plugin and marketplace validation pass.
- Installed and enabled in both Codex and Claude Code at version 0.1.0.
  Claude's native component inventory reports one skill. SHA-256 of each
  installed SKILL.md matches the source payload.
- Real Markdown and Word generation passes, with every body text node compared
  against the shared report content model. Hyperlinks and table widths checked.
- Synthetic DOCX rendered with the host document renderer; all three final pages
  visually inspected. The portable LibreOffice/Poppler fallback also completed.
- Failure tests cover unknown/duplicate IDs, dependency cycles, missing review
  surfaces, unreviewed inventory, unsupported clean verdicts, missing render
  tools, conversion timeout cleanup, and no-clobber report publication.
- Test-first failures were observed for the initial absent compiler, render
  timeout cleanup, semantic-review verdict gate, and concurrent-output protection.

## Review notes

Three independent simplification reviewers examined reuse, quality, and
efficiency. Removed duplicate validation; fixed temporary rendering cleanup
with a regression test. A suggested schema correction was rejected because
the code already checks exact fixed fields before validating their values.
The output-directory precheck was retained as an early safety check; staging
and error handling now preserve retryability.

Code review: skipped (ce-code-review unavailable). The initial repository has
no commit ancestor; the review scope tool requires a commit endpoint and
returned `status: unknown`, `reason: invalid base endpoint`. An explicit manual
diff/file review and the independent simplification passes were used for this
initial publication. This is not a completed full code-review receipt.

The manual review covered input validation, report recommendation gates,
source/finding references, plain-text escaping, DOCX geometry and links,
filesystem overwrite behavior, subprocess arguments/timeouts, native package
paths, and accidental disclosure in the public file set. No unresolved
material finding was identified within that review scope.

## Limits and follow-up

- No end-to-end real-resource sweep has yet been evaluated in a fresh Codex or
  Claude agent session. A resource owner's first live review should verify
  source completeness, finding accuracy, and correction/suggestion calibration.
- The compiler cannot verify the truth of agent-authored evidence, exhaustiveness
  of its inventory, clinical validity, or whether a claimed validator actually ran.
- There is no configured static type checker or lint tool. Syntax compilation,
  automated tests, native manifest validation, and manual inspection are used.
- At initial packaging, generated samples, local environment paths, prior user
  reports, and downloaded FHIR content were not part of the public package.
  The sample-report update below records the subsequently added public sample.
- The shared fixture intentionally retains `DOCX visual QA: not-run`: generating
  it on another machine is not automatically a visually verified result.

After installation, confirm skill discovery in a fresh session and run a small
resource sweep. Healthy output is two matching reports with truthful provenance
and coverage. Missing skills, mismatched content IDs, invented findings, or
unreported coverage gaps should block reliance on the report and be filed as
issues with a public or synthetic reproduction. Repository owner controls
merges and releases.

## Observation sample update - 2026-09-03

The shared plugin now includes unchanged Markdown and Word copies of the
completed September 3 Observation sweep, with provenance, limitations, and
SHA-256 checksums. The root README and skill entrypoint link to the sample.
Only the final report pair is bundled, not task-local evidence, working JSON,
rendered pages, or tool logs. This adds a real-run illustration; it does not
establish independent review accuracy or fresh-session parity between hosts.

The original report's matching content ID is `c87d13fc58ef7836`. The Word file
had all 49 pages rendered and visually inspected during that review; unchanged
file hashes preserve that artifact, without claiming a new rendering run here.
Formal FHIR validation, comprehensive terminology validation, and a fresh
Publisher build remain unrun for that report.

Regression tests cover sample-file checksums, paired filenames/content IDs,
Word ZIP integrity, and the existing self-contained plugin reference checks.
These are packaging checks, not a repeated FHIR review. At the end of the
documentation-edit step, plugin version and release/install state were unchanged.

Update verification: all 23 automated tests pass; Codex plugin/skill validators
and Claude Code strict marketplace/plugin validators pass. README links resolve,
the two report files match their original SHA-256 checksums, and the Word package
contains 131 HTTPS links with no local filesystem paths or user metadata markers
found by the targeted check. `git diff --check` passes. That edit step did not
perform a release, remote push, or installed-plugin refresh.

The subsequent commit/push/install request uses matching native manifest versions
`0.1.0+codex.20260903143253` to refresh the local plugin caches while preserving
the `0.1.0` base version. This cache-busting suffix is not a new FHIR review or a
semantic-version feature release.

## Classification ordering update - 2026-09-04

Version: 0.1.1. The report contract and compiler now require every finding to
have one of three change classifications: `Must fix (implementation or testing
impact)`, `Minor fix`, or `Net new addition`. Must fix is limited to content that
materially impairs implementation or test design. Clinically implausible values
and internally inconsistent example data remain minor fixes unless the same
finding also contains such a blocker. Missing examples are always net new
additions.

Detailed findings are now grouped first by change classification, then by report
area, and finally by numeric finding ID within each area. Empty groups are
omitted. Finding type (`Correction`, `Suggestion`, `Question`, or `Missing
example`) and P1/P2/P3 priority remain separate metadata. Markdown and Word use
the same grouping and content model, and Word finding titles are real Heading 3
paragraphs.

The bundled Observation sample demonstrates the revised contract across all 54
findings: 27 must-fix items, 17 minor fixes, and 10 net new additions. Its revised
Markdown and Word files retain matching content ID `c8b1e82d9f3e15be`. All 51
Word pages were rendered and visually inspected during the classification
revision. This is a reorganization and classification of the dated September 3
review, not a fresh FHIR sweep; its recorded source, evidence limitations, and
unrun formal validation steps remain unchanged.

Automated tests now cover allowed classifications, the missing-example rule,
classification/area/numeric-ID ordering, Word heading levels, and the shipped
sample's classification totals and order. The full suite passes 26 tests. A
fresh synthetic report was rendered to four pages and every page was inspected;
no clipping, overlap, split table rows, or hierarchy defect was found. The
fixture truthfully retains `DOCX visual QA: not-run` because generation alone
does not confer visual-QA status on later runs.

Update verification: all 26 automated tests pass with the bundled document
runtime; Codex skill and plugin validators pass; Claude Code strict marketplace
and plugin validation pass; and the bundled Observation checksums verify. A
targeted source scan found no task-local filesystem paths in the packaged text.
`git diff --check` passes. These checks validate the report contract, generated
artifacts, and plugin packaging; they do not independently establish the
substantive accuracy or completeness of the dated Observation review.
