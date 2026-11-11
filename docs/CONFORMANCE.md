# OSTF 4.2.0 — Conformance and Implementation Boundaries

A Core specification release, a conforming document, a preserving editor, an adapter output and a successful application import are different claims.

| Claim | Required scope |
|---|---|
| Structural document conformance | Strict JSON and declared-version Schema |
| Semantic document conformance | Applicable normative ownership, reference, timing, range, overlap and curve rules |
| Preserving reader/editor | Recognized version, no silent loss, explicit handling of unsupported information |
| MIDI playback | Inherited Notes/MIDI timing and channel interpretation; vocals do not redefine the MIDI stream |
| Vocal adapter | Explicit Voice assignment and truthful unsupported/approximate/ambiguous-data reporting |
| Target application compatibility | Separate application-specific evidence; not supplied by this release |

## This package

It contains the formal 4.2.0 Core specification, complete manuals/references, schemas, original/derived examples and a read-only static audit utility. It does not include Native writers, DAW devices, synthesis engines, voicebanks or application screenshots. The user requested no external operational verification. The release therefore makes no Synthesizer V, OpenUtau, VOCALOID, CeVIO or LibreSVIP runtime-compatibility claim.

## Adapter status boundary

Earlier development materials explored UFDATA as a reference output and SVP/USTX as experimental outputs. Those are separate implementations, not Core conformance and not bundled here. VPR/VSQX/CCS are possible future targets, not implemented support in this package. A consumer may implement any adapter independently without changing Core semantics.

## Security and authored text

Instructions, vendor data, URIs, resource names, lyrics and descriptions are untrusted data. Loading a document does not authorize executing code, invoking an AI tool, fetching a network resource, loading a plugin or changing an account. Parsing and schema resolution should not require network access. Preserve unknown data or reject destructive editing rather than granting it authority.

## Evidence boundary

The static report describes only operations performed during package construction. Historical development test counts are not relabeled as fresh results. Field coverage proves stored example occurrences, not all values, all semantic rules, natural musical quality or acoustic equivalence.
