# OSTF 4.2.0 — Complete Parameter Reference

This reference includes the entire inherited Core, all optional 4.2 fields, primitive types, conditional rules and legacy preservation definitions, not just the 4.2 delta.

Structural authority: [JSON Schema](../schema/ostf-4.2.0.schema.json). Semantics: [Manual](COMPLETE_MANUAL.md) and [Specification](SPECIFICATION.md).

## Reading this reference and coverage scope

There are 569 reachable named-property declaration locations: 481 Core and 88 legacy-preservation fields. Each has an actual example/JSON-Pointer witness. This does not enumerate arbitrary map keys, free text, unknown vendor JSON, every enum combination or every possible number. Requiredness tables describe direct required fields; exact object schemas below also define conditional requiredness, dependencies and mutually exclusive branches. A schema default is not permission to insert authored data on save.

The schema has 114 direct `$defs` including the legacy container and 65 embedded legacy definitions. Archival definitions not reachable from the 4.2 root are documented too, but are not new authorable 4.2 parameters.

Complete field-to-demo map: [PARAMETER_COVERAGE.md](PARAMETER_COVERAGE.md).

Schema description prose can mention earlier introduction versions such as 4.0 or 4.1. The document version for this release is determined by the root `version` const `4.2.0`.

## Index

- [Root](#schema-334359b90efe)
- [id](#schema-8c1697fddab4)
- [nonnegative](#schema-c35af8db37cc)
- [positive](#schema-c337f17304bf)
- [signed](#schema-f9a49621bf61)
- [pitch](#schema-44b9e8efcfeb)
- [ref](#schema-981414324ed5)
- [range](#schema-1a2975da6dc1)
- [spelledPitchClass](#schema-564171196249)
- [song](#schema-8e772ecd20dd)
- [section](#schema-e852a1ccdb07)
- [tempo](#schema-402caf4cc3df)
- [meter](#schema-7ab4411e74dc)
- [timeline](#schema-5532f237d17d)
- [chord](#schema-5728fe0e89d0)
- [scale](#schema-7120179dfd85)
- [harmony](#schema-d9a56b61ff7e)
- [instrument](#schema-81166c6fec71)
- [note](#schema-96e72b83e194)
- [clip](#schema-6cef7ff6a8f2)
- [track](#schema-63477fd6abf3)
- [soundSlot](#schema-0ddd4ff5938f)
- [lyricDocument](#schema-1f5cbf9e5e4b)
- [lyricPhrase](#schema-d24fe48780db)
- [lyricUnit](#schema-27b0290397e0)
- [lyricAlignment](#schema-4bce9d4af5d4)
- [lyrics](#schema-2160208bc94c)
- [sha256](#schema-3aab424c33aa)
- [resource](#schema-6d9d5986fda3)
- [dependencies](#schema-75af29175dd3)
- [relativeAssignment](#schema-a1d368bd2745)
- [generator](#schema-7f5580e4d853)
- [generationInput](#schema-c843883807fe)
- [generationProcess](#schema-7d1dd7d6e9ff)
- [color](#schema-da077ea23895)
- [roleDefinition](#schema-caba67c7caf4)
- [roleColorMap](#schema-26f521dabf80)
- [customRoleColorMap](#schema-f6caa7165a5e)
- [objectColor](#schema-442e7bcaa5f8)
- [phraseTemplate](#schema-5dfc7b11c09b)
- [phraseNoteMapping](#schema-7033ad6b2acc)
- [phraseInstance](#schema-f17bdbf88127)
- [clipCandidate](#schema-57909b1ed915)
- [clipChoiceGroup](#schema-7e2d711ae826)
- [midiMapping](#schema-2f2e34aa29d7)
- [soundSource](#schema-05eae897621a)
- [localizedNames](#schema-e6f4a4f748b6)
- [drumKit](#schema-a7835568e37b)
- [voicing](#schema-5c862cc3e40d)
- [contributor](#schema-b59d15df5050)
- [credit](#schema-d24adedd38df)
- [alternateTitle](#schema-73647ae405b9)
- [languageMap32](#schema-b88bcc6edf81)
- [localizationTarget](#schema-354471cd4b0d)
- [localizationEntry](#schema-1f6858ae510d)
- [genre](#schema-70e3c989db70)
- [opaqueDocumentId](#schema-0771f9ca6fb2)
- [revisionRef](#schema-ed4d016a64c1)
- [software](#schema-d8bfbf4d7086)
- [documentInfo](#schema-1808c384c579)
- [key](#schema-60e537075bf2)
- [keyChange](#schema-be378667ebe6)
- [scaleDefinition](#schema-168efc29897b)
- [scaleTarget](#schema-68828d63bc6c)
- [mood](#schema-bcdeab4b5e49)
- [rightsStatement](#schema-8cf8ca085d8a)
- [grooveIntent](#schema-afef10ac955e)
- [generationIntent](#schema-f5a441896302)
- [relativePhrases](#schema-b8bdd265b21e)
- [generation](#schema-d97c4e182ee5)
- [presentation](#schema-6a454ca6c7cd)
- [phraseLibrary](#schema-688ef61fcbb9)
- [clipChoices](#schema-087f3401a094)
- [localization](#schema-d217ff47f679)
- [corePhraseSourceNote](#schema-4f2bcba3af0a)
- [provenanceSource](#schema-d0530816027d)
- [provenanceRecord](#schema-a903cfe5aef0)
- [provenance](#schema-ba37b5c7146e)
- [midiChannel](#schema-d9e2f6960cc4)
- [midiBus](#schema-243e98d145a8)
- [midi](#schema-e63c7a3ec0d1)
- [mpeSettings](#schema-4f2c12c54b18)
- [trackMidi](#schema-a037cff7c14c)
- [controlChangeEvent](#schema-6f54f21ac661)
- [channelModeEvent](#schema-6b19d423c196)
- [programChangeEvent](#schema-0db111a5d987)
- [pitchBendEvent](#schema-7df32ddccc21)
- [channelPressureEvent](#schema-272c93d6fd9f)
- [polyPressureEvent](#schema-ba1b5c1a9ff9)
- [midiEvent](#schema-1c0cd2d1203f)
- [lyricVoice](#schema-d187205a3e8b)
- [playablePitchRange](#schema-91234b29badc)
- [directionPitchCollection](#schema-968a8b410378)
- [directionPitchSource](#schema-6ffe903f72ae)
- [improvisationDirectionParameters](#schema-ee9de698d509)
- [playingRoleDirectionParameters](#schema-2d9985e68214)
- [pitchRangeDirectionParameters](#schema-10257f9b295f)
- [vendorDirectionParameters](#schema-02bfecf4e43a)
- [improvisationDirection](#schema-033764cd9dd6)
- [playingRoleDirection](#schema-becf3213fa2e)
- [pitchRangeDirection](#schema-9b1fe7d5388c)
- [vendorRangeDirection](#schema-006c4953cb58)
- [vendorPointDirection](#schema-edc04f37e799)
- [trackDirection](#schema-00f7629b4a96)
- [vocalPhonetics](#schema-8d401d008180)
- [vocalProfile](#schema-4b68a4083047)
- [vocalPerformance](#schema-151525915c48)
- [vocalPhonemeEvent](#schema-fcd572a52128)
- [vocalCurvePointPitch](#schema-45a386c6e0a3)
- [vocalCurvePointNormalized](#schema-7f0781f571df)
- [vocalPitchCurve](#schema-5f14feb1db08)
- [vocalExpressionCurve](#schema-23c97f8c4086)
- [vocalTechnique](#schema-4cd016e7774f)
- [vocalBreathEvent](#schema-ec2f019b423f)
- [Legacy / id](#schema-89e7c47e4e36)
- [Legacy / nonnegative](#schema-0e7b3ba09160)
- [Legacy / positive](#schema-499e1b38d212)
- [Legacy / signed](#schema-9c0955d738e2)
- [Legacy / pitch](#schema-807646b0fce0)
- [Legacy / ref](#schema-76351f8f7ee7)
- [Legacy / range](#schema-92f7f746fea9)
- [Legacy / spelledPitchClass](#schema-aa6c1bbd7d55)
- [Legacy / song](#schema-cf3060dc5fe4)
- [Legacy / section](#schema-6ec56b313dbf)
- [Legacy / tempo](#schema-f1a7c5685d6c)
- [Legacy / meter](#schema-31c401ec2fe1)
- [Legacy / timeline](#schema-1d0bbb380e5a)
- [Legacy / chord](#schema-724bf82722f0)
- [Legacy / scale](#schema-855503cf7f47)
- [Legacy / harmony](#schema-d1738fe99d18)
- [Legacy / instrument](#schema-67614c4a2158)
- [Legacy / note](#schema-71b274e4ebf6)
- [Legacy / clip](#schema-352905fa076c)
- [Legacy / track](#schema-59b87a2e0933)
- [Legacy / soundSlot](#schema-2a2c3b2903fc)
- [Legacy / lyricDocument](#schema-4c6d1a69fe9e)
- [Legacy / lyricPhrase](#schema-7eaf29dd50c5)
- [Legacy / lyricUnit](#schema-4a1ae1742a3e)
- [Legacy / lyricAlignment](#schema-7484ca2e8e21)
- [Legacy / lyrics](#schema-103328dc0e5b)
- [Legacy / sha256](#schema-c2db6cd8f3e9)
- [Legacy / resource](#schema-9e19b5836345)
- [Legacy / dependencies](#schema-1c75c4bf6382)
- [Legacy / extension](#schema-83e73de19250)
- [Legacy / relativeAssignment](#schema-a20bc23fbf4f)
- [Legacy / relativeData](#schema-a9777d5f71bd)
- [Legacy / generator](#schema-abae7bc69673)
- [Legacy / generationInput](#schema-3bcfec9bb3d8)
- [Legacy / generationProcess](#schema-b97284b5732d)
- [Legacy / generationData](#schema-aa74d437308f)
- [Legacy / color](#schema-6baefb234944)
- [Legacy / roleDefinition](#schema-2e7fb7685f53)
- [Legacy / roleColorMap](#schema-1c4f374f3163)
- [Legacy / customRoleColorMap](#schema-47795aef91d3)
- [Legacy / objectColor](#schema-5f73ffdead81)
- [Legacy / appearanceData](#schema-88792dd6c736)
- [Legacy / legacyData](#schema-2776ab3e0302)
- [Legacy / extensions](#schema-2fea9a3b8b7e)
- [Legacy / phraseTemplate](#schema-b373e44b1698)
- [Legacy / phraseNoteMapping](#schema-44d3bca2e7c7)
- [Legacy / phraseInstance](#schema-3d626178543f)
- [Legacy / phraseLibraryData](#schema-a52806e307ba)
- [Legacy / clipCandidate](#schema-d66fe864df92)
- [Legacy / clipChoiceGroup](#schema-7f4e9208b732)
- [Legacy / clipChoicesData](#schema-b00cf26c6c42)
- [Legacy / midiMapping](#schema-80fae39efba5)
- [Legacy / soundSource](#schema-5036418e8e2b)
- [Legacy / localizedNames](#schema-7039e6a853e2)
- [Legacy / drumKit](#schema-fd9a025522cc)
- [Legacy / phraseSourceNote](#schema-475dcf47369e)
- [Legacy / voicing](#schema-57f91803a575)
- [Legacy / contributor](#schema-c1506d82e789)
- [Legacy / credit](#schema-dfb18f087d21)
- [Legacy / alternateTitle](#schema-776d222783e2)
- [Legacy / languageMap32](#schema-dd0a6f194be8)
- [Legacy / localizationTarget](#schema-5443a9c8e25b)
- [Legacy / localizationEntry](#schema-8918b9a525df)
- [Legacy / localizationData](#schema-3a6707a441dd)
- [Legacy / genre](#schema-7ec55152a967)

<a id="schema-334359b90efe"></a>
## Root

`#`

OSTF 4.2.0: backward-compatible OSTF 4.1 Core plus optional phonetics, vocal profiles, and vocal performances; instrumental MIDI semantics remain intact.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `format` | `{"const":"OSTF"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/format` |
| `version` | `{"const":"4.2.0"}` | Yes | Version identifier for this owning object. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/version` |
| `ppq` | `{"type":"integer","minimum":1,"maximum":960000}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/ppq` |
| `song` | `{"$ref":"#/$defs/song"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song` |
| `timeline` | `{"$ref":"#/$defs/timeline"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/timeline` |
| `harmony` | `{"$ref":"#/$defs/harmony"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/harmony` |
| `tracks` | `{"type":"array","items":{"$ref":"#/$defs/track"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks` |
| `soundSlots` | `{"type":"array","items":{"$ref":"#/$defs/soundSlot"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/soundSlots` |
| `lyrics` | `{"$ref":"#/$defs/lyrics"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics` |
| `resources` | `{"type":"array","items":{"$ref":"#/$defs/resource"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/resources` |
| `extensions` | `{"$ref":"#/$defs/legacy33/$defs/extensions"}` | No / conditional | Optional third-party or verbatim legacy compatibility payloads. Standard Core always remains authoritative. New first-party common information must not be stored only here. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions` |
| `drumKits` | `{"type":"array","items":{"$ref":"#/$defs/drumKit"}}` | No / conditional | Optional multiple percussion-kit definitions; absent = no declared kits (3.0 compatible). | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/drumKits` |
| `contributors` | `{"type":"array","items":{"$ref":"#/$defs/contributor"}}` | No / conditional | Optional unordered identity records referenced by song.credits. No contributor limit is imposed by this format. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/contributors` |
| `document` | `{"$ref":"#/$defs/documentInfo"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/document` |
| `relativePhrases` | `{"$ref":"#/$defs/relativePhrases"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/relativePhrases` |
| `generation` | `{"$ref":"#/$defs/generation"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation` |
| `presentation` | `{"$ref":"#/$defs/presentation"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/presentation` |
| `phraseLibrary` | `{"$ref":"#/$defs/phraseLibrary"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary` |
| `clipChoices` | `{"$ref":"#/$defs/clipChoices"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/clipChoices` |
| `localization` | `{"$ref":"#/$defs/localization"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/localization` |
| `provenance` | `{"$ref":"#/$defs/provenance"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/provenance` |
| `midi` | `{"$ref":"#/$defs/midi"}` | No / conditional | Optional document-level logical MIDI bus declarations. No physical device or DAW port assignment is encoded. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/midi` |

### Exact structure, conditions and ranges

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://yoh-nak.github.io/ostf/schema/ostf-4.2.0.schema.json",
  "title": "Open Song Timeline Format (OSTF) 4.2.0",
  "description": "OSTF 4.2.0: backward-compatible OSTF 4.1 Core plus optional phonetics, vocal profiles, and vocal performances; instrumental MIDI semantics remain intact.",
  "$comment": "OSTF 4.2.0 structural authority. Normative semantics: docs/SPECIFICATION.md and docs/COMPLETE_MANUAL.md. Schema identifiers do not require network retrieval. Native application interoperability is not certified by this specification release.",
  "type": "object",
  "properties": {
    "format": {
      "const": "OSTF"
    },
    "version": {
      "const": "4.2.0"
    },
    "ppq": {
      "type": "integer",
      "minimum": 1,
      "maximum": 960000
    },
    "song": {
      "$ref": "#/$defs/song"
    },
    "timeline": {
      "$ref": "#/$defs/timeline"
    },
    "harmony": {
      "$ref": "#/$defs/harmony"
    },
    "tracks": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/track"
      }
    },
    "soundSlots": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/soundSlot"
      }
    },
    "lyrics": {
      "$ref": "#/$defs/lyrics"
    },
    "resources": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/resource"
      }
    },
    "extensions": {
      "$ref": "#/$defs/legacy33/$defs/extensions",
      "description": "Optional third-party or verbatim legacy compatibility payloads. Standard Core always remains authoritative. New first-party common information must not be stored only here."
    },
    "drumKits": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/drumKit"
      },
      "description": "Optional multiple percussion-kit definitions; absent = no declared kits (3.0 compatible)."
    },
    "contributors": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/contributor"
      },
      "description": "Optional unordered identity records referenced by song.credits. No contributor limit is imposed by this format."
    },
    "document": {
      "$ref": "#/$defs/documentInfo"
    },
    "relativePhrases": {
      "$ref": "#/$defs/relativePhrases"
    },
    "generation": {
      "$ref": "#/$defs/generation"
    },
    "presentation": {
      "$ref": "#/$defs/presentation"
    },
    "phraseLibrary": {
      "$ref": "#/$defs/phraseLibrary"
    },
    "clipChoices": {
      "$ref": "#/$defs/clipChoices"
    },
    "localization": {
      "$ref": "#/$defs/localization"
    },
    "provenance": {
      "$ref": "#/$defs/provenance"
    },
    "midi": {
      "$ref": "#/$defs/midi",
      "description": "Optional document-level logical MIDI bus declarations. No physical device or DAW port assignment is encoded."
    }
  },
  "required": [
    "format",
    "version",
    "ppq",
    "song",
    "timeline",
    "harmony",
    "tracks",
    "soundSlots",
    "lyrics",
    "resources"
  ],
  "additionalProperties": false
}
```

<a id="schema-8c1697fddab4"></a>
## id

`#/$defs/id`


### Exact structure, conditions and ranges

```json
{
  "type": "string",
  "pattern": "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="schema-c35af8db37cc"></a>
## nonnegative

`#/$defs/nonnegative`


### Exact structure, conditions and ranges

```json
{
  "type": "integer",
  "minimum": 0,
  "maximum": 9007199254740991
}
```

<a id="schema-c337f17304bf"></a>
## positive

`#/$defs/positive`


### Exact structure, conditions and ranges

```json
{
  "type": "integer",
  "minimum": 1,
  "maximum": 9007199254740991
}
```

<a id="schema-f9a49621bf61"></a>
## signed

`#/$defs/signed`


### Exact structure, conditions and ranges

```json
{
  "type": "integer",
  "minimum": -9007199254740991,
  "maximum": 9007199254740991
}
```

<a id="schema-44b9e8efcfeb"></a>
## pitch

`#/$defs/pitch`


### Exact structure, conditions and ranges

```json
{
  "type": "integer",
  "minimum": 0,
  "maximum": 127
}
```

<a id="schema-981414324ed5"></a>
## ref

`#/$defs/ref`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `type` | `{"enum":["section","track","clip","note","chord","scale","soundSlot","drumKit","lyricDocument","lyricPhrase","lyricUnit","lyricAlignment","resource","genre","contributor","credit","alternateTitle","mood","keyChange","phraseTemplate","phraseInstance","clipChoiceGroup","clipCandidate","roleDefinition","generationProcess","provenanceRecord","midiBus","midiEvent","lyricVoice","trackDirection"]}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/relativePhrases/dependencies/refs/0/type` |
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/relativePhrases/dependencies/refs/0/id` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "type": {
      "enum": [
        "section",
        "track",
        "clip",
        "note",
        "chord",
        "scale",
        "soundSlot",
        "drumKit",
        "lyricDocument",
        "lyricPhrase",
        "lyricUnit",
        "lyricAlignment",
        "resource",
        "genre",
        "contributor",
        "credit",
        "alternateTitle",
        "mood",
        "keyChange",
        "phraseTemplate",
        "phraseInstance",
        "clipChoiceGroup",
        "clipCandidate",
        "roleDefinition",
        "generationProcess",
        "provenanceRecord",
        "midiBus",
        "midiEvent",
        "lyricVoice",
        "trackDirection"
      ]
    },
    "id": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "type",
    "id"
  ],
  "additionalProperties": false
}
```

<a id="schema-1a2975da6dc1"></a>
## range

`#/$defs/range`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `start` | `{"$ref":"#/$defs/nonnegative"}` | Yes | Start in the owner-defined time domain; see the manual. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/processes/0/targetRange/start` |
| `duration` | `{"$ref":"#/$defs/positive"}` | Yes | Positive duration in ticks. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/processes/0/targetRange/duration` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    }
  },
  "required": [
    "start",
    "duration"
  ],
  "additionalProperties": false
}
```

<a id="schema-564171196249"></a>
## spelledPitchClass

`#/$defs/spelledPitchClass`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `step` | `{"enum":["A","B","C","D","E","F","G"]}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/key/tonic/step` |
| `alter` | `{"type":"integer","minimum":-2,"maximum":2}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/key/tonic/alter` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "step": {
      "enum": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G"
      ]
    },
    "alter": {
      "type": "integer",
      "minimum": -2,
      "maximum": 2
    }
  },
  "required": [
    "step",
    "alter"
  ],
  "additionalProperties": false
}
```

<a id="schema-8e772ecd20dd"></a>
## song

`#/$defs/song`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `title` | `{"type":"string"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/title` |
| `primaryMelodyTrackId` | `{"$ref":"#/$defs/id"}` | No / conditional | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/song/primaryMelodyTrackId` |
| `localizedTitles` | `{"$ref":"#/$defs/localizedNames"}` | No / conditional | Optional localized song-title alternatives. song.title is the stable fallback. | [36-localized-names.ostf](../examples/36-localized-names.ostf)<br>`/song/localizedTitles` |
| `subtitle` | `{"type":"string"}` | No / conditional | Optional original-language subtitle. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/subtitle` |
| `description` | `{"type":"string"}` | No / conditional | Optional original-language description, including Unicode and line breaks. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/description` |
| `alternateTitles` | `{"type":"array","items":{"$ref":"#/$defs/alternateTitle"}}` | No / conditional | Additional stable-ID source-language titles. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/alternateTitles` |
| `credits` | `{"type":"array","items":{"$ref":"#/$defs/credit"}}` | No / conditional | Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/credits` |
| `genres` | `{"type":"array","items":{"$ref":"#/$defs/genre"}}` | No / conditional | Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/genres` |
| `key` | `{"$ref":"#/$defs/key"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/key` |
| `scale` | `{"$ref":"#/$defs/scaleDefinition"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/scale` |
| `languages` | `{"type":"array","items":{"type":"string","minLength":1,"description":"Authored language tag, preferably BCP 47. Unknown spelling is retained; case-insensitive duplicate tags forbidden."},"uniqueItems":true}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/languages` |
| `primaryLyricDocumentId` | `{"$ref":"#/$defs/id"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/primaryLyricDocumentId` |
| `moods` | `{"type":"array","items":{"$ref":"#/$defs/mood"}}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/moods` |
| `rights` | `{"$ref":"#/$defs/rightsStatement"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/rights` |
| `melodyTrackIds` | `{"type":"array","uniqueItems":true,"items":{"$ref":"#/$defs/id"}}` | No / conditional | Optional ordered set of tracks explicitly authored as melody-bearing tracks. If present with primaryMelodyTrackId, the primary track must be a member. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/melodyTrackIds` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    },
    "primaryMelodyTrackId": {
      "$ref": "#/$defs/id"
    },
    "localizedTitles": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized song-title alternatives. song.title is the stable fallback."
    },
    "subtitle": {
      "type": "string",
      "description": "Optional original-language subtitle."
    },
    "description": {
      "type": "string",
      "description": "Optional original-language description, including Unicode and line breaks."
    },
    "alternateTitles": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/alternateTitle"
      },
      "description": "Additional stable-ID source-language titles."
    },
    "credits": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/credit"
      },
      "description": "Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted."
    },
    "genres": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/genre"
      },
      "description": "Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified."
    },
    "key": {
      "$ref": "#/$defs/key"
    },
    "scale": {
      "$ref": "#/$defs/scaleDefinition"
    },
    "languages": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1,
        "description": "Authored language tag, preferably BCP 47. Unknown spelling is retained; case-insensitive duplicate tags forbidden."
      },
      "uniqueItems": true
    },
    "primaryLyricDocumentId": {
      "$ref": "#/$defs/id"
    },
    "moods": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/mood"
      }
    },
    "rights": {
      "$ref": "#/$defs/rightsStatement"
    },
    "melodyTrackIds": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "$ref": "#/$defs/id"
      },
      "description": "Optional ordered set of tracks explicitly authored as melody-bearing tracks. If present with primaryMelodyTrackId, the primary track must be a member."
    }
  },
  "required": [
    "title"
  ],
  "additionalProperties": false
}
```

<a id="schema-e852a1ccdb07"></a>
## section

`#/$defs/section`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/timeline/sections/0/id` |
| `name` | `{"type":"string","minLength":1}` | Yes | Authored display name; never an identity or executable instruction. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/timeline/sections/0/name` |
| `start` | `{"$ref":"#/$defs/nonnegative"}` | Yes | Start in the owner-defined time domain; see the manual. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/timeline/sections/0/start` |
| `duration` | `{"$ref":"#/$defs/positive"}` | Yes | Positive duration in ticks. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/timeline/sections/0/duration` |
| `role` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/timeline/sections/0/role` |
| `localizedNames` | `{"$ref":"#/$defs/localizedNames"}` | No / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/timeline/sections/0/localizedNames` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "role": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "name",
    "start",
    "duration"
  ],
  "additionalProperties": false
}
```

<a id="schema-402caf4cc3df"></a>
## tempo

`#/$defs/tempo`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `at` | `{"$ref":"#/$defs/nonnegative"}` | Yes | Time point in the owner-defined time domain. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/timeline/tempoChanges/0/at` |
| `bpm` | `{"type":"number","exclusiveMinimum":0,"maximum":1000}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/timeline/tempoChanges/0/bpm` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/nonnegative"
    },
    "bpm": {
      "type": "number",
      "exclusiveMinimum": 0,
      "maximum": 1000
    }
  },
  "required": [
    "at",
    "bpm"
  ],
  "additionalProperties": false
}
```

<a id="schema-7ab4411e74dc"></a>
## meter

`#/$defs/meter`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `at` | `{"$ref":"#/$defs/nonnegative"}` | Yes | Time point in the owner-defined time domain. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/timeline/meterChanges/0/at` |
| `numerator` | `{"type":"integer","minimum":1,"maximum":64}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/timeline/meterChanges/0/numerator` |
| `denominator` | `{"enum":[1,2,4,8,16,32,64],"type":"integer"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/timeline/meterChanges/0/denominator` |
| `beatGroups` | `{"type":"array","items":{"type":"integer","minimum":1,"maximum":64},"minItems":1,"maxItems":64}` | No / conditional | Optional additive grouping in denominator units. Values must sum to numerator. Descriptive only; does not change note timestamps. | [40-meter-map.ostf](../examples/40-meter-map.ostf)<br>`/timeline/meterChanges/1/beatGroups` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/nonnegative"
    },
    "numerator": {
      "type": "integer",
      "minimum": 1,
      "maximum": 64
    },
    "denominator": {
      "enum": [
        1,
        2,
        4,
        8,
        16,
        32,
        64
      ],
      "type": "integer"
    },
    "beatGroups": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 1,
        "maximum": 64
      },
      "minItems": 1,
      "maxItems": 64,
      "description": "Optional additive grouping in denominator units. Values must sum to numerator. Descriptive only; does not change note timestamps."
    }
  },
  "required": [
    "at",
    "numerator",
    "denominator"
  ],
  "additionalProperties": false
}
```

<a id="schema-5532f237d17d"></a>
## timeline

`#/$defs/timeline`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `sections` | `{"type":"array","items":{"$ref":"#/$defs/section"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/timeline/sections` |
| `tempoChanges` | `{"type":"array","items":{"$ref":"#/$defs/tempo"},"minItems":1}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/timeline/tempoChanges` |
| `meterChanges` | `{"type":"array","items":{"$ref":"#/$defs/meter"},"minItems":1}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/timeline/meterChanges` |
| `keyChanges` | `{"type":"array","items":{"$ref":"#/$defs/keyChange"}}` | No / conditional | See the owning object semantics and exact constraints below. | [31-effective-key-scale.ostf](../examples/31-effective-key-scale.ostf)<br>`/timeline/keyChanges` |
| `duration` | `{"$ref":"#/$defs/nonnegative"}` | No / conditional | Positive duration in ticks. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/timeline/duration` |
| `barOrigin` | `{"$ref":"#/$defs/nonnegative"}` | No / conditional | See the owning object semantics and exact constraints below. | [41-bar-origin.ostf](../examples/41-bar-origin.ostf)<br>`/timeline/barOrigin` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "sections": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/section"
      }
    },
    "tempoChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/tempo"
      },
      "minItems": 1
    },
    "meterChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/meter"
      },
      "minItems": 1
    },
    "keyChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/keyChange"
      }
    },
    "duration": {
      "$ref": "#/$defs/nonnegative"
    },
    "barOrigin": {
      "$ref": "#/$defs/nonnegative"
    }
  },
  "required": [
    "sections",
    "tempoChanges",
    "meterChanges"
  ],
  "additionalProperties": false
}
```

<a id="schema-5728fe0e89d0"></a>
## chord

`#/$defs/chord`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/harmony/chords/0/id` |
| `start` | `{"$ref":"#/$defs/nonnegative"}` | Yes | Start in the owner-defined time domain; see the manual. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/harmony/chords/0/start` |
| `duration` | `{"$ref":"#/$defs/positive"}` | Yes | Positive duration in ticks. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/harmony/chords/0/duration` |
| `label` | `{"type":"string","minLength":1}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/harmony/chords/0/label` |
| `root` | `{"$ref":"#/$defs/spelledPitchClass"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/harmony/chords/0/root` |
| `intervals` | `{"type":"array","items":{"type":"integer","minimum":0,"maximum":35},"minItems":1,"maxItems":36,"uniqueItems":true,"contains":{"const":0}}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/harmony/chords/0/intervals` |
| `bass` | `{"$ref":"#/$defs/spelledPitchClass"}` | No / conditional | See the owning object semantics and exact constraints below. | [42-slash-chord.ostf](../examples/42-slash-chord.ostf)<br>`/harmony/chords/0/bass` |
| `voicing` | `{"$ref":"#/$defs/voicing"}` | No / conditional | Optional pitch snapshot (not an arrangement note sequence). No automatic playback. | [33-chord-voicing.ostf](../examples/33-chord-voicing.ostf)<br>`/harmony/chords/0/voicing` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string",
      "minLength": 1
    },
    "root": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 35
      },
      "minItems": 1,
      "maxItems": 36,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "bass": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "voicing": {
      "$ref": "#/$defs/voicing",
      "description": "Optional pitch snapshot (not an arrangement note sequence). No automatic playback."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "label"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "root": [
      "intervals"
    ],
    "intervals": [
      "root"
    ]
  }
}
```

<a id="schema-7120179dfd85"></a>
## scale

`#/$defs/scale`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [25-integrated-jazz-session.ostf](../examples/25-integrated-jazz-session.ostf)<br>`/harmony/scales/0/id` |
| `start` | `{"$ref":"#/$defs/nonnegative"}` | Yes | Start in the owner-defined time domain; see the manual. | [25-integrated-jazz-session.ostf](../examples/25-integrated-jazz-session.ostf)<br>`/harmony/scales/0/start` |
| `duration` | `{"$ref":"#/$defs/positive"}` | Yes | Positive duration in ticks. | [25-integrated-jazz-session.ostf](../examples/25-integrated-jazz-session.ostf)<br>`/harmony/scales/0/duration` |
| `label` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [43-timed-harmony-scales.ostf](../examples/43-timed-harmony-scales.ostf)<br>`/harmony/scales/0/label` |
| `tonic` | `{"$ref":"#/$defs/spelledPitchClass"}` | Yes | See the owning object semantics and exact constraints below. | [25-integrated-jazz-session.ostf](../examples/25-integrated-jazz-session.ostf)<br>`/harmony/scales/0/tonic` |
| `intervals` | `{"type":"array","items":{"type":"integer","minimum":0,"maximum":11},"minItems":1,"maxItems":12,"uniqueItems":true,"contains":{"const":0}}` | Yes | See the owning object semantics and exact constraints below. | [25-integrated-jazz-session.ostf](../examples/25-integrated-jazz-session.ostf)<br>`/harmony/scales/0/intervals` |
| `targets` | `{"type":"array","items":{"$ref":"#/$defs/scaleTarget"},"minItems":1,"uniqueItems":true}` | No / conditional | Optional explicit scope. Absence means general timed context, not a global key. Overlapping contexts are not resolved by array order. | [25-integrated-jazz-session.ostf](../examples/25-integrated-jazz-session.ostf)<br>`/harmony/scales/0/targets` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 11
      },
      "minItems": 1,
      "maxItems": 12,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "targets": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/scaleTarget"
      },
      "minItems": 1,
      "uniqueItems": true,
      "description": "Optional explicit scope. Absence means general timed context, not a global key. Overlapping contexts are not resolved by array order."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "tonic",
    "intervals"
  ],
  "additionalProperties": false
}
```

<a id="schema-d9a56b61ff7e"></a>
## harmony

`#/$defs/harmony`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `chords` | `{"type":"array","items":{"$ref":"#/$defs/chord"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/harmony/chords` |
| `scales` | `{"type":"array","items":{"$ref":"#/$defs/scale"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/harmony/scales` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "chords": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/chord"
      }
    },
    "scales": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/scale"
      }
    }
  },
  "required": [
    "chords",
    "scales"
  ],
  "additionalProperties": false
}
```

<a id="schema-81166c6fec71"></a>
## instrument

`#/$defs/instrument`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `name` | `{"type":"string"}` | Yes | Authored display name; never an identity or executable instruction. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/instrument/name` |
| `family` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/instrument/family` |
| `localizedNames` | `{"$ref":"#/$defs/localizedNames"}` | No / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/instrument/localizedNames` |
| `playablePitchRange` | `{"$ref":"#/$defs/playablePitchRange"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/instrument/playablePitchRange` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "family": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    },
    "playablePitchRange": {
      "$ref": "#/$defs/playablePitchRange"
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```

<a id="schema-96e72b83e194"></a>
## note

`#/$defs/note`

Concrete Core DAW-note event. The event target is pitch or soundSlotId. Optional 3.5 note-local properties preserve mute, release velocity, probability and velocity variation. pitchRole=fixedTrigger marks a literal MIDI key trigger that must not be musically transposed or analyzed.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/clips/0/notes/0/id` |
| `start` | `{"$ref":"#/$defs/signed"}` | Yes | Start in the owner-defined time domain; see the manual. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/clips/0/notes/0/start` |
| `duration` | `{"$ref":"#/$defs/positive"}` | Yes | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/clips/0/notes/0/duration` |
| `pitch` | `{"$ref":"#/$defs/pitch"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/clips/0/notes/0/pitch` |
| `soundSlotId` | `{"$ref":"#/$defs/id"}` | No / conditional | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/2/clips/0/notes/0/soundSlotId` |
| `velocity` | `{"type":"integer","minimum":1,"maximum":127}` | No / conditional | Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/clips/0/notes/0/velocity` |
| `enabled` | `{"type":"boolean","default":true}` | No / conditional | Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0. | [37-note-performance-state.ostf](../examples/37-note-performance-state.ostf)<br>`/tracks/0/clips/0/notes/0/enabled` |
| `releaseVelocity` | `{"type":"integer","minimum":0,"maximum":127}` | No / conditional | Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default. | [37-note-performance-state.ostf](../examples/37-note-performance-state.ostf)<br>`/tracks/0/clips/0/notes/0/releaseVelocity` |
| `probability` | `{"type":"number","minimum":0,"maximum":1,"default":1}` | No / conditional | Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange. | [38-note-probability-deviation.ostf](../examples/38-note-probability-deviation.ostf)<br>`/tracks/0/clips/0/notes/0/probability` |
| `velocityDeviation` | `{"type":"integer","minimum":-126,"maximum":126,"default":0}` | No / conditional | Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0. | [38-note-probability-deviation.ostf](../examples/38-note-probability-deviation.ostf)<br>`/tracks/0/clips/0/notes/0/velocityDeviation` |
| `pitchRole` | `{"enum":["musical","fixedTrigger"],"default":"musical"}` | No / conditional | Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes. | [44-fixed-trigger-note.ostf](../examples/44-fixed-trigger-note.ostf)<br>`/tracks/0/clips/0/notes/0/pitchRole` |
| `channel` | `{"$ref":"#/$defs/midiChannel"}` | No / conditional | Optional concrete MIDI channel for this performed note. In singleChannel mode it may be omitted and inherited from the track; in multiChannel/MPE mode semantic rules require explicit channel where channel identity matters. | [23-mpe-per-note-expression.ostf](../examples/23-mpe-per-note-expression.ostf)<br>`/tracks/0/clips/0/notes/0/channel` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive",
      "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
    },
    "pitch": {
      "$ref": "#/$defs/pitch"
    },
    "soundSlotId": {
      "$ref": "#/$defs/id",
      "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
    },
    "velocity": {
      "type": "integer",
      "minimum": 1,
      "maximum": 127,
      "description": "Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving."
    },
    "enabled": {
      "type": "boolean",
      "default": true,
      "description": "Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0."
    },
    "releaseVelocity": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127,
      "description": "Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default."
    },
    "probability": {
      "type": "number",
      "minimum": 0,
      "maximum": 1,
      "default": 1,
      "description": "Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange."
    },
    "velocityDeviation": {
      "type": "integer",
      "minimum": -126,
      "maximum": 126,
      "default": 0,
      "description": "Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0."
    },
    "pitchRole": {
      "enum": [
        "musical",
        "fixedTrigger"
      ],
      "default": "musical",
      "description": "Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel",
      "description": "Optional concrete MIDI channel for this performed note. In singleChannel mode it may be omitted and inherited from the track; in multiChannel/MPE mode semantic rules require explicit channel where channel identity matters."
    }
  },
  "required": [
    "id",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "required": [
        "pitch"
      ],
      "not": {
        "required": [
          "soundSlotId"
        ]
      }
    },
    {
      "required": [
        "soundSlotId"
      ],
      "not": {
        "required": [
          "pitch"
        ]
      }
    }
  ],
  "description": "Concrete Core DAW-note event. The event target is pitch or soundSlotId. Optional 3.5 note-local properties preserve mute, release velocity, probability and velocity variation. pitchRole=fixedTrigger marks a literal MIDI key trigger that must not be musically transposed or analyzed.",
  "dependentRequired": {
    "velocityDeviation": [
      "velocity"
    ]
  },
  "allOf": [
    {
      "if": {
        "required": [
          "soundSlotId"
        ]
      },
      "then": {
        "not": {
          "required": [
            "pitchRole"
          ]
        }
      }
    }
  ]
}
```

<a id="schema-6cef7ff6a8f2"></a>
## clip

`#/$defs/clip`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/clips/0/id` |
| `name` | `{"type":"string"}` | No / conditional | Authored display name; never an identity or executable instruction. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/clips/0/name` |
| `start` | `{"$ref":"#/$defs/nonnegative"}` | Yes | Start in the owner-defined time domain; see the manual. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/clips/0/start` |
| `duration` | `{"$ref":"#/$defs/positive"}` | Yes | Positive duration in ticks. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/clips/0/duration` |
| `enabled` | `{"type":"boolean","default":true}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/clips/0/enabled` |
| `notes` | `{"type":"array","items":{"$ref":"#/$defs/note"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/clips/0/notes` |
| `localizedNames` | `{"$ref":"#/$defs/localizedNames"}` | No / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/clips/0/localizedNames` |
| `midiEvents` | `{"type":"array","items":{"$ref":"#/$defs/midiEvent"}}` | No / conditional | Optional clip-local MIDI performance/control events. start is local to the clip and may be negative if absolute time remains nonnegative. Notes remain authoritative in notes[]. | [06-instrument-midi-unchanged.ostf](../examples/06-instrument-midi-unchanged.ostf)<br>`/tracks/0/clips/0/midiEvents` |
| `vocalPerformances` | `{"type":"array","items":{"$ref":"#/$defs/vocalPerformance"},"minItems":1}` | No / conditional | Optional voice-specific phoneme and singing-performance data; references lyrics.voices. Notes/MIDI remain authoritative for MIDI playback. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "enabled": {
      "type": "boolean",
      "default": true
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/note"
      }
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    },
    "midiEvents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/midiEvent"
      },
      "description": "Optional clip-local MIDI performance/control events. start is local to the clip and may be negative if absolute time remains nonnegative. Notes remain authoritative in notes[]."
    },
    "vocalPerformances": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalPerformance"
      },
      "minItems": 1,
      "description": "Optional voice-specific phoneme and singing-performance data; references lyrics.voices. Notes/MIDI remain authoritative for MIDI playback."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "notes"
  ],
  "additionalProperties": false
}
```

<a id="schema-63477fd6abf3"></a>
## track

`#/$defs/track`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/id` |
| `name` | `{"type":"string"}` | Yes | Authored display name; never an identity or executable instruction. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/name` |
| `role` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/role` |
| `instrument` | `{"$ref":"#/$defs/instrument"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/instrument` |
| `enabled` | `{"type":"boolean","default":true}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/enabled` |
| `clips` | `{"type":"array","items":{"$ref":"#/$defs/clip"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/clips` |
| `trackType` | `{"enum":["melodic","drum","mixed"]}` | No / conditional | Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/trackType` |
| `preferredView` | `{"enum":["auto","pianoRoll","drumGrid"],"default":"auto"}` | No / conditional | Non-binding presentation preference. Does not change note meaning. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/2/preferredView` |
| `soundSource` | `{"$ref":"#/$defs/soundSource"}` | No / conditional | Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee. | [34-sound-source-external-midi.ostf](../examples/34-sound-source-external-midi.ostf)<br>`/tracks/0/soundSource` |
| `localizedNames` | `{"$ref":"#/$defs/localizedNames"}` | No / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [36-localized-names.ostf](../examples/36-localized-names.ostf)<br>`/tracks/0/localizedNames` |
| `drumKitId` | `{"$ref":"#/$defs/id"}` | No / conditional | Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/2/drumKitId` |
| `midi` | `{"$ref":"#/$defs/trackMidi"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/midi` |
| `directions` | `{"type":"array","items":{"$ref":"#/$defs/trackDirection"}}` | No / conditional | Optional typed semantic instructions for performance, interpretation, or generation. Uses the global OSTF timebase; it is not a second timeline. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string"
    },
    "instrument": {
      "$ref": "#/$defs/instrument"
    },
    "enabled": {
      "type": "boolean",
      "default": true
    },
    "clips": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/clip"
      }
    },
    "trackType": {
      "enum": [
        "melodic",
        "drum",
        "mixed"
      ],
      "description": "Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class."
    },
    "preferredView": {
      "enum": [
        "auto",
        "pianoRoll",
        "drumGrid"
      ],
      "default": "auto",
      "description": "Non-binding presentation preference. Does not change note meaning."
    },
    "soundSource": {
      "$ref": "#/$defs/soundSource",
      "description": "Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee."
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    },
    "drumKitId": {
      "$ref": "#/$defs/id",
      "description": "Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit."
    },
    "midi": {
      "$ref": "#/$defs/trackMidi"
    },
    "directions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/trackDirection"
      },
      "description": "Optional typed semantic instructions for performance, interpretation, or generation. Uses the global OSTF timebase; it is not a second timeline."
    }
  },
  "required": [
    "id",
    "name",
    "clips"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "trackType": {
            "const": "melodic"
          }
        },
        "required": [
          "trackType"
        ]
      },
      "then": {
        "not": {
          "required": [
            "drumKitId"
          ]
        }
      }
    }
  ]
}
```

<a id="schema-0ddd4ff5938f"></a>
## soundSlot

`#/$defs/soundSlot`

Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/soundSlots/0/id` |
| `name` | `{"type":"string"}` | Yes | Authored display name; never an identity or executable instruction. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/soundSlots/0/name` |
| `role` | `{"type":"string"}` | No / conditional | Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier. | [39-sound-slot-midi-mapping.ostf](../examples/39-sound-slot-midi-mapping.ostf)<br>`/soundSlots/0/role` |
| `midiNote` | `{"$ref":"#/$defs/pitch"}` | No / conditional | Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity. | [39-sound-slot-midi-mapping.ostf](../examples/39-sound-slot-midi-mapping.ostf)<br>`/soundSlots/0/midiNote` |
| `midiMapping` | `{"$ref":"#/$defs/midiMapping"}` | No / conditional | Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/soundSlots/0/midiMapping` |
| `localizedNames` | `{"$ref":"#/$defs/localizedNames"}` | No / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [36-localized-names.ostf](../examples/36-localized-names.ostf)<br>`/soundSlots/0/localizedNames` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string",
      "description": "Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier."
    },
    "midiNote": {
      "$ref": "#/$defs/pitch",
      "description": "Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity."
    },
    "midiMapping": {
      "$ref": "#/$defs/midiMapping",
      "description": "Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity."
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false,
  "description": "Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded."
}
```

<a id="schema-1f5cbf9e5e4b"></a>
## lyricDocument

`#/$defs/lyricDocument`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/documents/0/id` |
| `title` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/documents/0/title` |
| `language` | `{"type":"string"}` | No / conditional | Authored language tag. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/documents/0/language` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "title": {
      "type": "string"
    },
    "language": {
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```

<a id="schema-d24fe48780db"></a>
## lyricPhrase

`#/$defs/lyricPhrase`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/phrases/0/id` |
| `documentId` | `{"$ref":"#/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/phrases/0/documentId` |
| `text` | `{"type":"string"}` | Yes | Authored text, preserved without executing its contents. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/phrases/0/text` |
| `pronunciation` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [45-lyrics-pronunciation.ostf](../examples/45-lyrics-pronunciation.ostf)<br>`/lyrics/phrases/0/pronunciation` |
| `start` | `{"$ref":"#/$defs/nonnegative"}` | No / conditional | Start in the owner-defined time domain; see the manual. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/phrases/0/start` |
| `duration` | `{"$ref":"#/$defs/positive"}` | No / conditional | Positive duration in ticks. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/phrases/0/duration` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "text": {
      "type": "string"
    },
    "pronunciation": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    }
  },
  "required": [
    "id",
    "documentId",
    "text"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```

<a id="schema-27b0290397e0"></a>
## lyricUnit

`#/$defs/lyricUnit`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/units/0/id` |
| `phraseId` | `{"$ref":"#/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/units/0/phraseId` |
| `text` | `{"type":"string"}` | Yes | Authored text, preserved without executing its contents. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/units/0/text` |
| `pronunciation` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/lyrics/units/0/pronunciation` |
| `start` | `{"$ref":"#/$defs/nonnegative"}` | No / conditional | Start in the owner-defined time domain; see the manual. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/lyrics/units/0/start` |
| `duration` | `{"$ref":"#/$defs/positive"}` | No / conditional | Positive duration in ticks. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/lyrics/units/0/duration` |
| `phonetics` | `{"type":"array","items":{"$ref":"#/$defs/vocalPhonetics"},"minItems":1}` | No / conditional | Optional alternate phoneme token sequences. Do not alter text/pronunciation. Multiple alphabets are permitted. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/lyrics/units/0/phonetics` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "phraseId": {
      "$ref": "#/$defs/id"
    },
    "text": {
      "type": "string"
    },
    "pronunciation": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "phonetics": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalPhonetics"
      },
      "minItems": 1,
      "description": "Optional alternate phoneme token sequences. Do not alter text/pronunciation. Multiple alphabets are permitted."
    }
  },
  "required": [
    "id",
    "phraseId",
    "text"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```

<a id="schema-4bce9d4af5d4"></a>
## lyricAlignment

`#/$defs/lyricAlignment`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/alignments/0/id` |
| `unitIds` | `{"type":"array","items":{"$ref":"#/$defs/id"},"uniqueItems":true,"minItems":1}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/alignments/0/unitIds` |
| `noteIds` | `{"type":"array","items":{"$ref":"#/$defs/id"},"uniqueItems":true,"minItems":1}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/alignments/0/noteIds` |
| `voiceId` | `{"$ref":"#/$defs/id"}` | No / conditional | Optional lyricVoice association. When present, aligned units must belong to that voice document and aligned notes must belong to that voice track. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/alignments/0/voiceId` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "unitIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true,
      "minItems": 1
    },
    "noteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true,
      "minItems": 1
    },
    "voiceId": {
      "$ref": "#/$defs/id",
      "description": "Optional lyricVoice association. When present, aligned units must belong to that voice document and aligned notes must belong to that voice track."
    }
  },
  "required": [
    "id",
    "unitIds",
    "noteIds"
  ],
  "additionalProperties": false
}
```

<a id="schema-2160208bc94c"></a>
## lyrics

`#/$defs/lyrics`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `documents` | `{"type":"array","items":{"$ref":"#/$defs/lyricDocument"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/documents` |
| `phrases` | `{"type":"array","items":{"$ref":"#/$defs/lyricPhrase"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/phrases` |
| `units` | `{"type":"array","items":{"$ref":"#/$defs/lyricUnit"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/units` |
| `alignments` | `{"type":"array","items":{"$ref":"#/$defs/lyricAlignment"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/alignments` |
| `voices` | `{"type":"array","items":{"$ref":"#/$defs/lyricVoice"}}` | No / conditional | Optional explicit vocal-part relationships for multi-voice, harmony and chorus lyrics. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/voices` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "documents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricDocument"
      }
    },
    "phrases": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricPhrase"
      }
    },
    "units": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricUnit"
      }
    },
    "alignments": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricAlignment"
      }
    },
    "voices": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricVoice"
      },
      "description": "Optional explicit vocal-part relationships for multi-voice, harmony and chorus lyrics."
    }
  },
  "required": [
    "documents",
    "phrases",
    "units",
    "alignments"
  ],
  "additionalProperties": false
}
```

<a id="schema-3aab424c33aa"></a>
## sha256

`#/$defs/sha256`


### Exact structure, conditions and ranges

```json
{
  "type": "string",
  "pattern": "^[0-9a-f]{64}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="schema-6d9d5986fda3"></a>
## resource

`#/$defs/resource`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/resources/0/id` |
| `kind` | `{"enum":["audio","midi","text","other"]}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/resources/0/kind` |
| `uri` | `{"type":"string","minLength":1}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/resources/0/uri` |
| `name` | `{"type":"string"}` | No / conditional | Authored display name; never an identity or executable instruction. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/resources/0/name` |
| `sha256` | `{"$ref":"#/$defs/sha256"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/resources/0/sha256` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "kind": {
      "enum": [
        "audio",
        "midi",
        "text",
        "other"
      ]
    },
    "uri": {
      "type": "string",
      "minLength": 1
    },
    "name": {
      "type": "string"
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    }
  },
  "required": [
    "id",
    "kind",
    "uri"
  ],
  "additionalProperties": false
}
```

<a id="schema-75af29175dd3"></a>
## dependencies

`#/$defs/dependencies`


### Exact structure, conditions and ranges

```json
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "scope": {
          "enum": [
            "document",
            "none"
          ]
        }
      },
      "required": [
        "scope"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "scope": {
          "const": "objects"
        },
        "refs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/ref"
          },
          "minItems": 1,
          "uniqueItems": true
        }
      },
      "required": [
        "scope",
        "refs"
      ],
      "additionalProperties": false
    }
  ]
}
```

<a id="schema-a1d368bd2745"></a>
## relativeAssignment

`#/$defs/relativeAssignment`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `noteId` | `{"$ref":"#/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/relativePhrases/assignments/0/noteId` |
| `basis` | `{"enum":["chordTone","scaleDegree"]}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/relativePhrases/assignments/0/basis` |
| `contextId` | `{"$ref":"#/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/relativePhrases/assignments/0/contextId` |
| `anchorPitch` | `{"$ref":"#/$defs/pitch"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/relativePhrases/assignments/0/anchorPitch` |
| `index` | `{"type":"integer","minimum":1,"maximum":36}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/relativePhrases/assignments/0/index` |
| `chromaticOffset` | `{"type":"integer","minimum":-24,"maximum":24}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/relativePhrases/assignments/0/chromaticOffset` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "noteId": {
      "$ref": "#/$defs/id"
    },
    "basis": {
      "enum": [
        "chordTone",
        "scaleDegree"
      ]
    },
    "contextId": {
      "$ref": "#/$defs/id"
    },
    "anchorPitch": {
      "$ref": "#/$defs/pitch"
    },
    "index": {
      "type": "integer",
      "minimum": 1,
      "maximum": 36
    },
    "chromaticOffset": {
      "type": "integer",
      "minimum": -24,
      "maximum": 24
    }
  },
  "required": [
    "noteId",
    "basis",
    "contextId",
    "anchorPitch",
    "index",
    "chromaticOffset"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "basis": {
            "const": "scaleDegree"
          }
        },
        "required": [
          "basis"
        ]
      },
      "then": {
        "properties": {
          "index": {
            "maximum": 12
          }
        }
      }
    }
  ]
}
```

<a id="schema-7f5580e4d853"></a>
## generator

`#/$defs/generator`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"type":"string","minLength":1}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/processes/0/generator/id` |
| `version` | `{"type":"string","minLength":1}` | Yes | Version identifier for this owning object. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/processes/0/generator/version` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "version"
  ],
  "additionalProperties": false
}
```

<a id="schema-c843883807fe"></a>
## generationInput

`#/$defs/generationInput`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `role` | `{"type":"string","minLength":1}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/processes/0/inputs/0/role` |
| `ref` | `{"$ref":"#/$defs/ref"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/processes/0/inputs/0/ref` |
| `readRange` | `{"$ref":"#/$defs/range"}` | No / conditional | See the owning object semantics and exact constraints below. | [49-generation-process.ostf](../examples/49-generation-process.ostf)<br>`/generation/processes/0/inputs/0/readRange` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "role": {
      "type": "string",
      "minLength": 1
    },
    "ref": {
      "$ref": "#/$defs/ref"
    },
    "readRange": {
      "$ref": "#/$defs/range"
    }
  },
  "required": [
    "role",
    "ref"
  ],
  "additionalProperties": false
}
```

<a id="schema-7d1dd7d6e9ff"></a>
## generationProcess

`#/$defs/generationProcess`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/processes/0/id` |
| `generator` | `{"$ref":"#/$defs/generator"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/processes/0/generator` |
| `inputs` | `{"type":"array","items":{"$ref":"#/$defs/generationInput"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/processes/0/inputs` |
| `outputs` | `{"type":"array","items":{"$ref":"#/$defs/ref"},"minItems":1}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/processes/0/outputs` |
| `targetRange` | `{"$ref":"#/$defs/range"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/processes/0/targetRange` |
| `protectedNoteIds` | `{"type":"array","items":{"$ref":"#/$defs/id"},"uniqueItems":true}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/processes/0/protectedNoteIds` |
| `intent` | `{"$ref":"#/$defs/generationIntent"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/processes/0/intent` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "generator": {
      "$ref": "#/$defs/generator"
    },
    "inputs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/generationInput"
      }
    },
    "outputs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/ref"
      },
      "minItems": 1
    },
    "targetRange": {
      "$ref": "#/$defs/range"
    },
    "protectedNoteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    },
    "intent": {
      "$ref": "#/$defs/generationIntent"
    }
  },
  "required": [
    "id",
    "generator",
    "inputs",
    "outputs",
    "protectedNoteIds"
  ],
  "additionalProperties": false
}
```

<a id="schema-da077ea23895"></a>
## color

`#/$defs/color`


### Exact structure, conditions and ranges

```json
{
  "type": "string",
  "pattern": "^#[0-9A-Fa-f]{6}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="schema-caba67c7caf4"></a>
## roleDefinition

`#/$defs/roleDefinition`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/presentation/roleDefinitions/0/id` |
| `name` | `{"type":"string","minLength":1}` | Yes | Authored display name; never an identity or executable instruction. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/presentation/roleDefinitions/0/name` |
| `baseRole` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/presentation/roleDefinitions/0/baseRole` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "baseRole": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="schema-26f521dabf80"></a>
## roleColorMap

`#/$defs/roleColorMap`


### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "additionalProperties": {
    "$ref": "#/$defs/color"
  }
}
```

<a id="schema-f6caa7165a5e"></a>
## customRoleColorMap

`#/$defs/customRoleColorMap`


### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "propertyNames": {
    "$ref": "#/$defs/id"
  },
  "additionalProperties": {
    "$ref": "#/$defs/color"
  }
}
```

<a id="schema-442e7bcaa5f8"></a>
## objectColor

`#/$defs/objectColor`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `target` | `{"$ref":"#/$defs/ref"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/presentation/appearance/objectColors/0/target` |
| `color` | `{"$ref":"#/$defs/color"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/presentation/appearance/objectColors/0/color` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "target": {
      "$ref": "#/$defs/ref"
    },
    "color": {
      "$ref": "#/$defs/color"
    }
  },
  "required": [
    "target",
    "color"
  ],
  "additionalProperties": false
}
```

<a id="schema-5dfc7b11c09b"></a>
## phraseTemplate

`#/$defs/phraseTemplate`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/templates/0/id` |
| `duration` | `{"$ref":"#/$defs/positive"}` | Yes | Positive duration in ticks. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/templates/0/duration` |
| `notes` | `{"type":"array","items":{"$ref":"#/$defs/corePhraseSourceNote"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/templates/0/notes` |
| `name` | `{"type":"string"}` | No / conditional | Authored display name; never an identity or executable instruction. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/templates/0/name` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/corePhraseSourceNote"
      }
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "duration",
    "notes"
  ],
  "additionalProperties": false
}
```

<a id="schema-7033ad6b2acc"></a>
## phraseNoteMapping

`#/$defs/phraseNoteMapping`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `templateNoteId` | `{"$ref":"#/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/instances/0/noteMap/0/templateNoteId` |
| `repeatIndex` | `{"$ref":"#/$defs/nonnegative"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/instances/0/noteMap/0/repeatIndex` |
| `noteId` | `{"$ref":"#/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/instances/0/noteMap/0/noteId` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "templateNoteId": {
      "$ref": "#/$defs/id"
    },
    "repeatIndex": {
      "$ref": "#/$defs/nonnegative"
    },
    "noteId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "templateNoteId",
    "repeatIndex",
    "noteId"
  ],
  "additionalProperties": false
}
```

<a id="schema-f17bdbf88127"></a>
## phraseInstance

`#/$defs/phraseInstance`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/instances/0/id` |
| `templateId` | `{"$ref":"#/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/instances/0/templateId` |
| `clipId` | `{"$ref":"#/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/instances/0/clipId` |
| `repeatCount` | `{"$ref":"#/$defs/positive"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/instances/0/repeatCount` |
| `transpose` | `{"type":"integer","minimum":-127,"maximum":127}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/instances/0/transpose` |
| `noteMap` | `{"type":"array","items":{"$ref":"#/$defs/phraseNoteMapping"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/instances/0/noteMap` |
| `velocityMode` | `{"enum":["independent","linked"],"default":"independent"}` | No / conditional | independent preserves concrete velocities on refresh; linked requires exact presence/value equality with the template. This field does not trigger refresh on load. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/instances/0/velocityMode` |
| `noteStateMode` | `{"enum":["independent","linked"],"default":"independent"}` | No / conditional | Controls enabled/releaseVelocity/probability/velocityDeviation after materialization. independent preserves concrete note-state values on refresh; linked requires exact presence/value equality with the template. pitchRole is structural and must always remain semantically equal between a source pitch note and its mapped concrete note. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/instances/0/noteStateMode` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "templateId": {
      "$ref": "#/$defs/id"
    },
    "clipId": {
      "$ref": "#/$defs/id"
    },
    "repeatCount": {
      "$ref": "#/$defs/positive"
    },
    "transpose": {
      "type": "integer",
      "minimum": -127,
      "maximum": 127
    },
    "noteMap": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/phraseNoteMapping"
      }
    },
    "velocityMode": {
      "enum": [
        "independent",
        "linked"
      ],
      "default": "independent",
      "description": "independent preserves concrete velocities on refresh; linked requires exact presence/value equality with the template. This field does not trigger refresh on load."
    },
    "noteStateMode": {
      "enum": [
        "independent",
        "linked"
      ],
      "default": "independent",
      "description": "Controls enabled/releaseVelocity/probability/velocityDeviation after materialization. independent preserves concrete note-state values on refresh; linked requires exact presence/value equality with the template. pitchRole is structural and must always remain semantically equal between a source pitch note and its mapped concrete note."
    }
  },
  "required": [
    "id",
    "templateId",
    "clipId",
    "repeatCount",
    "transpose",
    "noteMap"
  ],
  "additionalProperties": false
}
```

<a id="schema-57909b1ed915"></a>
## clipCandidate

`#/$defs/clipCandidate`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/clipChoices/groups/0/candidates/0/id` |
| `clipIds` | `{"type":"array","items":{"$ref":"#/$defs/id"},"uniqueItems":true}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/clipChoices/groups/0/candidates/0/clipIds` |
| `name` | `{"type":"string"}` | No / conditional | Authored display name; never an identity or executable instruction. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/clipChoices/groups/0/candidates/0/name` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "clipIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "clipIds"
  ],
  "additionalProperties": false
}
```

<a id="schema-7e2d711ae826"></a>
## clipChoiceGroup

`#/$defs/clipChoiceGroup`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/clipChoices/groups/0/id` |
| `candidates` | `{"type":"array","items":{"$ref":"#/$defs/clipCandidate"},"minItems":1}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/clipChoices/groups/0/candidates` |
| `selectedCandidateId` | `{"anyOf":[{"$ref":"#/$defs/id"},{"type":"null"}]}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/clipChoices/groups/0/selectedCandidateId` |
| `name` | `{"type":"string"}` | No / conditional | Authored display name; never an identity or executable instruction. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/clipChoices/groups/0/name` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "candidates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/clipCandidate"
      },
      "minItems": 1
    },
    "selectedCandidateId": {
      "anyOf": [
        {
          "$ref": "#/$defs/id"
        },
        {
          "type": "null"
        }
      ]
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "candidates",
    "selectedCandidateId"
  ],
  "additionalProperties": false
}
```

<a id="schema-2f2e34aa29d7"></a>
## midiMapping

`#/$defs/midiMapping`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `standard` | `{"enum":["gm1","custom"]}` | Yes | gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/soundSlots/0/midiMapping/standard` |
| `note` | `{"$ref":"#/$defs/pitch"}` | Yes | MIDI1 note number in 0..127; for gm1 restrict to 35..81. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/soundSlots/0/midiMapping/note` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "standard": {
      "enum": [
        "gm1",
        "custom"
      ],
      "description": "gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number."
    },
    "note": {
      "$ref": "#/$defs/pitch",
      "description": "MIDI1 note number in 0..127; for gm1 restrict to 35..81."
    }
  },
  "required": [
    "standard",
    "note"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "standard": {
            "const": "gm1"
          }
        },
        "required": [
          "standard"
        ]
      },
      "then": {
        "properties": {
          "note": {
            "type": "integer",
            "minimum": 35,
            "maximum": 81
          }
        }
      }
    }
  ]
}
```

<a id="schema-05eae897621a"></a>
## soundSource

`#/$defs/soundSource`

Optional informational rendering class or opaque destination hint. In OSTF 4.0, track.midi.busId is the Core logical MIDI routing reference; soundSource does not bind a physical device, plugin state or preset.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `kind` | `{"enum":["unassigned","gm1","externalMidi","plugin","hostManaged"]}` | Yes | See the owning object semantics and exact constraints below. | [34-sound-source-external-midi.ostf](../examples/34-sound-source-external-midi.ostf)<br>`/tracks/0/soundSource/kind` |
| `identifier` | `{"type":"string","minLength":1}` | No / conditional | Opaque informational target identifier (for example a URI or plug-in identifier), not a physical MIDI-port binding or loading command. | [34-sound-source-external-midi.ostf](../examples/34-sound-source-external-midi.ostf)<br>`/tracks/0/soundSource/identifier` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "Optional informational rendering class or opaque destination hint. In OSTF 4.0, track.midi.busId is the Core logical MIDI routing reference; soundSource does not bind a physical device, plugin state or preset.",
  "properties": {
    "kind": {
      "enum": [
        "unassigned",
        "gm1",
        "externalMidi",
        "plugin",
        "hostManaged"
      ]
    },
    "identifier": {
      "type": "string",
      "minLength": 1,
      "description": "Opaque informational target identifier (for example a URI or plug-in identifier), not a physical MIDI-port binding or loading command."
    }
  },
  "required": [
    "kind"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "kind": {
            "enum": [
              "gm1",
              "unassigned"
            ]
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "not": {
          "required": [
            "identifier"
          ]
        }
      }
    }
  ]
}
```

<a id="schema-e6f4a4f748b6"></a>
## localizedNames

`#/$defs/localizedNames`

Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically.


### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "minProperties": 1,
  "propertyNames": {
    "type": "string",
    "pattern": "^(?:[A-Za-z]{2,3}|[A-Za-z]{5,8})(?:-[A-Za-z0-9]{2,8})*$"
  },
  "additionalProperties": {
    "type": "string",
    "minLength": 1
  },
  "description": "Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically."
}
```

<a id="schema-a7835568e37b"></a>
## drumKit

`#/$defs/drumKit`

Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/drumKits/0/id` |
| `name` | `{"type":"string"}` | Yes | Authored display name; never an identity or executable instruction. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/drumKits/0/name` |
| `localizedNames` | `{"$ref":"#/$defs/localizedNames"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/drumKits/0/localizedNames` |
| `soundSlotIds` | `{"type":"array","uniqueItems":true,"items":{"$ref":"#/$defs/id"}}` | Yes | Ordered, unique references to global soundSlots; may be empty. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/drumKits/0/soundSlotIds` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames"
    },
    "soundSlotIds": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "$ref": "#/$defs/id"
      },
      "description": "Ordered, unique references to global soundSlots; may be empty."
    }
  },
  "required": [
    "id",
    "name",
    "soundSlotIds"
  ],
  "additionalProperties": false
}
```

<a id="schema-5c862cc3e40d"></a>
## voicing

`#/$defs/voicing`

Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `pitches` | `{"type":"array","minItems":1,"items":{"$ref":"#/$defs/pitch"}}` | Yes | Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed. | [33-chord-voicing.ostf](../examples/33-chord-voicing.ostf)<br>`/harmony/chords/0/voicing/pitches` |
| `velocities` | `{"type":"array","minItems":1,"items":{"anyOf":[{"type":"integer","minimum":1,"maximum":127},{"type":"null"}]}}` | No / conditional | Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic. | [33-chord-voicing.ostf](../examples/33-chord-voicing.ostf)<br>`/harmony/chords/0/voicing/velocities` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.",
  "properties": {
    "pitches": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/pitch"
      },
      "description": "Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed."
    },
    "velocities": {
      "type": "array",
      "minItems": 1,
      "items": {
        "anyOf": [
          {
            "type": "integer",
            "minimum": 1,
            "maximum": 127
          },
          {
            "type": "null"
          }
        ]
      },
      "description": "Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic."
    }
  },
  "required": [
    "pitches"
  ]
}
```

<a id="schema-b59d15df5050"></a>
## contributor

`#/$defs/contributor`

One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/contributors/0/id` |
| `name` | `{"type":"string","minLength":1}` | Yes | Authored display name; never an identity or executable instruction. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/contributors/0/name` |
| `kind` | `{"enum":["person","organization","other"]}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/contributors/0/kind` |
| `localizedNames` | `{"$ref":"#/$defs/localizedNames"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/contributors/0/localizedNames` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "kind": {
      "enum": [
        "person",
        "organization",
        "other"
      ]
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames"
    }
  },
  "required": [
    "id",
    "name"
  ]
}
```

<a id="schema-d24adedd38df"></a>
## credit

`#/$defs/credit`

Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/credits/0/id` |
| `contributorId` | `{"$ref":"#/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/credits/0/contributorId` |
| `role` | `{"type":"string","pattern":"^[a-z][a-z0-9.-]*$"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/credits/0/role` |
| `label` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [46-contributors-credits.ostf](../examples/46-contributors-credits.ostf)<br>`/song/credits/0/label` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "contributorId": {
      "$ref": "#/$defs/id"
    },
    "role": {
      "type": "string",
      "pattern": "^[a-z][a-z0-9.-]*$"
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "contributorId",
    "role"
  ]
}
```

<a id="schema-73647ae405b9"></a>
## alternateTitle

`#/$defs/alternateTitle`

Stable-ID song title alternative; array position and title text do not identify it.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/alternateTitles/0/id` |
| `title` | `{"type":"string","minLength":1}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/alternateTitles/0/title` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Stable-ID song title alternative; array position and title text do not identify it.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "title": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "title"
  ]
}
```

<a id="schema-b88bcc6edf81"></a>
## languageMap32

`#/$defs/languageMap32`

Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank.


### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "minProperties": 1,
  "propertyNames": {
    "type": "string",
    "pattern": "^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*$"
  },
  "additionalProperties": {
    "type": "string"
  },
  "description": "Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank."
}
```

<a id="schema-354471cd4b0d"></a>
## localizationTarget

`#/$defs/localizationTarget`

Core target; song is ID-less, all others use global Core ID. No namespace/profile selector.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `kind` | `{"enum":["song","alternateTitle","contributor","credit","section","track","clip","soundSlot","drumKit","lyricDocument","resource","phraseTemplate","clipCandidate","clipChoiceGroup","roleDefinition","genre","mood","keyChange","scale","midiBus","lyricVoice"]}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/localization/entries/0/target/kind` |
| `id` | `{"$ref":"#/$defs/id"}` | No / conditional | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/localization/entries/1/target/id` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "kind": {
      "enum": [
        "song",
        "alternateTitle",
        "contributor",
        "credit",
        "section",
        "track",
        "clip",
        "soundSlot",
        "drumKit",
        "lyricDocument",
        "resource",
        "phraseTemplate",
        "clipCandidate",
        "clipChoiceGroup",
        "roleDefinition",
        "genre",
        "mood",
        "keyChange",
        "scale",
        "midiBus",
        "lyricVoice"
      ]
    },
    "id": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "kind"
  ],
  "allOf": [
    {
      "if": {
        "properties": {
          "kind": {
            "const": "song"
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "not": {
          "required": [
            "id"
          ]
        }
      },
      "else": {
        "required": [
          "id"
        ]
      }
    }
  ],
  "description": "Core target; song is ID-less, all others use global Core ID. No namespace/profile selector."
}
```

<a id="schema-1f6858ae510d"></a>
## localizationEntry

`#/$defs/localizationEntry`

Independent translations for one stable source field. Original source text remains authoritative as fallback.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `target` | `{"$ref":"#/$defs/localizationTarget"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/localization/entries/0/target` |
| `field` | `{"type":"string","minLength":1}` | Yes | Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/localization/entries/0/field` |
| `values` | `{"$ref":"#/$defs/languageMap32"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/localization/entries/0/values` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "target": {
      "$ref": "#/$defs/localizationTarget"
    },
    "field": {
      "type": "string",
      "minLength": 1,
      "description": "Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields."
    },
    "values": {
      "$ref": "#/$defs/languageMap32"
    }
  },
  "required": [
    "target",
    "field",
    "values"
  ],
  "description": "Independent translations for one stable source field. Original source text remains authoritative as fallback."
}
```

<a id="schema-70e3c989db70"></a>
## genre

`#/$defs/genre`

One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable song-local ID unique among all Core objects. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/genres/0/id` |
| `name` | `{"type":"string","minLength":1}` | Yes | Original Unicode genre label, never normalized or rewritten during import. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/genres/0/name` |
| `externalUri` | `{"type":"string","minLength":1,"format":"uri"}` | No / conditional | Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced. | [48-genres-moods.ostf](../examples/48-genres-moods.ostf)<br>`/song/genres/0/externalUri` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id",
      "description": "Stable song-local ID unique among all Core objects."
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "description": "Original Unicode genre label, never normalized or rewritten during import."
    },
    "externalUri": {
      "type": "string",
      "minLength": 1,
      "format": "uri",
      "description": "Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="schema-0771f9ca6fb2"></a>
## opaqueDocumentId

`#/$defs/opaqueDocumentId`

Stable URI or UUID-style identifier for a document lineage. Compared as exact Unicode text; never fetched.


### Exact structure, conditions and ranges

```json
{
  "type": "string",
  "minLength": 1,
  "description": "Stable URI or UUID-style identifier for a document lineage. Compared as exact Unicode text; never fetched."
}
```

<a id="schema-ed4d016a64c1"></a>
## revisionRef

`#/$defs/revisionRef`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `documentId` | `{"$ref":"#/$defs/opaqueDocumentId"}` | Yes | See the owning object semantics and exact constraints below. | [32-document-identity-revision.ostf](../examples/32-document-identity-revision.ostf)<br>`/document/parents/0/documentId` |
| `revisionId` | `{"$ref":"#/$defs/opaqueDocumentId"}` | Yes | See the owning object semantics and exact constraints below. | [32-document-identity-revision.ostf](../examples/32-document-identity-revision.ostf)<br>`/document/parents/0/revisionId` |
| `sha256` | `{"$ref":"#/$defs/sha256"}` | No / conditional | See the owning object semantics and exact constraints below. | [32-document-identity-revision.ostf](../examples/32-document-identity-revision.ostf)<br>`/document/parents/0/sha256` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "documentId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "revisionId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    }
  },
  "required": [
    "documentId",
    "revisionId"
  ],
  "additionalProperties": false
}
```

<a id="schema-d8bfbf4d7086"></a>
## software

`#/$defs/software`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `name` | `{"type":"string","minLength":1}` | Yes | Authored display name; never an identity or executable instruction. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/document/createdBy/name` |
| `version` | `{"type":"string","minLength":1}` | No / conditional | Version identifier for this owning object. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/document/createdBy/version` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```

<a id="schema-1808c384c579"></a>
## documentInfo

`#/$defs/documentInfo`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/opaqueDocumentId"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/document/id` |
| `revisionId` | `{"$ref":"#/$defs/opaqueDocumentId"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/document/revisionId` |
| `parents` | `{"type":"array","items":{"$ref":"#/$defs/revisionRef"},"uniqueItems":true}` | No / conditional | See the owning object semantics and exact constraints below. | [32-document-identity-revision.ostf](../examples/32-document-identity-revision.ostf)<br>`/document/parents` |
| `createdBy` | `{"$ref":"#/$defs/software"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/document/createdBy` |
| `modifiedBy` | `{"$ref":"#/$defs/software"}` | No / conditional | See the owning object semantics and exact constraints below. | [32-document-identity-revision.ostf](../examples/32-document-identity-revision.ostf)<br>`/document/modifiedBy` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "revisionId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "parents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/revisionRef"
      },
      "uniqueItems": true
    },
    "createdBy": {
      "$ref": "#/$defs/software"
    },
    "modifiedBy": {
      "$ref": "#/$defs/software"
    }
  },
  "required": [
    "id",
    "revisionId"
  ],
  "additionalProperties": false
}
```

<a id="schema-60e537075bf2"></a>
## key

`#/$defs/key`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `state` | `{"enum":["tonal","atonal","unspecified"]}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/key/state` |
| `tonic` | `{"$ref":"#/$defs/spelledPitchClass"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/key/tonic` |
| `mode` | `{"type":"string","minLength":1}` | No / conditional | Authored mode identifier. Canonical recognized values include major, minor, dorian, phrygian, lydian, mixolydian, locrian. Unknown values are preserved, never converted to major/minor. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/key/mode` |
| `label` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/key/label` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "state": {
      "enum": [
        "tonal",
        "atonal",
        "unspecified"
      ]
    },
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "mode": {
      "type": "string",
      "minLength": 1,
      "description": "Authored mode identifier. Canonical recognized values include major, minor, dorian, phrygian, lydian, mixolydian, locrian. Unknown values are preserved, never converted to major/minor."
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "state"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "state": {
            "const": "tonal"
          }
        },
        "required": [
          "state"
        ]
      },
      "then": {
        "required": [
          "tonic",
          "mode"
        ]
      },
      "else": {
        "not": {
          "anyOf": [
            {
              "required": [
                "tonic"
              ]
            },
            {
              "required": [
                "mode"
              ]
            }
          ]
        }
      }
    }
  ]
}
```

<a id="schema-be378667ebe6"></a>
## keyChange

`#/$defs/keyChange`

A change after tick zero; initial key is stored only at song.key. Change at tick 0 is forbidden to prevent dual authority.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [31-effective-key-scale.ostf](../examples/31-effective-key-scale.ostf)<br>`/timeline/keyChanges/0/id` |
| `at` | `{"$ref":"#/$defs/positive"}` | Yes | Time point in the owner-defined time domain. | [31-effective-key-scale.ostf](../examples/31-effective-key-scale.ostf)<br>`/timeline/keyChanges/0/at` |
| `key` | `{"$ref":"#/$defs/key"}` | Yes | See the owning object semantics and exact constraints below. | [31-effective-key-scale.ostf](../examples/31-effective-key-scale.ostf)<br>`/timeline/keyChanges/0/key` |
| `label` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [31-effective-key-scale.ostf](../examples/31-effective-key-scale.ostf)<br>`/timeline/keyChanges/0/label` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "at": {
      "$ref": "#/$defs/positive"
    },
    "key": {
      "$ref": "#/$defs/key"
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "at",
    "key"
  ],
  "additionalProperties": false,
  "description": "A change after tick zero; initial key is stored only at song.key. Change at tick 0 is forbidden to prevent dual authority."
}
```

<a id="schema-168efc29897b"></a>
## scaleDefinition

`#/$defs/scaleDefinition`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/scale/id` |
| `tonic` | `{"$ref":"#/$defs/spelledPitchClass"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/scale/tonic` |
| `intervals` | `{"type":"array","items":{"type":"integer","minimum":0,"maximum":11},"minItems":1,"maxItems":12,"uniqueItems":true,"contains":{"const":0}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/scale/intervals` |
| `label` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/scale/label` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 11
      },
      "minItems": 1,
      "maxItems": 12,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "tonic",
    "intervals"
  ],
  "additionalProperties": false
}
```

<a id="schema-68828d63bc6c"></a>
## scaleTarget

`#/$defs/scaleTarget`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `type` | `{"enum":["section","track","clip","chord","note"]}` | Yes | See the owning object semantics and exact constraints below. | [25-integrated-jazz-session.ostf](../examples/25-integrated-jazz-session.ostf)<br>`/harmony/scales/0/targets/0/type` |
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [25-integrated-jazz-session.ostf](../examples/25-integrated-jazz-session.ostf)<br>`/harmony/scales/0/targets/0/id` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "type": {
      "enum": [
        "section",
        "track",
        "clip",
        "chord",
        "note"
      ]
    },
    "id": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "type",
    "id"
  ],
  "additionalProperties": false
}
```

<a id="schema-bcdeab4b5e49"></a>
## mood

`#/$defs/mood`

Authored descriptive mood tag; not a generator preset or a probability.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable song-local ID unique among all Core objects. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/moods/0/id` |
| `name` | `{"type":"string","minLength":1}` | Yes | Original Unicode genre label, never normalized or rewritten during import. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/moods/0/name` |
| `externalUri` | `{"type":"string","minLength":1,"format":"uri"}` | No / conditional | Optional external vocabulary URI hint; never authoritative for the authored mood name and never auto-dereferenced. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/moods/0/externalUri` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "Authored descriptive mood tag; not a generator preset or a probability.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id",
      "description": "Stable song-local ID unique among all Core objects."
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "description": "Original Unicode genre label, never normalized or rewritten during import."
    },
    "externalUri": {
      "type": "string",
      "minLength": 1,
      "format": "uri",
      "description": "Optional external vocabulary URI hint; never authoritative for the authored mood name and never auto-dereferenced."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="schema-8cf8ca085d8a"></a>
## rightsStatement

`#/$defs/rightsStatement`

Authored rights statement only; no rights or permissions are inferred or granted by the format.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `notice` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/rights/notice` |
| `licenseUri` | `{"type":"string","minLength":1}` | No / conditional | See the owning object semantics and exact constraints below. | [47-rights-statement.ostf](../examples/47-rights-statement.ostf)<br>`/song/rights/licenseUri` |
| `rightsHolderIds` | `{"type":"array","items":{"$ref":"#/$defs/id"},"uniqueItems":true}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/song/rights/rightsHolderIds` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "notice": {
      "type": "string"
    },
    "licenseUri": {
      "type": "string",
      "minLength": 1
    },
    "rightsHolderIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Authored rights statement only; no rights or permissions are inferred or granted by the format.",
  "minProperties": 1
}
```

<a id="schema-afef10ac955e"></a>
## grooveIntent

`#/$defs/grooveIntent`

Descriptive generation intent only. Never re-apply to already stored notes. unitTicks is one unswung subdivision; two subdivisions form a pair.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `name` | `{"type":"string"}` | No / conditional | Authored display name; never an identity or executable instruction. | [27-generation-intent.ostf](../examples/27-generation-intent.ostf)<br>`/generation/processes/0/intent/groove/name` |
| `unitTicks` | `{"$ref":"#/$defs/positive"}` | No / conditional | See the owning object semantics and exact constraints below. | [27-generation-intent.ostf](../examples/27-generation-intent.ostf)<br>`/generation/processes/0/intent/groove/unitTicks` |
| `longWeight` | `{"type":"integer","minimum":1,"maximum":1000000}` | No / conditional | See the owning object semantics and exact constraints below. | [27-generation-intent.ostf](../examples/27-generation-intent.ostf)<br>`/generation/processes/0/intent/groove/longWeight` |
| `shortWeight` | `{"type":"integer","minimum":1,"maximum":1000000}` | No / conditional | See the owning object semantics and exact constraints below. | [27-generation-intent.ostf](../examples/27-generation-intent.ostf)<br>`/generation/processes/0/intent/groove/shortWeight` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "unitTicks": {
      "$ref": "#/$defs/positive"
    },
    "longWeight": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000000
    },
    "shortWeight": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000000
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Descriptive generation intent only. Never re-apply to already stored notes. unitTicks is one unswung subdivision; two subdivisions form a pair.",
  "minProperties": 1,
  "dependentRequired": {
    "unitTicks": [
      "longWeight",
      "shortWeight"
    ],
    "longWeight": [
      "unitTicks",
      "shortWeight"
    ],
    "shortWeight": [
      "unitTicks",
      "longWeight"
    ]
  }
}
```

<a id="schema-f5a441896302"></a>
## generationIntent

`#/$defs/generationIntent`

Portable description of intent, not a promise to reproduce an algorithm. Does not change song.genres or song.moods.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `genreNames` | `{"type":"array","items":{"type":"string","minLength":1}}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/processes/0/intent/genreNames` |
| `moodNames` | `{"type":"array","items":{"type":"string","minLength":1}}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/processes/0/intent/moodNames` |
| `groove` | `{"$ref":"#/$defs/grooveIntent"}` | No / conditional | See the owning object semantics and exact constraints below. | [27-generation-intent.ostf](../examples/27-generation-intent.ostf)<br>`/generation/processes/0/intent/groove` |
| `prompt` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/processes/0/intent/prompt` |
| `seed` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [27-generation-intent.ostf](../examples/27-generation-intent.ostf)<br>`/generation/processes/0/intent/seed` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "genreNames": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      }
    },
    "moodNames": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      }
    },
    "groove": {
      "$ref": "#/$defs/grooveIntent"
    },
    "prompt": {
      "type": "string"
    },
    "seed": {
      "type": "string"
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Portable description of intent, not a promise to reproduce an algorithm. Does not change song.genres or song.moods."
}
```

<a id="schema-b8bdd265b21e"></a>
## relativePhrases

`#/$defs/relativePhrases`

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `status` | `{"enum":["current","stale","unverified"]}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/relativePhrases/status` |
| `dependencies` | `{"$ref":"#/$defs/dependencies"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/relativePhrases/dependencies` |
| `assignments` | `{"type":"array","items":{"$ref":"#/$defs/relativeAssignment"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/relativePhrases/assignments` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "assignments": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/relativeAssignment"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "assignments"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="schema-d97c4e182ee5"></a>
## generation

`#/$defs/generation`

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `status` | `{"enum":["current","stale","unverified"]}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/status` |
| `dependencies` | `{"$ref":"#/$defs/dependencies"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/dependencies` |
| `processes` | `{"type":"array","items":{"$ref":"#/$defs/generationProcess"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/generation/processes` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "processes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/generationProcess"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "processes"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="schema-6a454ca6c7cd"></a>
## presentation

`#/$defs/presentation`

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `status` | `{"enum":["current","stale","unverified"]}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/presentation/status` |
| `dependencies` | `{"$ref":"#/$defs/dependencies"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/presentation/dependencies` |
| `roleDefinitions` | `{"type":"array","items":{"$ref":"#/$defs/roleDefinition"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/presentation/roleDefinitions` |
| `sectionRoleAssignments` | `{"type":"object","propertyNames":{"$ref":"#/$defs/id"},"additionalProperties":{"$ref":"#/$defs/id"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/presentation/sectionRoleAssignments` |
| `appearance` | `{"type":"object","properties":{"roleColors":{"$ref":"#/$defs/roleColorMap"},"customRoleColors":{"$ref":"#/$defs/customRoleColorMap"},"objectColors":{"type":"array","items":{"$ref":"#/$defs/objectColor"}}},"required":["roleColors","customRoleColors","objectColors"],"additionalProperties":false}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/presentation/appearance` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "roleDefinitions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/roleDefinition"
      }
    },
    "sectionRoleAssignments": {
      "type": "object",
      "propertyNames": {
        "$ref": "#/$defs/id"
      },
      "additionalProperties": {
        "$ref": "#/$defs/id"
      }
    },
    "appearance": {
      "type": "object",
      "properties": {
        "roleColors": {
          "$ref": "#/$defs/roleColorMap"
        },
        "customRoleColors": {
          "$ref": "#/$defs/customRoleColorMap"
        },
        "objectColors": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/objectColor"
          }
        }
      },
      "required": [
        "roleColors",
        "customRoleColors",
        "objectColors"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "status",
    "dependencies",
    "roleDefinitions",
    "sectionRoleAssignments",
    "appearance"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="schema-688ef61fcbb9"></a>
## phraseLibrary

`#/$defs/phraseLibrary`

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `status` | `{"enum":["current","stale","unverified"]}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/status` |
| `dependencies` | `{"$ref":"#/$defs/dependencies"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/dependencies` |
| `templates` | `{"type":"array","items":{"$ref":"#/$defs/phraseTemplate"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/templates` |
| `instances` | `{"type":"array","items":{"$ref":"#/$defs/phraseInstance"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/instances` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "templates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/phraseTemplate"
      }
    },
    "instances": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/phraseInstance"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "templates",
    "instances"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="schema-087f3401a094"></a>
## clipChoices

`#/$defs/clipChoices`

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `status` | `{"enum":["current","stale","unverified"]}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/clipChoices/status` |
| `dependencies` | `{"$ref":"#/$defs/dependencies"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/clipChoices/dependencies` |
| `groups` | `{"type":"array","items":{"$ref":"#/$defs/clipChoiceGroup"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/clipChoices/groups` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "groups": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/clipChoiceGroup"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "groups"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="schema-d217ff47f679"></a>
## localization

`#/$defs/localization`

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `status` | `{"enum":["current","stale","unverified"]}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/localization/status` |
| `dependencies` | `{"$ref":"#/$defs/dependencies"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/localization/dependencies` |
| `entries` | `{"type":"array","items":{"$ref":"#/$defs/localizationEntry"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/localization/entries` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "entries": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/localizationEntry"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "entries"
  ],
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="schema-4f2bcba3af0a"></a>
## corePhraseSourceNote

`#/$defs/corePhraseSourceNote`

Template-local source note for phrase materialization. It carries the same note-local 3.5 properties as concrete notes. It is not performed by itself; concrete track notes remain the saved playback events.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/templates/0/notes/0/id` |
| `start` | `{"$ref":"#/$defs/signed"}` | Yes | Start in the owner-defined time domain; see the manual. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/templates/0/notes/0/start` |
| `duration` | `{"$ref":"#/$defs/positive"}` | Yes | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/templates/0/notes/0/duration` |
| `pitch` | `{"$ref":"#/$defs/pitch"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/templates/0/notes/0/pitch` |
| `soundSlotId` | `{"$ref":"#/$defs/id"}` | No / conditional | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/templates/1/notes/0/soundSlotId` |
| `velocity` | `{"type":"integer","minimum":1,"maximum":127}` | No / conditional | Optional template note-on velocity, 1–127. Applied only by an explicit materialization/update according to instance.velocityMode; never a performed event by itself. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/templates/0/notes/0/velocity` |
| `enabled` | `{"type":"boolean","default":true}` | No / conditional | Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/templates/0/notes/0/enabled` |
| `releaseVelocity` | `{"type":"integer","minimum":0,"maximum":127}` | No / conditional | Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/templates/0/notes/0/releaseVelocity` |
| `probability` | `{"type":"number","minimum":0,"maximum":1,"default":1}` | No / conditional | Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/templates/0/notes/0/probability` |
| `velocityDeviation` | `{"type":"integer","minimum":-126,"maximum":126,"default":0}` | No / conditional | Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/templates/0/notes/0/velocityDeviation` |
| `pitchRole` | `{"enum":["musical","fixedTrigger"],"default":"musical"}` | No / conditional | Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/phraseLibrary/templates/0/notes/0/pitchRole` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive",
      "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
    },
    "pitch": {
      "$ref": "#/$defs/pitch"
    },
    "soundSlotId": {
      "$ref": "#/$defs/id",
      "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
    },
    "velocity": {
      "type": "integer",
      "minimum": 1,
      "maximum": 127,
      "description": "Optional template note-on velocity, 1–127. Applied only by an explicit materialization/update according to instance.velocityMode; never a performed event by itself."
    },
    "enabled": {
      "type": "boolean",
      "default": true,
      "description": "Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0."
    },
    "releaseVelocity": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127,
      "description": "Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default."
    },
    "probability": {
      "type": "number",
      "minimum": 0,
      "maximum": 1,
      "default": 1,
      "description": "Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange."
    },
    "velocityDeviation": {
      "type": "integer",
      "minimum": -126,
      "maximum": 126,
      "default": 0,
      "description": "Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0."
    },
    "pitchRole": {
      "enum": [
        "musical",
        "fixedTrigger"
      ],
      "default": "musical",
      "description": "Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes."
    }
  },
  "required": [
    "id",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "required": [
        "pitch"
      ],
      "not": {
        "required": [
          "soundSlotId"
        ]
      }
    },
    {
      "required": [
        "soundSlotId"
      ],
      "not": {
        "required": [
          "pitch"
        ]
      }
    }
  ],
  "description": "Template-local source note for phrase materialization. It carries the same note-local 3.5 properties as concrete notes. It is not performed by itself; concrete track notes remain the saved playback events.",
  "dependentRequired": {
    "velocityDeviation": [
      "velocity"
    ]
  },
  "allOf": [
    {
      "if": {
        "required": [
          "soundSlotId"
        ]
      },
      "then": {
        "not": {
          "required": [
            "pitchRole"
          ]
        }
      }
    }
  ]
}
```

<a id="schema-d0530816027d"></a>
## provenanceSource

`#/$defs/provenanceSource`

Historical source; hashes refer to exact source bytes, not the current document. No automatic retrieval.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `format` | `{"type":"string","minLength":1}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/provenance/records/0/sources/0/format` |
| `version` | `{"type":"string","minLength":1}` | No / conditional | Version identifier for this owning object. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/provenance/records/0/sources/0/version` |
| `sha256` | `{"$ref":"#/$defs/sha256"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/provenance/records/0/sources/0/sha256` |
| `uri` | `{"type":"string","minLength":1}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/provenance/records/0/sources/0/uri` |
| `documentId` | `{"$ref":"#/$defs/opaqueDocumentId"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/provenance/records/0/sources/0/documentId` |
| `revisionId` | `{"$ref":"#/$defs/opaqueDocumentId"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/provenance/records/0/sources/0/revisionId` |
| `resourceId` | `{"$ref":"#/$defs/id"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/provenance/records/0/sources/0/resourceId` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "format": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    },
    "uri": {
      "type": "string",
      "minLength": 1
    },
    "documentId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "revisionId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "resourceId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Historical source; hashes refer to exact source bytes, not the current document. No automatic retrieval.",
  "minProperties": 1,
  "dependentRequired": {
    "revisionId": [
      "documentId"
    ]
  }
}
```

<a id="schema-a903cfe5aef0"></a>
## provenanceRecord

`#/$defs/provenanceRecord`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/provenance/records/0/id` |
| `action` | `{"enum":["create","import","conversion","edit","transpose","merge","generation","other"]}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/provenance/records/0/action` |
| `description` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/provenance/records/0/description` |
| `tool` | `{"$ref":"#/$defs/software"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/provenance/records/0/tool` |
| `sources` | `{"type":"array","items":{"$ref":"#/$defs/provenanceSource"}}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/provenance/records/0/sources` |
| `semitones` | `{"type":"integer","minimum":-127,"maximum":127}` | No / conditional | See the owning object semantics and exact constraints below. | [35-provenance.ostf](../examples/35-provenance.ostf)<br>`/provenance/records/1/semitones` |
| `beforeKey` | `{"$ref":"#/$defs/key"}` | No / conditional | See the owning object semantics and exact constraints below. | [35-provenance.ostf](../examples/35-provenance.ostf)<br>`/provenance/records/1/beforeKey` |
| `afterKey` | `{"$ref":"#/$defs/key"}` | No / conditional | See the owning object semantics and exact constraints below. | [35-provenance.ostf](../examples/35-provenance.ostf)<br>`/provenance/records/1/afterKey` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "action": {
      "enum": [
        "create",
        "import",
        "conversion",
        "edit",
        "transpose",
        "merge",
        "generation",
        "other"
      ]
    },
    "description": {
      "type": "string"
    },
    "tool": {
      "$ref": "#/$defs/software"
    },
    "sources": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/provenanceSource"
      }
    },
    "semitones": {
      "type": "integer",
      "minimum": -127,
      "maximum": 127
    },
    "beforeKey": {
      "$ref": "#/$defs/key"
    },
    "afterKey": {
      "$ref": "#/$defs/key"
    }
  },
  "required": [
    "id",
    "action"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "not": {
          "properties": {
            "action": {
              "const": "transpose"
            }
          },
          "required": [
            "action"
          ]
        }
      },
      "then": {
        "not": {
          "required": [
            "semitones"
          ]
        }
      }
    }
  ]
}
```

<a id="schema-ba37b5c7146e"></a>
## provenance

`#/$defs/provenance`

Non-executable historical assertions; not composer credits and not a substitute for current metadata. Does not prove authorship or operation correctness.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `records` | `{"type":"array","items":{"$ref":"#/$defs/provenanceRecord"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/provenance/records` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "records": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/provenanceRecord"
      }
    }
  },
  "required": [
    "records"
  ],
  "additionalProperties": false,
  "description": "Non-executable historical assertions; not composer credits and not a substitute for current metadata. Does not prove authorship or operation correctness."
}
```

<a id="schema-d9e2f6960cc4"></a>
## midiChannel

`#/$defs/midiChannel`

Human-readable MIDI 1.0 channel number 1..16. Wire status-nibble channel = value - 1.


### Exact structure, conditions and ranges

```json
{
  "type": "integer",
  "minimum": 1,
  "maximum": 16,
  "description": "Human-readable MIDI 1.0 channel number 1..16. Wire status-nibble channel = value - 1."
}
```

<a id="schema-243e98d145a8"></a>
## midiBus

`#/$defs/midiBus`

Document-local logical MIDI destination. Each bus has its own MIDI channel namespace. It is not a physical OS/USB/DAW port binding.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/midi/buses/0/id` |
| `name` | `{"type":"string"}` | Yes | Authored display name; never an identity or executable instruction. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/midi/buses/0/name` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "Document-local logical MIDI destination. Each bus has its own MIDI channel namespace. It is not a physical OS/USB/DAW port binding.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="schema-e63c7a3ec0d1"></a>
## midi

`#/$defs/midi`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `buses` | `{"type":"array","items":{"$ref":"#/$defs/midiBus"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/midi/buses` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "buses": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/midiBus"
      }
    }
  },
  "required": [
    "buses"
  ],
  "additionalProperties": false
}
```

<a id="schema-4f2c12c54b18"></a>
## mpeSettings

`#/$defs/mpeSettings`

Semantic MPE zone declaration. Lower-zone master is channel 1 and upper-zone master is channel 16; member channels are derived contiguously from memberChannelCount.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `zone` | `{"enum":["lower","upper"]}` | Yes | See the owning object semantics and exact constraints below. | [23-mpe-per-note-expression.ostf](../examples/23-mpe-per-note-expression.ostf)<br>`/tracks/0/midi/mpe/zone` |
| `memberChannelCount` | `{"type":"integer","minimum":1,"maximum":15}` | Yes | See the owning object semantics and exact constraints below. | [23-mpe-per-note-expression.ostf](../examples/23-mpe-per-note-expression.ostf)<br>`/tracks/0/midi/mpe/memberChannelCount` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "Semantic MPE zone declaration. Lower-zone master is channel 1 and upper-zone master is channel 16; member channels are derived contiguously from memberChannelCount.",
  "properties": {
    "zone": {
      "enum": [
        "lower",
        "upper"
      ]
    },
    "memberChannelCount": {
      "type": "integer",
      "minimum": 1,
      "maximum": 15
    }
  },
  "required": [
    "zone",
    "memberChannelCount"
  ],
  "additionalProperties": false
}
```

<a id="schema-a037cff7c14c"></a>
## trackMidi

`#/$defs/trackMidi`

Optional MIDI channel/routing interpretation for a track. busId is a logical OSTF bus, never a physical MIDI port.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `busId` | `{"$ref":"#/$defs/id"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/midi/busId` |
| `mode` | `{"enum":["singleChannel","multiChannel","mpe"]}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/midi/mode` |
| `channel` | `{"$ref":"#/$defs/midiChannel"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/midi/channel` |
| `mpe` | `{"$ref":"#/$defs/mpeSettings"}` | No / conditional | See the owning object semantics and exact constraints below. | [23-mpe-per-note-expression.ostf](../examples/23-mpe-per-note-expression.ostf)<br>`/tracks/0/midi/mpe` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "Optional MIDI channel/routing interpretation for a track. busId is a logical OSTF bus, never a physical MIDI port.",
  "properties": {
    "busId": {
      "$ref": "#/$defs/id"
    },
    "mode": {
      "enum": [
        "singleChannel",
        "multiChannel",
        "mpe"
      ]
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "mpe": {
      "$ref": "#/$defs/mpeSettings"
    }
  },
  "required": [
    "mode"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "mode": {
            "const": "singleChannel"
          }
        },
        "required": [
          "mode"
        ]
      },
      "then": {
        "required": [
          "channel"
        ],
        "not": {
          "required": [
            "mpe"
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "mode": {
            "const": "multiChannel"
          }
        },
        "required": [
          "mode"
        ]
      },
      "then": {
        "not": {
          "anyOf": [
            {
              "required": [
                "channel"
              ]
            },
            {
              "required": [
                "mpe"
              ]
            }
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "mode": {
            "const": "mpe"
          }
        },
        "required": [
          "mode"
        ]
      },
      "then": {
        "required": [
          "mpe"
        ],
        "not": {
          "required": [
            "channel"
          ]
        }
      }
    }
  ]
}
```

<a id="schema-6f54f21ac661"></a>
## controlChangeEvent

`#/$defs/controlChangeEvent`

MIDI 1.0 Control Change. Controllers 120..127 use channelMode instead.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [06-instrument-midi-unchanged.ostf](../examples/06-instrument-midi-unchanged.ostf)<br>`/tracks/0/clips/0/midiEvents/0/id` |
| `start` | `{"$ref":"#/$defs/signed"}` | Yes | Start in the owner-defined time domain; see the manual. | [06-instrument-midi-unchanged.ostf](../examples/06-instrument-midi-unchanged.ostf)<br>`/tracks/0/clips/0/midiEvents/0/start` |
| `order` | `{"$ref":"#/$defs/signed","default":1}` | No / conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. | [23-mpe-per-note-expression.ostf](../examples/23-mpe-per-note-expression.ostf)<br>`/tracks/0/clips/0/midiEvents/2/order` |
| `channel` | `{"$ref":"#/$defs/midiChannel"}` | No / conditional | See the owning object semantics and exact constraints below. | [06-instrument-midi-unchanged.ostf](../examples/06-instrument-midi-unchanged.ostf)<br>`/tracks/0/clips/0/midiEvents/0/channel` |
| `type` | `{"const":"controlChange"}` | Yes | See the owning object semantics and exact constraints below. | [06-instrument-midi-unchanged.ostf](../examples/06-instrument-midi-unchanged.ostf)<br>`/tracks/0/clips/0/midiEvents/0/type` |
| `targetNoteId` | `{"$ref":"#/$defs/id"}` | No / conditional | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. | [23-mpe-per-note-expression.ostf](../examples/23-mpe-per-note-expression.ostf)<br>`/tracks/0/clips/0/midiEvents/2/targetNoteId` |
| `controller` | `{"type":"integer","minimum":0,"maximum":119}` | Yes | See the owning object semantics and exact constraints below. | [06-instrument-midi-unchanged.ostf](../examples/06-instrument-midi-unchanged.ostf)<br>`/tracks/0/clips/0/midiEvents/0/controller` |
| `value` | `{"type":"integer","minimum":0,"maximum":127}` | Yes | Numeric value with the units and constraints specified by the owner. | [06-instrument-midi-unchanged.ostf](../examples/06-instrument-midi-unchanged.ostf)<br>`/tracks/0/clips/0/midiEvents/0/value` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "MIDI 1.0 Control Change. Controllers 120..127 use channelMode instead.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "controlChange"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
    },
    "controller": {
      "type": "integer",
      "minimum": 0,
      "maximum": 119
    },
    "value": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "controller",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="schema-6b19d423c196"></a>
## channelModeEvent

`#/$defs/channelModeEvent`

MIDI 1.0 Channel Mode message represented separately from ordinary Control Change.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [28-channel-mode.ostf](../examples/28-channel-mode.ostf)<br>`/tracks/0/clips/0/midiEvents/0/id` |
| `start` | `{"$ref":"#/$defs/signed"}` | Yes | Start in the owner-defined time domain; see the manual. | [28-channel-mode.ostf](../examples/28-channel-mode.ostf)<br>`/tracks/0/clips/0/midiEvents/0/start` |
| `order` | `{"$ref":"#/$defs/signed","default":1}` | No / conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. | [28-channel-mode.ostf](../examples/28-channel-mode.ostf)<br>`/tracks/0/clips/0/midiEvents/0/order` |
| `channel` | `{"$ref":"#/$defs/midiChannel"}` | No / conditional | See the owning object semantics and exact constraints below. | [28-channel-mode.ostf](../examples/28-channel-mode.ostf)<br>`/tracks/0/clips/0/midiEvents/0/channel` |
| `type` | `{"const":"channelMode"}` | Yes | See the owning object semantics and exact constraints below. | [28-channel-mode.ostf](../examples/28-channel-mode.ostf)<br>`/tracks/0/clips/0/midiEvents/0/type` |
| `controller` | `{"type":"integer","minimum":120,"maximum":127}` | Yes | See the owning object semantics and exact constraints below. | [28-channel-mode.ostf](../examples/28-channel-mode.ostf)<br>`/tracks/0/clips/0/midiEvents/0/controller` |
| `value` | `{"type":"integer","minimum":0,"maximum":127}` | Yes | Numeric value with the units and constraints specified by the owner. | [28-channel-mode.ostf](../examples/28-channel-mode.ostf)<br>`/tracks/0/clips/0/midiEvents/0/value` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "MIDI 1.0 Channel Mode message represented separately from ordinary Control Change.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "channelMode"
    },
    "controller": {
      "type": "integer",
      "minimum": 120,
      "maximum": 127
    },
    "value": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "controller",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="schema-0db111a5d987"></a>
## programChangeEvent

`#/$defs/programChangeEvent`

MIDI 1.0 Program Change using the wire data value 0..127. UI may display 1..128.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [30-bank-select-program-change.ostf](../examples/30-bank-select-program-change.ostf)<br>`/tracks/0/clips/0/midiEvents/2/id` |
| `start` | `{"$ref":"#/$defs/signed"}` | Yes | Start in the owner-defined time domain; see the manual. | [30-bank-select-program-change.ostf](../examples/30-bank-select-program-change.ostf)<br>`/tracks/0/clips/0/midiEvents/2/start` |
| `order` | `{"$ref":"#/$defs/signed","default":1}` | No / conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. | [30-bank-select-program-change.ostf](../examples/30-bank-select-program-change.ostf)<br>`/tracks/0/clips/0/midiEvents/2/order` |
| `channel` | `{"$ref":"#/$defs/midiChannel"}` | No / conditional | See the owning object semantics and exact constraints below. | [30-bank-select-program-change.ostf](../examples/30-bank-select-program-change.ostf)<br>`/tracks/0/clips/0/midiEvents/2/channel` |
| `type` | `{"const":"programChange"}` | Yes | See the owning object semantics and exact constraints below. | [30-bank-select-program-change.ostf](../examples/30-bank-select-program-change.ostf)<br>`/tracks/0/clips/0/midiEvents/2/type` |
| `program` | `{"type":"integer","minimum":0,"maximum":127}` | Yes | See the owning object semantics and exact constraints below. | [30-bank-select-program-change.ostf](../examples/30-bank-select-program-change.ostf)<br>`/tracks/0/clips/0/midiEvents/2/program` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "MIDI 1.0 Program Change using the wire data value 0..127. UI may display 1..128.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "programChange"
    },
    "program": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "program"
  ],
  "additionalProperties": false
}
```

<a id="schema-7df32ddccc21"></a>
## pitchBendEvent

`#/$defs/pitchBendEvent`

MIDI 1.0 14-bit Pitch Bend Change. Bend range is receiver state/RPN data, not encoded in value14.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [06-instrument-midi-unchanged.ostf](../examples/06-instrument-midi-unchanged.ostf)<br>`/tracks/0/clips/0/midiEvents/1/id` |
| `start` | `{"$ref":"#/$defs/signed"}` | Yes | Start in the owner-defined time domain; see the manual. | [06-instrument-midi-unchanged.ostf](../examples/06-instrument-midi-unchanged.ostf)<br>`/tracks/0/clips/0/midiEvents/1/start` |
| `order` | `{"$ref":"#/$defs/signed","default":1}` | No / conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. | [23-mpe-per-note-expression.ostf](../examples/23-mpe-per-note-expression.ostf)<br>`/tracks/0/clips/0/midiEvents/0/order` |
| `channel` | `{"$ref":"#/$defs/midiChannel"}` | No / conditional | See the owning object semantics and exact constraints below. | [06-instrument-midi-unchanged.ostf](../examples/06-instrument-midi-unchanged.ostf)<br>`/tracks/0/clips/0/midiEvents/1/channel` |
| `type` | `{"const":"pitchBend"}` | Yes | See the owning object semantics and exact constraints below. | [06-instrument-midi-unchanged.ostf](../examples/06-instrument-midi-unchanged.ostf)<br>`/tracks/0/clips/0/midiEvents/1/type` |
| `targetNoteId` | `{"$ref":"#/$defs/id"}` | No / conditional | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. | [23-mpe-per-note-expression.ostf](../examples/23-mpe-per-note-expression.ostf)<br>`/tracks/0/clips/0/midiEvents/0/targetNoteId` |
| `value14` | `{"type":"integer","minimum":0,"maximum":16383}` | Yes | Raw MIDI 1.0 14-bit pitch-bend value; center is 8192. | [06-instrument-midi-unchanged.ostf](../examples/06-instrument-midi-unchanged.ostf)<br>`/tracks/0/clips/0/midiEvents/1/value14` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "MIDI 1.0 14-bit Pitch Bend Change. Bend range is receiver state/RPN data, not encoded in value14.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "pitchBend"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
    },
    "value14": {
      "type": "integer",
      "minimum": 0,
      "maximum": 16383,
      "description": "Raw MIDI 1.0 14-bit pitch-bend value; center is 8192."
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "value14"
  ],
  "additionalProperties": false
}
```

<a id="schema-272c93d6fd9f"></a>
## channelPressureEvent

`#/$defs/channelPressureEvent`

MIDI 1.0 Channel Pressure (channel aftertouch).

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [23-mpe-per-note-expression.ostf](../examples/23-mpe-per-note-expression.ostf)<br>`/tracks/0/clips/0/midiEvents/1/id` |
| `start` | `{"$ref":"#/$defs/signed"}` | Yes | Start in the owner-defined time domain; see the manual. | [23-mpe-per-note-expression.ostf](../examples/23-mpe-per-note-expression.ostf)<br>`/tracks/0/clips/0/midiEvents/1/start` |
| `order` | `{"$ref":"#/$defs/signed","default":1}` | No / conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. | [23-mpe-per-note-expression.ostf](../examples/23-mpe-per-note-expression.ostf)<br>`/tracks/0/clips/0/midiEvents/1/order` |
| `channel` | `{"$ref":"#/$defs/midiChannel"}` | No / conditional | See the owning object semantics and exact constraints below. | [23-mpe-per-note-expression.ostf](../examples/23-mpe-per-note-expression.ostf)<br>`/tracks/0/clips/0/midiEvents/1/channel` |
| `type` | `{"const":"channelPressure"}` | Yes | See the owning object semantics and exact constraints below. | [23-mpe-per-note-expression.ostf](../examples/23-mpe-per-note-expression.ostf)<br>`/tracks/0/clips/0/midiEvents/1/type` |
| `targetNoteId` | `{"$ref":"#/$defs/id"}` | No / conditional | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. | [23-mpe-per-note-expression.ostf](../examples/23-mpe-per-note-expression.ostf)<br>`/tracks/0/clips/0/midiEvents/1/targetNoteId` |
| `value` | `{"type":"integer","minimum":0,"maximum":127}` | Yes | Numeric value with the units and constraints specified by the owner. | [23-mpe-per-note-expression.ostf](../examples/23-mpe-per-note-expression.ostf)<br>`/tracks/0/clips/0/midiEvents/1/value` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "MIDI 1.0 Channel Pressure (channel aftertouch).",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "channelPressure"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
    },
    "value": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="schema-ba1b5c1a9ff9"></a>
## polyPressureEvent

`#/$defs/polyPressureEvent`

MIDI 1.0 Polyphonic Key Pressure (poly aftertouch).

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [26-poly-pressure.ostf](../examples/26-poly-pressure.ostf)<br>`/tracks/0/clips/0/midiEvents/0/id` |
| `start` | `{"$ref":"#/$defs/signed"}` | Yes | Start in the owner-defined time domain; see the manual. | [26-poly-pressure.ostf](../examples/26-poly-pressure.ostf)<br>`/tracks/0/clips/0/midiEvents/0/start` |
| `order` | `{"$ref":"#/$defs/signed","default":1}` | No / conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. | [26-poly-pressure.ostf](../examples/26-poly-pressure.ostf)<br>`/tracks/0/clips/0/midiEvents/0/order` |
| `channel` | `{"$ref":"#/$defs/midiChannel"}` | No / conditional | See the owning object semantics and exact constraints below. | [26-poly-pressure.ostf](../examples/26-poly-pressure.ostf)<br>`/tracks/0/clips/0/midiEvents/0/channel` |
| `type` | `{"const":"polyPressure"}` | Yes | See the owning object semantics and exact constraints below. | [26-poly-pressure.ostf](../examples/26-poly-pressure.ostf)<br>`/tracks/0/clips/0/midiEvents/0/type` |
| `targetNoteId` | `{"$ref":"#/$defs/id"}` | No / conditional | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. | [26-poly-pressure.ostf](../examples/26-poly-pressure.ostf)<br>`/tracks/0/clips/0/midiEvents/0/targetNoteId` |
| `pitch` | `{"$ref":"#/$defs/pitch"}` | Yes | See the owning object semantics and exact constraints below. | [26-poly-pressure.ostf](../examples/26-poly-pressure.ostf)<br>`/tracks/0/clips/0/midiEvents/0/pitch` |
| `value` | `{"type":"integer","minimum":0,"maximum":127}` | Yes | Numeric value with the units and constraints specified by the owner. | [26-poly-pressure.ostf](../examples/26-poly-pressure.ostf)<br>`/tracks/0/clips/0/midiEvents/0/value` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "MIDI 1.0 Polyphonic Key Pressure (poly aftertouch).",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "polyPressure"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
    },
    "pitch": {
      "$ref": "#/$defs/pitch"
    },
    "value": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "pitch",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="schema-1c0cd2d1203f"></a>
## midiEvent

`#/$defs/midiEvent`


### Exact structure, conditions and ranges

```json
{
  "oneOf": [
    {
      "$ref": "#/$defs/controlChangeEvent"
    },
    {
      "$ref": "#/$defs/channelModeEvent"
    },
    {
      "$ref": "#/$defs/programChangeEvent"
    },
    {
      "$ref": "#/$defs/pitchBendEvent"
    },
    {
      "$ref": "#/$defs/channelPressureEvent"
    },
    {
      "$ref": "#/$defs/polyPressureEvent"
    }
  ]
}
```

<a id="schema-d187205a3e8b"></a>
## lyricVoice

`#/$defs/lyricVoice`

Explicit relationship between a vocal/melody track and a lyric document. Several voices may reference the same lyric document without duplicating text.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/voices/0/id` |
| `name` | `{"type":"string"}` | No / conditional | Authored display name; never an identity or executable instruction. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/voices/0/name` |
| `role` | `{"type":"string","minLength":1}` | No / conditional | Open authored role. Recommended values include lead, harmony, backing, unison, double, counter, adlib, response. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/voices/0/role` |
| `trackId` | `{"$ref":"#/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/voices/0/trackId` |
| `documentId` | `{"$ref":"#/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/lyrics/voices/0/documentId` |
| `vocalProfile` | `{"$ref":"#/$defs/vocalProfile"}` | No / conditional | Optional engine-neutral vocal defaults; absence does not mean an instrument voice. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/lyrics/voices/0/vocalProfile` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "Explicit relationship between a vocal/melody track and a lyric document. Several voices may reference the same lyric document without duplicating text.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string",
      "minLength": 1,
      "description": "Open authored role. Recommended values include lead, harmony, backing, unison, double, counter, adlib, response."
    },
    "trackId": {
      "$ref": "#/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "vocalProfile": {
      "$ref": "#/$defs/vocalProfile",
      "description": "Optional engine-neutral vocal defaults; absence does not mean an instrument voice."
    }
  },
  "required": [
    "id",
    "trackId",
    "documentId"
  ],
  "additionalProperties": false
}
```

<a id="schema-91234b29badc"></a>
## playablePitchRange

`#/$defs/playablePitchRange`

Authored playable pitch capability in the same 0..127 pitch-number domain as melodic notes. Semantic rule: lowPitch <= highPitch.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `lowPitch` | `{"$ref":"#/$defs/pitch"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/instrument/playablePitchRange/lowPitch` |
| `highPitch` | `{"$ref":"#/$defs/pitch"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/instrument/playablePitchRange/highPitch` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "lowPitch": {
      "$ref": "#/$defs/pitch"
    },
    "highPitch": {
      "$ref": "#/$defs/pitch"
    }
  },
  "required": [
    "lowPitch",
    "highPitch"
  ],
  "additionalProperties": false,
  "description": "Authored playable pitch capability in the same 0..127 pitch-number domain as melodic notes. Semantic rule: lowPitch <= highPitch."
}
```

<a id="schema-968a8b410378"></a>
## directionPitchCollection

`#/$defs/directionPitchCollection`

Direction-local pitch-class collection relative to tonic. It is not a harmonic scale-context object and has no independent timeline identity.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `tonic` | `{"$ref":"#/$defs/spelledPitchClass"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/1/parameters/pitchSource/scale/tonic` |
| `intervals` | `{"type":"array","items":{"type":"integer","minimum":0,"maximum":11},"minItems":1,"maxItems":12,"uniqueItems":true,"contains":{"const":0}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/1/parameters/pitchSource/scale/intervals` |
| `label` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/1/parameters/pitchSource/scale/label` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 11
      },
      "minItems": 1,
      "maxItems": 12,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "tonic",
    "intervals"
  ],
  "additionalProperties": false,
  "description": "Direction-local pitch-class collection relative to tonic. It is not a harmonic scale-context object and has no independent timeline identity."
}
```

<a id="schema-6ffe903f72ae"></a>
## directionPitchSource

`#/$defs/directionPitchSource`

Source of pitch vocabulary for an improvisation Direction.


### Exact structure, conditions and ranges

```json
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "type": {
          "const": "effectiveKeyScale"
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "const": "songScale"
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "const": "harmonyScales"
        },
        "scaleIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "minItems": 1,
          "uniqueItems": true
        }
      },
      "required": [
        "type",
        "scaleIds"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "const": "explicitScale"
        },
        "scale": {
          "$ref": "#/$defs/directionPitchCollection"
        }
      },
      "required": [
        "type",
        "scale"
      ],
      "additionalProperties": false
    }
  ],
  "description": "Source of pitch vocabulary for an improvisation Direction."
}
```

<a id="schema-ee9de698d509"></a>
## improvisationDirectionParameters

`#/$defs/improvisationDirectionParameters`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `pitchSource` | `{"$ref":"#/$defs/directionPitchSource"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/1/parameters/pitchSource` |
| `adherence` | `{"enum":["strict","preferred"]}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/1/parameters/adherence` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "pitchSource": {
      "$ref": "#/$defs/directionPitchSource"
    },
    "adherence": {
      "enum": [
        "strict",
        "preferred"
      ]
    }
  },
  "required": [
    "pitchSource",
    "adherence"
  ],
  "additionalProperties": false
}
```

<a id="schema-2d9985e68214"></a>
## playingRoleDirectionParameters

`#/$defs/playingRoleDirectionParameters`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `role` | `{"type":"string","minLength":1}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/0/parameters/role` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "role": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "role"
  ],
  "additionalProperties": false
}
```

<a id="schema-10257f9b295f"></a>
## pitchRangeDirectionParameters

`#/$defs/pitchRangeDirectionParameters`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `lowPitch` | `{"$ref":"#/$defs/pitch"}` | Yes | See the owning object semantics and exact constraints below. | [24-pitch-range-high-register.ostf](../examples/24-pitch-range-high-register.ostf)<br>`/tracks/0/directions/0/parameters/lowPitch` |
| `highPitch` | `{"$ref":"#/$defs/pitch"}` | Yes | See the owning object semantics and exact constraints below. | [24-pitch-range-high-register.ostf](../examples/24-pitch-range-high-register.ostf)<br>`/tracks/0/directions/0/parameters/highPitch` |
| `constraint` | `{"enum":["strict","preferred"]}` | Yes | See the owning object semantics and exact constraints below. | [24-pitch-range-high-register.ostf](../examples/24-pitch-range-high-register.ostf)<br>`/tracks/0/directions/0/parameters/constraint` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "lowPitch": {
      "$ref": "#/$defs/pitch"
    },
    "highPitch": {
      "$ref": "#/$defs/pitch"
    },
    "constraint": {
      "enum": [
        "strict",
        "preferred"
      ]
    }
  },
  "required": [
    "lowPitch",
    "highPitch",
    "constraint"
  ],
  "additionalProperties": false
}
```

<a id="schema-02bfecf4e43a"></a>
## vendorDirectionParameters

`#/$defs/vendorDirectionParameters`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `namespace` | `{"type":"string","minLength":3,"pattern":"^[a-z][a-z0-9-]*(?:\\.[a-z][a-z0-9-]*){2,}$","not":{"pattern":"^org\\.ostf(?:\\.\|$)"}}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/2/parameters/namespace` |
| `name` | `{"type":"string","minLength":1}` | Yes | Authored display name; never an identity or executable instruction. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/2/parameters/name` |
| `version` | `{"type":"string","minLength":1}` | No / conditional | Version identifier for this owning object. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/2/parameters/version` |
| `data` | `{"type":"object"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/2/parameters/data` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "namespace": {
      "type": "string",
      "minLength": 3,
      "pattern": "^[a-z][a-z0-9-]*(?:\\.[a-z][a-z0-9-]*){2,}$",
      "not": {
        "pattern": "^org\\.ostf(?:\\.|$)"
      }
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    },
    "data": {
      "type": "object"
    }
  },
  "required": [
    "namespace",
    "name",
    "data"
  ],
  "additionalProperties": false
}
```

<a id="schema-033764cd9dd6"></a>
## improvisationDirection

`#/$defs/improvisationDirection`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/1/id` |
| `start` | `{"$ref":"#/$defs/nonnegative"}` | Yes | Start in the owner-defined time domain; see the manual. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/1/start` |
| `duration` | `{"$ref":"#/$defs/positive"}` | Yes | Positive duration in ticks. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/1/duration` |
| `label` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/1/label` |
| `instruction` | `{"type":"string"}` | No / conditional | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/1/instruction` |
| `type` | `{"const":"improvisation"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/1/type` |
| `parameters` | `{"$ref":"#/$defs/improvisationDirectionParameters"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/1/parameters` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
    },
    "type": {
      "const": "improvisation"
    },
    "parameters": {
      "$ref": "#/$defs/improvisationDirectionParameters"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```

<a id="schema-becf3213fa2e"></a>
## playingRoleDirection

`#/$defs/playingRoleDirection`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/0/id` |
| `start` | `{"$ref":"#/$defs/nonnegative"}` | Yes | Start in the owner-defined time domain; see the manual. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/0/start` |
| `duration` | `{"$ref":"#/$defs/positive"}` | Yes | Positive duration in ticks. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/0/duration` |
| `label` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/0/label` |
| `instruction` | `{"type":"string"}` | No / conditional | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/0/instruction` |
| `type` | `{"const":"playingRole"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/0/type` |
| `parameters` | `{"$ref":"#/$defs/playingRoleDirectionParameters"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/0/parameters` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
    },
    "type": {
      "const": "playingRole"
    },
    "parameters": {
      "$ref": "#/$defs/playingRoleDirectionParameters"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```

<a id="schema-9b1fe7d5388c"></a>
## pitchRangeDirection

`#/$defs/pitchRangeDirection`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [24-pitch-range-high-register.ostf](../examples/24-pitch-range-high-register.ostf)<br>`/tracks/0/directions/0/id` |
| `start` | `{"$ref":"#/$defs/nonnegative"}` | Yes | Start in the owner-defined time domain; see the manual. | [24-pitch-range-high-register.ostf](../examples/24-pitch-range-high-register.ostf)<br>`/tracks/0/directions/0/start` |
| `duration` | `{"$ref":"#/$defs/positive"}` | Yes | Positive duration in ticks. | [24-pitch-range-high-register.ostf](../examples/24-pitch-range-high-register.ostf)<br>`/tracks/0/directions/0/duration` |
| `label` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [24-pitch-range-high-register.ostf](../examples/24-pitch-range-high-register.ostf)<br>`/tracks/0/directions/0/label` |
| `instruction` | `{"type":"string"}` | No / conditional | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. | [24-pitch-range-high-register.ostf](../examples/24-pitch-range-high-register.ostf)<br>`/tracks/0/directions/0/instruction` |
| `type` | `{"const":"pitchRange"}` | Yes | See the owning object semantics and exact constraints below. | [24-pitch-range-high-register.ostf](../examples/24-pitch-range-high-register.ostf)<br>`/tracks/0/directions/0/type` |
| `parameters` | `{"$ref":"#/$defs/pitchRangeDirectionParameters"}` | Yes | See the owning object semantics and exact constraints below. | [24-pitch-range-high-register.ostf](../examples/24-pitch-range-high-register.ostf)<br>`/tracks/0/directions/0/parameters` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
    },
    "type": {
      "const": "pitchRange"
    },
    "parameters": {
      "$ref": "#/$defs/pitchRangeDirectionParameters"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```

<a id="schema-006c4953cb58"></a>
## vendorRangeDirection

`#/$defs/vendorRangeDirection`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [29-vendor-range-direction.ostf](../examples/29-vendor-range-direction.ostf)<br>`/tracks/0/directions/0/id` |
| `start` | `{"$ref":"#/$defs/nonnegative"}` | Yes | Start in the owner-defined time domain; see the manual. | [29-vendor-range-direction.ostf](../examples/29-vendor-range-direction.ostf)<br>`/tracks/0/directions/0/start` |
| `duration` | `{"$ref":"#/$defs/positive"}` | Yes | Positive duration in ticks. | [29-vendor-range-direction.ostf](../examples/29-vendor-range-direction.ostf)<br>`/tracks/0/directions/0/duration` |
| `label` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [29-vendor-range-direction.ostf](../examples/29-vendor-range-direction.ostf)<br>`/tracks/0/directions/0/label` |
| `instruction` | `{"type":"string"}` | No / conditional | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. | [29-vendor-range-direction.ostf](../examples/29-vendor-range-direction.ostf)<br>`/tracks/0/directions/0/instruction` |
| `type` | `{"const":"vendor"}` | Yes | See the owning object semantics and exact constraints below. | [29-vendor-range-direction.ostf](../examples/29-vendor-range-direction.ostf)<br>`/tracks/0/directions/0/type` |
| `parameters` | `{"$ref":"#/$defs/vendorDirectionParameters"}` | Yes | See the owning object semantics and exact constraints below. | [29-vendor-range-direction.ostf](../examples/29-vendor-range-direction.ostf)<br>`/tracks/0/directions/0/parameters` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
    },
    "type": {
      "const": "vendor"
    },
    "parameters": {
      "$ref": "#/$defs/vendorDirectionParameters"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```

<a id="schema-edc04f37e799"></a>
## vendorPointDirection

`#/$defs/vendorPointDirection`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/2/id` |
| `at` | `{"$ref":"#/$defs/nonnegative"}` | Yes | Time point in the owner-defined time domain. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/2/at` |
| `type` | `{"const":"vendor"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/2/type` |
| `parameters` | `{"$ref":"#/$defs/vendorDirectionParameters"}` | Yes | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/2/parameters` |
| `label` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/2/label` |
| `instruction` | `{"type":"string"}` | No / conditional | Supplemental human/AI-readable semantic instruction. Structured/vendor parameters remain authoritative. | [01-all-core.ostf](../examples/01-all-core.ostf)<br>`/tracks/0/directions/2/instruction` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "at": {
      "$ref": "#/$defs/nonnegative"
    },
    "type": {
      "const": "vendor"
    },
    "parameters": {
      "$ref": "#/$defs/vendorDirectionParameters"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured/vendor parameters remain authoritative."
    }
  },
  "required": [
    "id",
    "at",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```

<a id="schema-00f7629b4a96"></a>
## trackDirection

`#/$defs/trackDirection`

Typed semantic instruction owned by a track and positioned on the OSTF global timebase.


### Exact structure, conditions and ranges

```json
{
  "oneOf": [
    {
      "$ref": "#/$defs/improvisationDirection"
    },
    {
      "$ref": "#/$defs/playingRoleDirection"
    },
    {
      "$ref": "#/$defs/pitchRangeDirection"
    },
    {
      "$ref": "#/$defs/vendorRangeDirection"
    },
    {
      "$ref": "#/$defs/vendorPointDirection"
    }
  ],
  "description": "Typed semantic instruction owned by a track and positioned on the OSTF global timebase."
}
```

<a id="schema-8d401d008180"></a>
## vocalPhonetics

`#/$defs/vocalPhonetics`

Ordered phoneme symbols for a lyric unit, not an absolute pronunciation engine command.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `alphabet` | `{"enum":["ipa","xsampa","arpabet","other"]}` | Yes | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/lyrics/units/0/phonetics/0/alphabet` |
| `language` | `{"type":"string","minLength":1}` | No / conditional | Authored language tag. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/lyrics/units/0/phonetics/0/language` |
| `symbols` | `{"type":"array","minItems":1,"items":{"type":"string","minLength":1}}` | Yes | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/lyrics/units/0/phonetics/0/symbols` |
| `namespace` | `{"type":"string","minLength":1}` | No / conditional | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/lyrics/units/0/phonetics/1/namespace` |
| `preferred` | `{"type":"boolean"}` | No / conditional | Optional preference only within the same (alphabet, language) set for this lyricUnit. At most one preferred variant per key; absent does not imply false or a guaranteed conversion. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/lyrics/units/0/phonetics/0/preferred` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "Ordered phoneme symbols for a lyric unit, not an absolute pronunciation engine command.",
  "properties": {
    "alphabet": {
      "enum": [
        "ipa",
        "xsampa",
        "arpabet",
        "other"
      ]
    },
    "language": {
      "type": "string",
      "minLength": 1
    },
    "symbols": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "string",
        "minLength": 1
      }
    },
    "namespace": {
      "type": "string",
      "minLength": 1
    },
    "preferred": {
      "type": "boolean",
      "description": "Optional preference only within the same (alphabet, language) set for this lyricUnit. At most one preferred variant per key; absent does not imply false or a guaranteed conversion."
    }
  },
  "required": [
    "alphabet",
    "symbols"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "alphabet": {
            "const": "other"
          }
        },
        "required": [
          "alphabet"
        ]
      },
      "then": {
        "required": [
          "namespace"
        ]
      }
    }
  ]
}
```

<a id="schema-4b68a4083047"></a>
## vocalProfile

`#/$defs/vocalProfile`

Voice default independent of commercial singer preset or license.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `language` | `{"type":"string","minLength":1}` | No / conditional | Authored language tag. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/lyrics/voices/0/vocalProfile/language` |
| `deliveryMode` | `{"enum":["sing","rap","speak","hum"]}` | No / conditional | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/lyrics/voices/0/vocalProfile/deliveryMode` |
| `voiceDescription` | `{"type":"string","minLength":1}` | No / conditional | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/lyrics/voices/0/vocalProfile/voiceDescription` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "Voice default independent of commercial singer preset or license.",
  "properties": {
    "language": {
      "type": "string",
      "minLength": 1
    },
    "deliveryMode": {
      "enum": [
        "sing",
        "rap",
        "speak",
        "hum"
      ]
    },
    "voiceDescription": {
      "type": "string",
      "minLength": 1
    }
  },
  "additionalProperties": false
}
```

<a id="schema-151525915c48"></a>
## vocalPerformance

`#/$defs/vocalPerformance`

Performance belonging to exactly one lyric voice within a containing clip.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/id` |
| `voiceId` | `{"$ref":"#/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/voiceId` |
| `phonemeEvents` | `{"type":"array","items":{"$ref":"#/$defs/vocalPhonemeEvent"}}` | No / conditional | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents` |
| `pitchCurves` | `{"type":"array","items":{"$ref":"#/$defs/vocalPitchCurve"}}` | No / conditional | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/pitchCurves` |
| `expressionCurves` | `{"type":"array","items":{"$ref":"#/$defs/vocalExpressionCurve"}}` | No / conditional | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/expressionCurves` |
| `techniques` | `{"type":"array","items":{"$ref":"#/$defs/vocalTechnique"}}` | No / conditional | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/techniques` |
| `breathEvents` | `{"type":"array","items":{"$ref":"#/$defs/vocalBreathEvent"}}` | No / conditional | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/breathEvents` |
| `noteIds` | `{"type":"array","items":{"$ref":"#/$defs/id"},"minItems":1,"uniqueItems":true}` | No / conditional | Optional exact list of existing note IDs performed by this voice in the containing clip. No duplicate note objects. When present it includes all locally aligned note IDs for that voice. When absent, derive ownership only from voice-specific alignments. Never infer from song.melodyTrackIds. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/noteIds` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "Performance belonging to exactly one lyric voice within a containing clip.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "voiceId": {
      "$ref": "#/$defs/id"
    },
    "phonemeEvents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalPhonemeEvent"
      }
    },
    "pitchCurves": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalPitchCurve"
      }
    },
    "expressionCurves": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalExpressionCurve"
      }
    },
    "techniques": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalTechnique"
      }
    },
    "breathEvents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalBreathEvent"
      }
    },
    "noteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "minItems": 1,
      "uniqueItems": true,
      "description": "Optional exact list of existing note IDs performed by this voice in the containing clip. No duplicate note objects. When present it includes all locally aligned note IDs for that voice. When absent, derive ownership only from voice-specific alignments. Never infer from song.melodyTrackIds."
    }
  },
  "required": [
    "id",
    "voiceId"
  ],
  "additionalProperties": false
}
```

<a id="schema-fcd572a52128"></a>
## vocalPhonemeEvent

`#/$defs/vocalPhonemeEvent`

Explicit phoneme timing, expressed in clip-relative ppq ticks, negative allowed with nonnegative absolute song time.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/id` |
| `unitId` | `{"$ref":"#/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/unitId` |
| `noteId` | `{"$ref":"#/$defs/id"}` | No / conditional | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/noteId` |
| `alphabet` | `{"enum":["ipa","xsampa","arpabet","other"]}` | Yes | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/alphabet` |
| `namespace` | `{"type":"string","minLength":1}` | No / conditional | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/namespace` |
| `symbol` | `{"type":"string","minLength":1}` | Yes | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/symbol` |
| `start` | `{"$ref":"#/$defs/signed"}` | Yes | Start in the owner-defined time domain; see the manual. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/start` |
| `duration` | `{"$ref":"#/$defs/positive"}` | Yes | Positive duration in ticks. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/duration` |
| `order` | `{"type":"integer"}` | No / conditional | Optional deterministic ordering when multiple phonemeEvents for one voice share the same start tick; distinct within a (voiceId, start) tie group. Not an audio rendering priority. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/order` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "Explicit phoneme timing, expressed in clip-relative ppq ticks, negative allowed with nonnegative absolute song time.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "unitId": {
      "$ref": "#/$defs/id"
    },
    "noteId": {
      "$ref": "#/$defs/id"
    },
    "alphabet": {
      "enum": [
        "ipa",
        "xsampa",
        "arpabet",
        "other"
      ]
    },
    "namespace": {
      "type": "string",
      "minLength": 1
    },
    "symbol": {
      "type": "string",
      "minLength": 1
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "order": {
      "type": "integer",
      "description": "Optional deterministic ordering when multiple phonemeEvents for one voice share the same start tick; distinct within a (voiceId, start) tie group. Not an audio rendering priority."
    }
  },
  "required": [
    "id",
    "unitId",
    "alphabet",
    "symbol",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "alphabet": {
            "const": "other"
          }
        },
        "required": [
          "alphabet"
        ]
      },
      "then": {
        "required": [
          "namespace"
        ]
      }
    }
  ]
}
```

<a id="schema-45a386c6e0a3"></a>
## vocalCurvePointPitch

`#/$defs/vocalCurvePointPitch`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `at` | `{"$ref":"#/$defs/signed"}` | Yes | Time point in the owner-defined time domain. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/pitchCurves/0/points/0/at` |
| `value` | `{"type":"number"}` | Yes | Semitone offset from the targeted MIDI note, in cents (signed). | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/pitchCurves/0/points/0/value` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/signed"
    },
    "value": {
      "type": "number",
      "description": "Semitone offset from the targeted MIDI note, in cents (signed)."
    }
  },
  "required": [
    "at",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="schema-7f0781f571df"></a>
## vocalCurvePointNormalized

`#/$defs/vocalCurvePointNormalized`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `at` | `{"$ref":"#/$defs/signed"}` | Yes | Time point in the owner-defined time domain. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/expressionCurves/0/points/0/at` |
| `value` | `{"type":"number","minimum":0,"maximum":1}` | Yes | Numeric value with the units and constraints specified by the owner. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/expressionCurves/0/points/0/value` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/signed"
    },
    "value": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    }
  },
  "required": [
    "at",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="schema-5f14feb1db08"></a>
## vocalPitchCurve

`#/$defs/vocalPitchCurve`

Specific vocal pitch offset for a single concrete Note, in cents; sample points use clip-relative ppq ticks.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/pitchCurves/0/id` |
| `targetNoteId` | `{"$ref":"#/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/pitchCurves/0/targetNoteId` |
| `unit` | `{"const":"cents"}` | Yes | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/pitchCurves/0/unit` |
| `interpolation` | `{"enum":["step","linear"]}` | Yes | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/pitchCurves/0/interpolation` |
| `points` | `{"type":"array","minItems":1,"items":{"$ref":"#/$defs/vocalCurvePointPitch"}}` | Yes | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/pitchCurves/0/points` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "Specific vocal pitch offset for a single concrete Note, in cents; sample points use clip-relative ppq ticks.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id"
    },
    "unit": {
      "const": "cents"
    },
    "interpolation": {
      "enum": [
        "step",
        "linear"
      ]
    },
    "points": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/vocalCurvePointPitch"
      }
    }
  },
  "required": [
    "id",
    "targetNoteId",
    "unit",
    "interpolation",
    "points"
  ],
  "additionalProperties": false
}
```

<a id="schema-23c97f8c4086"></a>
## vocalExpressionCurve

`#/$defs/vocalExpressionCurve`

Portable vocal parameters, each normalized 0..1, with no promise of perceptually identical output across engines.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/expressionCurves/0/id` |
| `parameter` | `{"enum":["dynamics","breathiness","tension","brightness","voicing"]}` | Yes | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/expressionCurves/0/parameter` |
| `interpolation` | `{"enum":["step","linear"]}` | Yes | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/expressionCurves/0/interpolation` |
| `points` | `{"type":"array","minItems":1,"items":{"$ref":"#/$defs/vocalCurvePointNormalized"}}` | Yes | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/expressionCurves/0/points` |
| `targetNoteId` | `{"$ref":"#/$defs/id"}` | No / conditional | Optional note-specific replacement of a clip-scoped curve of the same parameter while the note is active. Points still use clip-relative ticks. Do not sum both curves. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/expressionCurves/5/targetNoteId` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "Portable vocal parameters, each normalized 0..1, with no promise of perceptually identical output across engines.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "parameter": {
      "enum": [
        "dynamics",
        "breathiness",
        "tension",
        "brightness",
        "voicing"
      ]
    },
    "interpolation": {
      "enum": [
        "step",
        "linear"
      ]
    },
    "points": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/vocalCurvePointNormalized"
      }
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional note-specific replacement of a clip-scoped curve of the same parameter while the note is active. Points still use clip-relative ticks. Do not sum both curves."
    }
  },
  "required": [
    "id",
    "parameter",
    "interpolation",
    "points"
  ],
  "additionalProperties": false
}
```

<a id="schema-4cd016e7774f"></a>
## vocalTechnique

`#/$defs/vocalTechnique`

Semantic artistic intention, not deterministic rendering or an extra pitch source.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/techniques/0/id` |
| `start` | `{"$ref":"#/$defs/signed"}` | Yes | Start in the owner-defined time domain; see the manual. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/techniques/0/start` |
| `duration` | `{"$ref":"#/$defs/positive"}` | Yes | Positive duration in ticks. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/techniques/0/duration` |
| `kind` | `{"enum":["scoop","fall","vibrato","portamento","legato","staccato","accent","whisper","growl","falsetto","humming","rap","melisma"]}` | Yes | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/techniques/0/kind` |
| `intensity` | `{"type":"number","minimum":0,"maximum":1}` | No / conditional | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/techniques/0/intensity` |
| `targetNoteId` | `{"$ref":"#/$defs/id"}` | No / conditional | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/techniques/0/targetNoteId` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "Semantic artistic intention, not deterministic rendering or an extra pitch source.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "kind": {
      "enum": [
        "scoop",
        "fall",
        "vibrato",
        "portamento",
        "legato",
        "staccato",
        "accent",
        "whisper",
        "growl",
        "falsetto",
        "humming",
        "rap",
        "melisma"
      ]
    },
    "intensity": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    },
    "targetNoteId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "kind"
  ],
  "additionalProperties": false
}
```

<a id="schema-ec2f019b423f"></a>
## vocalBreathEvent

`#/$defs/vocalBreathEvent`

Optional breath marker. The renderer decides whether to synthesize audible breath.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/breathEvents/0/id` |
| `start` | `{"$ref":"#/$defs/signed"}` | Yes | Start in the owner-defined time domain; see the manual. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/breathEvents/0/start` |
| `duration` | `{"$ref":"#/$defs/positive"}` | Yes | Positive duration in ticks. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/breathEvents/0/duration` |
| `kind` | `{"enum":["inhale","exhale"]}` | Yes | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/breathEvents/0/kind` |
| `intensity` | `{"type":"number","minimum":0,"maximum":1}` | No / conditional | See the owning object semantics and exact constraints below. | [02-all-vocal-parameters.ostf](../examples/02-all-vocal-parameters.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/breathEvents/0/intensity` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "Optional breath marker. The renderer decides whether to synthesize audible breath.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "kind": {
      "enum": [
        "inhale",
        "exhale"
      ]
    },
    "intensity": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "kind"
  ],
  "additionalProperties": false
}
```

<a id="schema-89e7c47e4e36"></a>
## Legacy / id

`#/$defs/legacy33/$defs/id`


### Exact structure, conditions and ranges

```json
{
  "type": "string",
  "pattern": "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="schema-0e7b3ba09160"></a>
## Legacy / nonnegative

`#/$defs/legacy33/$defs/nonnegative`


### Exact structure, conditions and ranges

```json
{
  "type": "integer",
  "minimum": 0,
  "maximum": 9007199254740991
}
```

<a id="schema-499e1b38d212"></a>
## Legacy / positive

`#/$defs/legacy33/$defs/positive`


### Exact structure, conditions and ranges

```json
{
  "type": "integer",
  "minimum": 1,
  "maximum": 9007199254740991
}
```

<a id="schema-9c0955d738e2"></a>
## Legacy / signed

`#/$defs/legacy33/$defs/signed`


### Exact structure, conditions and ranges

```json
{
  "type": "integer",
  "minimum": -9007199254740991,
  "maximum": 9007199254740991
}
```

<a id="schema-807646b0fce0"></a>
## Legacy / pitch

`#/$defs/legacy33/$defs/pitch`


### Exact structure, conditions and ranges

```json
{
  "type": "integer",
  "minimum": 0,
  "maximum": 127
}
```

<a id="schema-76351f8f7ee7"></a>
## Legacy / ref

`#/$defs/legacy33/$defs/ref`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `type` | `{"enum":["section","track","clip","note","chord","scale","soundSlot","drumKit","lyricDocument","lyricPhrase","lyricUnit","lyricAlignment","resource","genre"]}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/dependencies/refs/0/type` |
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/dependencies/refs/0/id` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "type": {
      "enum": [
        "section",
        "track",
        "clip",
        "note",
        "chord",
        "scale",
        "soundSlot",
        "drumKit",
        "lyricDocument",
        "lyricPhrase",
        "lyricUnit",
        "lyricAlignment",
        "resource",
        "genre"
      ]
    },
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    }
  },
  "required": [
    "type",
    "id"
  ],
  "additionalProperties": false
}
```

<a id="schema-92f7f746fea9"></a>
## Legacy / range

`#/$defs/legacy33/$defs/range`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `start` | `{"$ref":"#/$defs/legacy33/$defs/nonnegative"}` | Yes | Start in the owner-defined time domain; see the manual. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/inputs/0/readRange/start` |
| `duration` | `{"$ref":"#/$defs/legacy33/$defs/positive"}` | Yes | Positive duration in ticks. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/inputs/0/readRange/duration` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    }
  },
  "required": [
    "start",
    "duration"
  ],
  "additionalProperties": false
}
```

<a id="schema-aa6c1bbd7d55"></a>
## Legacy / spelledPitchClass

`#/$defs/legacy33/$defs/spelledPitchClass`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `step` | `{"enum":["A","B","C","D","E","F","G"]}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `alter` | `{"type":"integer","minimum":-2,"maximum":2}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "step": {
      "enum": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G"
      ]
    },
    "alter": {
      "type": "integer",
      "minimum": -2,
      "maximum": 2
    }
  },
  "required": [
    "step",
    "alter"
  ],
  "additionalProperties": false
}
```

<a id="schema-cf3060dc5fe4"></a>
## Legacy / song

`#/$defs/legacy33/$defs/song`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `title` | `{"type":"string"}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `primaryMelodyTrackId` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `localizedTitles` | `{"$ref":"#/$defs/legacy33/$defs/localizedNames"}` | No / conditional | Optional localized song-title alternatives. song.title is the stable fallback. | Conditional/archival definition; see exact constraints. |
| `subtitle` | `{"type":"string"}` | No / conditional | Optional original-language subtitle. | Conditional/archival definition; see exact constraints. |
| `description` | `{"type":"string"}` | No / conditional | Optional original-language description, including Unicode and line breaks. | Conditional/archival definition; see exact constraints. |
| `alternateTitles` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/alternateTitle"}}` | No / conditional | Additional stable-ID source-language titles. | Conditional/archival definition; see exact constraints. |
| `credits` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/credit"}}` | No / conditional | Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted. | Conditional/archival definition; see exact constraints. |
| `genres` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/genre"}}` | No / conditional | Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    },
    "primaryMelodyTrackId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "localizedTitles": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized song-title alternatives. song.title is the stable fallback."
    },
    "subtitle": {
      "type": "string",
      "description": "Optional original-language subtitle."
    },
    "description": {
      "type": "string",
      "description": "Optional original-language description, including Unicode and line breaks."
    },
    "alternateTitles": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/alternateTitle"
      },
      "description": "Additional stable-ID source-language titles."
    },
    "credits": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/credit"
      },
      "description": "Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted."
    },
    "genres": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/genre"
      },
      "description": "Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified."
    }
  },
  "required": [
    "title"
  ],
  "additionalProperties": false
}
```

<a id="schema-6ec56b313dbf"></a>
## Legacy / section

`#/$defs/legacy33/$defs/section`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | Conditional/archival definition; see exact constraints. |
| `name` | `{"type":"string","minLength":1}` | Yes | Authored display name; never an identity or executable instruction. | Conditional/archival definition; see exact constraints. |
| `start` | `{"$ref":"#/$defs/legacy33/$defs/nonnegative"}` | Yes | Start in the owner-defined time domain; see the manual. | Conditional/archival definition; see exact constraints. |
| `duration` | `{"$ref":"#/$defs/legacy33/$defs/positive"}` | Yes | Positive duration in ticks. | Conditional/archival definition; see exact constraints. |
| `role` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `localizedNames` | `{"$ref":"#/$defs/legacy33/$defs/localizedNames"}` | No / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "role": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "name",
    "start",
    "duration"
  ],
  "additionalProperties": false
}
```

<a id="schema-f1a7c5685d6c"></a>
## Legacy / tempo

`#/$defs/legacy33/$defs/tempo`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `at` | `{"$ref":"#/$defs/legacy33/$defs/nonnegative"}` | Yes | Time point in the owner-defined time domain. | Conditional/archival definition; see exact constraints. |
| `bpm` | `{"type":"number","exclusiveMinimum":0,"maximum":1000}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "bpm": {
      "type": "number",
      "exclusiveMinimum": 0,
      "maximum": 1000
    }
  },
  "required": [
    "at",
    "bpm"
  ],
  "additionalProperties": false
}
```

<a id="schema-31c401ec2fe1"></a>
## Legacy / meter

`#/$defs/legacy33/$defs/meter`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `at` | `{"$ref":"#/$defs/legacy33/$defs/nonnegative"}` | Yes | Time point in the owner-defined time domain. | Conditional/archival definition; see exact constraints. |
| `numerator` | `{"type":"integer","minimum":1,"maximum":64}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `denominator` | `{"enum":[1,2,4,8,16,32,64],"type":"integer"}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "numerator": {
      "type": "integer",
      "minimum": 1,
      "maximum": 64
    },
    "denominator": {
      "enum": [
        1,
        2,
        4,
        8,
        16,
        32,
        64
      ],
      "type": "integer"
    }
  },
  "required": [
    "at",
    "numerator",
    "denominator"
  ],
  "additionalProperties": false
}
```

<a id="schema-1d0bbb380e5a"></a>
## Legacy / timeline

`#/$defs/legacy33/$defs/timeline`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `sections` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/section"}}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `tempoChanges` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/tempo"},"minItems":1}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `meterChanges` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/meter"},"minItems":1}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "sections": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/section"
      }
    },
    "tempoChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/tempo"
      },
      "minItems": 1
    },
    "meterChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/meter"
      },
      "minItems": 1
    }
  },
  "required": [
    "sections",
    "tempoChanges",
    "meterChanges"
  ],
  "additionalProperties": false
}
```

<a id="schema-724bf82722f0"></a>
## Legacy / chord

`#/$defs/legacy33/$defs/chord`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | Conditional/archival definition; see exact constraints. |
| `start` | `{"$ref":"#/$defs/legacy33/$defs/nonnegative"}` | Yes | Start in the owner-defined time domain; see the manual. | Conditional/archival definition; see exact constraints. |
| `duration` | `{"$ref":"#/$defs/legacy33/$defs/positive"}` | Yes | Positive duration in ticks. | Conditional/archival definition; see exact constraints. |
| `label` | `{"type":"string","minLength":1}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `root` | `{"$ref":"#/$defs/legacy33/$defs/spelledPitchClass"}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `intervals` | `{"type":"array","items":{"type":"integer","minimum":0,"maximum":35},"minItems":1,"maxItems":36,"uniqueItems":true,"contains":{"const":0}}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `bass` | `{"$ref":"#/$defs/legacy33/$defs/spelledPitchClass"}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `voicing` | `{"$ref":"#/$defs/legacy33/$defs/voicing"}` | No / conditional | Optional pitch snapshot (not an arrangement note sequence). No automatic playback. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "label": {
      "type": "string",
      "minLength": 1
    },
    "root": {
      "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 35
      },
      "minItems": 1,
      "maxItems": 36,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "bass": {
      "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
    },
    "voicing": {
      "$ref": "#/$defs/legacy33/$defs/voicing",
      "description": "Optional pitch snapshot (not an arrangement note sequence). No automatic playback."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "label"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "root": [
      "intervals"
    ],
    "intervals": [
      "root"
    ]
  }
}
```

<a id="schema-855503cf7f47"></a>
## Legacy / scale

`#/$defs/legacy33/$defs/scale`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | Conditional/archival definition; see exact constraints. |
| `start` | `{"$ref":"#/$defs/legacy33/$defs/nonnegative"}` | Yes | Start in the owner-defined time domain; see the manual. | Conditional/archival definition; see exact constraints. |
| `duration` | `{"$ref":"#/$defs/legacy33/$defs/positive"}` | Yes | Positive duration in ticks. | Conditional/archival definition; see exact constraints. |
| `label` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `tonic` | `{"$ref":"#/$defs/legacy33/$defs/spelledPitchClass"}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `intervals` | `{"type":"array","items":{"type":"integer","minimum":0,"maximum":11},"minItems":1,"maxItems":12,"uniqueItems":true,"contains":{"const":0}}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "tonic": {
      "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 11
      },
      "minItems": 1,
      "maxItems": 12,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "tonic",
    "intervals"
  ],
  "additionalProperties": false
}
```

<a id="schema-d1738fe99d18"></a>
## Legacy / harmony

`#/$defs/legacy33/$defs/harmony`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `chords` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/chord"}}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `scales` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/scale"}}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "chords": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/chord"
      }
    },
    "scales": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/scale"
      }
    }
  },
  "required": [
    "chords",
    "scales"
  ],
  "additionalProperties": false
}
```

<a id="schema-67614c4a2158"></a>
## Legacy / instrument

`#/$defs/legacy33/$defs/instrument`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `name` | `{"type":"string"}` | Yes | Authored display name; never an identity or executable instruction. | Conditional/archival definition; see exact constraints. |
| `family` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `localizedNames` | `{"$ref":"#/$defs/legacy33/$defs/localizedNames"}` | No / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "family": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```

<a id="schema-71b274e4ebf6"></a>
## Legacy / note

`#/$defs/legacy33/$defs/note`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

Concrete Core note; optional velocity is a note-on attribute. Phrase templates use a separate version-frozen sourceNote shape.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | Conditional/archival definition; see exact constraints. |
| `start` | `{"$ref":"#/$defs/legacy33/$defs/signed"}` | Yes | Start in the owner-defined time domain; see the manual. | Conditional/archival definition; see exact constraints. |
| `duration` | `{"$ref":"#/$defs/legacy33/$defs/positive"}` | Yes | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. | Conditional/archival definition; see exact constraints. |
| `pitch` | `{"$ref":"#/$defs/legacy33/$defs/pitch"}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `soundSlotId` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | No / conditional | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre. | Conditional/archival definition; see exact constraints. |
| `velocity` | `{"type":"integer","minimum":1,"maximum":127}` | No / conditional | Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive",
      "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
    },
    "pitch": {
      "$ref": "#/$defs/legacy33/$defs/pitch"
    },
    "soundSlotId": {
      "$ref": "#/$defs/legacy33/$defs/id",
      "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
    },
    "velocity": {
      "type": "integer",
      "minimum": 1,
      "maximum": 127,
      "description": "Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving."
    }
  },
  "required": [
    "id",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "required": [
        "pitch"
      ],
      "not": {
        "required": [
          "soundSlotId"
        ]
      }
    },
    {
      "required": [
        "soundSlotId"
      ],
      "not": {
        "required": [
          "pitch"
        ]
      }
    }
  ],
  "description": "Concrete Core note; optional velocity is a note-on attribute. Phrase templates use a separate version-frozen sourceNote shape."
}
```

<a id="schema-352905fa076c"></a>
## Legacy / clip

`#/$defs/legacy33/$defs/clip`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | Conditional/archival definition; see exact constraints. |
| `name` | `{"type":"string"}` | No / conditional | Authored display name; never an identity or executable instruction. | Conditional/archival definition; see exact constraints. |
| `start` | `{"$ref":"#/$defs/legacy33/$defs/nonnegative"}` | Yes | Start in the owner-defined time domain; see the manual. | Conditional/archival definition; see exact constraints. |
| `duration` | `{"$ref":"#/$defs/legacy33/$defs/positive"}` | Yes | Positive duration in ticks. | Conditional/archival definition; see exact constraints. |
| `enabled` | `{"type":"boolean","default":true}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `notes` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/note"}}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `localizedNames` | `{"$ref":"#/$defs/legacy33/$defs/localizedNames"}` | No / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "enabled": {
      "type": "boolean",
      "default": true
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/note"
      }
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "notes"
  ],
  "additionalProperties": false
}
```

<a id="schema-59b87a2e0933"></a>
## Legacy / track

`#/$defs/legacy33/$defs/track`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | Conditional/archival definition; see exact constraints. |
| `name` | `{"type":"string"}` | Yes | Authored display name; never an identity or executable instruction. | Conditional/archival definition; see exact constraints. |
| `role` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `instrument` | `{"$ref":"#/$defs/legacy33/$defs/instrument"}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `enabled` | `{"type":"boolean","default":true}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `clips` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/clip"}}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `trackType` | `{"enum":["melodic","drum","mixed"]}` | No / conditional | Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class. | Conditional/archival definition; see exact constraints. |
| `preferredView` | `{"enum":["auto","pianoRoll","drumGrid"],"default":"auto"}` | No / conditional | Non-binding presentation preference. Does not change note meaning. | Conditional/archival definition; see exact constraints. |
| `soundSource` | `{"$ref":"#/$defs/legacy33/$defs/soundSource"}` | No / conditional | Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee. | Conditional/archival definition; see exact constraints. |
| `localizedNames` | `{"$ref":"#/$defs/legacy33/$defs/localizedNames"}` | No / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | Conditional/archival definition; see exact constraints. |
| `drumKitId` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | No / conditional | Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string"
    },
    "instrument": {
      "$ref": "#/$defs/legacy33/$defs/instrument"
    },
    "enabled": {
      "type": "boolean",
      "default": true
    },
    "clips": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/clip"
      }
    },
    "trackType": {
      "enum": [
        "melodic",
        "drum",
        "mixed"
      ],
      "description": "Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class."
    },
    "preferredView": {
      "enum": [
        "auto",
        "pianoRoll",
        "drumGrid"
      ],
      "default": "auto",
      "description": "Non-binding presentation preference. Does not change note meaning."
    },
    "soundSource": {
      "$ref": "#/$defs/legacy33/$defs/soundSource",
      "description": "Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee."
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    },
    "drumKitId": {
      "$ref": "#/$defs/legacy33/$defs/id",
      "description": "Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit."
    }
  },
  "required": [
    "id",
    "name",
    "clips"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "trackType": {
            "const": "melodic"
          }
        },
        "required": [
          "trackType"
        ]
      },
      "then": {
        "not": {
          "required": [
            "drumKitId"
          ]
        }
      }
    }
  ]
}
```

<a id="schema-2a2c3b2903fc"></a>
## Legacy / soundSlot

`#/$defs/legacy33/$defs/soundSlot`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | Conditional/archival definition; see exact constraints. |
| `name` | `{"type":"string"}` | Yes | Authored display name; never an identity or executable instruction. | Conditional/archival definition; see exact constraints. |
| `role` | `{"type":"string"}` | No / conditional | Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier. | Conditional/archival definition; see exact constraints. |
| `midiNote` | `{"$ref":"#/$defs/legacy33/$defs/pitch"}` | No / conditional | Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity. | Conditional/archival definition; see exact constraints. |
| `midiMapping` | `{"$ref":"#/$defs/legacy33/$defs/midiMapping"}` | No / conditional | Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity. | Conditional/archival definition; see exact constraints. |
| `localizedNames` | `{"$ref":"#/$defs/legacy33/$defs/localizedNames"}` | No / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string",
      "description": "Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier."
    },
    "midiNote": {
      "$ref": "#/$defs/legacy33/$defs/pitch",
      "description": "Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity."
    },
    "midiMapping": {
      "$ref": "#/$defs/legacy33/$defs/midiMapping",
      "description": "Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity."
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false,
  "description": "Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded."
}
```

<a id="schema-4c6d1a69fe9e"></a>
## Legacy / lyricDocument

`#/$defs/legacy33/$defs/lyricDocument`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | Conditional/archival definition; see exact constraints. |
| `title` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `language` | `{"type":"string"}` | No / conditional | Authored language tag. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "title": {
      "type": "string"
    },
    "language": {
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```

<a id="schema-7eaf29dd50c5"></a>
## Legacy / lyricPhrase

`#/$defs/legacy33/$defs/lyricPhrase`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | Conditional/archival definition; see exact constraints. |
| `documentId` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `text` | `{"type":"string"}` | Yes | Authored text, preserved without executing its contents. | Conditional/archival definition; see exact constraints. |
| `pronunciation` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `start` | `{"$ref":"#/$defs/legacy33/$defs/nonnegative"}` | No / conditional | Start in the owner-defined time domain; see the manual. | Conditional/archival definition; see exact constraints. |
| `duration` | `{"$ref":"#/$defs/legacy33/$defs/positive"}` | No / conditional | Positive duration in ticks. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "text": {
      "type": "string"
    },
    "pronunciation": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    }
  },
  "required": [
    "id",
    "documentId",
    "text"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```

<a id="schema-4a1ae1742a3e"></a>
## Legacy / lyricUnit

`#/$defs/legacy33/$defs/lyricUnit`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | Conditional/archival definition; see exact constraints. |
| `phraseId` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `text` | `{"type":"string"}` | Yes | Authored text, preserved without executing its contents. | Conditional/archival definition; see exact constraints. |
| `pronunciation` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `start` | `{"$ref":"#/$defs/legacy33/$defs/nonnegative"}` | No / conditional | Start in the owner-defined time domain; see the manual. | Conditional/archival definition; see exact constraints. |
| `duration` | `{"$ref":"#/$defs/legacy33/$defs/positive"}` | No / conditional | Positive duration in ticks. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "phraseId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "text": {
      "type": "string"
    },
    "pronunciation": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    }
  },
  "required": [
    "id",
    "phraseId",
    "text"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```

<a id="schema-7484ca2e8e21"></a>
## Legacy / lyricAlignment

`#/$defs/legacy33/$defs/lyricAlignment`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | Conditional/archival definition; see exact constraints. |
| `unitIds` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/id"},"uniqueItems":true,"minItems":1}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `noteIds` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/id"},"uniqueItems":true,"minItems":1}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "unitIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "uniqueItems": true,
      "minItems": 1
    },
    "noteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "uniqueItems": true,
      "minItems": 1
    }
  },
  "required": [
    "id",
    "unitIds",
    "noteIds"
  ],
  "additionalProperties": false
}
```

<a id="schema-103328dc0e5b"></a>
## Legacy / lyrics

`#/$defs/legacy33/$defs/lyrics`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `documents` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/lyricDocument"}}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `phrases` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/lyricPhrase"}}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `units` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/lyricUnit"}}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `alignments` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/lyricAlignment"}}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "documents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/lyricDocument"
      }
    },
    "phrases": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/lyricPhrase"
      }
    },
    "units": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/lyricUnit"
      }
    },
    "alignments": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/lyricAlignment"
      }
    }
  },
  "required": [
    "documents",
    "phrases",
    "units",
    "alignments"
  ],
  "additionalProperties": false
}
```

<a id="schema-c2db6cd8f3e9"></a>
## Legacy / sha256

`#/$defs/legacy33/$defs/sha256`


### Exact structure, conditions and ranges

```json
{
  "type": "string",
  "pattern": "^[0-9a-f]{64}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="schema-9e19b5836345"></a>
## Legacy / resource

`#/$defs/legacy33/$defs/resource`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | Conditional/archival definition; see exact constraints. |
| `kind` | `{"enum":["audio","midi","text","other"]}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `uri` | `{"type":"string","minLength":1}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `name` | `{"type":"string"}` | No / conditional | Authored display name; never an identity or executable instruction. | Conditional/archival definition; see exact constraints. |
| `sha256` | `{"$ref":"#/$defs/legacy33/$defs/sha256"}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "kind": {
      "enum": [
        "audio",
        "midi",
        "text",
        "other"
      ]
    },
    "uri": {
      "type": "string",
      "minLength": 1
    },
    "name": {
      "type": "string"
    },
    "sha256": {
      "$ref": "#/$defs/legacy33/$defs/sha256"
    }
  },
  "required": [
    "id",
    "kind",
    "uri"
  ],
  "additionalProperties": false
}
```

<a id="schema-1c75c4bf6382"></a>
## Legacy / dependencies

`#/$defs/legacy33/$defs/dependencies`


### Exact structure, conditions and ranges

```json
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "scope": {
          "enum": [
            "document",
            "none"
          ]
        }
      },
      "required": [
        "scope"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "scope": {
          "const": "objects"
        },
        "refs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/ref"
          },
          "minItems": 1,
          "uniqueItems": true
        }
      },
      "required": [
        "scope",
        "refs"
      ],
      "additionalProperties": false
    }
  ]
}
```

<a id="schema-83e73de19250"></a>
## Legacy / extension

`#/$defs/legacy33/$defs/extension`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `version` | `{"type":"string","minLength":1}` | Yes | Version identifier for this owning object. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/version` |
| `status` | `{"enum":["current","stale","unverified"]}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/status` |
| `dependencies` | `{"$ref":"#/$defs/legacy33/$defs/dependencies"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/dependencies` |
| `data` | `{}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/data` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "string",
      "minLength": 1
    },
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/legacy33/$defs/dependencies"
    },
    "data": {}
  },
  "required": [
    "version",
    "status",
    "dependencies",
    "data"
  ],
  "additionalProperties": false
}
```

<a id="schema-a20bc23fbf4f"></a>
## Legacy / relativeAssignment

`#/$defs/legacy33/$defs/relativeAssignment`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `noteId` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/data/assignments/0/noteId` |
| `basis` | `{"enum":["chordTone","scaleDegree"]}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/data/assignments/0/basis` |
| `contextId` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/data/assignments/0/contextId` |
| `anchorPitch` | `{"$ref":"#/$defs/legacy33/$defs/pitch"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/data/assignments/0/anchorPitch` |
| `index` | `{"type":"integer","minimum":1,"maximum":36}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/data/assignments/0/index` |
| `chromaticOffset` | `{"type":"integer","minimum":-24,"maximum":24}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/data/assignments/0/chromaticOffset` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "noteId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "basis": {
      "enum": [
        "chordTone",
        "scaleDegree"
      ]
    },
    "contextId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "anchorPitch": {
      "$ref": "#/$defs/legacy33/$defs/pitch"
    },
    "index": {
      "type": "integer",
      "minimum": 1,
      "maximum": 36
    },
    "chromaticOffset": {
      "type": "integer",
      "minimum": -24,
      "maximum": 24
    }
  },
  "required": [
    "noteId",
    "basis",
    "contextId",
    "anchorPitch",
    "index",
    "chromaticOffset"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "basis": {
            "const": "scaleDegree"
          }
        },
        "required": [
          "basis"
        ]
      },
      "then": {
        "properties": {
          "index": {
            "maximum": 12
          }
        }
      }
    }
  ]
}
```

<a id="schema-a9777d5f71bd"></a>
## Legacy / relativeData

`#/$defs/legacy33/$defs/relativeData`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `assignments` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/relativeAssignment"}}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/data/assignments` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "assignments": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/relativeAssignment"
      }
    }
  },
  "required": [
    "assignments"
  ],
  "additionalProperties": false
}
```

<a id="schema-abae7bc69673"></a>
## Legacy / generator

`#/$defs/legacy33/$defs/generator`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"type":"string","minLength":1}` | Yes | Stable identity; distinguish definition from reference by its owner. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/generator/id` |
| `version` | `{"type":"string","minLength":1}` | Yes | Version identifier for this owning object. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/generator/version` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "version"
  ],
  "additionalProperties": false
}
```

<a id="schema-3bcfec9bb3d8"></a>
## Legacy / generationInput

`#/$defs/legacy33/$defs/generationInput`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `role` | `{"type":"string","minLength":1}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/inputs/0/role` |
| `ref` | `{"$ref":"#/$defs/legacy33/$defs/ref"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/inputs/0/ref` |
| `readRange` | `{"$ref":"#/$defs/legacy33/$defs/range"}` | No / conditional | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/inputs/0/readRange` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "role": {
      "type": "string",
      "minLength": 1
    },
    "ref": {
      "$ref": "#/$defs/legacy33/$defs/ref"
    },
    "readRange": {
      "$ref": "#/$defs/legacy33/$defs/range"
    }
  },
  "required": [
    "role",
    "ref"
  ],
  "additionalProperties": false
}
```

<a id="schema-b97284b5732d"></a>
## Legacy / generationProcess

`#/$defs/legacy33/$defs/generationProcess`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/id` |
| `generator` | `{"$ref":"#/$defs/legacy33/$defs/generator"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/generator` |
| `inputs` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/generationInput"}}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/inputs` |
| `outputs` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/ref"},"minItems":1}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/outputs` |
| `targetRange` | `{"$ref":"#/$defs/legacy33/$defs/range"}` | No / conditional | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/targetRange` |
| `protectedNoteIds` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/id"},"uniqueItems":true}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/protectedNoteIds` |
| `vendorExtension` | `{"type":"string","minLength":1}` | No / conditional | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/vendorExtension` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "generator": {
      "$ref": "#/$defs/legacy33/$defs/generator"
    },
    "inputs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/generationInput"
      }
    },
    "outputs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/ref"
      },
      "minItems": 1
    },
    "targetRange": {
      "$ref": "#/$defs/legacy33/$defs/range"
    },
    "protectedNoteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "uniqueItems": true
    },
    "vendorExtension": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "generator",
    "inputs",
    "outputs",
    "protectedNoteIds"
  ],
  "additionalProperties": false
}
```

<a id="schema-aa74d437308f"></a>
## Legacy / generationData

`#/$defs/legacy33/$defs/generationData`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `processes` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/generationProcess"}}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "processes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/generationProcess"
      }
    }
  },
  "required": [
    "processes"
  ],
  "additionalProperties": false
}
```

<a id="schema-6baefb234944"></a>
## Legacy / color

`#/$defs/legacy33/$defs/color`


### Exact structure, conditions and ranges

```json
{
  "type": "string",
  "pattern": "^#[0-9A-Fa-f]{6}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="schema-2e7fb7685f53"></a>
## Legacy / roleDefinition

`#/$defs/legacy33/$defs/roleDefinition`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.appearance.v1/data/roleDefinitions/0/id` |
| `name` | `{"type":"string","minLength":1}` | Yes | Authored display name; never an identity or executable instruction. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.appearance.v1/data/roleDefinitions/0/name` |
| `baseRole` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.appearance.v1/data/roleDefinitions/0/baseRole` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "baseRole": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="schema-1c4f374f3163"></a>
## Legacy / roleColorMap

`#/$defs/legacy33/$defs/roleColorMap`


### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "additionalProperties": {
    "$ref": "#/$defs/legacy33/$defs/color"
  }
}
```

<a id="schema-47795aef91d3"></a>
## Legacy / customRoleColorMap

`#/$defs/legacy33/$defs/customRoleColorMap`


### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "propertyNames": {
    "$ref": "#/$defs/legacy33/$defs/id"
  },
  "additionalProperties": {
    "$ref": "#/$defs/legacy33/$defs/color"
  }
}
```

<a id="schema-5f73ffdead81"></a>
## Legacy / objectColor

`#/$defs/legacy33/$defs/objectColor`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `target` | `{"$ref":"#/$defs/legacy33/$defs/ref"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.appearance.v1/data/appearance/objectColors/0/target` |
| `color` | `{"$ref":"#/$defs/legacy33/$defs/color"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.appearance.v1/data/appearance/objectColors/0/color` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "target": {
      "$ref": "#/$defs/legacy33/$defs/ref"
    },
    "color": {
      "$ref": "#/$defs/legacy33/$defs/color"
    }
  },
  "required": [
    "target",
    "color"
  ],
  "additionalProperties": false
}
```

<a id="schema-88792dd6c736"></a>
## Legacy / appearanceData

`#/$defs/legacy33/$defs/appearanceData`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `roleDefinitions` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/roleDefinition"}}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.appearance.v1/data/roleDefinitions` |
| `sectionRoleAssignments` | `{"type":"object","propertyNames":{"$ref":"#/$defs/legacy33/$defs/id"},"additionalProperties":{"$ref":"#/$defs/legacy33/$defs/id"}}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.appearance.v1/data/sectionRoleAssignments` |
| `appearance` | `{"type":"object","properties":{"roleColors":{"$ref":"#/$defs/legacy33/$defs/roleColorMap"},"customRoleColors":{"$ref":"#/$defs/legacy33/$defs/customRoleColorMap"},"objectColors":{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/objectColor"}}},"required":["roleColors","customRoleColors","objectColors"],"additionalProperties":false}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.appearance.v1/data/appearance` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "roleDefinitions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/roleDefinition"
      }
    },
    "sectionRoleAssignments": {
      "type": "object",
      "propertyNames": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "additionalProperties": {
        "$ref": "#/$defs/legacy33/$defs/id"
      }
    },
    "appearance": {
      "type": "object",
      "properties": {
        "roleColors": {
          "$ref": "#/$defs/legacy33/$defs/roleColorMap"
        },
        "customRoleColors": {
          "$ref": "#/$defs/legacy33/$defs/customRoleColorMap"
        },
        "objectColors": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/objectColor"
          }
        }
      },
      "required": [
        "roleColors",
        "customRoleColors",
        "objectColors"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "roleDefinitions",
    "sectionRoleAssignments",
    "appearance"
  ],
  "additionalProperties": false
}
```

<a id="schema-2776ab3e0302"></a>
## Legacy / legacyData

`#/$defs/legacy33/$defs/legacyData`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `sourceVersion` | `{"const":"2.3.0"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.legacy-import.v1/data/sourceVersion` |
| `sourceSha256` | `{"$ref":"#/$defs/legacy33/$defs/sha256"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.legacy-import.v1/data/sourceSha256` |
| `sourceText` | `{"type":"string","minLength":1}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.legacy-import.v1/data/sourceText` |
| `conversionReport` | `{"type":"object"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.legacy-import.v1/data/conversionReport` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "sourceVersion": {
      "const": "2.3.0"
    },
    "sourceSha256": {
      "$ref": "#/$defs/legacy33/$defs/sha256"
    },
    "sourceText": {
      "type": "string",
      "minLength": 1
    },
    "conversionReport": {
      "type": "object"
    }
  },
  "required": [
    "sourceVersion",
    "sourceSha256",
    "sourceText",
    "conversionReport"
  ],
  "additionalProperties": false
}
```

<a id="schema-2fea9a3b8b7e"></a>
## Legacy / extensions

`#/$defs/legacy33/$defs/extensions`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `org.ostf.relative-phrase.v1` | `{"allOf":[{"$ref":"#/$defs/legacy33/$defs/extension"},{"if":{"properties":{"version":{"const":"1.0.0-draft.1"}},"required":["version"]},"then":{"properties":{"data":{"$ref":"#/$defs/legacy33/$defs/relativeData"}}}}]}` | No / conditional | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.relative-phrase.v1` |
| `org.ostf.generation-context.v1` | `{"allOf":[{"$ref":"#/$defs/legacy33/$defs/extension"},{"if":{"properties":{"version":{"const":"1.0.0-draft.1"}},"required":["version"]},"then":{"properties":{"data":{"$ref":"#/$defs/legacy33/$defs/generationData"}}}}]}` | No / conditional | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.generation-context.v1` |
| `org.ostf.appearance.v1` | `{"allOf":[{"$ref":"#/$defs/legacy33/$defs/extension"},{"if":{"properties":{"version":{"const":"1.0.0-draft.1"}},"required":["version"]},"then":{"properties":{"data":{"$ref":"#/$defs/legacy33/$defs/appearanceData"}}}}]}` | No / conditional | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.appearance.v1` |
| `org.ostf.legacy-import.v1` | `{"allOf":[{"$ref":"#/$defs/legacy33/$defs/extension"},{"if":{"properties":{"version":{"const":"1.0.0-draft.1"}},"required":["version"]},"then":{"properties":{"data":{"$ref":"#/$defs/legacy33/$defs/legacyData"}}}}]}` | No / conditional | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.legacy-import.v1` |
| `org.ostf.phrase-library.v1` | `{"allOf":[{"$ref":"#/$defs/legacy33/$defs/extension"},{"if":{"properties":{"version":{"const":"1.0.0-draft.1"}},"required":["version"]},"then":{"properties":{"data":{"$ref":"#/$defs/legacy33/$defs/phraseLibraryData"}}}}]}` | No / conditional | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1` |
| `org.ostf.clip-choices.v1` | `{"allOf":[{"$ref":"#/$defs/legacy33/$defs/extension"},{"if":{"properties":{"version":{"const":"1.0.0-draft.1"}},"required":["version"]},"then":{"properties":{"data":{"$ref":"#/$defs/legacy33/$defs/clipChoicesData"}}}}]}` | No / conditional | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.clip-choices.v1` |
| `org.ostf.localization.v1` | `{"allOf":[{"$ref":"#/$defs/legacy33/$defs/extension"},{"if":{"properties":{"version":{"const":"1.0.0"}},"required":["version"]},"then":{"properties":{"data":{"$ref":"#/$defs/legacy33/$defs/localizationData"}}}}]}` | No / conditional | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.localization.v1` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "propertyNames": {
    "pattern": "^[a-z][a-z0-9-]*(?:\\.[a-z][a-z0-9-]*){2,}$",
    "not": {
      "pattern": "[\\r\\n\\u2028\\u2029]"
    }
  },
  "properties": {
    "org.ostf.relative-phrase.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/relativeData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.generation-context.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/generationData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.appearance.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/appearanceData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.legacy-import.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/legacyData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.phrase-library.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/phraseLibraryData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.clip-choices.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/clipChoicesData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.localization.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/localizationData"
              }
            }
          }
        }
      ]
    }
  },
  "additionalProperties": {
    "$ref": "#/$defs/legacy33/$defs/extension"
  }
}
```

<a id="schema-b373e44b1698"></a>
## Legacy / phraseTemplate

`#/$defs/legacy33/$defs/phraseTemplate`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/0/id` |
| `duration` | `{"$ref":"#/$defs/legacy33/$defs/positive"}` | Yes | Positive duration in ticks. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/0/duration` |
| `notes` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/phraseSourceNote"}}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/0/notes` |
| `name` | `{"type":"string"}` | No / conditional | Authored display name; never an identity or executable instruction. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/0/name` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/phraseSourceNote"
      }
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "duration",
    "notes"
  ],
  "additionalProperties": false
}
```

<a id="schema-44d3bca2e7c7"></a>
## Legacy / phraseNoteMapping

`#/$defs/legacy33/$defs/phraseNoteMapping`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `templateNoteId` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/noteMap/0/templateNoteId` |
| `repeatIndex` | `{"$ref":"#/$defs/legacy33/$defs/nonnegative"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/noteMap/0/repeatIndex` |
| `noteId` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/noteMap/0/noteId` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "templateNoteId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "repeatIndex": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "noteId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    }
  },
  "required": [
    "templateNoteId",
    "repeatIndex",
    "noteId"
  ],
  "additionalProperties": false
}
```

<a id="schema-3d626178543f"></a>
## Legacy / phraseInstance

`#/$defs/legacy33/$defs/phraseInstance`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/id` |
| `templateId` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/templateId` |
| `clipId` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/clipId` |
| `repeatCount` | `{"$ref":"#/$defs/legacy33/$defs/positive"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/repeatCount` |
| `transpose` | `{"type":"integer","minimum":-127,"maximum":127}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/transpose` |
| `noteMap` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/phraseNoteMapping"}}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/noteMap` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "templateId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "clipId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "repeatCount": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "transpose": {
      "type": "integer",
      "minimum": -127,
      "maximum": 127
    },
    "noteMap": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/phraseNoteMapping"
      }
    }
  },
  "required": [
    "id",
    "templateId",
    "clipId",
    "repeatCount",
    "transpose",
    "noteMap"
  ],
  "additionalProperties": false
}
```

<a id="schema-a52806e307ba"></a>
## Legacy / phraseLibraryData

`#/$defs/legacy33/$defs/phraseLibraryData`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `templates` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/phraseTemplate"}}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates` |
| `instances` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/phraseInstance"}}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "templates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/phraseTemplate"
      }
    },
    "instances": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/phraseInstance"
      }
    }
  },
  "required": [
    "templates",
    "instances"
  ],
  "additionalProperties": false
}
```

<a id="schema-d66fe864df92"></a>
## Legacy / clipCandidate

`#/$defs/legacy33/$defs/clipCandidate`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.clip-choices.v1/data/groups/0/candidates/0/id` |
| `clipIds` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/id"},"uniqueItems":true}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.clip-choices.v1/data/groups/0/candidates/0/clipIds` |
| `name` | `{"type":"string"}` | No / conditional | Authored display name; never an identity or executable instruction. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.clip-choices.v1/data/groups/0/candidates/0/name` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "clipIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "uniqueItems": true
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "clipIds"
  ],
  "additionalProperties": false
}
```

<a id="schema-7f4e9208b732"></a>
## Legacy / clipChoiceGroup

`#/$defs/legacy33/$defs/clipChoiceGroup`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.clip-choices.v1/data/groups/0/id` |
| `candidates` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/clipCandidate"},"minItems":1}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.clip-choices.v1/data/groups/0/candidates` |
| `selectedCandidateId` | `{"anyOf":[{"$ref":"#/$defs/legacy33/$defs/id"},{"type":"null"}]}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.clip-choices.v1/data/groups/0/selectedCandidateId` |
| `name` | `{"type":"string"}` | No / conditional | Authored display name; never an identity or executable instruction. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.clip-choices.v1/data/groups/0/name` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "candidates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/clipCandidate"
      },
      "minItems": 1
    },
    "selectedCandidateId": {
      "anyOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        {
          "type": "null"
        }
      ]
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "candidates",
    "selectedCandidateId"
  ],
  "additionalProperties": false
}
```

<a id="schema-b00cf26c6c42"></a>
## Legacy / clipChoicesData

`#/$defs/legacy33/$defs/clipChoicesData`

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `groups` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/clipChoiceGroup"}}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.clip-choices.v1/data/groups` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "groups": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/clipChoiceGroup"
      }
    }
  },
  "required": [
    "groups"
  ],
  "additionalProperties": false
}
```

<a id="schema-80fae39efba5"></a>
## Legacy / midiMapping

`#/$defs/legacy33/$defs/midiMapping`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `standard` | `{"enum":["gm1","custom"]}` | Yes | gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number. | Conditional/archival definition; see exact constraints. |
| `note` | `{"$ref":"#/$defs/legacy33/$defs/pitch"}` | Yes | MIDI1 note number in 0..127; for gm1 restrict to 35..81. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "standard": {
      "enum": [
        "gm1",
        "custom"
      ],
      "description": "gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number."
    },
    "note": {
      "$ref": "#/$defs/legacy33/$defs/pitch",
      "description": "MIDI1 note number in 0..127; for gm1 restrict to 35..81."
    }
  },
  "required": [
    "standard",
    "note"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "standard": {
            "const": "gm1"
          }
        },
        "required": [
          "standard"
        ]
      },
      "then": {
        "properties": {
          "note": {
            "type": "integer",
            "minimum": 35,
            "maximum": 81
          }
        }
      }
    }
  ]
}
```

<a id="schema-5036418e8e2b"></a>
## Legacy / soundSource

`#/$defs/legacy33/$defs/soundSource`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

Optional informational rendering class or opaque destination hint. Program Change, Bank Select and plugin presets are not standardized by Core.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `kind` | `{"enum":["unassigned","gm1","externalMidi","plugin","hostManaged"]}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `identifier` | `{"type":"string","minLength":1}` | No / conditional | Opaque target identifier, e.g. URI, plug-in identifier or port alias, not a loading command. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "Optional informational rendering class or opaque destination hint. Program Change, Bank Select and plugin presets are not standardized by Core.",
  "properties": {
    "kind": {
      "enum": [
        "unassigned",
        "gm1",
        "externalMidi",
        "plugin",
        "hostManaged"
      ]
    },
    "identifier": {
      "type": "string",
      "minLength": 1,
      "description": "Opaque target identifier, e.g. URI, plug-in identifier or port alias, not a loading command."
    }
  },
  "required": [
    "kind"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "kind": {
            "enum": [
              "gm1",
              "unassigned"
            ]
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "not": {
          "required": [
            "identifier"
          ]
        }
      }
    }
  ]
}
```

<a id="schema-7039e6a853e2"></a>
## Legacy / localizedNames

`#/$defs/legacy33/$defs/localizedNames`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically.


### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "minProperties": 1,
  "propertyNames": {
    "type": "string",
    "pattern": "^(?:[A-Za-z]{2,3}|[A-Za-z]{5,8})(?:-[A-Za-z0-9]{2,8})*$"
  },
  "additionalProperties": {
    "type": "string",
    "minLength": 1
  },
  "description": "Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically."
}
```

<a id="schema-fd9a025522cc"></a>
## Legacy / drumKit

`#/$defs/legacy33/$defs/drumKit`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | Conditional/archival definition; see exact constraints. |
| `name` | `{"type":"string"}` | Yes | Authored display name; never an identity or executable instruction. | Conditional/archival definition; see exact constraints. |
| `localizedNames` | `{"$ref":"#/$defs/legacy33/$defs/localizedNames"}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `soundSlotIds` | `{"type":"array","uniqueItems":true,"items":{"$ref":"#/$defs/legacy33/$defs/id"}}` | Yes | Ordered, unique references to global soundSlots; may be empty. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames"
    },
    "soundSlotIds": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "description": "Ordered, unique references to global soundSlots; may be empty."
    }
  },
  "required": [
    "id",
    "name",
    "soundSlotIds"
  ],
  "additionalProperties": false
}
```

<a id="schema-475dcf47369e"></a>
## Legacy / phraseSourceNote

`#/$defs/legacy33/$defs/phraseSourceNote`

Version-frozen 1.0.0-draft.1 phrase source note. Does NOT admit velocity; a linked Core instance may independently set velocity.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/0/notes/0/id` |
| `start` | `{"$ref":"#/$defs/legacy33/$defs/signed"}` | Yes | Start in the owner-defined time domain; see the manual. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/0/notes/0/start` |
| `duration` | `{"$ref":"#/$defs/legacy33/$defs/positive"}` | Yes | Positive duration in ticks. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/0/notes/0/duration` |
| `pitch` | `{"$ref":"#/$defs/legacy33/$defs/pitch"}` | No / conditional | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/0/notes/0/pitch` |
| `soundSlotId` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | No / conditional | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/1/notes/0/soundSlotId` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "pitch": {
      "$ref": "#/$defs/legacy33/$defs/pitch"
    },
    "soundSlotId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    }
  },
  "required": [
    "id",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "required": [
        "pitch"
      ],
      "not": {
        "required": [
          "soundSlotId"
        ]
      }
    },
    {
      "required": [
        "soundSlotId"
      ],
      "not": {
        "required": [
          "pitch"
        ]
      }
    }
  ],
  "description": "Version-frozen 1.0.0-draft.1 phrase source note. Does NOT admit velocity; a linked Core instance may independently set velocity."
}
```

<a id="schema-57f91803a575"></a>
## Legacy / voicing

`#/$defs/legacy33/$defs/voicing`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `pitches` | `{"type":"array","minItems":1,"items":{"$ref":"#/$defs/legacy33/$defs/pitch"}}` | Yes | Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed. | Conditional/archival definition; see exact constraints. |
| `velocities` | `{"type":"array","minItems":1,"items":{"anyOf":[{"type":"integer","minimum":1,"maximum":127},{"type":"null"}]}}` | No / conditional | Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.",
  "properties": {
    "pitches": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/legacy33/$defs/pitch"
      },
      "description": "Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed."
    },
    "velocities": {
      "type": "array",
      "minItems": 1,
      "items": {
        "anyOf": [
          {
            "type": "integer",
            "minimum": 1,
            "maximum": 127
          },
          {
            "type": "null"
          }
        ]
      },
      "description": "Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic."
    }
  },
  "required": [
    "pitches"
  ]
}
```

<a id="schema-c1506d82e789"></a>
## Legacy / contributor

`#/$defs/legacy33/$defs/contributor`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | Conditional/archival definition; see exact constraints. |
| `name` | `{"type":"string","minLength":1}` | Yes | Authored display name; never an identity or executable instruction. | Conditional/archival definition; see exact constraints. |
| `kind` | `{"enum":["person","organization","other"]}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `localizedNames` | `{"$ref":"#/$defs/legacy33/$defs/localizedNames"}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "kind": {
      "enum": [
        "person",
        "organization",
        "other"
      ]
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames"
    }
  },
  "required": [
    "id",
    "name"
  ]
}
```

<a id="schema-dfb18f087d21"></a>
## Legacy / credit

`#/$defs/legacy33/$defs/credit`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | Conditional/archival definition; see exact constraints. |
| `contributorId` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `role` | `{"type":"string","pattern":"^[a-z][a-z0-9.-]*$"}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |
| `label` | `{"type":"string"}` | No / conditional | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "contributorId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "role": {
      "type": "string",
      "pattern": "^[a-z][a-z0-9.-]*$"
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "contributorId",
    "role"
  ]
}
```

<a id="schema-776d222783e2"></a>
## Legacy / alternateTitle

`#/$defs/legacy33/$defs/alternateTitle`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

Stable-ID song title alternative; array position and title text do not identify it.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable identity; distinguish definition from reference by its owner. | Conditional/archival definition; see exact constraints. |
| `title` | `{"type":"string","minLength":1}` | Yes | See the owning object semantics and exact constraints below. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Stable-ID song title alternative; array position and title text do not identify it.",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "title": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "title"
  ]
}
```

<a id="schema-dd0a6f194be8"></a>
## Legacy / languageMap32

`#/$defs/legacy33/$defs/languageMap32`

Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank.


### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "minProperties": 1,
  "propertyNames": {
    "type": "string",
    "pattern": "^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*$"
  },
  "additionalProperties": {
    "type": "string"
  },
  "description": "Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank."
}
```

<a id="schema-5443a9c8e25b"></a>
## Legacy / localizationTarget

`#/$defs/legacy33/$defs/localizationTarget`

Stable target by Core ID or profile-local scoped ID; song is the only ID-less target. No array indexes or mutable names as locators.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `kind` | `{"enum":["song","alternateTitle","contributor","credit","section","track","clip","soundSlot","drumKit","lyricDocument","resource","phraseTemplate","clipCandidate","clipChoiceGroup","roleDefinition","genre"]}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.localization.v1/data/entries/0/target/kind` |
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | No / conditional | Stable identity; distinguish definition from reference by its owner. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.localization.v1/data/entries/0/target/id` |
| `profile` | `{"type":"string","enum":["org.ostf.phrase-library.v1","org.ostf.clip-choices.v1","org.ostf.appearance.v1"]}` | No / conditional | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.localization.v1/data/entries/0/target/profile` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "kind": {
      "enum": [
        "song",
        "alternateTitle",
        "contributor",
        "credit",
        "section",
        "track",
        "clip",
        "soundSlot",
        "drumKit",
        "lyricDocument",
        "resource",
        "phraseTemplate",
        "clipCandidate",
        "clipChoiceGroup",
        "roleDefinition",
        "genre"
      ]
    },
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "profile": {
      "type": "string",
      "enum": [
        "org.ostf.phrase-library.v1",
        "org.ostf.clip-choices.v1",
        "org.ostf.appearance.v1"
      ]
    }
  },
  "required": [
    "kind"
  ],
  "allOf": [
    {
      "if": {
        "properties": {
          "kind": {
            "const": "song"
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "not": {
          "anyOf": [
            {
              "required": [
                "id"
              ]
            },
            {
              "required": [
                "profile"
              ]
            }
          ]
        }
      },
      "else": {
        "required": [
          "id"
        ]
      }
    },
    {
      "if": {
        "properties": {
          "kind": {
            "enum": [
              "phraseTemplate",
              "clipCandidate",
              "clipChoiceGroup",
              "roleDefinition"
            ]
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "required": [
          "profile"
        ]
      },
      "else": {
        "not": {
          "required": [
            "profile"
          ]
        }
      }
    }
  ],
  "description": "Stable target by Core ID or profile-local scoped ID; song is the only ID-less target. No array indexes or mutable names as locators."
}
```

<a id="schema-8918b9a525df"></a>
## Legacy / localizationEntry

`#/$defs/legacy33/$defs/localizationEntry`

Independent translations for one stable source field. Original source text remains authoritative as fallback.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `target` | `{"$ref":"#/$defs/legacy33/$defs/localizationTarget"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.localization.v1/data/entries/0/target` |
| `field` | `{"type":"string","minLength":1}` | Yes | Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.localization.v1/data/entries/0/field` |
| `values` | `{"$ref":"#/$defs/legacy33/$defs/languageMap32"}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.localization.v1/data/entries/0/values` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "target": {
      "$ref": "#/$defs/legacy33/$defs/localizationTarget"
    },
    "field": {
      "type": "string",
      "minLength": 1,
      "description": "Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields."
    },
    "values": {
      "$ref": "#/$defs/legacy33/$defs/languageMap32"
    }
  },
  "required": [
    "target",
    "field",
    "values"
  ],
  "description": "Independent translations for one stable source field. Original source text remains authoritative as fallback."
}
```

<a id="schema-3a6707a441dd"></a>
## Legacy / localizationData

`#/$defs/legacy33/$defs/localizationData`

Language-map translations indexed by stable kind/id/field, never by names or array positions.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `entries` | `{"type":"array","items":{"$ref":"#/$defs/legacy33/$defs/localizationEntry"}}` | Yes | See the owning object semantics and exact constraints below. | [03-all-legacy-profiles.ostf](../examples/03-all-legacy-profiles.ostf)<br>`/extensions/org.ostf.localization.v1/data/entries` |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "entries": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/localizationEntry"
      }
    }
  },
  "required": [
    "entries"
  ],
  "description": "Language-map translations indexed by stable kind/id/field, never by names or array positions."
}
```

<a id="schema-7ec55152a967"></a>
## Legacy / genre

`#/$defs/legacy33/$defs/genre`

**Archive-only definition: not reachable from the current 4.2 root; excluded from the active demo-coverage denominator.**

One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.

| Field | Type / constraints | Direct required | Schema description | Example / pointer |
|---|---|---|---|---|
| `id` | `{"$ref":"#/$defs/legacy33/$defs/id"}` | Yes | Stable song-local ID unique among all Core objects. | Conditional/archival definition; see exact constraints. |
| `name` | `{"type":"string","minLength":1}` | Yes | Original Unicode genre label, never normalized or rewritten during import. | Conditional/archival definition; see exact constraints. |
| `externalUri` | `{"type":"string","minLength":1,"format":"uri"}` | No / conditional | Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced. | Conditional/archival definition; see exact constraints. |

### Exact structure, conditions and ranges

```json
{
  "type": "object",
  "description": "One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id",
      "description": "Stable song-local ID unique among all Core objects."
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "description": "Original Unicode genre label, never normalized or rewritten during import."
    },
    "externalUri": {
      "type": "string",
      "minLength": 1,
      "format": "uri",
      "description": "Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```
