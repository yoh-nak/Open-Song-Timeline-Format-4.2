# Open Song Timeline Format 4.2.0

**Formal specification release · Optional Vocal Performance Interchange**

OSTF is an open, DAW-independent JSON format for song structure, harmony, tracks, clips, notes, MIDI performance, lyrics and semantic Track Directions. Version 4.2 preserves the 4.1 Core and adds optional phonetics, voice profiles and vocal performance data. Instrumental melodies remain instrumental; no dedicated singing device is required.

## Start here

- [Complete implementation manual](docs/COMPLETE_MANUAL.md) · [日本語マニュアル](docs/COMPLETE_MANUAL.ja.md)
- [Complete parameter reference](docs/PARAMETER_REFERENCE.md) · [日本語リファレンス](docs/PARAMETER_REFERENCE.ja.md)
- [Normative specification](docs/SPECIFICATION.md) · [日本語規範仕様](docs/SPECIFICATION.ja.md)
- [All demos](docs/EXAMPLES_GUIDE.md) · [All-parameter coverage](docs/PARAMETER_COVERAGE.md)

## Data model

```text
Song / Timeline / Harmony
Tracks → Clips → Notes + MIDI events
Lyrics → Documents / Phrases / Units / Voices / Alignments
4.2 optional: Unit.phonetics / Voice.vocalProfile / Clip.vocalPerformances
```

The Schema is [schema/ostf-4.2.0.schema.json](schema/ostf-4.2.0.schema.json). Files use `.ostf`, UTF-8 JSON and `version: "4.2.0"`.

## Included examples

53 `.ostf` files: 50 technical/reference scenarios plus three original musical arrangements (32-bar vocal Pop, 24-bar Jazz and 32-bar Electronic). Together they contain **569/569 reachable named-property declarations: 481 Core + 88 legacy-preservation fields**. See the witness table for the counting method; this is not every possible enum/value combination.

## Release scope

This is the formal **Core specification**, not a certified synthesizer/DAW implementation. No external application operation was tested for this release. Native converters and voicebanks are not bundled. Read [Conformance](docs/CONFORMANCE.md), [Migration](docs/MIGRATION.md) and [Release Notes](RELEASE_NOTES.md).

## Optional read-only static audit

```bash
python -m pip install -r requirements.txt
python tools/audit_release.py
```

The audit checks package structure and field coverage, not every semantic rule or acoustic output. Source hashes are listed in [SHA256SUMS.txt](SHA256SUMS.txt).

## License

Specification, schemas, documentation and `.ostf` examples: **CC0-1.0**, [LICENSE](LICENSE). Python utility: **MIT**, [LICENSE-CODE](LICENSE-CODE). See [NOTICE](NOTICE.md) for inherited material, scope and third-party boundaries.

## Distribution record

[Static report](STATIC_REPORT.md) / [Machine-readable report](RELEASE_REPORT.json)
