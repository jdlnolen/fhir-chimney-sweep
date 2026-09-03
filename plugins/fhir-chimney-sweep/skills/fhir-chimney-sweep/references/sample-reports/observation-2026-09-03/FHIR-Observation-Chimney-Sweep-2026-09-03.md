# FHIR Observation: Chimney Sweep

Resource continuity and prepublication review

Recommendation: Changes required

Reviewed: 2026-09-03

FHIR version: 6.0.0-ballot4 \(current official R6 CI snapshot\)

Package: hl7.fhir.r6.core\#6.0.0-ballot4

Source revision: 09dfb700767aa757dd405d56c62bf41c5007e0f0

[Build](<https://build.fhir.org/observation.html>)

Report content ID: c87d13fc58ef7836 \(identical in Markdown and Word\)

The current Observation build needs coordinated corrections across documentation, examples and modules. Highest-priority issues include unsupported genomic and operation paths, organizer/absence contradictions, inconsistent calculations and coded results, and a medication/device boundary error. Questions and missing-example proposals are separate from demonstrated defects. No publication sign-off is implied.

Triage: P1: 13; P2: 36; P3: 5. Correction: 34; Suggestion: 3; Question: 11; Missing example: 6.

## Scope and review boundary

Whole Observation resource, not laboratory-only: resource prose, structure/definitions, mappings, profiles, search/operation guidance and relevant modules. The index contains 60 entries: 59 standalone Observation files and one three-entry Bundle, yielding 60 Observation instances. These indexed files also contain eight contained resource instances \(five separate newborn Patient copies, two Specimens and one Group\); none is an additional contained Observation. Seven source-only Observation roots, four contained Observations in the linked lipid report, and two complete inline $stats results bring the explicitly reviewed non-truncated Observation instance count to 73. Three $lastn excerpts contain 23 additional abbreviated fragments, counted separately. Seventeen directly linked dependency files and the blood-examination report Bundle were reviewed only as needed for continuity. Six substantive modules were reviewed: Diagnostics, Device, Nutrition, Biologically Derived Product, Workflow and Medication Definition. The official page footer was generated 2026-08-28 18:42 UTC; version.info generation time is 18:37:46 UTC. Retrieved 2026-09-03; downloads, timestamps and hashes are retained in task-local capture logs. P1 denotes a material semantic/conformance or usability issue, not an automated release gate; P2 denotes other correctness/coverage work, and P3 editorial or optional improvement.

Advisory change list only. No FHIR source was modified by this sweep. Parsing, FHIR validation, terminology verification, semantic review, and document rendering are distinct checks. This report does not confer clinical or publication approval.

## Review inventory

| Area | Artifact | Disposition | Finding IDs |
| --- | --- | --- | --- |
| Documentation | Scope and boundaries | reviewed | D02, D05, D06, X01 |
| Documentation | Element definitions and structure | reviewed | D01, D02, D03, D07, D08 |
| Documentation | Usage notes and search | reviewed | D04, D06, D07, X01, X02 |
| Documentation | Mappings and profiles | reviewed | D09, D10, D11, X02 |
| Documentation | Operations | reviewed | D12, E24, E25 |
| Examples | EX01: Observation/example | reviewed | E01 |
| Examples | EX02: Observation/respiratory-rate | reviewed | E13 |
| Examples | EX03: Observation/heart-rate | reviewed | E13, E18 |
| Examples | EX04: Observation/body-temperature | reviewed | D06, E13 |
| Examples | EX05: Observation/body-height | reviewed | E01 |
| Examples | EX06: Observation/body-length | reviewed | E12 |
| Examples | EX07: Observation/head-circumference | reviewed | None |
| Examples | EX08: Observation/bmi | reviewed | D11 |
| Examples | EX09: Observation/bmi-using-related | reviewed | D11, E01 |
| Examples | EX10: Bundle/example-observation-device-flowratemetric | reviewed | D02, E07, E08 |
| Examples | EX11: Observation/blood-pressure | reviewed | E13 |
| Examples | EX12: Observation/blood-pressure-dar | reviewed | None |
| Examples | EX13: Observation/mbp | reviewed | None |
| Examples | EX14: Observation/vitals-panel | reviewed | X02, E13 |
| Examples | EX15: Observation/blood-pressure-cancel | reviewed | D04, E09 |
| Examples | EX16: Observation/f001 | reviewed | E21 |
| Examples | EX17: Observation/unsat | reviewed | D04 |
| Examples | EX18: Observation/f002 | reviewed | E12, E21 |
| Examples | EX19: Observation/f003 | reviewed | E21 |
| Examples | EX20: Observation/f004 | reviewed | E21 |
| Examples | EX21: Observation/f005 | reviewed | E12, E21 |
| Examples | EX22: Observation/date-lastmp | reviewed | E05 |
| Examples | EX23: Observation/f202 | reviewed | D06, M02 |
| Examples | EX24: Observation/f203 | reviewed | E23 |
| Examples | EX25: Observation/f204 | reviewed | E23 |
| Examples | EX26: Observation/f205 | reviewed | E10 |
| Examples | EX27: Observation/f206 | reviewed | E23 |
| Examples | EX28: Observation/ekg | reviewed | E23 |
| Examples | EX29: Observation/glasgow | reviewed | None |
| Examples | EX30: Observation/gcs-qa | reviewed | E22 |
| Examples | EX31: Observation/1minute-apgar-score | reviewed | E02 |
| Examples | EX32: Observation/2minute-apgar-score | reviewed | E02, E03 |
| Examples | EX33: Observation/5minute-apgar-score | reviewed | E02, E03 |
| Examples | EX34: Observation/10minute-apgar-score | reviewed | E02, E03 |
| Examples | EX35: Observation/20minute-apgar-score | reviewed | E02, E03 |
| Examples | EX36: Observation/clinical-gender | reviewed | E14 |
| Examples | EX37: Observation/eye-color | reviewed | None |
| Examples | EX38: Observation/bmd | reviewed | E04 |
| Examples | EX39: Observation/656 | reviewed | E06, E22 |
| Examples | EX40: Observation/alcohol-type | reviewed | None |
| Examples | EX41: Observation/vp-oyster | reviewed | E15 |
| Examples | EX42: Observation/herd1 | reviewed | E19 |
| Examples | EX43: Observation/vomiting | reviewed | E06 |
| Examples | EX44: Observation/secondsmoke | reviewed | E06 |
| Examples | EX45: Observation/trachcare | reviewed | E06 |
| Examples | EX46: Observation/bgpanel | reviewed | E06, E17 |
| Examples | EX47: Observation/bloodgroup | reviewed | E06, E17 |
| Examples | EX48: Observation/rhstatus | reviewed | E06, E17 |
| Examples | EX49: Observation/decimal | reviewed | None |
| Examples | EX50: Observation/map-sitting | reviewed | E11 |
| Examples | EX51: Observation/abdo-tender | reviewed | D09 |
| Examples | EX52: Observation/krcore-observation-labresult-example-01 | reviewed | E16 |
| Examples | EX53: Observation/body-weight-with-arabic-code | reviewed | None |
| Examples | EX54: Observation/cholesterol | reviewed | E22 |
| Examples | EX55: Observation/hdl | reviewed | None |
| Examples | EX56: Observation/ldl | reviewed | None |
| Examples | EX57: Observation/non-hdl | reviewed | E22, E23 |
| Examples | EX58: Observation/triglycerides | reviewed | E22 |
| Examples | EX59: Observation/vldl | reviewed | E22 |
| Examples | EX60: Observation/lipidpanel-organizer | reviewed | X02 |
| Examples | SO1: apgar-panel \(source only\) | reviewed | E18 |
| Examples | SO2: apgar-score \(source only\) | reviewed | E18 |
| Examples | SO3: color \(source only\) | reviewed | E18 |
| Examples | SO4: muscle-tone \(source only\) | reviewed | E18 |
| Examples | SO5: reflex-irritability \(source only\) | reviewed | E18 |
| Examples | SO6: respiratory-effort \(source only\) | reviewed | E18 |
| Examples | SO7: body-height-merged \(source only\) | reviewed | E18 |
| Examples | Linked lipid report | reviewed | E20 |
| Examples | Linked blood examination Bundle | reviewed | E21 |
| Examples | Inline $stats results | reviewed | D11, D12, E24 |
| Examples | Inline $lastn excerpts | reviewed | D12, E25 |
| Examples | Directly linked dependency fixtures | reviewed | E01, E06, E07, E12, E19, E20 |
| Examples | Intentional failing invariant fixture | excluded | None |
| Examples | Other core/IG resource corpora | excluded | None |
| Module | Diagnostics | reviewed | X01, X02, M01, M09, E20 |
| Module | Device | reviewed | D02, M02, M03, M04, M05, M06 |
| Module | Nutrition | reviewed | M07 |
| Module | Biologically Derived Product | reviewed | None |
| Module | Workflow | reviewed | None |
| Module | Medication Definition | reviewed | M08 |
| Module | Incidental module mentions | excluded | None |
| Cross-layer | Pinned source/rendered correspondence | reviewed | X01, X02 |

Documentation / Scope and boundaries: Read scope, core profiles, boundaries, reference lists and linked definition context. Sources: DOC, DEF.

Documentation / Element definitions and structure: Compared all resource-specific definitions/comments, choices, cardinalities, bindings, constraints and current reference targets. Sources: DEF, DETAIL, PSRC.

Documentation / Usage notes and search: Read grouping, subject, coding, timing, reference ranges, cancellation, genomics and search guidance. Sources: DOC, NOTESRC.

Documentation / Mappings and profiles: Read mapping tables and profile index; checked relevant Vital Signs base, BP, height and panel definitions. Sources: MAP, PROFILES, VITAL, VB, BP, BH, VP.

Documentation / Operations: Read $lastn and $stats prose, formal definitions, parameters and inline examples. No live operation implementation was executed. Sources: OPS, LASTN, STATS, STATOP, LASTNOP.

Examples / EX01: Observation/example: 185 lb fixture retained; contributes to the inconsistent derived-BMI graph. Sources: EX01.

Examples / EX02: Observation/respiratory-rate: Respiratory-rate value/unit and point-time structure reviewed; no standalone correction identified. Sources: EX02.

Examples / EX03: Observation/heart-rate: Heart-rate value/unit reviewed; the adult 1999 fixture is unsuitable as the alternate Apgar panel member. Sources: EX03.

Examples / EX04: Observation/body-temperature: Ordinary body-temperature example is a better scope illustration than entered-in-error f202. Sources: EX04.

Examples / EX05: Observation/body-height: High-precision height is identical in raw JSON/XML; do not mistake binary floating-point display for source corruption. Sources: EX05.

Examples / EX06: Observation/body-length: Adult subject/body-length plausibility requires owner review. Sources: EX06.

Examples / EX07: Observation/head-circumference: Head-circumference example reviewed; optional contextual omissions alone are not errors. Sources: EX07.

Examples / EX08: Observation/bmi: Standalone BMI can be valid without explicit input references; clarify the guide on calculated measurements. Sources: EX08.

Examples / EX09: Observation/bmi-using-related: Derived inputs, references, chronology and arithmetic reviewed. Sources: EX09.

Examples / EX10: Bundle/example-observation-device-flowratemetric: One collection Bundle, three entries: one Observation, one DeviceAssociation and one DeviceMetric. Pump Device missing; internal metric present. Sources: EX10.

Examples / EX11: Observation/blood-pressure: Systolic/diastolic values and interpretations reviewed. Identifier-only basedOn is a valid logical Reference, not an automatic broken link. Sources: EX11.

Examples / EX12: Observation/blood-pressure-dar: One component has no value and has an absence reason; no invented diastolic value is needed. Optional note could explain aggregate interpretation. Sources: EX12.

Examples / EX13: Observation/mbp: Mean blood-pressure numeric/UCUM point-time example reviewed. Sources: EX13.

Examples / EX14: Observation/vitals-panel: Organizer constraints are met; member timing is inconsistent. Sources: EX14.

Examples / EX15: Observation/blood-pressure-cancel: Cancelled example has no numeric results; retained Low interpretation is unsupported. Sources: EX15.

Examples / EX16: Observation/f001: Glucose value, units, high flag and reference interval are internally consistent; linked CBC context is not. Sources: EX16.

Examples / EX17: Observation/unsat: Unsatisfactory-specimen absence example reviewed; missing optional Specimen is not itself a base violation. Sources: EX17.

Examples / EX18: Observation/f002: Base-excess range needs clinical provenance; also linked from the mismatched CBC report. Sources: EX18.

Examples / EX19: Observation/f003: Carbon-dioxide value/unit/flag reviewed; linked report membership needs correction. Sources: EX19.

Examples / EX20: Observation/f004: Erythrocyte value/unit and range text reviewed; optional age/sex structuring not required in every fixture. Sources: EX20.

Examples / EX21: Observation/f005: Hemoglobin already uses g/dL in this build. Clinical range, not a stale mmol/L claim, is the open question. Sources: EX21.

Examples / EX22: Observation/date-lastmp: Last-event date is after the assessment date. Sources: EX22.

Examples / EX23: Observation/f202: Entered-in-error may retain its original value. Do not convert it to final merely to make it look ordinary. Sources: EX23.

Examples / EX24: Observation/f203: Bicarbonate reviewed. Additional timing/specimen context and UCUM normalization are suggestions, not blanket validity requirements. Sources: EX24.

Examples / EX25: Observation/f204: Creatinine reviewed; local coding and alternate unit coding are not automatically prohibited. Sources: EX25.

Examples / EX26: Observation/f205: The first eGFR component population does not agree with its reference-range applicability. Sources: EX26.

Examples / EX27: Observation/f206: Organism result reviewed. A richer culture/Specimen graph would improve teaching but is not universally mandatory. Sources: EX27.

Examples / EX28: Observation/ekg: Three component SampledData leads are present. Identical synthetic samples and amplitude scaling deserve explanation. Sources: EX28.

Examples / EX29: Observation/glasgow: GCS component weights sum to the stated total 13. Sources: EX29.

Examples / EX30: Observation/gcs-qa: Derived QuestionnaireResponse identity/time/score reviewed; stale catalog resource name needs correction. Sources: EX30.

Examples / EX31: Observation/1minute-apgar-score: Total 0 and component weights reviewed; birth-relative timestamp inconsistent. Sources: EX31.

Examples / EX32: Observation/2minute-apgar-score: Total 5 matches local weights, but reflex answer coding contradicts its one-point score; timestamp inconsistent. Sources: EX32.

Examples / EX33: Observation/5minute-apgar-score: Total 10 and component weights reviewed; timestamp inconsistent. Sources: EX33.

Examples / EX34: Observation/10minute-apgar-score: Total 10 and component weights reviewed; timestamp inconsistent. Sources: EX34.

Examples / EX35: Observation/20minute-apgar-score: Total 10 and component weights reviewed; timestamp inconsistent. Sources: EX35.

Examples / EX36: Observation/clinical-gender: Question and answer concepts describe different assertions. Sources: EX36.

Examples / EX37: Observation/eye-color: Intentional minimal coded eye-color assertion retained. Sources: EX37.

Examples / EX38: Observation/bmd: Areal-density display and UCUM code disagree. Sources: EX38.

Examples / EX39: Observation/656: Subject/performer targets and catalog DeviceComponent claim require repair. Sources: EX39.

Examples / EX40: Observation/alcohol-type: Multiple component answers with the same question code and no parent value are compatible with obs-7. Sources: EX40.

Examples / EX41: Observation/vp-oyster: Two contained Specimens and one contained Group reviewed; Group.type mismatch identified. Sources: EX41.

Examples / EX42: Observation/herd1: Herd/specimen graph reviewed; ratio/percent and collection-time intent unresolved. Sources: EX42.

Examples / EX43: Observation/vomiting: Negative vomiting assertion reviewed; infant target missing. Sources: EX43.

Examples / EX44: Observation/secondsmoke: Second-hand smoke assertion reviewed; infant target missing. Sources: EX44.

Examples / EX45: Observation/trachcare: Caregiver focus is distinct from infant subject; focus Patient reference is not inherently invalid. Sources: EX45.

Examples / EX46: Observation/bgpanel: ABO/Rh membership is not a complete explanation of the antibody-screen panel code. Sources: EX46.

Examples / EX47: Observation/bloodgroup: ABO answer reviewed; infant target missing. Sources: EX47.

Examples / EX48: Observation/rhstatus: Rh answer reviewed; infant target missing. Sources: EX48.

Examples / EX49: Observation/decimal: Intentional decimal lexical-precision/stress fixture retained; not judged as clinical physiology. Sources: EX49.

Examples / EX50: Observation/map-sitting: Category, advertised extension features and effective/issued chronology disagree. Sources: EX50.

Examples / EX51: Observation/abdo-tender: Clinical-finding coding pattern reviewed; mapping scope needs clarification. Sources: EX51.

Examples / EX52: Observation/krcore-observation-labresult-example-01: Korean text retained; fictitious profile assertion and incomplete UCUM coding require repair. Sources: EX52.

Examples / EX53: Observation/body-weight-with-arabic-code: Arabic multilingual weight example reviewed; no translation-driven code mutation proposed. Sources: EX53.

Examples / EX54: Observation/cholesterol: Cholesterol value and shared 2015 subject/specimen reviewed; stored website links need repair. Sources: EX54.

Examples / EX55: Observation/hdl: HDL 46 mg/dL, patient and specimen reviewed; no material standalone inconsistency identified. Sources: EX55.

Examples / EX56: Observation/ldl: LDL 161 mg/dL uses a generic LDL concept, not an asserted calculated LDL method; no forced Friedewald recalculation. Sources: EX56.

Examples / EX57: Observation/non-hdl: Non-HDL 191 equals total 237 minus HDL 46. Optional derivation references and qualified goal prose would improve teaching. Sources: EX57.

Examples / EX58: Observation/triglycerides: Triglycerides value, units and range reviewed; stored website links need repair. Sources: EX58.

Examples / EX59: Observation/vldl: VLDL value, units and range reviewed; stored website links need repair. Sources: EX59.

Examples / EX60: Observation/lipidpanel-organizer: Pure organizer with six member references and no result/absence/components is consistent with obs-11. Text-only CodeableConcept is permitted. Sources: EX60.

Examples / SO1: apgar-panel \(source only\): Read pinned XML; not counted among the 60 published index entries. Publication/graph repair requires an owner decision. Sources: SO1.

Examples / SO2: apgar-score \(source only\): Read pinned XML; not counted among the 60 published index entries. Publication/graph repair requires an owner decision. Sources: SO2.

Examples / SO3: color \(source only\): Read pinned XML; not counted among the 60 published index entries. Publication/graph repair requires an owner decision. Sources: SO3.

Examples / SO4: muscle-tone \(source only\): Read pinned XML; not counted among the 60 published index entries. Publication/graph repair requires an owner decision. Sources: SO4.

Examples / SO5: reflex-irritability \(source only\): Read pinned XML; not counted among the 60 published index entries. Publication/graph repair requires an owner decision. Sources: SO5.

Examples / SO6: respiratory-effort \(source only\): Read pinned XML; not counted among the 60 published index entries. Publication/graph repair requires an owner decision. Sources: SO6.

Examples / SO7: body-height-merged \(source only\): Read pinned XML; not counted among the 60 published index entries. Publication/graph repair requires an owner decision. Sources: SO7.

Examples / Linked lipid report: Four additional contained Observations reviewed with the report narrative, patient identity and timing. Separate from the six 2015 standalone lipid results. Sources: LIPIDREPORT.

Examples / Linked blood examination Bundle: Two entries: DiagnosticReport and ServiceRequest. Its result references point to already counted indexed Observations. Sources: CBCREPORT.

Examples / Inline $stats results: Two complete Observation instances within the displayed Parameters response; terminology and aggregate-result meaning reviewed. Sources: STATS, STATDEF.

Examples / Inline $lastn excerpts: Three deliberately abbreviated response snippets containing 23 Observation fragments. Reviewed as illustrations, not counted as complete instances or syntax-validated JSON. Sources: LASTN.

Examples / Directly linked dependency fixtures: 17 catalog-mapped dependency files checked for identity, role, timing or reference continuity: encounter-example, group-example-herd1, organization-example-lab, patient-example, patient-example-a, patient-example-b, patient-example-chinese, patient-example-f001-pieter, patient-example-f201-roel, patient-example-infant-mom, practitioner-example, practitioner-example-f005-al, practitioner-example-f201-ab, practitioner-example-f202-lm, questionnaireresponse-example-gcs, specimen-example-pooled-serum, specimen-example-serum. This is not a full sweep of those resources. Sources: DEP01, DEP02, DEP03, DEP04, DEP05, DEP06, DEP07, DEP08, DEP09, DEP10, DEP11, DEP12, DEP13, DEP14, DEP15, DEP16, DEP17.

Examples / Intentional failing invariant fixture: obs-10.f2.fail.xml deliberately tests failure and is not a positive publication example. Sources: FAILFIX.

Examples / Other core/IG resource corpora: Other Observations scattered through independent examples, IG packages or external clinical systems are outside this resource-index sweep except the explicitly listed linked/inline cases. No private examples were supplied. Sources: None available.

Module / Diagnostics: Read prose, tables and use cases; visually inspected the resource map, three grouping/additional-testing diagrams and all four imaging figures. Sources: DIAG, DGM, GROUP1, GROUP2, GROUP3.

Module / Device: Read use cases A-F, tables and guidance; visually inspected DeviceModule.svg against current reference types. Sources: DEVICE, DEVMAP, DA, DM.

Module / Nutrition: Reviewed substantive Observation roles in assessment and diagnosis scenarios; did not audit dietary prescriptions. Sources: NUTR, DOC.

Module / Biologically Derived Product: Reviewed Observation roles and visually inspected the general and cell-therapy workflow diagrams. No additional Observation-specific correction identified. Sources: BDP.

Module / Workflow: Reviewed overview/event-pattern references relevant to Observation; no additional material inconsistency identified. Sources: WORKFLOW, DEF.

Module / Medication Definition: Reviewed relevant boundary/profiling discussion; identified a false universal profile claim. Sources: MEDDEF.

Module / Incidental module mentions: Clinical Summary, Clinical Reasoning and Security/Privacy were screened; no further substantive Observation-specific modeling content selected. General security and independent IG guidance are not full resource reviews. Sources: None available.

Cross-layer / Pinned source/rendered correspondence: version.info identifies buildId v5.0.0-7582-g09dfb70076; inspected source was pinned to the matching full commit, not the newer working checkout. Sources: BUILD, PSRC, NOTESRC, LISTSRC.

## Documentation findings

### D12 \| P1 \| Correction: Update obsolete paths in operation guidance

Location: Observation $lastn grouping rule; $stats code parameter and overview

Evidence: $lastn compares coding.value, which is not a Coding element. $stats traverses .related with type=has-member, a removed Observation representation, rather than hasMember. Its overview also uses stale patient/duration-only wording.

Evidence sources: LASTN, STATS, STATOP, LASTNOP, DEF, DATATYPES

Proposed change: Use current paths and align the operation descriptions with formal parameters.

Replacement / minimum content:

```
$lastn: compare Coding.code and Coding.system. $stats: traverse Observation.hasMember references and Observation.component according to the documented panel behavior. Describe subject and duration or period consistently. Clarify component-value inclusion instead of implying only top-level valueQuantity is evaluated.
```

Rationale: These are executable algorithm instructions, not merely historical terms.

Acceptance check: Compare every path with R6 definitions and test top-level values, component BP and an organizer panel.

Human decision: Editorial approval; no new design decision required.

Depends on: None

### D01 \| P2 \| Correction: Describe category as a preferred binding

Location: Observation.category comment

Evidence: The comment calls the category value set required; the actual base binding strength is preferred.

Evidence sources: DEF, DETAIL

Proposed change: Align the comment with the binding; retain support for multiple categorization schemes.

Replacement / minimum content:

```
In addition to the preferred Observation Category Codes value set, this element allows other categorization schemes. Multiple categories may be used.
```

Rationale: Avoids teaching a stronger base constraint than the definition supplies.

Acceptance check: Compare the regenerated comment with category.binding.strength and the Vital Signs category requirements.

Human decision: Editorial approval; no new design decision required.

Depends on: None

### D02 \| P2 \| Question: Reconcile subject, focus and patient-device rules

Location: Observation.subject definition/comment, focus comment, Notes on subject; Device use case A

Evidence: The subject type list includes Medication, Substance, BiologicallyDerivedProduct and NutritionProduct, but its definition omits them. The device-to-patient SHALL and focus example do not clearly align with de-identified/device exceptions in the notes.

Evidence sources: DEF, DOC, DEVICE, EX10

Proposed change: Agree on device-centric versus patient-centric semantics, then update every affected explanation and fixture.

Replacement / minimum content:

```
Define subject as the entity the Observation record is about; distinguish it from the object directly observed (focus), specimen, and recording device. State exactly when an initially unassociated patient measurement must later be associated with a Patient. Do not apply that rule to unrelated non-patient observations.
```

Rationale: Prevents contradictory modeling advice and accidental prohibition of valid non-patient subjects.

Acceptance check: Walk patient-attached measurement, device-performance and de-identified cases through the prose and EX10.

Human decision: OO and Devices must decide the intended normative patient-association rule and device-centric example design.

Depends on: None

### D03 \| P2 \| Correction: Use actual Observation status codes in statusReason guidance

Location: Observation.statusReason.comment

Evidence: The comment illustrates not-done and suspended, neither of which belongs to the required Observation status value set.

Evidence sources: DEF, STATUS

Proposed change: Replace foreign workflow codes with Observation-specific examples.

Replacement / minimum content:

```
This element is generally used to explain an exception status, such as cancelled or entered-in-error. Select a status from the Observation Status value set; use statusReason to explain why that status applies.
```

Rationale: A new R6 element should not teach unsupported codes.

Acceptance check: Check all status names against the pinned required value set.

Human decision: Editorial approval; no new design decision required.

Depends on: None

### D04 \| P2 \| Question: Clarify cancellation versus an unobtainable result

Location: Notes 10.1.5.11; Observation Status definitions

Evidence: The notes prescribe cancelled whenever a test could not be completed, but the current value set also includes cannot-be-obtained. The relationship is not explained.

Evidence sources: DOC, STATUS, EX15, EX17

Proposed change: Define the lifecycle distinction before changing example statuses.

Replacement / minimum content:

```
Add a short decision table for an order cancelled before performance, an attempted measurement whose result cannot be obtained, and a result record entered in error. Specify status, statusReason and result-level absence handling for each.
```

Rationale: A universal mechanical replacement would conceal the unresolved design intent.

Acceptance check: Review the table with cancellation, rejected-specimen and entered-in-error examples; preserve history.

Human decision: OO must decide the intended status transition and when existing cancelled examples remain appropriate.

Depends on: None

### D05 \| P2 \| Correction: Remove undefined ObservationDefinition inheritance wording

Location: Boundaries and Relationships: ObservationDefinition paragraph and linked section

Evidence: The paragraph implies instantiation/inheritance, while Observation has no instantiates\[x\] in this build. The linked numbered fragment is stale.

Evidence sources: DOC, DEF

Proposed change: Describe definitional guidance without inventing a runtime inheritance mechanism; repair the link.

Replacement / minimum content:

```
ObservationDefinition describes characteristics of an observation that can guide creation and interpretation of Observation instances. An instance must explicitly carry the information required for its use case and profiles. This statement does not create implicit inheritance or a core instantiates element.
```

Rationale: Separates design-time definitions from actual instance conformance.

Acceptance check: Verify the live ObservationDefinition link and search the complete Observation structure for the relationship described.

Human decision: OO should confirm whether a separately defined extension or profile mechanism also needs an explicit link.

Depends on: None

### D07 \| P2 \| Suggestion: Explain the new contextual and device roles together

Location: Notes 10.1.5.7 and device/anatomy guidance

Evidence: The structure contains context, supportingDevice and bodyStructure, but the usage discussion does not adequately contrast these roles with existing relationships.

Evidence sources: DOC, DEF

Proposed change: Add a short role comparison and link a worked R6 example.

Replacement / minimum content:

```
Contrast basedOn (request), partOf (containing event), derivedFrom (source evidence), triggeredBy (trigger), context (interpretive context), device (measurement device), supportingDevice (supporting equipment), and bodyStructure (coded or referenced anatomy). Show the actual R6 cardinalities and CodeableReference shape.
```

Rationale: Reduces the need to infer modeling intent from element names alone.

Acceptance check: Check every role and example path against snapshot.element; do not imply that all roles must be populated.

Human decision: Editorial approval; no new design decision required.

Depends on: None

### D08 \| P2 \| Question: Resolve normalValue-only reference ranges

Location: Observation.referenceRange.normalValue and invariant obs-3

Evidence: normalValue permits a coded normal result, but obs-3 still requires low, high or text. A normalValue-only referenceRange is therefore rejected by the stated rule.

Evidence sources: DEF, DETAIL

Proposed change: Decide whether coded-only normal ranges are intended to stand alone.

Replacement / minimum content:

```
If yes, update both the invariant expression and human text to include normalValue. If no, explicitly require companion text and demonstrate it in an example. Do not silently change the rule based only on the new element.
```

Rationale: The semantic intent cannot be established from the conflicting affordances alone.

Acceptance check: Validate one coded-only and one coded-plus-text fixture against the approved rule.

Human decision: OO must decide whether normalValue alone is a sufficient reference range.

Depends on: None

### D09 \| P2 \| Question: Align the SNOMED concept-domain mapping with allowed coding patterns

Location: Observation mappings: Observation.code; Notes on SNOMED CT patterns 3 and 4

Evidence: The concept-domain mapping names observable entities/evaluation procedures, while the notes and abdominal-tenderness example also use clinical findings.

Evidence sources: MAP, DOC, EX51

Proposed change: Clarify whether the mapping is illustrative or intended to exclude other documented patterns.

Replacement / minimum content:

```
Either label the mapping non-exhaustive and link the coding-pattern guidance, or revise the documented domain after terminology-owner review. Do not invalidate the clinical-finding pattern by inference.
```

Rationale: Mappings should not appear to contradict sanctioned examples.

Acceptance check: Review each documented SNOMED pattern against the final mapping and example code systems.

Human decision: Terminology and OO owners must confirm the mapping scope and any extension to its expression.

Depends on: None

### D10 \| P2 \| Correction: Synchronize Vital Signs profile descriptions and constraint IDs

Location: bp.profile.json root definition; vitalspanel.profile.json root definition; bodyheight.profile.json condition links

Evidence: BP prose permits one systolic and/or diastolic component, but both slices are mandatory. Panel prose still describes links with type=has-member. Body Height references vsp-4 although its local invariant is named vs-4.

Evidence sources: BP, VP, BH

Proposed change: Update descriptive text and repair the dangling condition identifier.

Replacement / minimum content:

```
BP: include both systolic and diastolic components, each carrying a value or appropriate dataAbsentReason. Panel: use Observation.hasMember with at least two members and organizer=true; remove the obsolete type=has-member syntax. Body Height: align condition with the declared invariant ID vs-4 (or rename both consistently).
```

Rationale: Generated guidance and constraint navigation must agree with the profile snapshot.

Acceptance check: Rebuild profiles; inspect slice minima, panel membership and resolved condition links.

Human decision: Editorial approval; no new design decision required.

Depends on: None

### D11 \| P2 \| Question: Distinguish temporal aggregation from calculated BMI

Location: Vital Signs Formal View introductory paragraphs

Evidence: The guide broadly excludes calculated observations based on two or more point-in-time vital signs, yet it defines BMI and links calculated BMI examples.

Evidence sources: VITAL, EX08, EX09

Proposed change: Narrow the statement to its intended class of calculations.

Replacement / minimum content:

```
If the intent is to exclude averages and other time-aggregated measurements from point-in-time profiles, say so explicitly and distinguish BMI calculated from appropriately related height and weight. Otherwise explain the intended BMI exception.
```

Rationale: The current wording can be read as forbidding a profile the same page supplies.

Acceptance check: Test the wording against same-event BMI, a 24-hour average and a single measured heart rate.

Human decision: Vital Signs owners must confirm the intended temporal-aggregation restriction.

Depends on: None

### D06 \| P3 \| Correction: Repair local wording and duplicated definitions

Location: Notes on subject, components, coded results, NaN and reference ranges; component.value\[x\].comment; Scope temperature link

Evidence: The prose says two attributes then names three; says one performer despite performer 0..\*; implies a base binding on valueCodeableConcept; names only valueCodeableConcept for NaN; and duplicates value-choice comments. The introductory temperature link leads to entered-in-error f202.

Evidence sources: DOC, DEF, EX04, EX23

Proposed change: Apply bounded copy edits without changing conformance strength.

Replacement / minimum content:

```
Use "several elements" for specimen/bodyStructure/focus; "shared Observation-level context, including the same performer list" for components; "a profile or use case may specify an answer value set" for coded results; "value[x] is absent" for NaN; and "type, appliesTo and age" for distinguishing reference ranges. Remove the duplicate value-type bullets. Link the ordinary temperature illustration to observation-example-body-temperature.html.
```

Rationale: Makes the prose precise without requiring optional data or invalidating error-history examples.

Acceptance check: Regenerate the notes and definitions; verify the linked ordinary temperature and retained entered-in-error example.

Human decision: Editorial approval; no new design decision required.

Depends on: None

## Examples findings

### E01 \| P1 \| Correction: Repair the derived BMI graph, not just its broken link

Location: Observation/bmi-using-related: derivedFrom, effectiveDateTime and valueQuantity

Evidence: The height reference is Observation/bodyheight, but the catalog ID is body-height. The referenced weight is 185 lb in 2016; height is about 66.9 inches in 1999. Those values imply BMI about 29.1, not the stated 16.2.

Evidence sources: EX09, EX05, EX01

Proposed change: Choose one coherent measurement set and regenerate the calculated result and narrative.

Replacement / minimum content:

```
Use a resolvable height reference, paired height and weight with compatible subject and timing, and BMI = weight[kg] / height[m]^2. Either preserve the inputs and recompute the result or preserve the teaching scenario with owner-approved replacement inputs; do not merely rename bodyheight.
```

Rationale: A fixed hyperlink alone leaves a materially incorrect calculation.

Acceptance check: Resolve both inputs, convert UCUM units, independently recompute BMI and compare timestamps.

Human decision: Owner must choose the intended inputs and measurement event; no replacement clinical values are fabricated.

Depends on: None

### E02 \| P1 \| Correction: Give timed Apgar scores distinct, birth-relative timestamps

Location: The 1-, 2-, 5-, 10- and 20-minute Apgar examples: effectiveDateTime and contained Patient birthTime

Evidence: All five observations share 2016-05-18T22:33:22Z. Each contained newborn has birthTime 2016-05-18T10:28:45Z, inconsistent with all five minute-specific codes.

Evidence sources: EX31, EX32, EX33, EX34, EX35

Proposed change: Synchronize observation times, newborn identity and narratives across the family.

Replacement / minimum content:

```
If retaining the recorded birth time, use 10:29:45Z, 10:30:45Z, 10:33:45Z, 10:38:45Z and 10:48:45Z on 2016-05-18 for the respective scores. Otherwise approve a different birth time and derive all five times from it.
```

Rationale: The minute after birth is part of what these coded observations mean.

Acceptance check: Calculate elapsed minutes from each contained birthTime and compare the code/display and narrative.

Human decision: Owner must confirm whether the birth time or observation timeline is the intended fixture.

Depends on: None

### E03 \| P1 \| Correction: Reconcile the 2-minute Apgar reflex answer and score

Location: Observation/2minute-apgar-score: reflex-irritability component

Evidence: LA6721-0 and its displayed response describe the same response scored 2 in the later examples, but this example assigns weight/local score 1 and text describing a lesser response. Its total of 5 follows the local weights.

Evidence sources: EX32, EX33, EX34, EX35

Proposed change: Make response code, display, free text, item weight and total mutually consistent.

Replacement / minimum content:

```
If the intended response is the one-point reflex response, select its verified answer code and matching display. If LA6721-0 is intended, correct the score/weight and recompute the total. Regenerate the narrative in either case.
```

Rationale: A scoring example must not teach a contradictory code-to-score mapping.

Acceptance check: Validate the chosen LOINC answer against its answer list, sum the component weights and compare the total.

Human decision: A scoring/terminology reviewer must select the intended response; an unverified substitute code is not supplied.

Depends on: None

### E04 \| P1 \| Correction: Correct the bone-density UCUM denominator

Location: Observation/bmd: valueQuantity.code

Evidence: The displayed unit is g/cm², but the UCUM code is g/cm-2. The negative exponent in the denominator changes the dimension. LOINC 24701-5 gives g/cm2 as an example UCUM unit.

Evidence sources: EX38, UCUM, LOINCBMD

Proposed change: Correct the machine-readable unit after confirming the stated areal-density intent.

Replacement / minimum content:

```
Set valueQuantity.code to g/cm2; retain system http://unitsofmeasure.org and the g/cm² display. Preserve 0.887 only after confirming it is an areal-density value.
```

Rationale: The current code and display describe different dimensions.

Acceptance check: Parse the UCUM code and verify mass per area; compare all published formats.

Human decision: Confirm the existing numeric value and intended dimension; this report does not clinically interpret the result.

Depends on: None

### E05 \| P1 \| Correction: Remove the future last-menstrual-period date

Location: Observation/date-lastmp: effectiveDateTime and valueDateTime

Evidence: The observation is effective 2016-01-24, but its last-menstrual-period value is 2016-12-30.

Evidence sources: EX22

Proposed change: Choose dates that fit the explicitly retrospective observation.

Replacement / minimum content:

```
Use an owner-approved last-menstrual-period date on or before the assessment time, or move the assessment date to the intended later encounter. Update narrative and all serializations together.
```

Rationale: The current result is future information presented as a last event.

Acceptance check: Assert valueDateTime &lt;= effectiveDateTime for this scenario.

Human decision: Owner must choose the intended dates; no historical date is guessed.

Depends on: None

### E14 \| P1 \| Correction: Use a gender-identity answer that matches the question

Location: Observation/clinical-gender: code and valueCodeableConcept

Evidence: LOINC 76691-5 asks about gender identity, but the answer uses SNOMED CT 191788006 with display Feminism in boy \(finding\), a different kind of assertion.

Evidence sources: EX36, PATIENT

Proposed change: Replace the mismatched answer and modernize the scenario wording.

Replacement / minimum content:

```
Use an owner-approved synthetic self-reported gender-identity response with a verified answer concept and matching display/text. Do not infer gender identity from Patient.gender or reuse a behavioral finding as the answer.
```

Rationale: The current example misrepresents the question-answer semantics and can mislead implementers.

Acceptance check: Verify the answer list/code and distinguish self-reported identity from administrative gender.

Human decision: Terminology and clinical owners must select the intended synthetic response.

Depends on: None

### E20 \| P1 \| Correction: Rebuild the linked lipid report as one consistent dataset

Location: Diagnostics-linked DiagnosticReport/lipid-panel-example and its four contained Observations

Evidence: Patient/pat2 is Donald Duck, but the report/narrative names Wile E. Coyote. Narrative and structured dates differ. The report names a direct-LDL panel, while the LDL component is calculated; narrative LDL is 4.2 versus structured 4.6. HDL/LDL mass-concentration codes use mmol/L.

Evidence sources: LIPIDREPORT, DIAG, DEP06

Proposed change: Choose an internally coherent synthetic report, then regenerate the complete narrative.

Replacement / minimum content:

```
Align patient identity, effective/issued dates, panel method, LDL value and component code-property-unit pairs. Resolve whether substance-concentration codes or converted mass values are intended. Preserve strict reference-limit meaning using the supported comparator where appropriate; do not let a narrative < or > become an inclusive structured limit.
```

Rationale: This linked teaching report has multiple mutually reinforcing identity and result inconsistencies.

Acceptance check: Recalculate any derived LDL after the method decision; verify all four contained results, reference limits and every narrative cell.

Human decision: Clinical and terminology owners must approve the intended dataset. Do not conflate this report with the six separate 2015 lipid examples.

Depends on: None

### E24 \| P1 \| Correction: Fix statistics example terminology and request parameters

Location: Observation $stats request and two inline XML Observation results

Evidence: The request and response use min/max, but the required CodeSystem defines minimum/maximum. Response Coding.system is a valueset URL rather than the canonical statistic code system.

Evidence sources: STATS, STATDEF, STATOP

Proposed change: Correct both sides of the worked operation exchange.

Replacement / minimum content:

```
Use statistic=minimum and statistic=maximum in the request. In each result component set Coding.system to http://hl7.org/fhir/observation-statistics; use average, maximum, minimum and count as appropriate. Keep UCUM units aligned with the statistic and preserve the two-result Parameters envelope.
```

Rationale: The worked exchange otherwise teaches invalid code-system/code pairs.

Acceptance check: Validate the request parameters against the bound value set and both response Observations against the chosen aggregate-result representation.

Human decision: OO should confirm aggregate-result profile guidance in D11; the code spelling/system corrections are directly supported.

Depends on: D11, D12

### E06 \| P2 \| Correction: Complete the infant and spirometry reference graphs

Location: Vomiting, smoke exposure, tracheostomy care, blood-group examples and spirometry

Evidence: Six indexed examples reference Patient/infant without a catalog target; spirometry references Patient/PatientId-patientId for subject and performer. Generated narratives contain broken-link.html.

Evidence sources: EX39, EX43, EX44, EX45, EX46, EX47, EX48, LISTSRC

Proposed change: Provide coherent synthetic targets or deliberately rebind to appropriate existing fixtures.

Replacement / minimum content:

```
Publish one consistent synthetic infant fixture for the six linked examples, retaining the mother-focused distinction in tracheostomy care. Resolve the spirometry patient and performer according to the intended scenario. Rebuild narratives and reference links.
```

Rationale: These are demonstrated publication/reference-completeness issues, not a rule that every logical Reference must resolve.

Acceptance check: Follow every published link and verify identities; do not substitute an unrelated adult merely to obtain HTTP 200.

Human decision: Owner must approve fixture identities and who performed spirometry.

Depends on: None

### E07 \| P2 \| Correction: Finish and correctly present the IV-pump Bundle

Location: observation-example-devicemetricfocus: Bundle entries and generated page

Evidence: The file is a collection Bundle with Observation, DeviceAssociation and DeviceMetric entries. The DeviceMetric resolves internally; Device/example-IV-pump does not. The page is labeled as an Observation example while its outer narrative is effectively empty.

Evidence sources: EX10, INDEX, DEF

Proposed change: Add or publish the missing pump Device and make the Bundle demonstration navigable.

Replacement / minimum content:

```
Resolve Device/example-IV-pump consistently from the Observation, DeviceAssociation and DeviceMetric. Label the index/page as a Bundle demonstrating Observation focus on DeviceMetric; render the nested entries and repair the nested focus hyperlink.
```

Rationale: Readers need to distinguish a present internal metric from a genuinely missing device.

Acceptance check: Resolve fullUrl, relative and contained references within the Bundle and catalog; inspect its rendered narrative.

Human decision: Resolve the patient/device subject decision in D02 before finalizing this teaching graph.

Depends on: D02

### E08 \| P2 \| Question: Decide whether the IV-pump example measures volume or flow

Location: Bundled Observation code, valueQuantity and focused DeviceMetric.type

Evidence: The Observation code describes intravascular fluid intake over eight hours, its unit is mL/\(8.h\), and the metric describes pump flow. These may mix interval volume and flow-rate semantics.

Evidence sources: EX10, DM

Proposed change: Select one measurand and align code, metric, unit and effective period.

Replacement / minimum content:

```
For accumulated eight-hour intake, use a compatible volume result and interval. For instantaneous or interval-normalized flow, use a verified flow-rate code and unit. Do not simply relabel the unit without resolving the intended quantity.
```

Rationale: Dimensional and temporal meaning matter more than whether the syntax parses.

Acceptance check: Have device/terminology reviewers verify the chosen code-property-unit combination.

Human decision: Devices and OO must decide the intended measurand.

Depends on: D02

### E09 \| P2 \| Correction: Remove result interpretation from an unperformed blood pressure

Location: Observation/blood-pressure-cancel: interpretation and component.dataAbsentReason

Evidence: There are no numeric results, but interpretation is Low. The note says the order was cancelled; component absence reasons say not-asked.

Evidence sources: EX15, DOC, STATUS

Proposed change: Remove unsupported interpretation and align the absence explanation with the scenario.

Replacement / minimum content:

```
Delete the Low interpretation. If the measurements were not performed because the order was cancelled, use the appropriate verified not-performed absence concept and explain cancellation with statusReason or note. Do not add invented measurements.
```

Rationale: An unperformed test does not establish low blood pressure.

Acceptance check: Confirm both components remain present as required by the BP profile and carry consistent absence reasons.

Human decision: Owner must confirm whether not-asked was intentional or an inherited placeholder.

Depends on: D04

### E10 \| P2 \| Correction: Match eGFR reference-range population to the result code

Location: Observation/f205: first component.code and component.referenceRange.appliesTo

Evidence: The first component uses the Black-population MDRD concept 48643-1, but its reference-range population text says non-black. The second component uses non-Black concept 48642-3; the top-level code is the general MDRD concept 33914-3.

Evidence sources: EX26, LOINCEGFR

Proposed change: Align population labels and range applicability without silently changing the historical equation.

Replacement / minimum content:

```
Confirm which population the first component represents and correct its code/display, referenceRange.appliesTo and narrative together. Keep the existing paired historical-method example only with explicit method/context; a modern equation would be a separate approved example.
```

Rationale: The result and its range currently describe different populations.

Acceptance check: Check both result concepts, population labels and method wording against verified terminology.

Human decision: Owner must choose the intended population and whether to retain this historical teaching case.

Depends on: None

### E11 \| P2 \| Correction: Reconcile the sitting-MAP caption, category and dates

Location: Observation/map-sitting and its example-index caption

Evidence: The mean blood-pressure example uses laboratory category, is advertised as demonstrating body-position/delta extensions that are absent, and is final with issued time preceding the end of its effective period.

Evidence sources: EX50, INDEX, VITAL

Proposed change: Choose whether this is a point measurement or a derived temporal result and align all representations.

Replacement / minimum content:

```
For a point-in-time MAP, use vital-signs categorization and coherent effective/issued times, and remove the unsupported extension claim. If a delta/temporal statistic is intended, supply its actual inputs, derivation and approved representation rather than keeping a misleading caption.
```

Rationale: The label, lifecycle and data should describe the same example.

Acceptance check: Check chronology, claimed profile applicability and every advertised feature in the payload.

Human decision: Owner must decide the intended MAP scenario; do not automatically apply a point-in-time profile to an aggregate.

Depends on: D11

### E12 \| P2 \| Question: Review unusual clinical fixture values and ranges

Location: Body-length example; f002 base excess; f005 hemoglobin

Evidence: A 25 cm body length is attached to a patient who is an adult at the observation date. Base excess uses a 7.1-11.2 mmol/L range. Hemoglobin is already 7.2 g/dL, but its 7.5-10 g/dL reference interval needs provenance for this patient.

Evidence sources: EX06, EX18, EX21, DEP04

Proposed change: Have a clinical example owner verify the intended populations, units and reference intervals.

Replacement / minimum content:

```
Use an appropriate synthetic subject/value pair for body length. For the two laboratory intervals, supply the intended method/population provenance or replace the fixtures with owner-approved internally consistent values. Do not replace them with a universal textbook interval.
```

Rationale: Unusual does not itself prove invalid; these require informed human review.

Acceptance check: Record clinical approval and recheck demographics, units, flags and ranges together.

Human decision: Clinical reviewers must decide the intended scenarios and intervals. There is no mmol/L-versus-g/dL serialization defect in f005.

Depends on: None

### E13 \| P2 \| Correction: Make the vital-sign panel represent a coherent time

Location: Observation/vitals-panel: effectiveDateTime and hasMember

Evidence: The panel is dated 1999 and groups three 1999 vital signs with a blood-pressure observation from 2012.

Evidence sources: EX14, EX02, EX03, EX04, EX11, VP

Proposed change: Group observations from the intended encounter/time or clearly select another use case.

Replacement / minimum content:

```
Use a compatible-time blood-pressure member for the 1999 point-in-time panel, or update the complete member set and panel time to a coherent encounter. Preserve organizer=true and at least two hasMember entries.
```

Rationale: A point-in-time teaching panel should not silently span thirteen years.

Acceptance check: Resolve every member; compare subject and effective times with the panel profile.

Human decision: Owner must select the intended measurement event.

Depends on: None

### E15 \| P2 \| Correction: Type the oyster specimen group as specimens

Location: Observation/vp-oyster: contained Group/group1.type

Evidence: Group.type is animal, but its member.entity references are the contained Specimen/bed1 and Specimen/bed2.

Evidence sources: EX41, DEF

Proposed change: Align the group type with its actual membership.

Replacement / minimum content:

```
Set contained Group/group1.type to specimen if retaining the two Specimen members. Keep the observation specimen reference to that group and describe the pooling/sample context clearly.
```

Rationale: The group describes sample members, not animal members. This is not an obs-9 failure: the referenced members are already Specimens.

Acceptance check: Resolve both contained members and compare each resource type with Group.type.

Human decision: Editorial approval; no new design decision required.

Depends on: None

### E16 \| P2 \| Correction: Remove the fictitious Korean profile assertion and complete its UCUM code

Location: krcore-observation-labresult-example-01: meta.profile and valueQuantity

Evidence: The asserted profile is under example.org and renders as a broken link. The glucose result states UCUM and mg/dL display but omits the machine-readable code.

Evidence sources: EX52, DATATYPES

Proposed change: Use a real, versioned profile only if verified; otherwise remove the conformance claim.

Replacement / minimum content:

```
Remove the example.org meta.profile assertion, or replace it with a verified resolvable profile that the instance actually meets. Set valueQuantity.code to mg/dL to match the stated unit. Preserve the Korean text.
```

Rationale: A multilingual example should be usable without a fictitious profile dependency.

Acceptance check: Resolve and validate any retained profile, check UCUM coding and inspect Korean rendering.

Human decision: The profile owner must approve any replacement canonical and package version.

Depends on: None

### E17 \| P2 \| Question: Explain incomplete blood-group panel membership

Location: Observation/bgpanel: code and hasMember

Evidence: The code describes blood type and indirect antibody screening, but members demonstrate only ABO and Rh status.

Evidence sources: EX46, EX47, EX48

Proposed change: Make explicit whether this is a partial panel or a complete panel demonstration.

Replacement / minimum content:

```
Either label the example as a deliberately partial result set and explain missing/pending antibody-screen results, add a coherent antibody-screen member, or use a verified narrower panel code. If it is a pure grouper, demonstrate organizer=true consistently with X02.
```

Rationale: A partial result set can be valid; unexplained incompleteness is a teaching problem, not an automatic cardinality error.

Acceptance check: Compare the approved panel meaning with every member and its lifecycle state.

Human decision: Owner must choose complete versus intentionally partial panel semantics.

Depends on: X02, E06

### E18 \| P2 \| Correction: Resolve the publication status of seven source-only examples

Location: Pinned Observation source files not registered in the example catalog

Evidence: Six alternate Apgar examples and body-height-merged are present in source but absent from the published index. The Apgar graph includes unresolved infant/component targets; body-height-merged is referenced by source Provenance examples. The alternate panel links to the adult 1999 heart-rate example. Its total-score file uses code 32411-1, also used for reflex irritability, and contains no result.

Evidence sources: SO1, SO2, SO3, SO4, SO5, SO6, SO7, LISTSRC, PROVMERGE, PROVVERIFY, EX03

Proposed change: Choose which files are intended for publication, then repair their graph and registration together.

Replacement / minimum content:

```
For the six Apgar files, register and publish a complete, coherent family or explicitly retire obsolete teaching variants with reference cleanup. For body-height-merged, preserve its merge/Provenance scenario and ensure it and its merge-survivor patient are available wherever linked. Do not delete a referenced file solely because it is absent from the index. Before publishing apgar-panel, supply an actual same-newborn Apgar heart-rate member. Correct apgar-score to a verified total-score concept and result, and reconcile its contained newborn with the panel subject and birth-relative time.
```

Rationale: Source-only content must not be mistaken for a successfully published example.

Acceptance check: Search source references before changing registration; build and follow every retained public target.

Human decision: Owners must decide the intended publication status. These are source-only findings, not seven additional published-page defects.

Depends on: E02, E06

### E19 \| P2 \| Question: Resolve the herd assay scale and sampling date

Location: Observation/herd1: valueQuantity, referenceRange.text and effectiveDateTime; pooled-serum specimen

Evidence: The value uses percent while the sample/positive-control thresholds are written as fractions. The specimen collection date is 2017-11-14, but observation effectiveDateTime is 2017-11-20. A leading greater-than sign in Markdown also renders the positive threshold as a blockquote.

Evidence sources: EX42, DOC, DEP16

Proposed change: Confirm the assay convention and relevant time; rewrite the range prose without Markdown ambiguity.

Replacement / minimum content:

```
State whether 0.2 means 0.2 percent or a ratio of 0.2, then align the unit and all thresholds. Use the specimen-collection time for physiologic relevance unless another meaning is explicitly justified. Write "Positive when the ratio is greater than ..." to preserve the comparison in the rendered narrative.
```

Rationale: A percentage/fraction mismatch can change interpretation by a factor of 100.

Acceptance check: Check assay documentation, specimen timing and the rendered inequality text.

Human decision: Assay owner must establish the actual scale and relevant date; no cutoff or numeric conversion is assumed.

Depends on: None

### E21 \| P2 \| Correction: Make the CBC order and report match their listed results

Location: diagnosticreport-example-f001-bloodexam Bundle: ServiceRequest/DiagnosticReport code and result list

Evidence: The request and report use CBC code 58410-2, but results include glucose, base excess and carbon-dioxide partial pressure alongside erythrocytes and hemoglobin.

Evidence sources: CBCREPORT, EX16, EX18, EX19, EX20, EX21

Proposed change: Align order, report code and result membership.

Replacement / minimum content:

```
Either demonstrate a genuine CBC with owner-approved CBC members, or use an appropriate verified code and caption for the mixed examination. Do not delete the valid standalone chemistry examples simply to repair this report.
```

Rationale: The order/report semantics should describe the measurements actually linked.

Acceptance check: Resolve each result and compare its test concept with the chosen report and order.

Human decision: The clinical example owner must choose the intended report type.

Depends on: None

### E22 \| P2 \| Correction: Repair stale catalog terms and stored narrative links

Location: GCS-from-questionnaire and spirometry captions; cholesterol/non-HDL/triglyceride/VLDL narratives

Evidence: The catalog still names QuestionnaireAnswer and DeviceComponent. Four lipid narratives use Patient/pat2 and Specimen/sst as HTML hyperlinks; both public URL paths returned HTTP 404 on 2026-09-03.

Evidence sources: INDEX, EX30, EX39, EX54, EX57, EX58, EX59

Proposed change: Use current resource names and publisher-resolved links.

Replacement / minimum content:

```
Rename the GCS caption to QuestionnaireResponse. Remove the unsupported DeviceComponent claim from spirometry or implement and describe a verified intended device pattern. Regenerate stored lipid narratives so hyperlinks point to published example pages while Reference.reference values remain valid FHIR references.
```

Rationale: FHIR reference strings and public website filenames serve different purposes.

Acceptance check: Open all corrected captions/links; verify the payload resource names and retain correct JSON/XML reference values.

Human decision: Editorial approval; no new design decision required.

Depends on: None

### E25 \| P2 \| Correction: Make abbreviated lastn responses internally consistent

Location: Observation $lastn: three response illustrations

Evidence: Several Bundle fullUrl values disagree with resource.id \(temperature, height, RBC and respiratory-rate fragments\). The examples are explicitly truncated, so their non-parseable JSON is intentional, but identity mismatches are not explained.

Evidence sources: LASTN

Proposed change: Correct identities and captions while preserving the explicit abbreviated-example label.

Replacement / minimum content:

```
Align each illustrated fullUrl tail with resource.id, fix the RBC ID missing its leading 2, and remove copied weight/Lipase labels from heart-rate/lipid sections. Prefer a linked complete downloadable response for each request, with the shortened view retained only as an excerpt.
```

Rationale: Abbreviation is not a reason to teach contradictory Bundle identities.

Acceptance check: Check all 23 illustrated Observation fragments; parse/validate any newly supplied complete responses.

Human decision: Owner chooses whether to add full response files; do not treat the existing snipped excerpts as standalone valid JSON.

Depends on: None

### E23 \| P3 \| Suggestion: Add selective teaching context without inflating every minimal example

Location: Laboratory f203/f204/f206, sampled-data ECG, non-HDL and existing minimal examples

Evidence: Some teaching cases omit collection/result context; ECG leads share identical samples without explaining the synthetic waveform or amplitude scaling. Non-HDL has an unconditional treatment-goal statement. The base resource permits many omitted fields.

Evidence sources: EX24, EX25, EX27, EX28, EX57, DEF

Proposed change: Improve representative examples and explain deliberate simplifications.

Replacement / minimum content:

```
Add meaningful time/specimen context to selected laboratory cases; prefer interoperable UCUM coding where appropriate without declaring all alternate units invalid. Explain the synthetic ECG signal and amplitude conversion/units. Qualify the non-HDL goal as an illustrative, population-dependent statement or remove it. Retain focused eye-color, decimal-precision and multilingual examples.
```

Rationale: Examples should teach their intended concept without unsupported clinical generalizations or mandatory boilerplate.

Acceptance check: Verify any added data clinically and structurally; confirm that no optional base element has been recast as required.

Human decision: Owners decide which examples need fuller context; no new patient data or clinical reference values are supplied.

Depends on: None

## Module findings

### M01 \| P1 \| Correction: Correct the additional-testing relationship arrows

Location: Diagnostics parent-child-structure-3.png

Evidence: The follow-up ServiceRequest points to an Observation using basedOn, but ServiceRequest.basedOn targets request resources, not Observation. The Observation trigger arrow abbreviates a backbone element as if it were a direct reference.

Evidence sources: GROUP3, DIAG, SR, DEF

Proposed change: Draw supported paths and explain the role of the prior result.

Replacement / minimum content:

```
For a result that clinically motivates the new request, use ServiceRequest.reason.reference; for supporting information use supportingInfo.reference, according to intent. Label the trigger arrow Observation.triggeredBy.observation and include its required type in the worked example. Replace obsolete specimenRequest-extension wording only with a verified current mechanism.
```

Rationale: The current diagram invites invalid element/target combinations.

Acceptance check: Instantiate and validate every depicted relationship using the R6 definitions.

Human decision: OO must choose reason versus supporting information and confirm the specimen extension/package.

Depends on: None

### M05 \| P1 \| Correction: Separate drug administration from device-state observations

Location: Device module use case F2: bolus narrative, command mapping and outcome artifacts

Evidence: The scenario records an administered drug bolus as an Observation and generically uses ServiceRequest for the medication action. Observation boundaries exclude uses with a dedicated resource; MedicationAdministration represents actual administration.

Evidence sources: DEVICE, DOC, MEDADMIN, DEF

Proposed change: Distinguish technical configuration/command records from medication ordering and administration.

Replacement / minimum content:

```
Keep configuration measurements or confirmed device state in Observation. Represent the actual bolus in MedicationAdministration and the medication authorization with the appropriate medication-request workflow. If needed, link a relevant Observation through supported partOf/basedOn relationships. State that the device command operates under valid medication authorization; do not imply authorization from the monitoring observation.
```

Rationale: Avoids teaching a medication event as a generic measurement and collapsing distinct workflow roles.

Acceptance check: Review the complete command/order/administration/measurement graph with Pharmacy and Devices owners.

Human decision: Joint owners must confirm the medication and device command workflow; no dose, drug choice or clinical action is recommended.

Depends on: None

### M02 \| P2 \| Correction: Do not use entered-in-error merely to mark suspect data

Location: Device module use case A: Implementation Guidance

Evidence: The module recommends marking suspect measurements with Observation.status such as entered-in-error or by amending with corrected results. Suspicion alone establishes neither an erroneous record nor a corrected result.

Evidence sources: DEVICE, STATUS, EX23

Proposed change: Separate investigation, invalidation and actual correction.

Replacement / minimum content:

```
Record an unresolved quality concern with an appropriate explicit annotation/context and audit trail. Use entered-in-error only when the record is determined erroneous under its definition. Use amended/corrected only for an actual approved update; preserve the prior record/version.
```

Rationale: Lifecycle status changes alter how downstream systems treat the result.

Acceptance check: Walk suspect, confirmed erroneous and corrected-result cases through the final guidance.

Human decision: Owners should agree the interoperable quality-concern representation; no new status code is proposed.

Depends on: None

### M03 \| P2 \| Correction: Retrieve settings already active at the start of a time window

Location: Device module use case B: settings-window query

Evidence: A query confined to settings observations timestamped within the desired interval can miss the last setting established before that interval and still in effect. DeviceMetric references also need resolution to their parent Device.

Evidence sources: DEVICE, DEF, DM

Proposed change: Describe state reconstruction, not just an in-window timestamp search.

Replacement / minimum content:

```
Retrieve the latest applicable setting at or before the window start plus subsequent changes, or retrieve effective periods overlapping the window. Resolve both Device and DeviceMetric linkage patterns. Handle missing history, clock alignment and superseded values explicitly.
```

Rationale: The proposed search otherwise cannot reliably reconstruct active settings.

Acceptance check: Test a setting established before the window, an in-window change, an overlapping period and a missing-history case.

Human decision: Editorial approval; no new design decision required.

Depends on: None

### M04 \| P2 \| Correction: Remove nonexistent DeviceAlert components from threshold guidance

Location: Device module use case C: Implementation Guidance and Data Requirements

Evidence: The module suggests DeviceAlert components, but DeviceAlert has no component element. DeviceMetric describes channels and does not itself supply a current threshold-value field.

Evidence sources: DEVICE, DA, DM, DEF

Proposed change: Use supported threshold Observations, or name a verified extension instead of implying a core element.

Replacement / minimum content:

```
Represent the threshold value and its effective time in an Observation linked to the appropriate DeviceMetric. Link alarm evidence through supported DeviceAlert relationships. If an IG-specific alternative is intended, cite the exact extension/profile and package, not "DeviceAlert components".
```

Rationale: Profiles cannot create an undeclared core component element.

Acceptance check: Validate a concrete alarm/threshold graph and verify every element path and reference target.

Human decision: Devices owners must approve any extension-based alternative.

Depends on: None

### M06 \| P2 \| Question: Make monitoring traceability requirements consistent

Location: Device module use case E: interoperability versus implementation guidance

Evidence: One paragraph says observations must reference both device and order; another says they should reference the device and may reference the order. Both base elements are optional.

Evidence sources: DEVICE, DEF

Proposed change: Decide whether this is a use-case-specific requirement or general implementation advice.

Replacement / minimum content:

```
If mandatory traceability is intended, label it as a requirement of this use case/profile and use consistent SHALL language. Otherwise soften the earlier must and explain that device/basedOn remain optional in the base resource.
```

Rationale: Readers need to know which requirements belong to the base resource and which to a workflow.

Acceptance check: Check the complete scenario for consistent must/should/may language and profile support.

Human decision: Devices and OO must choose the intended traceability requirement.

Depends on: None

### M07 \| P2 \| Question: Clarify nutrition measurements, assessments and diagnoses

Location: Nutrition module clinical scenarios

Evidence: The narrative labels comprehensive assessment as Observation, places weight/history in ClinicalImpression, and uses both Observation and Condition for moderate malnutrition. Observation boundaries distinguish measurements from diagnoses and refer to ClinicalAssessment.

Evidence sources: NUTR, DOC

Proposed change: Assign each statement a deliberate resource role and update relocated-resource links.

Replacement / minimum content:

```
Represent measured weight and defined assessment scores/findings as Observations; represent an asserted malnutrition diagnosis as Condition. Identify the intended assessment container and its current package/resource name, rather than retaining an unexplained ClinicalImpression label. Explain any legitimate overlap between a screening finding and diagnosis.
```

Rationale: Preserves the distinction between evidence, assessment process and diagnostic assertion.

Acceptance check: Trace each scenario statement to its approved resource and verify any incubator link/package.

Human decision: Nutrition and OO owners must approve the intended assessment workflow and relocation terminology.

Depends on: None

### M08 \| P2 \| Correction: Remove the false universal claim about mandatory profiles

Location: Medication Definition module: profiling comparison

Evidence: The module says no other core resources mandate profiles. Observation Core Profiles and Vital Signs explicitly impose profile conformance for specified concepts.

Evidence sources: MEDDEF, DOC, VITAL

Proposed change: Remove the universal contrast without changing Medication Definition design decisions.

Replacement / minimum content:

```
Delete "No other core resources mandate the use of profiles." Explain the Medication Definition resource-design rationale on its own terms, or qualify any comparison with the actual scope and exceptions.
```

Rationale: A module-level architectural explanation should not contradict an explicit core SHALL.

Acceptance check: Compare the revised passage with Observation core-profile conformance wording.

Human decision: Editorial approval; no new design decision required.

Depends on: None

### M09 \| P3 \| Suggestion: Make grouping diagrams readable and domain-neutral

Location: Diagnostics grouping prose and parent-child diagrams

Evidence: The grouping explanation centers on a patient at one point in time even though Observation supports non-patient subjects and periods. The microbiology diagram needs a clearer distinction between a result-bearing organism parent and a pure susceptibility grouper.

Evidence sources: DIAG, GROUP1, GROUP2, GROUP3, DEF

Proposed change: Refine captions and legends, preserving both approved grouping patterns.

Replacement / minimum content:

```
Use subject and clinically relevant time/period where patient-only wording is unnecessary. Explain Bundle as packaging, not a universal report requirement. Label pure organizers separately from result-bearing parents, clarify the apparent organism self-loop, and remove spell-check underlines from publication artwork.
```

Rationale: Helps non-laboratory implementers understand the patterns without mistaking diagram shorthand for constraints.

Acceptance check: Have a non-laboratory reviewer follow the diagram legend and inspect the final exported artwork.

Human decision: Editorial approval; no new design decision required.

Depends on: X02, M01

## Cross-layer findings

### X01 \| P1 \| Correction: Remove unsupported genomic reference paths

Location: Genomic Reporting notes; Diagnostics resource map and legend

Evidence: The prose permits Observation.partOf and derivedFrom to target GenomicStudy. Current target lists exclude it. The module diagram also presents direct Observation links to GenomicStudy/MolecularDefinition as core references.

Evidence sources: DOC, DEF, DIAG, DGM

Proposed change: Align prose and diagram with this release and clearly separate additional-resource or IG mechanisms.

Replacement / minimum content:

```
Delete the two unsupported core GenomicStudy reference instructions. Retain the supported derivedFrom-to-DocumentReference case for source files. Depict any alternative genomic relationship only after naming and verifying its extension/profile and package. Revise arrows and legend so they do not imply unsupported core target types.
```

Rationale: Following the current guidance would create instances outside the R6 core reference model.

Acceptance check: Compare every Observation arrow and prose path with the pinned targetProfile/type lists, including removed MolecularSequence value/reference types.

Human decision: OO and Clinical Genomics must choose the supported package-specific alternative; none is invented here.

Depends on: None

### X02 \| P1 \| Correction: Apply organizer constraints consistently across panels and absence guidance

Location: Cancellation notes; Vital Signs mandatory-data list; grouping notes and Diagnostics diagrams

Evidence: obs-11 forbids value\[x\], dataAbsentReason and component when organizer=true. Cancellation instructions require dataAbsentReason for every requested panel, and the Vital Signs list requires a result or absent reason without a panel exception.

Evidence sources: DOC, DEF, VITAL, VP, DIAG, GROUP1, GROUP2, EX14, EX60

Proposed change: Add the organizer exception wherever result/absence requirements are stated; distinguish grouping from result-bearing parents.

Replacement / minimum content:

```
For an organizer Observation, set organizer=true and use hasMember; do not populate value[x], dataAbsentReason or component. Explain cancellation with statusReason/note as appropriate, and apply absence reasons to unperformed result-bearing members. A result-bearing parent may also have hasMember without being an organizer. The Vital Signs Panel requires at least two members; an unspecified member is optional, not the entire membership list.
```

Rationale: Reconciles the new R6 organizer model without banning valid microbiology value-plus-members patterns.

Acceptance check: Check cancelled panels, vital-sign panels and organism/susceptibility diagrams against obs-11 and profile cardinalities.

Human decision: OO should confirm panel lifecycle wording with D04; the current obs-11 prohibition itself is explicit.

Depends on: D04

## Suggested missing examples

### N01 \| P2 \| Missing example: Publish complete examples of both R6 grouping patterns

Location: Observation index and Diagnostics grouping guidance

Evidence: The index includes organizer panels, but not a matched, end-to-end example pair that clearly distinguishes the two newly emphasized report-grouping patterns.

Evidence sources: INDEX, DOC, DIAG, EX60

Proposed change: Add a small pair using the same synthetic scenario.

Replacement / minimum content:

```
Include a coherent subject, ServiceRequest, Specimen where relevant, DiagnosticReport and atomic results. Demonstrate one report pointing to a panel organizer and another directly grouping its result Observations. Include codes, states, times and resolved links; label organizer=true only on pure groupers.
```

Rationale: Makes the ballot grouping guidance executable and comparable.

Acceptance check: Validate both graphs, exercise the documented search paths and compare rendered narratives.

Human decision: OO selects the approved clinical fixture and decides whether both belong in core.

Depends on: X02, E20, E21

### N02 \| P2 \| Missing example: Demonstrate triggeredBy with a reflex/additional-testing chain

Location: Observation.triggeredBy and Diagnostics additional-testing guidance

Evidence: No indexed Observation uses triggeredBy; the additional-testing diagram currently has incorrect relationship labels.

Evidence sources: DEF, INDEX, DIAG

Proposed change: Add a complete trigger-to-order-to-result example.

Replacement / minimum content:

```
Include the original result, a new request with a supported reason/supportingInfo reference, and the follow-up Observation with triggeredBy.observation and required type. State whether testing is reflex, repeat or re-run using verified allowed terminology; distinguish basedOn from derivedFrom.
```

Rationale: Exercises an otherwise unillustrated relationship and anchors the corrected diagram.

Acceptance check: Resolve and validate the graph; confirm the trigger type and lifecycle.

Human decision: OO selects the trigger scenario and its terminology.

Depends on: M01

### N03 \| P2 \| Missing example: Show exception statusReason and correction history

Location: Observation lifecycle examples

Evidence: The 60 indexed Observations contain 56 final, two cancelled, one entered-in-error and one preliminary result. None populates statusReason.

Evidence sources: INDEX, DEF, STATUS, EX15, EX17, EX23

Proposed change: Add a compact lifecycle family after resolving the status semantics.

Replacement / minimum content:

```
Show a cancelled order result, an attempted but unobtainable result if distinct, and an actual corrected or entered-in-error record with appropriate statusReason/note. Explain version/history or Provenance handling. Include an organizer cancellation without forbidden dataAbsentReason.
```

Rationale: Covers new status explanation and prevents ambiguous examples from defining the lifecycle by accident.

Acceptance check: Validate each instance and manually review transitions, absent reasons and retained history.

Human decision: OO must approve the lifecycle distinctions and synthetic values.

Depends on: D04, X02, M02

### N04 \| P2 \| Missing example: Exercise the new R6 contextual and supporting-device elements

Location: Observation.context, supportingDevice and bodyStructure

Evidence: None of the 60 indexed Observations uses these elements; five still illustrate deprecated bodySite.

Evidence sources: DEF, INDEX, DOC

Proposed change: Add or deliberately modernize representative examples rather than changing every legacy fixture.

Replacement / minimum content:

```
Show clinically relevant interpretive context, a measurement device distinct from supporting equipment, and coded/referenced anatomy using the actual bodyStructure CodeableReference shape. Use resolved targets and state which optional elements are present solely for teaching.
```

Rationale: The R6 structure should have at least one clear, current worked illustration.

Acceptance check: Validate target types/cardinalities and check the new role comparison against the example.

Human decision: OO/Devices select a plausible scenario and approve supporting-device semantics.

Depends on: D07, D02

### N05 \| P3 \| Missing example: Illustrate coded normal values and result attachments

Location: Observation.referenceRange.normalValue and valueAttachment

Evidence: The indexed examples do not demonstrate a coded normal value or top-level Attachment result. The sampled-data example already demonstrates waveform components and should not be counted as missing waveform coverage.

Evidence sources: DEF, INDEX, DOC, EX28

Proposed change: Add two focused examples with explicit boundaries.

Replacement / minimum content:

```
First, show a coded result with a normalValue reference range using the rule approved in D08. Second, show a small synthetic result Attachment and explain how it differs from an Observation derived from a DocumentReference source file. Avoid private data and external unresolved binaries.
```

Rationale: Covers supported forms without implying that attachments replace diagnostic reports.

Acceptance check: Validate the chosen normal-range form, attachment metadata/content and the derivedFrom comparison.

Human decision: OO selects appropriate examples and settles normalValue semantics.

Depends on: D08

### N06 \| P3 \| Missing example: Show an R6 product subject and device-setting history

Location: Observation.subject target expansion; Device/BDP/Nutrition module roles

Evidence: The current corpus has patient, animal/specimen and device scenarios, but not a worked product-subject example or a complete reconstructable settings history.

Evidence sources: DEF, INDEX, DEVICE, BDP, NUTR

Proposed change: Add a small non-patient product-quality example and a time-window settings example.

Replacement / minimum content:

```
For product quality, use one supported product subject with approved measurement/unit and optional specimen context. For settings, include an initial setting before the query window, a change within it, linked DeviceMetric/Device and a measurement affected by the active setting. Clearly identify synthetic values.
```

Rationale: Demonstrates broader R6 scope and makes the module search advice testable.

Acceptance check: Verify product target types and reconstruct the correct active setting at both window boundaries.

Human decision: Relevant domain owners select the product and device fixtures.

Depends on: D02, M03

## Verification performed

FHIR validator: not-run. No full validator run against a version-locked core/profile/terminology dependency set was performed. Static checks below do not establish FHIR conformance.

Publisher: not-run. The existing official CI output was inspected; no new core build was run and no source was changed. Publisher logs for the final proposed revision do not yet exist.

Terminology: not-run. No comprehensive terminology-server validation. Targeted checks used the published FHIR status/statistics code systems, LOINC 24701-5 and 48642-3, and the UCUM specification. Unverified replacement codes and clinical ranges are explicitly gated.

Semantic review: failed. Review completed across the inventoried documentation, examples and six relevant modules; demonstrated contradictions remain. Failed means the consistency acceptance bar was not met, not that review execution stopped.

Serialization syntax: passed. All 60 indexed JSON files parsed with Decimal-preserving numeric handling, all 60 XML files parsed, and all 60 Turtle files parsed with task-local rdflib 7.1.4. static-qa.json records the results; syntax success is not model or clinical validation.

Targeted XML/JSON consistency: passed. Compared overlapping non-narrative primitive paths with exact decimal handling and normalized line endings; no differences found. This is not a complete round-trip check: primitive-extension/attribute special cases, path cardinality parity and RDF semantic equivalence were not proven.

Selected invariant screening: passed. No failures found in the limited checks for required code/status, single value choice, obs-3/6/10/11 in the indexed corpus. This script does not execute FHIRPath, profile slicing, all base invariants, terminology bindings or reference constraints.

Published narrative/reference review: failed. Inspected every indexed HTML narrative and direct graph context. Broken generated links and incoherent references are identified in E01, E06, E07, E16, E18 and E22; not all external URLs in the full specification were crawled.

Module visual review: passed. Visually inspected 11 relevant diagrams: eight Diagnostics figures, DeviceModule.svg and two Biologically Derived Product workflows. Semantic corrections are listed separately; inspection success does not mean the diagrams are correct.

DOCX visual QA: passed. All 49 pages rendered with render\_docx.py/LibreOffice and visually inspected. A split replacement label was repaired. Final pages and Markdown/Word text parity were rechecked; internal QA is retained.

## Publication acceptance checklist

- Pending: Resolve each P1 correction and document disposition of every P2/P3 item and owner question; do not relabel suggestions as mandatory base requirements.

- Pending: Approve each clinical fixture, terminology change, population label, assay scale and chronology; regenerate all representations and narratives from the approved source.

- Pending: Build a final example inventory from the publication revision, including source-only and inline examples; explain all remaining exclusions and eliminate unintended missing targets.

- Pending: Run the current FHIR validator with pinned core/profile/extension and terminology dependencies; record versions, commands, warnings and errors. Include Bundle/contained graphs, operation examples and negative/positive invariant tests.

- Pending: Run the relevant core Publisher build; inspect generated HTML, JSON, XML, Turtle, links, profile/invariant pages and all changed module diagrams. A green build alone is not semantic approval.

- Pending: Recheck organizer/absence rules, subject/focus semantics, genomic reference paths, operation traversal/terminology and medication/device boundaries across all affected surfaces.

- Pending: Test documented search/operation examples and device-state reconstruction against an implementation or controlled fixture set; distinguish results from examples that are only illustrative.

- Pending: Record the actual final revision and regenerate both review formats from the same data after dispositions change; obtain human publication review separately.

## Limitations and decision gates

- This is a pinned CI review, not a claim about every R6 release or every Observation across all FHIR/IG packages. CI can be inconsistent and can change after retrieval. Recheck the final publication revision.

- The banner mentions Ballot5, while package/version metadata remains 6.0.0-ballot4. This report identifies the actual metadata and commit; release editors should confirm banner/version alignment rather than infer a different package version.

- No FHIR validator, terminology service or fresh Publisher build was run. JSON/XML/Turtle parsing and selected static checks are explicitly limited. Clinical plausibility, answer-list membership, assay ranges and normative design decisions require the identified owners.

- The seven source-only examples were inspected in pinned source. Missing public/index output is disclosed, not concealed as reviewed published content. The intentional failing invariant test is excluded.

- Independent IG examples, exhaustive linked-resource reviews, live search/operation execution, full terminology verification and external clinical workflows are outside scope. The current build has no fully exercised acceptance suite for these proposed changes in this review.

- Prior example-review claims were rechecked rather than copied. f005 already uses g/dL; cancelled blood pressure has no numeric result; the DeviceMetric exists inside its Bundle; logical/display-only references and optional omissions are not automatically invalid.

- Replacement text and element edits are advisory. Bounded owner decisions are supplied when evidence does not justify an exact replacement code, date, value, range or workflow. No actual FHIR source edits, tickets or external publication were made.

D02: OO and Devices must decide the intended normative patient-association rule and device-centric example design.

D04: OO must decide the intended status transition and when existing cancelled examples remain appropriate.

D08: OO must decide whether normalValue alone is a sufficient reference range.

D09: Terminology and OO owners must confirm the mapping scope and any extension to its expression.

D11: Vital Signs owners must confirm the intended temporal-aggregation restriction.

E08: Devices and OO must decide the intended measurand.

E12: Clinical reviewers must decide the intended scenarios and intervals. There is no mmol/L-versus-g/dL serialization defect in f005.

E17: Owner must choose complete versus intentionally partial panel semantics.

E19: Assay owner must establish the actual scale and relevant date; no cutoff or numeric conversion is assumed.

M06: Devices and OO must choose the intended traceability requirement.

M07: Nutrition and OO owners must approve the intended assessment workflow and relocation terminology.

## Sources

[BUILD: Current build identity](<https://build.fhir.org/version.info>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: FhirVersion, buildId, generation date.

[DOC: Observation documentation](<https://build.fhir.org/observation.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Scope, boundaries, Notes 10.1.5, core profiles, search and operations overview.

[DEF: Observation computable definition](<https://build.fhir.org/observation.profile.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: snapshot.element; cardinalities, types, bindings and constraints.

[DETAIL: Observation detailed definitions](<https://build.fhir.org/observation-definitions.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Element definitions and comments.

[INDEX: Observation example index](<https://build.fhir.org/observation-examples.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: All 60 listed entries and captions.

[MAP: Observation mappings](<https://build.fhir.org/observation-mappings.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: SNOMED CT concept-domain mapping and other mappings.

[PROFILES: Observation profile index](<https://build.fhir.org/observation-profiles.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Core and shared profiles.

[OPS: Observation operations](<https://build.fhir.org/observation-operations.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Operations index; lastn and stats overview.

[VITAL: Vital Signs guidance](<https://build.fhir.org/observation-vitalsigns.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Mandatory data, conformance, formal-view introduction and profile table.

[VP: Vital Signs Panel profile](<https://build.fhir.org/vitalspanel.profile.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation definition, organizer, hasMember.

[BP: Blood Pressure profile](<https://build.fhir.org/bp.profile.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation definition; component slices.

[BH: Body Height profile](<https://build.fhir.org/bodyheight.profile.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Constraint vs-4 and dataAbsentReason.condition.

[VB: Vital Signs Base profile](<https://build.fhir.org/vitalsigns.profile.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: effective\[x\], vsp-1 and vsp-2.

[STATUS: Observation status codes](<https://build.fhir.org/codesystem-observation-status.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Required status codes and definitions.

[DIAG: Diagnostics module](<https://build.fhir.org/diagnostics-module.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Resource map, grouping, additional testing, imaging, common use cases.

[DEVICE: Device module](<https://build.fhir.org/device-module.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Use cases A-F, implementation guidance, data requirements and resource map.

[NUTR: Nutrition module](<https://build.fhir.org/nutrition-module.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Assessment and malnutrition scenarios.

[BDP: Biologically Derived Product module](<https://build.fhir.org/biologically-derived-product-module.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation roles and workflow illustrations.

[WORKFLOW: Workflow module](<https://build.fhir.org/workflow-module.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Event pattern and Observation roles.

[MEDDEF: Medication Definition module](<https://build.fhir.org/medication-definition-module.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Resource-boundary and profiling discussion.

[SR: ServiceRequest structure](<https://build.fhir.org/servicerequest.profile.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: basedOn, reason, supportingInfo.

[DA: DeviceAlert structure](<https://build.fhir.org/devicealert.profile.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Elements and derivedFrom; no component element.

[DM: DeviceMetric structure](<https://build.fhir.org/devicemetric.profile.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: device, type and unit; no current threshold-value element.

[PATIENT: Patient guidance](<https://build.fhir.org/patient.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Gender identity and administrative gender.

[DATATYPES: FHIR datatypes](<https://build.fhir.org/datatypes.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Reference, Quantity, CodeableConcept and SampledData.

[MEDADMIN: MedicationAdministration](<https://build.fhir.org/medicationadministration.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Scope and boundaries of medication administration records.

[LIPIDREPORT: Linked lipid DiagnosticReport](<https://build.fhir.org/diagnosticreport-example-lipid-panel.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Narrative, subject, dates and four contained Observations.

[CBCREPORT: Linked blood examination Bundle](<https://build.fhir.org/diagnosticreport-example-f001-bloodexam.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: DiagnosticReport and ServiceRequest codes and result membership.

[DGM: Diagnostics resource diagram](<https://build.fhir.org/diagnostic-module-resources.png>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Solid reference arrows and legend.

[GROUP1: Grouping pattern 1 diagram](<https://build.fhir.org/parent-child-structure-1.png>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Organizer grouping.

[GROUP2: Microbiology grouping diagram](<https://build.fhir.org/parent-child-structure-2.png>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Organism result and susceptibility grouping.

[GROUP3: Additional testing diagram](<https://build.fhir.org/parent-child-structure-3.png>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Follow-up ServiceRequest basedOn and Observation triggeredBy arrows.

[DEVMAP: Device resource diagram](<https://build.fhir.org/DeviceModule.svg>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Device, DeviceMetric, Observation and association relationships.

[PSRC: Pinned Observation source](<https://github.com/HL7/fhir/blob/09dfb700767aa757dd405d56c62bf41c5007e0f0/source/observation/structuredefinition-Observation.xml>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Computable source matching buildId 09dfb70076.

[NOTESRC: Pinned Observation notes](<https://github.com/HL7/fhir/blob/09dfb700767aa757dd405d56c62bf41c5007e0f0/source/observation/observation-notes.xml>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Source of the rendered Notes sections.

[LISTSRC: Pinned Observation example catalog](<https://github.com/HL7/fhir/blob/09dfb700767aa757dd405d56c62bf41c5007e0f0/source/observation/list-Observation-examples.xml>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Build example registration and captions.

[FAILFIX: Intentional negative invariant fixture](<https://github.com/HL7/fhir/blob/09dfb700767aa757dd405d56c62bf41c5007e0f0/source/observation/invariant-tests/obs-10.f2.fail.xml>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Excluded negative test; not a publication example.

[UCUM: UCUM specification](<https://ucum.org/ucum>)

Version/snapshot: Official primary source accessed 2026-09-03. Location: Unit exponents and division syntax; accessed 2026-09-03.

[LOINCBMD: LOINC 24701-5](<https://loinc.org/24701-5/>)

Version/snapshot: Official primary source accessed 2026-09-03. Location: Bone density concept; example UCUM g/cm2.

[LOINCEGFR: LOINC 48642-3](<https://loinc.org/48642-3/>)

Version/snapshot: Official primary source accessed 2026-09-03. Location: Non-Black MDRD estimated GFR concept.

[EX01: observation-example](<https://build.fhir.org/observation-example.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/example; associated .json, .xml and .ttl files captured with hashes.

[EX02: observation-example-respiratory-rate](<https://build.fhir.org/observation-example-respiratory-rate.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/respiratory-rate; associated .json, .xml and .ttl files captured with hashes.

[EX03: observation-example-heart-rate](<https://build.fhir.org/observation-example-heart-rate.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/heart-rate; associated .json, .xml and .ttl files captured with hashes.

[EX04: observation-example-body-temperature](<https://build.fhir.org/observation-example-body-temperature.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/body-temperature; associated .json, .xml and .ttl files captured with hashes.

[EX05: observation-example-body-height](<https://build.fhir.org/observation-example-body-height.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/body-height; associated .json, .xml and .ttl files captured with hashes.

[EX06: observation-example-body-length](<https://build.fhir.org/observation-example-body-length.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/body-length; associated .json, .xml and .ttl files captured with hashes.

[EX07: observation-example-head-circumference](<https://build.fhir.org/observation-example-head-circumference.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/head-circumference; associated .json, .xml and .ttl files captured with hashes.

[EX08: observation-example-bmi](<https://build.fhir.org/observation-example-bmi.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/bmi; associated .json, .xml and .ttl files captured with hashes.

[EX09: observation-example-bmi-using-related](<https://build.fhir.org/observation-example-bmi-using-related.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/bmi-using-related; associated .json, .xml and .ttl files captured with hashes.

[EX10: observation-example-devicemetricfocus](<https://build.fhir.org/observation-example-devicemetricfocus.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Bundle/example-observation-device-flowratemetric; associated .json, .xml and .ttl files captured with hashes.

[EX11: observation-example-bloodpressure](<https://build.fhir.org/observation-example-bloodpressure.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/blood-pressure; associated .json, .xml and .ttl files captured with hashes.

[EX12: observation-example-bloodpressure-dar](<https://build.fhir.org/observation-example-bloodpressure-dar.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/blood-pressure-dar; associated .json, .xml and .ttl files captured with hashes.

[EX13: observation-example-mbp](<https://build.fhir.org/observation-example-mbp.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/mbp; associated .json, .xml and .ttl files captured with hashes.

[EX14: observation-example-vitals-panel](<https://build.fhir.org/observation-example-vitals-panel.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/vitals-panel; associated .json, .xml and .ttl files captured with hashes.

[EX15: observation-example-bloodpressure-cancel](<https://build.fhir.org/observation-example-bloodpressure-cancel.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/blood-pressure-cancel; associated .json, .xml and .ttl files captured with hashes.

[EX16: observation-example-f001-glucose](<https://build.fhir.org/observation-example-f001-glucose.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/f001; associated .json, .xml and .ttl files captured with hashes.

[EX17: observation-example-unsat](<https://build.fhir.org/observation-example-unsat.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/unsat; associated .json, .xml and .ttl files captured with hashes.

[EX18: observation-example-f002-excess](<https://build.fhir.org/observation-example-f002-excess.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/f002; associated .json, .xml and .ttl files captured with hashes.

[EX19: observation-example-f003-co2](<https://build.fhir.org/observation-example-f003-co2.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/f003; associated .json, .xml and .ttl files captured with hashes.

[EX20: observation-example-f004-erythrocyte](<https://build.fhir.org/observation-example-f004-erythrocyte.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/f004; associated .json, .xml and .ttl files captured with hashes.

[EX21: observation-example-f005-hemoglobin](<https://build.fhir.org/observation-example-f005-hemoglobin.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/f005; associated .json, .xml and .ttl files captured with hashes.

[EX22: observation-example-date-lastmp](<https://build.fhir.org/observation-example-date-lastmp.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/date-lastmp; associated .json, .xml and .ttl files captured with hashes.

[EX23: observation-example-f202-temperature](<https://build.fhir.org/observation-example-f202-temperature.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/f202; associated .json, .xml and .ttl files captured with hashes.

[EX24: observation-example-f203-bicarbonate](<https://build.fhir.org/observation-example-f203-bicarbonate.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/f203; associated .json, .xml and .ttl files captured with hashes.

[EX25: observation-example-f204-creatinine](<https://build.fhir.org/observation-example-f204-creatinine.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/f204; associated .json, .xml and .ttl files captured with hashes.

[EX26: observation-example-f205-egfr](<https://build.fhir.org/observation-example-f205-egfr.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/f205; associated .json, .xml and .ttl files captured with hashes.

[EX27: observation-example-f206-staphylococcus](<https://build.fhir.org/observation-example-f206-staphylococcus.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/f206; associated .json, .xml and .ttl files captured with hashes.

[EX28: observation-example-sample-data](<https://build.fhir.org/observation-example-sample-data.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/ekg; associated .json, .xml and .ttl files captured with hashes.

[EX29: observation-example-glasgow](<https://build.fhir.org/observation-example-glasgow.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/glasgow; associated .json, .xml and .ttl files captured with hashes.

[EX30: observation-example-glasgow-qa](<https://build.fhir.org/observation-example-glasgow-qa.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/gcs-qa; associated .json, .xml and .ttl files captured with hashes.

[EX31: observation-example-1minute-apgar-score](<https://build.fhir.org/observation-example-1minute-apgar-score.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/1minute-apgar-score; associated .json, .xml and .ttl files captured with hashes.

[EX32: observation-example-2minute-apgar-score](<https://build.fhir.org/observation-example-2minute-apgar-score.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/2minute-apgar-score; associated .json, .xml and .ttl files captured with hashes.

[EX33: observation-example-5minute-apgar-score](<https://build.fhir.org/observation-example-5minute-apgar-score.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/5minute-apgar-score; associated .json, .xml and .ttl files captured with hashes.

[EX34: observation-example-10minute-apgar-score](<https://build.fhir.org/observation-example-10minute-apgar-score.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/10minute-apgar-score; associated .json, .xml and .ttl files captured with hashes.

[EX35: observation-example-20minute-apgar-score](<https://build.fhir.org/observation-example-20minute-apgar-score.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/20minute-apgar-score; associated .json, .xml and .ttl files captured with hashes.

[EX36: observation-example-clinical-gender](<https://build.fhir.org/observation-example-clinical-gender.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/clinical-gender; associated .json, .xml and .ttl files captured with hashes.

[EX37: observation-example-eye-color](<https://build.fhir.org/observation-example-eye-color.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/eye-color; associated .json, .xml and .ttl files captured with hashes.

[EX38: observation-example-bmd](<https://build.fhir.org/observation-example-bmd.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/bmd; associated .json, .xml and .ttl files captured with hashes.

[EX39: observation-example-spirometry](<https://build.fhir.org/observation-example-spirometry.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/656; associated .json, .xml and .ttl files captured with hashes.

[EX40: observation-example-alcohol-type](<https://build.fhir.org/observation-example-alcohol-type.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/alcohol-type; associated .json, .xml and .ttl files captured with hashes.

[EX41: observation-example-vp-oyster](<https://build.fhir.org/observation-example-vp-oyster.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/vp-oyster; associated .json, .xml and .ttl files captured with hashes.

[EX42: observation-example-herd1](<https://build.fhir.org/observation-example-herd1.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/herd1; associated .json, .xml and .ttl files captured with hashes.

[EX43: observation-example-vomiting](<https://build.fhir.org/observation-example-vomiting.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/vomiting; associated .json, .xml and .ttl files captured with hashes.

[EX44: observation-example-secondsmoke](<https://build.fhir.org/observation-example-secondsmoke.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/secondsmoke; associated .json, .xml and .ttl files captured with hashes.

[EX45: observation-example-trachcare](<https://build.fhir.org/observation-example-trachcare.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/trachcare; associated .json, .xml and .ttl files captured with hashes.

[EX46: observation-example-bgpanel](<https://build.fhir.org/observation-example-bgpanel.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/bgpanel; associated .json, .xml and .ttl files captured with hashes.

[EX47: observation-example-bloodgroup](<https://build.fhir.org/observation-example-bloodgroup.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/bloodgroup; associated .json, .xml and .ttl files captured with hashes.

[EX48: observation-example-rhstatus](<https://build.fhir.org/observation-example-rhstatus.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/rhstatus; associated .json, .xml and .ttl files captured with hashes.

[EX49: observation-decimal](<https://build.fhir.org/observation-decimal.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/decimal; associated .json, .xml and .ttl files captured with hashes.

[EX50: observation-example-map-sitting](<https://build.fhir.org/observation-example-map-sitting.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/map-sitting; associated .json, .xml and .ttl files captured with hashes.

[EX51: observation-example-abdo-tender](<https://build.fhir.org/observation-example-abdo-tender.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/abdo-tender; associated .json, .xml and .ttl files captured with hashes.

[EX52: krcore-observation-labresult-example-01](<https://build.fhir.org/krcore-observation-labresult-example-01.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/krcore-observation-labresult-example-01; associated .json, .xml and .ttl files captured with hashes.

[EX53: observation-example-body-weight-with-arabic-code](<https://build.fhir.org/observation-example-body-weight-with-arabic-code.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/body-weight-with-arabic-code; associated .json, .xml and .ttl files captured with hashes.

[EX54: observation-example-cholesterol](<https://build.fhir.org/observation-example-cholesterol.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/cholesterol; associated .json, .xml and .ttl files captured with hashes.

[EX55: observation-example-hdl](<https://build.fhir.org/observation-example-hdl.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/hdl; associated .json, .xml and .ttl files captured with hashes.

[EX56: observation-example-ldl](<https://build.fhir.org/observation-example-ldl.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/ldl; associated .json, .xml and .ttl files captured with hashes.

[EX57: observation-example-non-hdl](<https://build.fhir.org/observation-example-non-hdl.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/non-hdl; associated .json, .xml and .ttl files captured with hashes.

[EX58: observation-example-triglycerides](<https://build.fhir.org/observation-example-triglycerides.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/triglycerides; associated .json, .xml and .ttl files captured with hashes.

[EX59: observation-example-vldl](<https://build.fhir.org/observation-example-vldl.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/vldl; associated .json, .xml and .ttl files captured with hashes.

[EX60: observation-example-lipidpanel-organizer](<https://build.fhir.org/observation-example-lipidpanel-organizer.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Observation/lipidpanel-organizer; associated .json, .xml and .ttl files captured with hashes.

[SO1: Source-only Observation/apgar-panel](<https://github.com/HL7/fhir/blob/09dfb700767aa757dd405d56c62bf41c5007e0f0/source/observation/observation-example-apgar-panel.xml>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Pinned XML, not registered in the current Observation example index.

[SO2: Source-only Observation/apgar-score](<https://github.com/HL7/fhir/blob/09dfb700767aa757dd405d56c62bf41c5007e0f0/source/observation/observation-example-apgar-score.xml>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Pinned XML, not registered in the current Observation example index.

[SO3: Source-only Observation/color](<https://github.com/HL7/fhir/blob/09dfb700767aa757dd405d56c62bf41c5007e0f0/source/observation/observation-example-color.xml>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Pinned XML, not registered in the current Observation example index.

[SO4: Source-only Observation/muscle-tone](<https://github.com/HL7/fhir/blob/09dfb700767aa757dd405d56c62bf41c5007e0f0/source/observation/observation-example-muscle-tone.xml>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Pinned XML, not registered in the current Observation example index.

[SO5: Source-only Observation/reflex-irritability](<https://github.com/HL7/fhir/blob/09dfb700767aa757dd405d56c62bf41c5007e0f0/source/observation/observation-example-reflex-irritability.xml>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Pinned XML, not registered in the current Observation example index.

[SO6: Source-only Observation/respiratory-effort](<https://github.com/HL7/fhir/blob/09dfb700767aa757dd405d56c62bf41c5007e0f0/source/observation/observation-example-respiratory-effort.xml>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Pinned XML, not registered in the current Observation example index.

[SO7: Source-only Observation/body-height-merged](<https://github.com/HL7/fhir/blob/09dfb700767aa757dd405d56c62bf41c5007e0f0/source/observation/observation-example-body-height-merged.xml>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Pinned XML, not registered in the current Observation example index.

[LASTN: Observation $lastn operation](<https://build.fhir.org/observation-operation-lastn.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Grouping rules, authorization prose and three abbreviated response examples.

[STATS: Observation $stats operation](<https://build.fhir.org/observation-operation-stats.html>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Panel traversal, parameters and two inline result Observations.

[STATDEF: Statistics CodeSystem](<https://build.fhir.org/codesystem-observation-statistics.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Canonical system and average/maximum/minimum/count codes.

[STATOP: Statistics OperationDefinition](<https://build.fhir.org/operation-observation-stats.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Parameter definitions and bound statistic value set.

[LASTNOP: Last N OperationDefinition](<https://build.fhir.org/operation-observation-lastn.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Formal operation scope and parameters.

[PROVMERGE: Provenance merge example source](<https://github.com/HL7/fhir/blob/09dfb700767aa757dd405d56c62bf41c5007e0f0/source/provenance/provenance-ex-patient-merged.xml>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Reference to Observation/body-height-merged.

[PROVVERIFY: Provenance verify example source](<https://github.com/HL7/fhir/blob/09dfb700767aa757dd405d56c62bf41c5007e0f0/source/provenance/provenance-example-verify.xml>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Reference to Observation/body-height-merged.

[DEP01: encounter-example](<https://build.fhir.org/encounter-example.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Encounter/example; identity, reference or timing check only.

[DEP02: group-example-herd1](<https://build.fhir.org/group-example-herd1.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Group/herd1; identity, reference or timing check only.

[DEP03: organization-example-lab](<https://build.fhir.org/organization-example-lab.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Organization/1832473e-2fe0-452d-abe9-3cdb9879522f; identity, reference or timing check only.

[DEP04: patient-example](<https://build.fhir.org/patient-example.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Patient/example; identity, reference or timing check only.

[DEP05: patient-example-a](<https://build.fhir.org/patient-example-a.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Patient/pat1; identity, reference or timing check only.

[DEP06: patient-example-b](<https://build.fhir.org/patient-example-b.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Patient/pat2; identity, reference or timing check only.

[DEP07: patient-example-chinese](<https://build.fhir.org/patient-example-chinese.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Patient/ch-example; identity, reference or timing check only.

[DEP08: patient-example-f001-pieter](<https://build.fhir.org/patient-example-f001-pieter.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Patient/f001; identity, reference or timing check only.

[DEP09: patient-example-f201-roel](<https://build.fhir.org/patient-example-f201-roel.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Patient/f201; identity, reference or timing check only.

[DEP10: patient-example-infant-mom](<https://build.fhir.org/patient-example-infant-mom.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Patient/infant-mom; identity, reference or timing check only.

[DEP11: practitioner-example](<https://build.fhir.org/practitioner-example.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Practitioner/example; identity, reference or timing check only.

[DEP12: practitioner-example-f005-al](<https://build.fhir.org/practitioner-example-f005-al.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Practitioner/f005; identity, reference or timing check only.

[DEP13: practitioner-example-f201-ab](<https://build.fhir.org/practitioner-example-f201-ab.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Practitioner/f201; identity, reference or timing check only.

[DEP14: practitioner-example-f202-lm](<https://build.fhir.org/practitioner-example-f202-lm.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Practitioner/f202; identity, reference or timing check only.

[DEP15: questionnaireresponse-example-gcs](<https://build.fhir.org/questionnaireresponse-example-gcs.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: QuestionnaireResponse/gcs; identity, reference or timing check only.

[DEP16: specimen-example-pooled-serum](<https://build.fhir.org/specimen-example-pooled-serum.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Specimen/pooled-serum; identity, reference or timing check only.

[DEP17: specimen-example-serum](<https://build.fhir.org/specimen-example-serum.json>)

Version/snapshot: 6.0.0-ballot4; retrieved 2026-09-03; source 09dfb70076. Location: Specimen/sst; identity, reference or timing check only.
