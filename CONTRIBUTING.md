# Contributing

Please open an issue with the resource, exact FHIR build/package or commit,
affected report finding, and a minimal public or synthetic reproduction.
Distinguish a wrong review conclusion from a report-format or plugin-install bug.
Do not post PHI, secrets, private examples, or private build content.

Use a feature branch and pull request. Include relevant tests, describe the
evidence supporting any review-rule change, and check both host manifests.
Changes to report content must keep Markdown and Word synchronized. Render and
inspect all pages after layout changes; record limitations if rendering is unavailable.

Keep defaults scoped: a preference from one resource or release must not become
a universal conformance rule. Avoid hardcoded current ballot numbers, resource
ownership lists, module maps, or clinical codes. The skill is review-only unless
the user separately authorizes implementation.

The repository owner reviews and merges contributions and publishes releases.
Contributions are offered under this repository's MIT license. Third-party FHIR
material remains subject to its own licensing and attribution requirements.
