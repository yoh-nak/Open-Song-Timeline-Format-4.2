# OSTF 4.2.0 — Release Notes

Specification release package prepared on 2026-11-11. Release tag: `v4.2.0`.

## Added to the format

Three optional ownership locations: `lyrics.units[].phonetics`, `lyrics.voices[].vocalProfile` and `tracks[].clips[].vocalPerformances`. They support phoneme candidates/timing, explicit voice note membership, note-scoped cents curves, abstract expression curves, technique intent and breath events. The existing Notes are the only authoritative pitch-note collection.

## Preserved

All 4.1 Core structure and semantics, including track directions, playable pitch range, metadata, timeline, harmony, lyrics, MIDI CC/Bend/AT/MPE, logical routing, provenance and editing relationships. An ordinary instrumental document does not need vocal fields.

## Distribution

Self-contained English/Japanese manuals and complete references, frozen structural definitions, 53 `.ostf` examples, per-field witnesses, active CC0/MIT notices and a read-only static audit. The direct `$defs`/`properties` content matches the publication-preparation Core; only the explanatory top-level schema comment changes to final release wording.

## Boundaries

This package does not claim external application import, playback, synthesis or acoustic equivalence. No fresh historical regression-test totals are claimed. Schema/field coverage is static and does not certify all semantic rules. Native converters are outside this distribution. GitHub publication itself is a separate user action; this archive is the content to publish.
