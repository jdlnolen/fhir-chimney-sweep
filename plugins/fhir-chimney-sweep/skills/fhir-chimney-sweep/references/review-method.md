# Review method

## Evidence and version control

Start with the chosen build's resource page, definitions, downloadable
StructureDefinition, example index, and module/overview pages. Inspect
source fragments and example files at an immutable repository commit when
available. Core source layout and incubator/IG layouts differ; discover them
rather than constructing URLs from a resource name and assuming they exist.
Record profile differentials and base definitions as well as snapshots where
profiling changes the rules. Read the owning repository's contribution/build
instructions as workflow context, not as permission to modify it.

Use the target version of the official guidance where possible:

- [FHIR validation](https://build.fhir.org/validation.html): parsers, schemas,
  validators, terminology checks, and human semantic review offer different
  evidence. No one check establishes all of them.
- [Conformance language](https://build.fhir.org/conformance-rules.html): preserve
  obligation strength and distinguish base requirements from profile rules.
- [Resource definitions](https://build.fhir.org/structuredefinition.html): inspect
  actual element definitions, constraints, bindings, and base/profile context.
- [References](https://build.fhir.org/references.html) and
  [Bundle](https://build.fhir.org/bundle.html): resolve using the representation's
  actual context rather than assuming all references are local filenames.

The CI site is mutable. Capture version/date and, when no immutable published
snapshot exists, retain downloaded evidence with URLs and checksums. Do not
compare yesterday's examples with today's structure without disclosing that
limitation. A source checkout or validator package must not be labeled the
published build just because both use the word "current".

## Documentation pass

Read the complete scope/usage and boundaries/relationships sections, notes,
definitions, mappings or workflow discussion where they explain the resource,
and linked normative constraints relevant to a claim. Check:

- Stated purpose, supported subjects, resource granularity, and lifecycle.
- Resource versus definitional resource; request versus event; instance versus
  catalog; grouping/panel versus component; report versus atomic result.
- Exact element paths and types, polymorphic choices, cardinalities, target
  types, modifier meaning, status/intent combinations, and conditional rules.
- SHALL/SHOULD/MAY statements, invariants, terminology binding strengths, and
  distinctions between base specification and a named profile or extension.
- Dead names, removed elements, superseded examples, renamed resources, and
  release/incubator links that imply capabilities no longer in the chosen build.
- Definitions with circular wording, inconsistent terminology, hidden referents,
  unexplained acronyms, or sentences that obscure who performs an action.

For a disagreement, cite both sides. Determine whether a known normative rule
resolves it; otherwise ask the owning work group which intent is authoritative.
A cleanup suggestion must not add a new requirement or imply all optional
elements are required. Do not import assumptions from another FHIR release.

## Example pass

Reconcile the published example list with source and generated artifacts. Inspect
all examples within the declared scope; report inaccessible items rather than
quietly sampling. Deduplicate one instance shown as XML/JSON/Turtle while still
checking serialization/narrative agreement. An indexed Bundle is one list entry,
not necessarily one instance; include relevant contained resources and dependencies.

Check actual content rather than presence-only checklists:

- Correct resource type, IDs, legal element paths/types, cardinality, invariants,
  valid choice use, extensions, profile declarations, and canonical versions.
- Display/text/code meaning, code system URL and version, binding strength,
  UCUM representation when applicable, and plausible value/unit combinations.
  Flag unavailable terminology verification as unavailable, not invalid.
- Patient/subject, encounter, specimen, order, performer, device, and report
  identities agree across linked resources. Check resolved resource content,
  not just matching names or successful HTTP requests.
- Status, intent, dates, quantities, reference intervals, interpretations, absent
  data, components, members, derived results, and corrections are coherent for
  the demonstrated use case. Partial dates/time zones may limit comparison.
- Narrative and captions match structured data. Generated narrative can be
  wrong or incomplete even after validation. Check clinically meaningful facts.
- Resolve contained `#id`, relative references, absolute references, Bundle
  `fullUrl`/URNs, and canonical references with their distinct semantics. Distinguish
  unresolved-in-this-corpus, intentional illustrative, external-unavailable,
  and confirmed broken/wrong-target references. Do not fetch arbitrary private
  endpoints or send examples to external services without authority.
- Inspect generated XML/JSON/Turtle/narrative and links where supplied by the
  build. Missing formats may be build limitations, not resource defects.

Build a use-case coverage view. Missing examples should teach a supported
distinction: simple versus composite, lifecycle transition, absent result,
boundary with a related resource, or a new release feature. Give minimum
content and expected semantic checks; do not invent new core fields to tell a
good story. Minimal examples remain useful when their intentional limits are clear.

## Module and reconciliation pass

Identify all module sections that materially describe this resource, not every
incidental mention. Review overview text, relationship diagrams, legends, tables,
implementation guidance, workflow sequences, and example links. Inspect actual
images/SVGs; text extraction alone can miss arrow directions or stale labels.

Trace a few important documented claims all the way through definition →
resource prose → example → module. Track gaps for every claimed use case;
do not claim exhaustive semantic coverage from only those traces. Check that
boundaries are reciprocal where necessary and that module wording neither
overstates nor hides resource capabilities. If no applicable module exists,
document the search and scope the closest official overview; do not manufacture
a module or silently skip this part.

A change may require edits in several places. Use one root-cause finding with
separate edit locations and an ordered dependency list. Proposed diagram changes
should state which node/edge/label changes and why. Suggested prose should be
read naturally aloud, retain defined terms, and avoid claims such as "always"
when the structure or workflow supports exceptions.

## Acceptance

A completed static sweep is not a validator run, terminology certification,
clinical endorsement, or publication decision by HL7. State which checks ran,
their exact package/tool versions and logs, what failed, and what remains for
the resource owner. Re-run affected checks on the final publication revision.
