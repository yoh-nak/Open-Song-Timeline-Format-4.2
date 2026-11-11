# OSTF 4.2.0 — Complete Demo Guide

All 53 files use `.ostf`, UTF-8 JSON and `version: "4.2.0"`. Files 01–50 are parameter/interchange technical examples; 51–53 are original continuous multi-track musical arrangements. A technical example is not a promise of natural acoustic performance.

Start with 01 (inherited Core), 02 (all vocal fields) and 51 (a 32-bar vocal Pop arrangement). File 03 preserves historical extension payloads; it does not recommend placing new shared first-party data only in private extensions. Core stays authoritative.

Files 16 (many-to-many alignment), 17 (tick rounding) and 18 (unresolved same-start phoneme order) deliberately illustrate export decisions. They are structurally valid OSTF documents, not fabricated claims of successful native conversion.

The custom phoneme namespace in 02 is illustrative, not a real voicebank dictionary. The short English lyrics in 51 are original. No vendor engine, audio, singer identity, artwork, sample library or external media dependency is required to inspect the musical data.

| No. | File / title | Category |
|---|---|---|
| 01 | [OSTF 4.2 Complete Core Reference](../examples/01-all-core.ostf) | parameter-reference |
| 02 | [All Vocal Parameters — Namespaces and Expression](../examples/02-all-vocal-parameters.ostf) | parameter-reference |
| 03 | [Legacy Profile Preservation — All Defined Fields](../examples/03-all-legacy-profiles.ostf) | parameter-reference |
| 04 | [OSTF 4.2 Basic Vocal Exchange](../examples/04-basic-vocal.ostf) | vocal-scenario |
| 05 | [Wind / 風 — expressive voice example](../examples/05-expressive-vocal.ostf) | vocal-scenario |
| 06 | [Instrumental Melody — no vocals](../examples/06-instrument-midi-unchanged.ostf) | vocal-scenario |
| 07 | [Lead + Harmony — separate vocal voices](../examples/07-multivoice-same-lyrics.ostf) | vocal-scenario |
| 08 | [Wordless vocal phrase — noteIds only](../examples/08-wordless-humming.ostf) | vocal-scenario |
| 09 | [Two vocal parts on one logical Track](../examples/09-two-voices-one-track.ostf) | vocal-scenario |
| 10 | [Same unit with IPA and X-SAMPA variants](../examples/10-parallel-phonetic-alphabets.ostf) | vocal-scenario |
| 11 | [A note-specific dynamics override](../examples/11-note-expression-override.ostf) | vocal-scenario |
| 12 | [Melisma: one lyric unit on two notes](../examples/12-melisma.ostf) | vocal-scenario |
| 13 | [Anticipated consonant before note](../examples/13-pre-note-consonant.ostf) | vocal-scenario |
| 14 | [Synth lead plus independent sung melody](../examples/14-instrument-and-vocal.ostf) | vocal-scenario |
| 15 | [Same-tick phonemes with explicit deterministic order](../examples/15-phoneme-same-tick-order.ostf) | vocal-scenario |
| 16 | [Ambiguous many-to-many lyrics requires export resolution](../examples/16-ambiguous-many-to-many.ostf) | vocal-scenario |
| 17 | [One-tick breath collapsed by 960 to 480 PPQ simulation](../examples/17-tick-rounding-loss.ostf) | vocal-scenario |
| 18 | [Same-tick phonemes without explicit order; valid but ambiguous to export](../examples/18-same-tick-implicit-order.ostf) | vocal-scenario |
| 19 | [Wind / 風 — tempo-change vocal example](../examples/19-tempo-change-vocal.ostf) | vocal-scenario |
| 20 | [Meter Shift / 拍子の変化 — 4/4 to 3/4 vocal example](../examples/20-meter-change-vocal.ostf) | vocal-scenario |
| 21 | [Single Late Pitch Anchor Conformance](../examples/21-single-late-pitch-anchor.ostf) | vocal-scenario |
| 22 | [OSTF 4.2 — consonant before next note](../examples/22-pre-note-consonant.ostf) | vocal-scenario |
| 23 | [MPE Per Note Expression](../examples/23-mpe-per-note-expression.ostf) | parameter-reference |
| 24 | [Pitch Range Direction](../examples/24-pitch-range-high-register.ostf) | parameter-reference |
| 25 | [Integrated Jazz Session](../examples/25-integrated-jazz-session.ostf) | parameter-reference |
| 26 | [Poly Pressure](../examples/26-poly-pressure.ostf) | parameter-reference |
| 27 | [Generation Intent](../examples/27-generation-intent.ostf) | parameter-reference |
| 28 | [Channel Mode](../examples/28-channel-mode.ostf) | parameter-reference |
| 29 | [Vendor Range Direction](../examples/29-vendor-range-direction.ostf) | parameter-reference |
| 30 | [Bank Program Change](../examples/30-bank-select-program-change.ostf) | parameter-reference |
| 31 | [Effective Key Scale](../examples/31-effective-key-scale.ostf) | parameter-reference |
| 32 | [Document Identity](../examples/32-document-identity-revision.ostf) | parameter-reference |
| 33 | [Chord Voicing](../examples/33-chord-voicing.ostf) | parameter-reference |
| 34 | [External MIDI Sound Source](../examples/34-sound-source-external-midi.ostf) | parameter-reference |
| 35 | [Provenance](../examples/35-provenance.ostf) | parameter-reference |
| 36 | [Localized Names](../examples/36-localized-names.ostf) | parameter-reference |
| 37 | [Note Performance State](../examples/37-note-performance-state.ostf) | parameter-reference |
| 38 | [Note Probability](../examples/38-note-probability-deviation.ostf) | parameter-reference |
| 39 | [Sound Slot Mappings](../examples/39-sound-slot-midi-mapping.ostf) | parameter-reference |
| 40 | [Meter Map](../examples/40-meter-map.ostf) | parameter-reference |
| 41 | [Bar Origin](../examples/41-bar-origin.ostf) | parameter-reference |
| 42 | [Slash Chord](../examples/42-slash-chord.ostf) | parameter-reference |
| 43 | [Timed Harmony Scales](../examples/43-timed-harmony-scales.ostf) | parameter-reference |
| 44 | [Fixed Trigger](../examples/44-fixed-trigger-note.ostf) | parameter-reference |
| 45 | [Lyrics Pronunciation](../examples/45-lyrics-pronunciation.ostf) | parameter-reference |
| 46 | [Contributors Credits](../examples/46-contributors-credits.ostf) | parameter-reference |
| 47 | [Rights](../examples/47-rights-statement.ostf) | parameter-reference |
| 48 | [Genres Moods](../examples/48-genres-moods.ostf) | parameter-reference |
| 49 | [Generation Process](../examples/49-generation-process.ostf) | parameter-reference |
| 50 | [Song Scale Improvisation](../examples/50-song-scale-improvisation.ostf) | parameter-reference |
| 51 | [Light We Make](../examples/51-musical-pop-vocal.ostf) | musical-demo · 32 bars · 108 BPM |
| 52 | [Evening Turns](../examples/52-musical-jazz-quartet.ostf) | musical-demo · 24 bars · 124 BPM |
| 53 | [Signal Garden](../examples/53-musical-electronic.ostf) | musical-demo · 32 bars · 126 BPM |

**Coverage:** see the [field map](PARAMETER_COVERAGE.md). External application import, playback and vocal quality are not tested.
