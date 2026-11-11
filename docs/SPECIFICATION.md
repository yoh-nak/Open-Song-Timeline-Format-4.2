# OSTF 4.2.0 — Normative Specification

Specification release: 2026-11-11. Structural authority: [4.2 Schema](../schema/ostf-4.2.0.schema.json). Complete inherited Core semantics: [Implementation Manual](COMPLETE_MANUAL.md). Every field and constraint: [Parameter Reference](PARAMETER_REFERENCE.md). MUST, MUST NOT, SHOULD and MAY are normative.

The 4.1 Core remains intact; Part A preserves its Direction rules and Part B adds optional vocal interchange. Historical 4.1 references in Part A name the origin of those unchanged requirements, not a different current document version. When discussing the 4.2 additions, Part B governs.

# Part A — Inherited Track Directions and authority boundaries

## 1. Purpose

OSTF 4.1 adds **Track Directions**: typed semantic instructions owned by a Track and placed on the existing OSTF global timebase.

The primary motivating case is:

> A guitar track should improvise with A minor pentatonic only during a specified interlude.

4.1 does not replace Harmony, MIDI, Notes, Generation history, or application routing.

## 2. One timebase

`tracks[].directions[]` is not an independent timeline.

Range Directions use absolute `start` + `duration`.  
Point Vendor Directions use absolute `at`.

Range intervals use the existing half-open convention `[start, start + duration)`.

## 3. Separation of authority

- `song.key`, `song.scale`, `timeline.keyChanges`, `harmony.scales`: harmonic/tonal context.
- `tracks[].clips[].notes[]`, `tracks[].clips[].midiEvents[]`: concrete stored performance.
- `tracks[].directions[]`: how that Track should be performed/interpreted/generated in a range.
- root `generation`: process, provenance-like generation history/intention; not an automatic playback command.

A Direction MUST NOT become a second authoritative location for an existing Core concept.

## 4. Standard Direction: `improvisation`

Range Direction for improvisational pitch-vocabulary guidance.

Required parameters:

- `pitchSource`
- `adherence`: `strict` or `preferred`

### 4.1 `effectiveKeyScale`

Uses the effective tonal key from `song.key` plus persistent `timeline.keyChanges`.

Canonical mappings:

- major → `[0,2,4,5,7,9,11]`
- minor → `[0,2,3,5,7,8,10]`
- dorian → `[0,2,3,5,7,9,10]`
- phrygian → `[0,1,3,5,7,8,10]`
- lydian → `[0,2,4,6,7,9,11]`
- mixolydian → `[0,2,4,5,7,9,10]`
- locrian → `[0,1,3,5,6,8,10]`

Atonal, unspecified, or unknown modes are unresolved. Consumers MUST NOT silently substitute another scale.

### 4.2 `songScale`

Uses explicit `song.scale`. It is invalid semantically if `song.scale` is absent.

### 4.3 `harmonyScales`

References existing `harmony.scales[].id` values. This is the standard chord-scale/jazz-style path.

Referenced IDs MUST resolve. Their own timing is authoritative. Array order MUST NOT create precedence. Referenced scale contexts MUST NOT overlap each other inside the Direction range.

### 4.4 `explicitScale`

Embeds a Direction-local pitch collection, for example A minor pentatonic.

It is not a harmonic-analysis assertion and MUST NOT automatically be copied into `harmony.scales`.

### 4.5 adherence

- `strict`: generated pitches SHOULD remain inside the selected vocabulary.
- `preferred`: selected vocabulary is primary, but intentional approaches, passing tones, ornaments, or other outside notes MAY occur.

Concrete authored Notes remain authoritative for playback even if they do not satisfy a Direction.

## 5. Standard Direction: `playingRole`

Range Direction that temporarily overrides `track.role` for performance/generation interpretation.

Typical interoperable values include `solo`, `lead`, `accompaniment`, `comping`, `fill`, `counter`, `response`, `unison`, `double`, `bassline`, `pad`, `drone`.

The vocabulary remains open; unknown values MUST be preserved.

## 6. Standard Direction: `pitchRange`

Range Direction with:

- `lowPitch`
- `highPitch`
- `constraint`: `strict` | `preferred`

Semantic rule: `lowPitch <= highPitch`.

This is a temporary register instruction, not a fingering/tuning/string model.

## 7. Instrument playable pitch capability

`tracks[].instrument.playablePitchRange` is optional and non-timed.

It defines an authored playable capability using the same 0..127 pitch-number domain as melodic Notes.

Semantic rule: `lowPitch <= highPitch`.

A timed `pitchRange` Direction MUST remain inside the declared playable range.

4.1 does not standardize string count, fret count, tuning, fingering, physical geometry, or written-vs-sounding notation transposition.

## 8. Vendor Directions

`type:"vendor"` provides controlled application-specific extension.

Parameters:

- `namespace`
- `name`
- optional `version`
- `data`

`namespace` uses reverse-domain style. `org.ostf` and descendants are reserved.

Vendor Directions may be range-timed or point-timed. This allows experimentation with future concepts such as breath points or one-shot gestures without prematurely defining them as Core.

Unknown Vendor Directions MAY be ignored behaviorally but MUST be preserved in a non-lossy round trip.

## 9. Optional `instruction`

A Direction may contain supplemental natural-language `instruction`.

It is advisory for humans and AI-capable systems. It does not imply network access or automatic prompt execution.

Structured Core parameters are authoritative when they conflict with `instruction`.

`instruction` is untrusted document content. It MUST NOT be treated as executable code, authorization for external actions, or privileged application/AI instructions. AI-capable software MUST NOT perform file, network, account, or other external actions solely because an OSTF `instruction` requests them. Vendor `data` is likewise data, not executable code.

## 10. Overlap

Different Standard Direction types MAY overlap.

Within one Track, overlapping ranges of the same Standard type are invalid for:

- improvisation
- playingRole
- pitchRange

4.1 defines no array-order precedence, last-wins behavior, or priority field.

## 11. Playback and generation

A 4.1-aware Player MAY ignore unsupported Directions while playing concrete Notes/MIDI.

Loading a file MUST NOT itself trigger generation.

A generator MAY materialize Direction-guided performance only through an explicit user/application action.

Saving MUST NOT silently convert a Direction into MIDI and delete the Direction.

## 12. IDs and references

Direction IDs participate in the document-wide Core ID namespace.

`trackDirection` is added to the Core `{type,id}` reference vocabulary.

## 13. Version compatibility

A 4.0-only Reader MUST NOT guess that `4.1.0` means `4.0.0`.

Graceful degradation applies only to software that explicitly recognizes 4.1.

A Writer MUST NOT silently delete unsupported 4.1 Core data.

## 14. Migration

A valid 4.0.0 document can be upgraded to 4.1.0 without inventing any new fields.

Do not infer Directions from Track names, Genres, Notes, Section names, or common musical expectations unless a user explicitly requests inference.

Downgrade to 4.0.0 is lossless only if no 4.1-only data is present.

## 15. 4.1 scope boundary

Not standardized as Core Direction taxonomies in 4.1:

- palm mute / hammer-on / pull-off / slide
- bass slap/pop/finger/pick
- orchestral articulation sets
- additional vendor-specific vocal taxonomies (standard 4.2 breath events are defined in Part B)
- string/fret/tuning/fingering models
- synth-engine-specific controls
- AI-model-specific settings

These may be tested through Vendor Directions and promoted later if cross-application semantics become stable.


## 16. Inherited OSTF 4.0 Core

OSTF 4.1.0 is additive. Every OSTF 4.0.0 Core concept and semantic rule remains unchanged unless this document explicitly extends it. This includes song/timeline/harmony structure, Sections, Key and Key Changes, song and timed Scale contexts, Chords/Voicing, Tracks/Clips/Notes, Drum Kits, Sound Slots, Lyrics, contributor/rights/resource data, Relative Phrases, Generation, Presentation, Phrase Library, Clip Choices, Localization, Provenance, Logical MIDI Buses, MIDI Channel modes, CC/Program/Pitch Bend/Pressure/Channel Mode events, MPE, multiple Melody Tracks and multiple Lyric Voices.

Implementations MUST use the 4.1 schema for `version="4.1.0"`; 4.0 rules are inherited semantics, not permission for a 4.0-only reader to guess a future version.


# Part B — OSTF 4.2 Vocal Performance

## 1. Purpose

OSTF 4.2 provides a neutral interchange representation, allowing AI or humans to author OSTF directly and separate adapters to translate explicitly assigned vocal content into singing-synthesizer project formats. Examples of *potential* targets include UFDATA, SVP, USTX, VPR/VSQX and CCS. Mentioning a target is **not** a claim of implemented or tested support. OSTF does not provide audio synthesis, vendor voicebanks, proprietary synthesizer APIs or a dedicated vocal Max for Live device.

## 2. OSTF 4.1 Core preservation

- Existing `ppq`, `timeline`, `harmony`, `tracks[]`, `clips[]`, `notes[]`, `midiEvents[]`, `lyrics.*`, and `resources[]` retain their 4.1 structures and meanings.
- Ordinary MIDI performance continues to be represented by `notes[]` and `midiEvents[]`. CC, 14-bit Pitch Bend, channel/poly aftertouch and MPE semantics are not redefined.
- `song.melodyTrackIds`, `primaryMelodyTrackId`, `track.role`, and `trackType="melodic"` **do not** imply a vocal track. Vocal parts can exist in non-melody roles; instrumental melodies remain valid.
- `lyrics.documents`, `phrases` and `units` retain lyric ownership; `lyrics.voices` and `lyrics.alignments` retain vocal assignment and lyric-to-note relationships.
- An otherwise valid OSTF 4.1 document can ordinarily be migrated by changing only `version` to `4.2.0`. New vocal fields MUST NOT be fabricated to satisfy a migration.

## 3. Optional 4.2 fields

```text
lyrics.units[].phonetics[]                   optional
lyrics.voices[].vocalProfile                 optional
tracks[].clips[].vocalPerformances[]         optional
  id, voiceId                                required within each performance
  noteIds[]                                  optional explicit ownership
  phonemeEvents[]                            optional phoneme timing
    order                                    optional same-tick tie breaker
  pitchCurves[]                              optional note-relative cents
  expressionCurves[]                         optional voice/clip or note curves
  techniques[]                               optional vocal intent
  breathEvents[]                             optional breath timing
```

These fields extend existing 4.1 objects and are never required for an instrumental track. Basic explicit voice + alignment can be exported without `vocalPerformances`. Field types, enums, numeric ranges and required properties are specified by the 4.2 Schema and `PARAMETER_REFERENCE.md`.

## 4. Identity, ownership and note authority

1. Each vocal performance references a `lyrics.voices[].id` using `voiceId`. That Voice's `trackId` MUST match the enclosing Track.
2. At most one VocalPerformance per Voice is permitted in the same Clip. A Clip MAY have several different Voices. Existing 4.1 pitch Notes are referenced, never recreated as separate authoritative vocal notes.
3. When `noteIds[]` is supplied, it explicitly identifies existing pitched Notes within the parent Clip. It MUST contain every Note assigned by the same Voice's scoped Alignments in that Clip. Missing Notes, fixed triggers and non-pitched sound slots MUST NOT be referenced.
4. Without `noteIds[]`, use Notes explicitly resolved through `lyrics.alignments[].voiceId`. A melody role MUST NOT be treated as a substitute for assignment.
5. A legacy Alignment without `voiceId` MUST NOT be silently attributed to a specific Voice. Require explicit resolution when necessary.
6. Alignments must reference existing Notes. Voice-scoped Alignments must use pitched Notes on the declared Voice Track. Multiple Voices MAY share a source Note ID, but exporting separate voices may require duplication/splitting with an explicit diagnostic.

## 5. Lyrics and pronunciation

`lyrics.units[].text` is display text; `pronunciation` is authored reading; `phonetics[]` supplies optional phoneme candidates. Neither field silently overwrites another. `phonetics[].alphabet` is one of `ipa`, `xsampa`, `arpabet`, `other`; `other` requires `namespace`, and `symbols[]` is ordered. `preferred:true` is permitted at most once for each alphabet and case-insensitively compared language grouping; different alphabets may each have a preferred entry.

The adapter's source priority is: explicitly timed `phonemeEvents` → target-mappable `phonetics` → `pronunciation` → a documented target dictionary estimate based on display `text`. Estimates MUST NOT silently modify the source. No interchange format guarantees pronunciation equivalence across languages, phoneme dictionaries or voicebanks.

### 5.1 Same-tick phoneme event order

`phonemeEvents[].order` is an optional signed integer that orders events of the same Voice, Clip and start Tick. If any event in such a same-start group supplies `order`, all events in that group MUST supply distinct values. If all omit it, structure remains valid, but their ordering is unresolved: an exporter MUST NOT claim a completely determined phoneme sequence without resolution. `order` does not govern MIDI or acoustic rendering priority.

### 5.2 Many-to-many lyric alignment

- One Unit to one Note: ordinary syllable-to-note association.
- One Unit to several Notes: melisma; do not invent repeated words or continuation symbols without a target-specific, disclosed loss/approximation policy.
- Several Units to one Note: requires explicit sequencing/timing to determine phoneme delivery; otherwise flag ambiguity.
- Several Units to several Notes: a valid representation but ambiguous for automated export until sufficiently disambiguated by alignment and phoneme timing.

`lyrics.alignments` is authoritative. A second, conflicting lyric mapping MUST NOT be invented in VocalPerformance. AI authors SHOULD prefer explicit, single-unit alignments when possible.

## 6. Vocal expression semantics

### 6.1 Vocal pitch

- Each `pitchCurves[].targetNoteId` references an existing pitched Note. `points[].value` is a **cents offset from that Note's base pitch**; `points[].at` is Clip-relative Tick. Interpolation is `step` or `linear`.
- At most one pitch curve exists per Voice/Clip/Note. Points are strictly ordered with no repeated Tick and MUST remain inside that Note's gate.
- A single-point curve defines a constant offset across the Note. With multiple points, values are **unspecified** outside the explicit point interval; do not extrapolate silently.
- For vocal export, an explicitly authored 4.2 pitch curve takes priority over overlapping 4.1 pitch-bend information for the corresponding Note. For ordinary MIDI playback, the **4.1 MIDI stream** remains authoritative. Do not sum curves and bend unconditionally.
- A legato or portamento contour across Note boundaries may exceed this note-scoped representation. Approximate or omit only with transparent loss reporting; do not create another authoritative melody.

### 6.2 Vocal expression curves

- Parameters are `dynamics`, `breathiness`, `tension`, `brightness`, and `voicing`, in abstract `[0, 1]` ranges. Missing is **unspecified**, not 0.5. These are not acoustically equivalent parameters across vendor engines.
- Without `targetNoteId`, the curve applies to the Voice/Clip; a note-scoped curve **replaces**, rather than adds to, the matching Clip-level parameter during its defined interval.
- A single point is a constant for the applicable scope. The interval outside a multi-point curve is unspecified; a note curve may fall back to a defined Clip curve outside its interval. Neither is silently extended.
- Vendor parameter mapping, audible fidelity and range conversions are adapter- and application-specific.

### 6.3 Techniques and breath events

Technique kinds (e.g., `scoop`, `fall`, `vibrato`, `legato`, `whisper`, `growl`, `falsetto`) are performance **intent**, not a replacement for explicit numeric curves. Optional intensity is abstract `[0,1]`. `breathEvents` represent timed `inhale` and `exhale`; rendering remains target-dependent. A technique MUST NOT be applied twice when the concrete curve already embodies it.

## 7. Shared timeline and tick conversion

- All time uses the existing song `ppq`. `clip.start` is song-absolute; Notes and vocal events/curves use Clip-relative Ticks.
- Negative local starts may represent preceding consonants or gestures, but the resulting song-absolute time MUST NOT be negative. Events MUST NOT extend beyond their parent Clip end.
- A target adapter SHOULD quantize absolute start/end positions using the exact rational PPQ ratio, then subtract the mapped end minus mapped start. Do not separately round an original duration and add it to the rounded start.
- The proposed deterministic reference rounding rule for target tick quantization is nearest integer, with exact halfway ties **away from zero**. It is an adapter reference rule and does not override a target format's specified interpretation.
- Positive events that collapse to zero duration, or distinct curve points that collide after quantization, MUST NOT be silently discarded or merged. Preflight must block or require an explicit approximation decision.
- `timeline.tempoChanges` remains authoritative. When converting Tick positions to milliseconds, integrate across every applicable tempo segment; never silently flatten tempo changes.

## 8. Rendering authority and compatibility

1. MIDI playback uses 4.1 `notes[]` and `midiEvents[]`; vocal metadata may be ignored.
2. Vocal export resolves Voice → Track/Clip/Note → Alignment → phonetic timing → pitch/expression → target-specific mapping.
3. Basic vocal data without VocalPerformance is a valid interchange input; a 4.1-to-4.2 version-only migration is valid when Schema and semantics pass.
4. Report exact mapping, approximations, omissions, ambiguity, and unverified features separately. Do not rewrite the source.
5. `unverified` or a successful local file write MUST NOT be described as an application-tested conversion. Application import, re-save and round-trip require independent evidence.
6. A 4.2 Reader MUST NOT silently drop future 4.3+ properties and save the result as if their meaning was preserved.

## 9. Conformance checks and limitations

Readers and writers must check structural validity and the applicable normative semantics: declared IDs, typed references, Voice/Track ownership, note membership, time bounds, curve order, value ranges and phoneme tie order. A reference containing an `id` is not a new ID definition. Export ambiguity is distinct from an invalid Core document. The bundled audit is a static package/field-coverage checker; it does not certify all semantic rules or execute a synthesizer.

## 10. Strict JSON intake

- OSTF 4.2 accepts UTF-8 JSON. Reject duplicate member names, NaN/Infinity, non-finite values, nonzero numeric underflow to zero, malformed UTF-8 and isolated Unicode surrogates before Schema validation. No implicit first-wins or last-wins interpretation.
- On rejection, do not silently repair or write source/converted documents. Reading a UTF-8 BOM MAY be supported solely for legacy input compatibility.
- Schema validity alone never proves complete semantic constraints (Voice/Note ownership, lyric mapping, same-tick order, PPQ conversion fidelity).

## 11. Adapter contracts (outside the Core Schema)

- **Export:** Explicitly resolve Voices from `lyrics.voices`/`lyrics.alignments`; do not infer them from a melodic Track. Disclose lost, approximated, ambiguous, and unsupported notes, phonemes, pitch, expression, voicebank, tempo or meter. Data loss is never implicitly approved.
- **Sidecar:** The opt-in `.vocal-sidecar.json` captures source vocal data and binds source/native/report hashes and original PPQ. It is neither a native synthesizer project nor a replacement for the source OSTF.
- **Edited-native review:** Independently verify source OSTF, baseline native, edited native, export report and sidecar. Display eligible lyric/pitch changes for read-only review; changed Notes, tempo, meter and Voice routing block safe mapping. Native pitch edits are not silently converted into OSTF cents.
- **Lyric-only approval/writeback:** New approval manifests default to `pending`/`false`. Only unambiguous one-Unit-to-one-Note edits with explicit approval may create a **new** OSTF containing changes limited to `lyrics.units[].text` and `lyrics.phrases[].text`. Preserving potentially stale pronunciation/phonetics/vocal performance requires additional explicit acknowledgement. Do not overwrite any existing file.
- SHA256 (SHA-256) is an identity/integrity check, not a signature or proof of authorship. Local adapter tests do not establish synth application interoperability.

Implementation-specific adapter contracts are outside this Core specification.

## 12. Versioning and compatibility

- Version-only migration from valid 4.1 changes `version: "4.1.0"` to `"4.2.0"` without inventing unspecified vocal data.
- Down-conversion to 4.1 when 4.2-only fields exist is lossy and MUST be disclosed. Unknown later-version fields MUST NOT be dropped through an apparently lossless save.
- Core conformance, locally tested adapter output, independently verified application import and acoustically equivalent rendering are **different claims with different evidence**.
- Post-release changes to an existing field's meaning, required status or timebase require a compatibility review. The 4.2.0 Core field definitions and normative semantics are frozen for this release.

For export and preservation boundaries, see [Conformance](CONFORMANCE.md) and [Migration](MIGRATION.md).

## 13. Specification release scope

This is the OSTF 4.2.0 Core specification release. It defines portable data and semantics, not target-application compatibility. Native converters, voicebanks and synthesizer programs are not shipped in this package. No external application test is claimed. See [conformance and implementation boundaries](CONFORMANCE.md).
