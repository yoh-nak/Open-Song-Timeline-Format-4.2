# OSTF 4.2.0 — デモファイル全ガイド

全53ファイルが拡張子`.ostf`、UTF-8 JSON、`version: "4.2.0"`です。01〜50はパラメーターと交換条件を示す技術例、51〜53は構成と演奏が連続したオリジナル楽曲デモです。技術例を自然な演奏・歌声の保証と誤解しないでください。

最初に見るファイルは01（継承Core総合）、02（歌唱追加の全フィールド）、51（32小節Pop歌唱）です。03の旧形式プロファイルは保存用の例であり、共通情報を新規に独自拡張へ格納する推奨ではありません。Coreを正本とします。

16の多対多Alignment、17のTick丸め、18の同Tick順序未指定は、Schemaには適合しても外部形式へ出す前に解決が必要な例です。エラーのあるファイルを正常デモとして紛れ込ませたものではありません。

02の独自音素体系は`com.example.demo.phonemes`という説明用名前空間で、実在のVoicebank用辞書ではありません。51の英語歌詞は新規の短いオリジナル文です。テンポや音符の値はデモの著者値で、実際の音声合成結果を保証しません。

| No. | ファイル / 曲名 | 分類 |
|---|---|---|
| 01 | [OSTF 4.2 Complete Core Reference](../examples/01-all-core.ostf) | パラメーター技術例 |
| 02 | [All Vocal Parameters — Namespaces and Expression](../examples/02-all-vocal-parameters.ostf) | パラメーター技術例 |
| 03 | [Legacy Profile Preservation — All Defined Fields](../examples/03-all-legacy-profiles.ostf) | パラメーター技術例 |
| 04 | [OSTF 4.2 Basic Vocal Exchange](../examples/04-basic-vocal.ostf) | 歌唱交換の技術例 |
| 05 | [Wind / 風 — expressive voice example](../examples/05-expressive-vocal.ostf) | 歌唱交換の技術例 |
| 06 | [Instrumental Melody — no vocals](../examples/06-instrument-midi-unchanged.ostf) | 歌唱交換の技術例 |
| 07 | [Lead + Harmony — separate vocal voices](../examples/07-multivoice-same-lyrics.ostf) | 歌唱交換の技術例 |
| 08 | [Wordless vocal phrase — noteIds only](../examples/08-wordless-humming.ostf) | 歌唱交換の技術例 |
| 09 | [Two vocal parts on one logical Track](../examples/09-two-voices-one-track.ostf) | 歌唱交換の技術例 |
| 10 | [Same unit with IPA and X-SAMPA variants](../examples/10-parallel-phonetic-alphabets.ostf) | 歌唱交換の技術例 |
| 11 | [A note-specific dynamics override](../examples/11-note-expression-override.ostf) | 歌唱交換の技術例 |
| 12 | [Melisma: one lyric unit on two notes](../examples/12-melisma.ostf) | 歌唱交換の技術例 |
| 13 | [Anticipated consonant before note](../examples/13-pre-note-consonant.ostf) | 歌唱交換の技術例 |
| 14 | [Synth lead plus independent sung melody](../examples/14-instrument-and-vocal.ostf) | 歌唱交換の技術例 |
| 15 | [Same-tick phonemes with explicit deterministic order](../examples/15-phoneme-same-tick-order.ostf) | 歌唱交換の技術例 |
| 16 | [Ambiguous many-to-many lyrics requires export resolution](../examples/16-ambiguous-many-to-many.ostf) | 歌唱交換の技術例 |
| 17 | [One-tick breath collapsed by 960 to 480 PPQ simulation](../examples/17-tick-rounding-loss.ostf) | 歌唱交換の技術例 |
| 18 | [Same-tick phonemes without explicit order; valid but ambiguous to export](../examples/18-same-tick-implicit-order.ostf) | 歌唱交換の技術例 |
| 19 | [Wind / 風 — tempo-change vocal example](../examples/19-tempo-change-vocal.ostf) | 歌唱交換の技術例 |
| 20 | [Meter Shift / 拍子の変化 — 4/4 to 3/4 vocal example](../examples/20-meter-change-vocal.ostf) | 歌唱交換の技術例 |
| 21 | [Single Late Pitch Anchor Conformance](../examples/21-single-late-pitch-anchor.ostf) | 歌唱交換の技術例 |
| 22 | [OSTF 4.2 — consonant before next note](../examples/22-pre-note-consonant.ostf) | 歌唱交換の技術例 |
| 23 | [MPE Per Note Expression](../examples/23-mpe-per-note-expression.ostf) | パラメーター技術例 |
| 24 | [Pitch Range Direction](../examples/24-pitch-range-high-register.ostf) | パラメーター技術例 |
| 25 | [Integrated Jazz Session](../examples/25-integrated-jazz-session.ostf) | パラメーター技術例 |
| 26 | [Poly Pressure](../examples/26-poly-pressure.ostf) | パラメーター技術例 |
| 27 | [Generation Intent](../examples/27-generation-intent.ostf) | パラメーター技術例 |
| 28 | [Channel Mode](../examples/28-channel-mode.ostf) | パラメーター技術例 |
| 29 | [Vendor Range Direction](../examples/29-vendor-range-direction.ostf) | パラメーター技術例 |
| 30 | [Bank Program Change](../examples/30-bank-select-program-change.ostf) | パラメーター技術例 |
| 31 | [Effective Key Scale](../examples/31-effective-key-scale.ostf) | パラメーター技術例 |
| 32 | [Document Identity](../examples/32-document-identity-revision.ostf) | パラメーター技術例 |
| 33 | [Chord Voicing](../examples/33-chord-voicing.ostf) | パラメーター技術例 |
| 34 | [External MIDI Sound Source](../examples/34-sound-source-external-midi.ostf) | パラメーター技術例 |
| 35 | [Provenance](../examples/35-provenance.ostf) | パラメーター技術例 |
| 36 | [Localized Names](../examples/36-localized-names.ostf) | パラメーター技術例 |
| 37 | [Note Performance State](../examples/37-note-performance-state.ostf) | パラメーター技術例 |
| 38 | [Note Probability](../examples/38-note-probability-deviation.ostf) | パラメーター技術例 |
| 39 | [Sound Slot Mappings](../examples/39-sound-slot-midi-mapping.ostf) | パラメーター技術例 |
| 40 | [Meter Map](../examples/40-meter-map.ostf) | パラメーター技術例 |
| 41 | [Bar Origin](../examples/41-bar-origin.ostf) | パラメーター技術例 |
| 42 | [Slash Chord](../examples/42-slash-chord.ostf) | パラメーター技術例 |
| 43 | [Timed Harmony Scales](../examples/43-timed-harmony-scales.ostf) | パラメーター技術例 |
| 44 | [Fixed Trigger](../examples/44-fixed-trigger-note.ostf) | パラメーター技術例 |
| 45 | [Lyrics Pronunciation](../examples/45-lyrics-pronunciation.ostf) | パラメーター技術例 |
| 46 | [Contributors Credits](../examples/46-contributors-credits.ostf) | パラメーター技術例 |
| 47 | [Rights](../examples/47-rights-statement.ostf) | パラメーター技術例 |
| 48 | [Genres Moods](../examples/48-genres-moods.ostf) | パラメーター技術例 |
| 49 | [Generation Process](../examples/49-generation-process.ostf) | パラメーター技術例 |
| 50 | [Song Scale Improvisation](../examples/50-song-scale-improvisation.ostf) | パラメーター技術例 |
| 51 | [Light We Make](../examples/51-musical-pop-vocal.ostf) | 楽曲デモ · 32 bars · 108 BPM |
| 52 | [Evening Turns](../examples/52-musical-jazz-quartet.ostf) | 楽曲デモ · 24 bars · 124 BPM |
| 53 | [Signal Garden](../examples/53-musical-electronic.ostf) | 楽曲デモ · 32 bars · 126 BPM |

**掲載範囲:** [全項目網羅表](PARAMETER_COVERAGE.md)を参照。外部ソフトの再生・読み込み・歌声品質は未検証です。
