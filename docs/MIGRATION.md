# OSTF 4.2.0 — Migration and Preservation

## From 4.1 to 4.2

Read the original as 4.1, preserve it, and create a new document with only the root `version` changed to `4.2.0`. Optional 4.2 fields are not required. Do not infer a voice from Track names, roles or melody references, and do not manufacture phonemes, voice profiles, curve defaults or expression values. All inherited Notes, MIDI CC/Bend/AT/MPE, Directions, IDs and relationships retain their meaning.

## From 4.2 to 4.1

A version-only downgrade is lossless only when `lyrics.units[].phonetics`, `lyrics.voices[].vocalProfile` and `tracks[].clips[].vocalPerformances` are absent. Otherwise, create a separate explicitly lossy export and report every removed field. Saving an untouched copy plus an optional sidecar is not the same as having preserved those fields inside a 4.1 document. Do not hide standardized 4.2 fields only in a vendor extension and claim ordinary Core equivalence.

## Older 3.x / 4.0 data

Use the semantics of the source version. The inherited 4.1 model adds Track Directions and playable pitch ranges to 4.0. Earlier releases have different Core/extension boundaries. Preserve old profile payloads verbatim when not migrated. The archived profiles in example 03 illustrate preservation, not new-data authoring or automatic profile execution.

## Merge and identity

Remap actual definition IDs and all dependent references atomically. A `{type,id}` reference is not a new ID definition. Document/revision identities, generator identifiers and language/namespace keys have their own meanings and must not be blindly renamed with Core IDs. Treat melodic/vocal assignment separately from display names.

## Time and curves

Clip moves normally preserve local event timing. Clip splits, Note duration changes and PPQ conversions require coordinated updates of Notes, MIDI, phonemes, technique/breath intervals and curve targets. Compute destination onset and end from the source time domain, then derive duration; do not round duration independently. Report collisions and zero-length results. Multi-point curves are undefined outside their authored interval; single-point curves cover their defined target scope.

## Source preservation

Native-project output is a derivative. Keep the OSTF source unchanged; report unsupported, approximated and ambiguous content. A hash identifies bytes, not authorship, and does not prove a target application imported them. Lyric-only writeback must not silently modify pronunciation, phonetics, Notes or expression.
