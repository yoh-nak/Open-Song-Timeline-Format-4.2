# OSTF 4.2.0 — 全網羅マニュアル 正式版

本書は **Open Song Timeline Format (OSTF) 4.2.0** を、作成・読込・再生・表示・編集・マージ・移行・検証するための総合実装マニュアルです。

OSTF 4.2.0 の正本は次の3層です。

1. **構造の正本** — `schema/ostf-4.2.0.schema.json`
2. **意味規則の正本** — `docs/SPECIFICATION.ja.md`
3. **全フィールドの型・必須性・値域** — `docs/PARAMETER_REFERENCE.ja.md`

本書はそれらを横断し、「実装するときに何をどの順番で扱うか」「どこを推測してはいけないか」「OSTF 3.xと4.0をどう共存させるか」を実務的に説明します。

---

## 1. OSTF 4.2の位置付け

OSTFはDAWプロジェクト形式ではありません。曲の意味と時間構造を、DAWやアプリケーションに依存せず交換するためのJSONフォーマットです。

OSTF 3.5までに扱っていた主な情報は次の通りです。

- 曲名・ジャンル・ムード・言語
- Key / Scale / Key Change
- Tempo / Meter / Section
- Chord / Scale context / Voicing
- Track / Clip / Note
- Drum Kit / Sound Slot
- Lyrics / Phrase / Unit / Alignment
- Credits / Rights / Resources
- Relative Phrase / Generation / Presentation
- Phrase Library / Clip Choice / Localization
- Document identity / Provenance

OSTF 4.2は4.1の全Coreを保持し、任意の音素候補・Voice Profile・VocalPerformanceを加えます。4.1は4.0にTrack Directionsを追加した版です。4.0では次がCoreへ追加されました。

- MIDI Channel 1–16
- Logical MIDI Bus
- `singleChannel` / `multiChannel` / `mpe`
- Control Change
- Channel Mode
- Program Change
- Bank Select（CC 0 / CC 32）
- 14-bit Pitch Bend
- Channel Pressure
- Polyphonic Key Pressure
- MPE Lower / Upper Zone
- per-note expressionと`targetNoteId`
- 同一tick MIDI Event順序
- 複数Melody Track
- 複数Lyric Voice
- Voice-specific Lyric Alignment

したがって4.1も、OSTF 3.5/4.0の曲構造を捨てて別形式へ置き換える版ではありません。

**OSTF 4.1 = OSTF 4.0 + Track Directions / Instrument Playable Pitch Capability**

です。

---

## 2. OSTF 4.1が扱わないもの

4.1.0 Coreでも次を標準化しません。

- 物理MIDI Port名
- USB MIDI device ID
- Ableton Live / Cubase等のTrack番号
- Audio routing
- Mixer state
- Plugin instance / plugin state
- VST/AUパラメーター一般
- Audio Clip
- SysEx
- MIDI Clock
- MIDI Time Code
- MIDI Machine Control
- MIDI Show Control
- MIDI 2.0 UMP / 32-bit Per-Note Controller

Logical MIDI BusはPortableな曲情報ですが、そのBusを「このPCのどの実機Portへ出すか」はHost設定です。

---

## 3. ファイル形式

推奨拡張子は `.ostf` です。

内容はUTF-8 JSON object一つです。

最小ルート概念：

```json
{
  "format": "OSTF",
  "version": "4.2.0",
  "ppq": 960,
  "song": {},
  "timeline": {},
  "harmony": {},
  "tracks": [],
  "soundSlots": [],
  "lyrics": {},
  "resources": []
}
```

実際の必須フィールドと型はSchemaを正本とします。

### 3.1 Root必須項目

4.1でも次の10項目を必須とし、3.5/4.0の基本形を維持します。

- `format`
- `version`
- `ppq`
- `song`
- `timeline`
- `harmony`
- `tracks`
- `soundSlots`
- `lyrics`
- `resources`

4.0で追加されたroot `midi`は任意です。MIDI演奏表現を使用しない曲へ空の`midi`を強制してはいけません。

### 3.2 バージョン

本版の文書は`format: "OSTF"`、`version: "4.2.0"`とします。4.1だけを理解するReaderが4.2を4.1として扱ってはいけません。4.2を理解するReaderも将来の4.3/5.xを既知とみなしてはいけません。旧版は対応するSchema/意味規則を選び、明示的な移行操作を除いて版を変更しません。

## 4. PPQと時間

OSTFの時間は整数tickです。

`ppq`は四分音符あたりのtick数です。

同じ曲内で、Tempo、Meter、Section、Chord、Clip、Note、Lyric Alignment、MIDI Eventなどは同じPPQ空間を共有します。

### 4.1 Global timeとClip-local time

代表的に、

- `clip.start` — global tick
- `note.start` — clip-local tick
- `midiEvent.start` — clip-local tick

です。

Noteのglobal onsetは、

```text
clip.start + note.start
```

MIDI Eventのglobal timeも、

```text
clip.start + midiEvent.start
```

です。

Clip-local `start`は一部の仕様で負値を許します。これは弱起やpre-roll的なEventを表すためのもので、Feature Fixtureで例示しています。

### 4.2 PPQ変換

異なるPPQの文書をマージする場合は、有理時間を壊さない共通PPQへ正確に変換します。

丸めが必要な場合、黙ってtickを丸めてはいけません。

---

## 5. IDと参照

OSTFはStable IDを多用します。

IDは表示名ではありません。

- Track名が同じでも別Trackになり得る
- Contributor名が同じでも別人として保持できる
- MIDI Bus名が同じでも別Busになり得る

Reader/Writerは、名前の一致だけでIDを統合してはいけません。

4.0で参照対象に加わった重要IDに加え、4.1では`trackDirection`がCore参照対象に加わります。

4.0で追加された重要ID：

- `midiBus`
- `midiEvent`
- `lyricVoice`

`targetNoteId`、`busId`、`trackId`、`documentId`等は実在対象へ解決する必要があります。

---

## 6. Song metadata

`song.title`は曲の基本表示名です。

その他のmetadataは「分からない場合は省略」が原則です。

推測して、

- C major
- 120 BPM
- Pop
- English

などを書き足してはいけません。

主要項目：

- `title`
- `subtitle`
- `description`
- `localizedTitles`
- `alternateTitles`
- `credits`
- `genres`
- `key`
- `scale`
- `languages`
- `primaryLyricDocumentId`
- `moods`
- `rights`
- `primaryMelodyTrackId`
- `melodyTrackIds`

### 6.1 Primary Melodyと複数Melody

`primaryMelodyTrackId`はPrimary Melodyの正本です。

4.0の`melodyTrackIds`は、曲に含まれる複数のMelody-bearing Track集合を明示します。

例：

```json
{
  "primaryMelodyTrackId": "lead-vocal",
  "melodyTrackIds": [
    "lead-vocal",
    "counter-melody",
    "harmony-high"
  ]
}
```

配列の先頭をPrimaryと自動推測してはいけません。

---

## 7. Genre / Mood / Language

GenreとMoodはopen-endedです。

固定の「OSTF公式ジャンル表」へ強制変換しません。

GenreやMoodの配列順は著者の表示順として保持します。

Language tagは著者情報を保持し、未知tagを勝手に別tagへ修正しません。

---

## 8. Credits / Contributors / Rights

`contributors`は人物・組織等のidentity recordです。

`song.credits`はContributorと役割の関係です。

役割例：

- composer
- lyricist
- arranger
- performer
- data-editor
- software-developer

同名を理由にContributorを統合してはいけません。

`song.rights`は権利表示を保持しますが、OSTFへの記載自体が権利認証になるわけではありません。

---

## 9. Timeline

`timeline`は曲全体の時間構造です。

主な要素：

- `sections`
- `tempoChanges`
- `meterChanges`
- `keyChanges`
- `duration`
- `barOrigin`

### 9.1 Section

SectionはIntro / Verse / Chorus等の曲構成を時間範囲で表します。

本版の3曲の楽曲デモでは、Sectionを曲頭から曲末まで連続して配置しています。個別技術例は短い確認用途なので、曲としての連続構成を必須にしません。

名前だけから意味を決めず、必要なら`role`を使います。

### 9.2 Tempo

TempoはBPMとして保存します。

Tempo Changeが複数ある場合、時系列で解釈します。

### 9.3 Meter

Meterはnumerator / denominatorです。

変拍子では`beatGroups`を使用できます。

例：7/8を2+2+3として扱う場合、

```json
{
  "numerator": 7,
  "denominator": 8,
  "beatGroups": [2, 2, 3]
}
```

### 9.4 barOrigin

弱起等で小節起点が0 tickと一致しない場合に利用します。

---

## 10. Key / Key Change / Scale

OSTFではKeyとScale Contextを分離します。

- `song.key` — 初期／全体Key
- `timeline.keyChanges` — 時間付きKey Change
- `song.scale` — 全体Scale definition
- `harmony.scales` — 時間付き局所Scale Context

Key labelだけで音楽的な値を推測しない実装が安全です。

移調時は、

- Chord
- musical Note
- Key
- Scale context
- Lyric text以外の関連pitch情報

を一貫して扱い、`fixedTrigger`は移調しません。

---

## 11. Harmony

`harmony`は、

- `chords`
- `scales`

を持ちます。

### 11.1 Chord

Chordはlabelを持ち、必要なら構造化された、

- root
- intervals
- bass
- voicing

を持てます。

LabelだけのChordも有効です。

### 11.2 Voicing

Chord `voicing`は和声スナップショットです。

Track内のConcrete Noteを自動生成する命令ではありません。

Chord Voicingと演奏Noteを二重正本にしないでください。

### 11.3 Golden Demo

Golden DemoではChord timelineのgap/overlapが0であることを監査しています。

---

## 12. Track

Trackは演奏パートの上位単位です。

代表項目：

- `id`
- `name`
- `role`
- `instrument`
- `trackType`
- `enabled`
- `clips`
- `midi`（4.0）

Track名だけで役割を推測しないでください。

---

## 13. Clip

ClipはTrack内の時間配置単位です。

代表項目：

- `id`
- `name`
- `start`
- `duration`
- `enabled`
- `notes`
- `midiEvents`（4.0）

Clipがdisabledなら、そのClipのNoteだけでなくMIDI Eventもscheduleしないのが4.0の重要な規則です。

---

## 14. Note

NoteはOSTFのConcrete Performance Noteです。

Note On / Note Offを別のMIDI Eventへ二重保存しません。

Noteは、

- `pitch`
- または` soundSlotId`

のどちらか一方を演奏対象として持ちます。

代表項目：

- `id`
- `start`
- `duration`
- `pitch`
- `soundSlotId`
- `velocity`
- `releaseVelocity`
- `enabled`
- `probability`
- `velocityDeviation`
- `pitchRole`
- `channel`（4.0）

### 14.1 velocity

Note On Velocityです。

省略は「未指定」であり、Writerが既定値を勝手に書き戻してはいけません。

### 14.2 releaseVelocity

Note Off / Release Velocityです。

### 14.3 enabled

falseならNoteを保持したまま発音抑制します。

### 14.4 probability

0.0–1.0の再生確率です。

乱数列そのものは標準化しません。

### 14.5 velocityDeviation

Velocityの変動幅です。

`velocity`が存在する場合だけ意味を持ちます。

### 14.6 pitchRole

- `musical`
- `fixedTrigger`

`fixedTrigger`はkeyswitch等の絶対MIDI Keyで、移調・Harmony分析対象にしません。

### 14.7 channel

4.0でConcrete Noteへ任意のMIDI Channelを追加しました。

---

## 15. Sound Slot / Drum Kit

打楽器や非音高トリガーは、安定した`soundSlotId`で表現できます。

Sound SlotとDrum Kitは、

- MIDI key mapping
- 音源識別
- percussion role

等の情報を曲内の安定した意味として扱うために使用します。

同じMIDI keyに複数Slotが存在しても、Slot IDが異なれば別の意味として保持できます。

---

## 16. Lyrics基本モデル

Lyricsは次の階層を持ちます。

```text
Lyric Document
  └─ Phrase
      └─ Unit
          └─ Alignment → Note
```

主な構造：

- `lyrics.documents`
- `lyrics.phrases`
- `lyrics.units`
- `lyrics.alignments`
- `lyrics.voices`（4.0）

Lyric textをNoteへ直接埋め込む方式にはしません。

---

## 17. Lyric Document

Lyric Documentは一つの歌詞本文系列です。

LeadとHarmonyが同じ歌詞を歌う場合、同じDocumentを共有できます。

Call & Responseで別の歌詞を歌う場合、別Documentを使用できます。

---

## 18. Lyric Alignment

AlignmentはLyric UnitとNoteを対応付けます。

4.0では任意`voiceId`を追加できます。

これにより、

- 同じLyric Unit
- 別Voice
- 別Note

を正しく表現できます。

Golden Demoの歌ものでは、各Voiceが歌う全NoteをVoice-specific Alignmentで一度だけ参照することを監査しています。

---

## 19. Lyric Voice

4.0の`lyrics.voices`は、Vocal VoiceとTrack / Lyric Documentの関係を明示します。

例：

```json
{
  "id": "voice-high",
  "name": "High Harmony",
  "role": "harmony",
  "trackId": "vocal-high",
  "documentId": "lyrics-main"
}
```

推奨role例：

- lead
- harmony
- backing
- unison
- double
- counter
- adlib
- response

roleはopen stringであり、未知roleをReaderが拒否してはいけません。

---

## 20. Resources

`resources`は外部素材参照です。

kind例：

- audio
- midi
- text
- other

Resource URIを読み込んだだけで自動ダウンロード・実行してはいけません。

Resourceが取得不能でも、OSTF文書内のNote/Chordが不正になるわけではありません。

---

## 21. Legacy extensions

OSTF 4.0でも`extensions`は互換性やthird-party dataの保持に使用できます。

ただし、4.0 Coreとして標準化済みの情報を新たにextensionsだけへ保存してはいけません。

Coreが現在の正本です。

未知Extensionを理解できないWriterは、可能な限りlosslessに保持します。

---

## 22. Dependencies / status

Relative Phrase、Generation、Presentation、Phrase Library、Clip Choices、Localization等の共有編集情報はCore本体との依存状態を持ちます。

代表status：

- `current`
- `stale`
- `unverified`

`current`は「Coreと対応が一致している」という意味です。

「高品質」「最新アルゴリズム」「生成成功」を意味しません。

Coreを編集して関係が壊れたら、再計算するかstale/unverifiedへ変更します。

---

## 23. Relative Phrases

`relativePhrases`はConcrete NoteとChord/Scale Contextの相対関係を保持します。

代表概念：

- chordTone
- scaleDegree
- anchorPitch
- index
- chromaticOffset

これは現在のConcrete Noteを置き換える正本ではありません。

staleな相対情報でNoteを書き換えてはいけません。

---

## 24. Generation

`generation`は生成履歴・生成意図を保存します。

保存対象例：

- generator id/version
- inputs
- outputs
- targetRange
- intent
- seed
- protectedNoteIds

Promptを保存しても、それを自動外部送信する命令ではありません。

Generatorが違えばseedが同じでも同じ結果を保証しません。

---

## 25. Presentation

`presentation`は表示・役割のportableな補助情報です。

例：

- roleDefinitions
- sectionRoleAssignments
- appearance
- roleColors
- objectColors

色や名前から演奏意味を推測しません。

Presentationは音楽値の正本ではありません。

---

## 26. Phrase Library

`phraseLibrary`は再利用可能なPhrase TemplateとConcrete Clip/Noteの対応を保存します。

重要な分離：

- Template Source Note — 原型
- Concrete Track Note — 実際に鳴るNote

Source Note自体は発音しません。

4.0の`channel`はPhrase Source Noteへ追加しません。

MPE Channelは具体的なPerformance配置であり、Phrase原型ではないためです。

Phrase refresh時は存続Concrete Noteのchannelを保持します。

---

## 27. Clip Choices

`clipChoices`は複数候補Clipと選択状態を保持します。

読み込んだだけで候補を再抽選してはいけません。

4.0ではClip enabledがMIDI Eventにも適用されるため、無効候補からController/Programだけが漏れないようにします。

---

## 28. Localization

原文は通常フィールドが正本です。

翻訳はLocalization layerで保持します。

4.0では次も翻訳対象にできます。

- MIDI Bus name
- Lyric Voice name

翻訳で、

- ID
- role
- mode
- chord value
- musical pitch

等の意味を変えてはいけません。

---

## 29. Document identity

`document`は文書系列のidentityとrevisionを扱います。

代表概念：

- document id
- revisionId
- parents
- createdBy
- modifiedBy

同じ作業文書系列と、独立コピーを区別できます。

ID宣言だけで暗号学的真正性を保証するものではありません。

---

## 30. Provenance

`provenance`は履歴・由来の自己申告記録です。

action例：

- create
- import
- conversion
- edit
- transpose
- merge
- generation
- other

Provenanceは現在の音楽値より優先する正本ではありません。

---

# Part II — OSTF 4.0 MIDI Performance

## 31. MIDI Performance Layerの基本原則

4.0では、ControllerやProgram等をClipの`midiEvents[]`へ保存します。

対応Event：

- `controlChange`
- `channelMode`
- `programChange`
- `pitchBend`
- `channelPressure`
- `polyPressure`

Note On / Note Offは`notes[]`が正本です。

---

## 32. MIDI Channel

OSTF内のChannel値は **1–16** です。

Wire status nibbleの0–15ではありません。

### 32.1 singleChannel

Track全体の既定Channelを持ちます。

Note/Eventは必要に応じてTrack Channelを継承できます。

### 32.2 multiChannel

同一Track内で複数Channelを利用します。

Channel identityが必要なNote/Eventには具体Channelを持たせます。

### 32.3 mpe

MPE Zoneに従ってMember ChannelをNote単位に割り当てます。

---

## 33. Logical MIDI Bus

Root `midi.buses[]`で論理出力空間を定義します。

例：

```json
{
  "midi": {
    "buses": [
      { "id": "bus-main", "name": "Main MIDI" },
      { "id": "bus-synth", "name": "External Synth" }
    ]
  }
}
```

各Busは独立した16 Channel namespaceを持ちます。

したがって、

```text
Bus A / Ch 1
Bus B / Ch 1
```

は別の演奏先です。

Physical Port名は保存しません。

---

## 34. Track MIDI設定

Trackの`midi`は、

- `mode`
- `busId`
- `channel`
- `mpe`

を組み合わせます。

`busId`がないことは、文書が不正という意味ではありません。Host既定空間等の扱いは意味規則に従います。

---

## 35. Control Change

```json
{
  "id": "cc-1",
  "start": 960,
  "type": "controlChange",
  "controller": 74,
  "value": 96
}
```

範囲：

- controller: 0–119
- value: 0–127

120–127は`channelMode`です。

---

## 36. Bank Select

Bank SelectのOSTF独自bank fieldは作りません。

MIDI標準と同様、

1. CC 0 — Bank Select MSB
2. CC 32 — Bank Select LSB
3. Program Change

として保持します。

この順序が重要な場合は配列順や`order`を使用します。

---

## 37. Program Change

```json
{
  "type": "programChange",
  "program": 40
}
```

保存値は0–127です。

UIがProgram 1–128と表示しても、保存時にwire valueへ戻します。

---

## 38. Pitch Bend

Pitch Bendは14-bitです。

- min = 0
- center = 8192
- max = 16383

```json
{
  "type": "pitchBend",
  "value14": 8192
}
```

Pitch Bend Sensitivityは別状態です。

必要ならRPNをraw CC sequenceとして保存します。

---

## 39. Channel Pressure

Channel全体のAftertouchです。

```json
{
  "type": "channelPressure",
  "value": 80
}
```

valueは0–127です。

---

## 40. Polyphonic Key Pressure

特定PitchへのPoly Aftertouchです。

```json
{
  "type": "polyPressure",
  "pitch": 64,
  "value": 90
}
```

必要なら`targetNoteId`も付けます。

---

## 41. Channel Mode

CC 120–127相当は`channelMode`へ分離します。

これにより普通のcontinuous controllerと、

- All Sound Off
- Reset All Controllers
- Local Control
- All Notes Off
- Omni
- Mono/Poly

等を構造上区別できます。

---

## 42. RPN / NRPN

4.0.0では独立`rpn` / `nrpn` Event型を作りません。

通常のCC列としてlosslessに保持します。

Feature Fixtureに、

- Pitch Bend Sensitivity RPN
- NRPN raw sequence

の例があります。

---

## 43. targetNoteId

4.0では次のEventが任意`targetNoteId`を持てます。

- Control Change
- Pitch Bend
- Channel Pressure
- Poly Pressure

これは特にMPE/per-note expressionの意味関係を明示するために使います。

targeted Eventは対象Noteと同じTrack/Channel文脈を満たす必要があります。

Golden DemoではtargetNoteId付きEventが対象Noteの発音時間外に出ないことを監査しています。

---

## 44. Probabilityとtargeted Event

対象Noteが`probability`によりその回に鳴らなかった場合、targetNoteId付きper-note Eventも送らないのが安全な意味規則です。

対象Noteなしでper-note Bend/CCだけ送ると、同じChannel上の別Noteへ表現が漏れる可能性があります。

---

## 45. 同一tick順序

既定概念順：

```text
Note Off     = 0
MIDI Event   = 1
Note On      = 2
```

MIDI Eventには任意`order`を付けられます。

例：

- order < 0 — Note Offより前
- order 0 — Note Off相当位置
- order 1 — 通常MIDI Event
- order 2 — Note On相当位置
- order > 2 — Note Onより後

同じstart/orderの場合は文書配列順を保持するのが安全です。

---

## 46. MPE基本

MPE専用のEvent typeは作りません。

MPEは、

- Note Channel
- Pitch Bend
- CC
- Channel Pressure
- Poly Pressure

の組み合わせです。

### 46.1 Lower Zone

Master Channel = 1

Member Channelは2から上方向へ連続します。

### 46.2 Upper Zone

Master Channel = 16

Member Channelは15から下方向へ連続します。

`memberChannelCount`は1–15です。

---

## 47. MPE Note配置

MPEでは同時発音Noteを別Member Channelへ割り当てます。

同一Member Channel上で同時Noteを衝突させると、Channel単位のPitch Bend等をNoteごとに分離できません。

Golden MPE Demoでは同一Member Channel同時衝突0を監査しています。

---

## 48. MPE per-note expression

代表的なper-note表現：

- Pitch Bend
- CC74
- Channel Pressure
- Poly Pressure

必要に応じて`targetNoteId`を使用します。

Golden Demo 07はLower Zone、Demo 08はUpper Zone、Demo 12は同一Logical Bus上のLower+Upper非重複共存を示します。

---

## 49. MPEとPhrase Library

Phrase Source NoteにMPE Channelを埋め込みません。

MPE ChannelはConcrete Performance時に決定されます。

Phraseをmaterializeした後で、TrackのMPE Zoneに従って有効Member Channelを割り当てます。

---

# Part III — 複数メロディー／複数ボーカル

## 50. Multi-Melody

`song.melodyTrackIds`は複数のMelody-bearing Trackを明示します。

用途：

- lead melody
- counter melody
- harmony melody
- obbligato
- instrumental secondary melody

Trackのrole/nameから自動推測して保存してはいけません。

---

## 51. Multi-Voice

`lyrics.voices`は「誰がどのTrackでどのLyric Documentを歌うか」を表します。

同一歌詞をLead/High/Lowが共有しても、Lyric text自体を3重に複製する必要はありません。

---

## 52. Shared Lyric Document

同じ歌詞を複数Voiceが歌う場合：

```text
Lyric Document A
├─ Lead Voice
├─ High Harmony Voice
└─ Low Harmony Voice
```

各VoiceのNoteへの対応は`alignment.voiceId`で分けます。

Golden Demo 09がこの例です。

---

## 53. Separate Lyric Documents

Call & Response等で別本文なら、

```text
Lead Voice     → Lyric Document A
Response Voice → Lyric Document B
```

とします。

Golden Demo 10がこの例です。

---

# Part IV — Reader / Writer / Editor

## 54. Reader実装順序

推奨手順：

1. UTF-8 JSON parse
2. `format`確認
3. `version`確認
4. Schema validation
5. Core ID collection
6. Reference validation
7. Timeline構築
8. Harmony構築
9. Track/Clip/Note構築
10. Lyrics構築
11. Shared editing layers構築
12. 4.0 MIDI Bus/Channel/Event構築
13. MPE semantic validation
14. Unsupported optional featureの扱い決定
15. Playback / UIへ渡す

読込だけで、

- regeneration
- candidate selection
- external download
- physical MIDI binding

を実行してはいけません。

---

## 55. Writer実装原則

Writerは「分からない情報を消さない」が重要です。

特に4.0ファイルを部分対応アプリで編集する場合、

- 未対応MIDI Event
- MPE
- Lyric Voice
- Generation
- Localization
- Provenance
- Extension

等を保持できないなら、原本への破壊的上書きを拒否します。

---

## 56. Editorの安全な削除

Noteを削除すると、

- Lyric Alignment
- targetNoteId
- Relative Phrase assignment
- Phrase Library mapping
- Generation protectedNoteIds
- Presentation objectColor
- Provenanceそのものではなく現在参照

等への影響を調べます。

参照を壊したまま保存してはいけません。

---

## 57. Track移動・Section編集

Track/Clip/Sectionを移動する場合、関連するTempo/Key/Meter/Chordが自動追従するとは限りません。

UIは、

- 移動対象
- 取り残す対象
- 新しい境界
- staleになる共有編集情報

を明示するのが安全です。

---

## 58. Merge

Mergeは「同じIDだから同じ物」と盲信しません。

特に独立文書間ではID衝突があり得ます。

担当TrackをMergeする場合、4.0では次も担当演奏データとして比較できます。

- Note.channel
- Clip.midiEvents
- Track.midi

ただしroot `midi.buses`は共有参照情報です。

同名Busへ黙って付け替えてはいけません。

---

## 59. Atomic save

MergeやMigrationは一部だけ書き換えた状態で失敗ファイルを残さないようにします。

すべての参照・制約・保持可否を確認後、一括保存します。

---

# Part V — 3.x互換

## 60. 3.5 → 4.0

3.5文書は、明示Migrationなしに自動で4.0へ書き換えないでください。

最小Migrationでは既存音楽データを変更する必要はありません。

4.0情報を推測追加しない例：

- MIDI Bus
- Channel
- MPE
- Lyric Voice
- Counter Melody

既存`primaryMelodyTrackId`から`melodyTrackIds:[primary]`を提案することはできますが、自動追加必須ではありません。

---

## 61. 4.0 → 3.5

Downgradeでは次を失う可能性があります。

- root midi
- Track MIDI mode/bus/channel
- Note channel
- MIDI Events
- MPE
- melodyTrackIds
- lyrics.voices
- alignment.voiceId

保存前にloss reportを提示します。

---

## 62. Compatibility Playback

4.1を明示認識するOSTF Playerは、

1. `version: "4.1.0"`を既知Versionとして受理
2. 対応済みのSection/Chord/Track/Clip/Note/Lyrics/MIDIを通常再生
3. 未対応Track DirectionはPlayback上だけskip

というCompatibility Playbackを実装できます。

これは未知Future Versionを推測する規則ではありません。4.0-only Readerが4.1を4.0として読むことは禁止です。また、Playbackでskipした4.1 dataを保存時に削除してはいけません。

---

# Part VI — Validation

## 63. 構造Validation

構造Validationの正本はJSON Schemaです。

検証対象：

- required
- type
- enum
- min/max
- pattern
- oneOf
- additionalProperties
- dependentRequired

等。

---

## 64. Semantic Validation

Schemaだけでは検証できない意味規則があります。

例：

- ID参照先の存在
- `primaryMelodyTrackId`のTrack存在
- `melodyTrackIds`参照
- busId参照
- targetNoteId参照
- MPE Channel範囲
- Lower/Upper Zone重複
- Lyric Voice Track/Document関係
- Voice AlignmentのDocument/Track整合
- Poly Pressure pitchとtarget Note pitchの整合
- Relative Phrase式
- Phrase Library materialization整合
- current dependency整合

---

## 65. 楽曲品質と規格適合の区別

Schema適合は音楽的な自然さや歌声エンジンの再現性を保証しません。本版は24〜32小節の3曲のミニアレンジと、個別パラメーター・曖昧さ・互換保存を示す技術例を区別して収録しています。外部アプリ再生・合成の認証は行っていません。[デモガイド](EXAMPLES_GUIDE.ja.md)を参照してください。

# Part VII — 公開Reference Set

## 66. 技術リファレンス

`examples/01-all-core.ostf`は継承Coreの総合例、`02-all-vocal-parameters.ostf`は歌唱追加情報、`03-all-legacy-profiles.ostf`は旧形式の保存用プロファイルを示します。これらだけで全音楽表現・全数値・全組合せを網羅するという意味ではありません。

## 67. 楽曲デモ

Pop歌唱32小節、Jazz24小節、Electronic32小節の3曲を収録しています。構成・コード・複数楽器・メロディーがつながった例として参照してください。

## 68. 歌唱とMIDIの個別例

Basic/Expressive Vocal、複数Voice、メリスマ、音素タイミング、曲線上書き、テンポ/拍子変更、MPE、MIDI各イベント、Track Directionsなどを別ファイルで確認できます。

## 69. 全フィールドの対応表

[パラメーター網羅表](PARAMETER_COVERAGE.md)にSchema内の宣言位置、掲載デモ、JSON Pointerを記録します。任意キーの辞書・未知Vendorデータ・無限の数値集合は有限の網羅率の母数にしません。

# Part VIII — Anti-patterns

## 70. Note On/OffをmidiEventsへ重複保存しない

Noteの正本は`notes[]`です。

---

## 71. Physical PortをLogical Busへ書かない

`"Scarlett MIDI Out"`のような実機名をPortable Coreの正本にしません。

---

## 72. Program番号をUI値のまま保存しない

UI 1–128でも保存値は0–127です。

---

## 73. Pitch Bendを7-bitへ丸めない

14-bit 0–16383を保持します。

---

## 74. MPE専用独自Event型を作らない

通常のChannel Voice EventをMember Channelで表します。

---

## 75. Harmonyを固定半音移動だけで作らない

Format上はどんなPitchも保存できますが、公式Demoでは音楽的に意味のあるHarmonyを使用します。

---

## 76. 未対応4.0情報を保存時に捨てない

Compatibility Playbackで無視することと、Writerが削除することは別です。

---

## 77. 名前からIDを推測しない

Track名、Bus名、Contributor名、Role名の一致で自動マージしません。

---

## 78. unknown future versionを4.0として読むと決めつけない

4.1/5.xには4.0とは異なる意味変更があり得ます。

---

# Part IX — Conformance

## 79. Reader適合

Readerは少なくとも、

- Versionを識別
- Core構造を安全にParse
- 未対応機能を明示
- 対応機能の意味規則を守る

必要があります。

---

## 80. Writer適合

Writerは、

- Schema適合
- Semantic reference整合
- 未対応情報の保持
- lossの明示
- 推測で正本を作らない

ことが重要です。

---

## 81. Full Performance Player

完全4.0 Performance Playerは、

- Logical Bus
- Channel modes
- MIDI Events
- same-tick order
- MPE Lower/Upper
- per-note expression
- Multi-Voice relationship

まで解釈します。

---

## 82. Format releaseとImplementation releaseの分離

OSTF 4.2.0の規格公開と、特定Player/Arranger/Adapterの4.2対応公開は別です。規格の正式版という表示は、Synthesizer V・OpenUtau・その他アプリの実動作確認済みを意味しません。

# Part X — 実装レシピ

## 83. 単純な1ch Piano

- Track `mode=singleChannel`
- `channel=1`
- Note channel省略可
- CC64等をmidiEventsへ保存

---

## 84. 16ch Multi-timbral Track

- `mode=multiChannel`
- 各Note/EventにChannel
- ChannelごとのProgram/Controllerを明示

---

## 85. External Synth群

- Logical Busを複数作る
- TrackからbusId参照
- Physical device mappingはHost設定

---

## 86. MPE Synth

- Track `mode=mpe`
- zone + memberChannelCount
- 同時Noteを別Member Channel
- targeted Bend/CC/Pressure
- 同一Member Channel衝突を避ける

---

## 87. Lead + Harmony

- melodyTrackIdsへ複数Track
- lyrics.voicesを作成
- 同じ歌詞ならDocument共有
- AlignmentでvoiceIdを分ける

---

## 88. Call & Response

- Lead/Response別Track
- 必要なら別Lyric Document
- VoiceごとにAlignment

---

## 89. DAWからImport

Import時は、

- Note pitch/velocity/duration
- Channel
- CC
- Program
- Bend
- Pressure
- ordering

の明示情報を保持します。

DAWの物理Port名をLogical Busへ自動変換しません。

---

## 90. SMFへExport

OSTFからSMFへ出す場合、

- Note
- Channel
- Program
- Bank
- CC
- Bend
- Pressure
- same-tick order

をMIDIへ変換できます。

OSTF固有のSection/Chord/Lyrics/Multi-Voice等はSMFだけでは完全保持できないため、lossを明示します。

---

# Part XI — 全構造索引

## 91. Root object

Rootの全フィールドは`PARAMETER_REFERENCE.ja.md`の`Root`を参照します。

---

## 92. Schema object catalog

Parameter ReferenceはSchemaの **全91 `$defs`** を1対1で見出し化しています。

主なグループ：

### 基本型
`id`, `nonnegative`, `positive`, `signed`, `pitch`, `ref`, `range`, `spelledPitchClass`

### Song / Timeline / Harmony
`song`, `section`, `tempo`, `meter`, `timeline`, `chord`, `scale`, `harmony`, `key`, `keyChange`, `scaleDefinition`, `scaleTarget`

### Performance
`instrument`, `note`, `clip`, `track`, `soundSlot`, `drumKit`, `midiMapping`, `soundSource`, `voicing`

### Lyrics
`lyricDocument`, `lyricPhrase`, `lyricUnit`, `lyricAlignment`, `lyrics`, `lyricVoice`

### Resource / identity
`sha256`, `resource`, `contributor`, `credit`, `alternateTitle`, `rightsStatement`, `documentInfo`, `revisionRef`, `software`

### Shared editing
`dependencies`, `relativeAssignment`, `relativePhrases`, `generator`, `generationInput`, `generationProcess`, `generation`, `generationIntent`, `grooveIntent`

### Presentation
`color`, `roleDefinition`, `roleColorMap`, `customRoleColorMap`, `objectColor`, `presentation`

### Phrase / choices
`phraseTemplate`, `phraseNoteMapping`, `phraseInstance`, `corePhraseSourceNote`, `phraseLibrary`, `clipCandidate`, `clipChoiceGroup`, `clipChoices`

### Localization
`localizedNames`, `languageMap32`, `localizationTarget`, `localizationEntry`, `localization`

### Provenance
`provenanceSource`, `provenanceRecord`, `provenance`

### OSTF 4 MIDI
`midiChannel`, `midiBus`, `midi`, `mpeSettings`, `trackMidi`, `controlChangeEvent`, `channelModeEvent`, `programChangeEvent`, `pitchBendEvent`, `channelPressureEvent`, `polyPressureEvent`, `midiEvent`

### Legacy compatibility
`legacy33`

各Objectの全Field・型・required・rangeは`PARAMETER_REFERENCE.ja.md`を参照してください。

---

# Part XII — 配布物の使い方

## 93. 参照順序

README → 本マニュアル → [規範仕様](SPECIFICATION.ja.md) → [全パラメーターリファレンス](PARAMETER_REFERENCE.ja.md) → [デモガイド](EXAMPLES_GUIDE.ja.md) → Schemaの順で利用できます。実装者はSchemaとリファレンスから読むこともできます。

## 94. 配布範囲

本版は規格・資料・`.ostf`デモ・読取専用の静的監査スクリプトを100ファイル以内でまとめたものです。外部歌声ソフトのプロジェクト変換実装・音源・Voicebankは含みません。

## 95. 静的監査

`python tools/audit_release.py`はJSON構文、Schema構造、全項目のデモ掲載、ファイル数、文書リンク、ハッシュを確認します。全意味条件の検証器や外部ソフトの動作試験ではありません。

## 96. 正本を分ける

構成はTimeline、和声はHarmony、具体演奏はNotes/MIDI、演奏指示はDirections、歌詞はLyrics、歌唱関係はVoice/Alignment、追加の歌唱表現はVocalPerformanceです。同じ事実の正本を複数作らず、未知情報を破棄しない設計を維持します。

# Part XIII — 4.1から継承したTrack Directions

## 97. Track Directionsの目的

4.1では`tracks[].directions[]`を追加する。これは別Timelineではなく、OSTF共通時間軸上のTrack固有意味情報である。Harmonyが「曲として何が起きているか」、Notes/MIDIが「何が実際に鳴るか」を表すのに対し、Directionは「そのTrackをどう演奏・解釈・生成してほしいか」を表す。

## 98. Improvisation

`improvisation`は区間型。`effectiveKeyScale`, `songScale`, `harmonyScales`, `explicitScale`の4つのPitch Sourceを使える。ポピュラーのKey中心アドリブ、JazzのChord Scale追従、間奏だけPentatonic等を同じ枠組みで表現できる。

## 99. Pentatonic間奏

ギターの17～24小節だけA minor pentatonicを使う場合、Song KeyやHarmony Scaleを書き換えず、そのGuitar TrackへRange `improvisation` Directionを置く。Bassや他Trackには影響しない。

## 100. Jazz Chord Scale

Jazz型では`harmonyScales`から既存`harmony.scales`をID参照する。和声分析の正本を複製せず、Directionは「このTrackのアドリブでそれを参照する」という意味だけを追加する。

## 101. strict / preferred

`strict`はPitch Source/Rangeを強い制約として扱う。`preferred`は主要材料・主要Registerとして扱い、音楽的なOutside Noteや一時的逸脱を許容する。Defaultを暗黙にせずAuthoring時に明示する。

## 102. Playing Role

`playingRole`でTrack-wide `role`を一時的に`solo`, `comping`, `fill`等へ変更できる。区間終了後はTrack defaultへ戻る。

## 103. Playable Pitch Range

`instrument.playablePitchRange`は楽器自体の能力。5弦BassのLow B等を表現する。Timed `pitchRange`は「この区間ではどのRegisterを使うか」であり、二つを混同しない。

## 104. Vendor Direction

標準化前の奏法、Breath、AI指示等はVendor Directionで試せる。未知Vendor Dataを非破壊Round Tripで保持し、複数Software間で意味が安定したものだけ将来Core化する。

## 105. Point Direction

4.1のStandard DirectionはRange中心だが、VendorはPoint `at`を使える。Breath PointやCue等を将来検証する余地を確保するためである。

## 106. Natural-language Instruction

`instruction`は人間/AI向け補助。構造化パラメータが正本で、文章だけを機械互換性の唯一の根拠にしない。

## 107. DirectionとMIDI

DirectionはMIDI Eventではない。CC/Bend/AT/Program等で確定している制御は従来どおりMIDIが正本。DirectionがあってもLoadだけでMIDIを生成しない。

## 108. DirectionとGeneration

root `generation`は過去の生成Process/履歴/意図。Directionは現在有効なTrack指示。生成履歴を実行命令に読み替えず、Directionを履歴に押し込まない。

## 109. Direction重複

同じTrackの同種Standard Directionは時間重複禁止。4.1はPriorityやLast Winsを導入しない。異なるtypeは同時Active可能。

## 110. Reader / Player

4.1 ReaderはVersionを明示認識する。Compatibility Playerは未対応DirectionをPlayback上無視できるが、4.1-only DataをSaveで削除しない。

## 111. Writer / Editor

WriterはDirection ID、時間、参照、Range、Vendor namespaceを検証する。Copyでは新ID、同一ObjectのMoveではID維持。未知Vendor Directionを保持できなければ原本上書きを避ける。

## 112. 4.0→4.1 Migration

4.0文書から新Directionを推測しない。Track名がLead GuitarでもSolo Rangeを自動生成せず、既存NoteがPentatonicだけでも`explicitScale`を推測追加しない。

## 113. 4.1→4.0 Downgrade

`directions`, `instrument.playablePitchRange`, `trackDirection`参照を失う場合はLossy。削除内容を提示し、確認なしに4.0として上書きしない。

## 114. 4.2の歌唱追加と今後の拡張

Palm Mute、Slap、Pizzicato、弦・指板・音源固有モデルは本版でも一括標準化しません。4.2では歌唱専用の音素、ピッチ、表現、技法、ブレスを任意フィールドとして追加します。既存Vendorデータを意味推測で勝手に標準フィールドへ変換しません。


# Part XIV — OSTF 4.2 歌唱交換の全規則

## 1. 目的

AIまたは人が生成したOSTFを、独立したExport AdapterからSVP、VPR/VSQX、USTX/UST、CCS、UFDATAなどの歌声合成ファイルへ変換できる中立的なデータ構造を設ける。**特定のボーカル用Max for Liveデバイスの開発は目的でも必須条件でもない**。OSTF自身は音声合成・音源ライブラリ・メーカーのプロジェクト状態・エンジン固有の調声APIを実装しない。

## 2. OSTF 4.1 Coreの保持

- 既存`ppq` / `timeline` / `harmony` / `tracks[]` / `clips[]` / `notes[]` / `midiEvents[]` / `lyrics.*` / `resources[]`などを変更しない。
- MIDI演奏の正本は引き続き`notes[]`および`midiEvents[]`。MIDI CC、14bit Pitch Bend、Channel/Poly Pressure、MPEを再定義しない。
- `song.melodyTrackIds`、`primaryMelodyTrackId`、`track.role`、`trackType="melodic"`は**歌唱であることを意味しない**。Synth/Guitar/Piano等のMelodyも有効。逆にHarmony/Backingも歌唱可能。
- 歌詞の正本は従来`lyrics.documents`、`phrases`、`units`。Voiceは`lyrics.voices`、歌詞とNoteの対応は`lyrics.alignments`。
- 4.1として有効なデータは原則`version`のみ`4.2.0`へ変更してSchemaに適合する。4.2用フィールドを捏造しない。

## 3. 4.2の追加フィールド

```text
lyrics.units[].phonetics[]                  optional
lyrics.voices[].vocalProfile                optional
tracks[].clips[].vocalPerformances[]        optional
    id, voiceId                             required inside a performance
    noteIds[]                               optional note ownership
    phonemeEvents[]                         optional, clip-local timing
       order                                optional tie-breaker
    pitchCurves[]                           optional, per Note, cents
    expressionCurves[]                      optional, clip-level or per Note
    techniques[]                            optional semantic performance intent
    breathEvents[]                          optional breath timing
```

追加フィールドはすべて**4.1の既存オブジェクトへのオプション付与**であり、歌唱しない楽器のTrack/Clipへは一切要求しない。`vocalPerformances`が存在しなくても、Voice+AlignmentがあればBasic Exportの入力になる。

## 4. 識別・所有・音符の正本

1. VocalPerformanceは`voiceId`で`lyrics.voices[].id`を参照する。該当Voiceの`trackId`は格納先TrackのIDと一致しなければならない。
2. 同じClip内の同一VoiceのVocalPerformanceは最大1件。1 Track/Clip内に複数Voiceは許容する。音符は新設せず、4.1の既存ノートを参照する。
3. 任意の`noteIds[]`を指定した場合、そのVoiceがこのClipで担当するピッチNote ID集合を明示する。既存AlignmentがそのVoiceに帰属させた当該Clipのノートをすべて包含しなければならない。存在しないノート、Sound Slot、`fixedTrigger`を指定してはならない。
4. `noteIds`省略時は、そのVoiceの`lyrics.alignments[].voiceId`に明示されたノートを使う。`song.melodyTrackIds`や`track.role`から推測して割り当ててはならない。
5. Voice指定のない従来Alignmentは、勝手に1つのVoiceへ帰属させない。必要なら明示的に紐付けるか、人が変換対象を確定する。
6. Alignmentが参照するNoteは実在し、Voiceが指定されているなら当該Track上の音楽的ピッチNoteでなければならない。複数Voiceで同じNote IDを参照することは構造上許すが、出力時には声部ごとに複製・分割が必要になり得る。

## 5. 歌詞・発音

- `lyrics.units[].text`は画面表示用の歌詞。既存`pronunciation`は読みの原文。`phonetics[]`は音素列の選択候補。互いに上書きしない。
- `phonetics[].alphabet`は`ipa`、`xsampa`、`arpabet`、`other`。`other`の場合は`namespace`必須。`symbols[]`は順序付きトークン列。
- 任意の`preferred:true`は同じ`(alphabet, language)`候補群で最大1つ。言語タグは比較時に大小文字を区別しない。IPAとX-SAMPAそれぞれにPreferredを持つのは構わない。
- 発音の優先順位は、明示時間付き`phonemeEvents` → ターゲットとマッピングできる`phonetics`候補 → `pronunciation` → `text`からの辞書推測。推測結果を元Coreへ無断保存しない。
- 異なる音素体系での同一性を保証しない。言語・辞書・Voicebank依存の変換はAdapterの責務。

### 5.1 同Tick音素イベントの順序（OSTF 4.2追加）

- `phonemeEvents[].order`は任意の符号付き整数。同一Voiceの同一Clip内で、`start`が同じイベント群を順序づけるためだけに使用する。
- 同じ開始Tickに複数イベントがあり、そのうち1つでも`order`が存在する場合、当該群のすべてが`order`を持ち、その値が重複してはならない（Semantic Rule）。
- すべて`order`が省略された同Tickイベント群は構造上有効。ただし**順序不明**であり、Adapterは順番を捏造して完全変換を名乗ってはならない。Preflightは`needs-resolution`として報告する。
- `order`は物理的な発音優先度、MIDI同Tickイベントや他Voiceとの合成順序を指定しない。

### 5.2 Lyric Alignmentの多対多

- **1 Unit → 1 Note**: 通常の発音。
- **1 Unit → 複数Note**: メリスマ。歌詞は同じまま、ノート列へ継続する。特殊な歌詞文字を自動で増やさない。
- **複数Unit → 1 Note**: 一音に複数の発音単位。音素タイミングが無い場合、順序と個々の長さが曖昧なのでPreflightで警告する。
- **複数Unit ↔ 複数Note**: 組み合わせが一意に決まらない。原データを不正扱いしないが、`phonemeEvents[].unitId/noteId`等で結合が完全に確認できなければ`needs-resolution`とする。AIは原則1UnitごとのAlignmentへ分割して作成する。
- `lyrics.alignments`は正本であり、VocalPerformance内に別の歌詞対応表を重複作成しない。

## 6. 歌唱表現の意味

### 6.1 Vocal Pitch

- `pitchCurves[].targetNoteId`は既存のピッチNoteを参照する。`points[].value`はそのNoteの`pitch`からの**Cent偏差**（+100cent=+1半音）。`points[].at`はClip相対Tick。曲線補間は`step`/`linear`。
- 同じVoice/Clip/NoteにPitch Curveは最大1本。ポイントは昇順で重複禁止、対象Noteのゲート内にある。
- 1点のみの場合はNoteゲート全域で固定偏差を示す。2点以上の場合、**明示ポイントの区間外は未指定**。最初/最後の点を暗黙外挿したり、MIDI Bendの値を勝手に合算したりしない。
- 歌声形式へ出力するとき、対象Noteで4.2の明示Curveと4.1のBendが重なれば4.2が優先する。MIDIとして演奏するときは**4.1のMIDIが正本**。
- 連続した複数Noteを跨ぐ精密なPortamentoはOSTF 4.2のNoteゲート型の外であり、記録できない場合は近似/省略を報告する。新しい正本として別のMelodyノート列を作らない。

### 6.2 Vocal Expression

- `expressionCurves[].parameter`: `dynamics`、`breathiness`、`tension`、`brightness`、`voicing`。
- 値は抽象スケール0..1。これはエンジン間で音響的に一致する絶対量ではない。**無指定は0.5ではなく未指定**。
- `targetNoteId`省略時はVoice/Clip全体に適用。指定時は対象Note内の値でClip全体の同一パラメーターを**置換**し、加算しない。
- 1点Curveはその対象範囲に固定値。複数点Curveの外側は未指定で、Note単位の明示Curveの範囲外では存在するClip全体のCurveへフォールバックしてよい。Clip全体にも指定がなければ未指定のまま。
- ベンダー固有の値への実数変換・知覚的同等性の検証はExport Profileと実アダプターが担当する。

### 6.3 Techniques / Breath

- `techniques`は歌唱意図を示す意味タグ（`scoop`、`fall`、`vibrato`、`legato`、`whisper`、`falsetto`、`growl`等）。`intensity`は任意の抽象0..1。具体的にどのピッチ/音量変化を生成したかは意味タグだけでは決定できない。
- `breathEvents`は吸気/呼気のクリップ内時間区間。ブレスとノートが同時に存在しても、どのように合成するかはターゲット依存。
- 同じ技法と数値Curveを**二度適用してはならない**。ノート/ピッチ/音素の具体データが優先。

## 7. 共通時間モデル

- 全て既存`ppq`に従う。`clip.start`は楽曲絶対Tick。Note、曲線、音素、技法、ブレスはClip相対Tick。
- `phonemeEvents.start`/`techniques.start`/`breathEvents.start`等は負のClip相対Tickを許すが、絶対位置 `clip.start + localStart` は負不可。イベント終端は所属Clip終端を越えてはならない。
- 時間を変換するAdapterは**絶対開始/終了を元PPQの有理数比で写像**し、変換後`end-start`を求める。元の長さを別に丸めて足す方式を避ける。
- 整数Tickへの標準提案丸め規則は**最近接・ちょうど半分なら0から遠い方向**。これは外部アダプターの検証用決定規則であり、対象ファイル独自の時間解釈を置換するものではない。
- 元の正の長さが変換先でゼロになったり、異なるCurve点が同一Tickへ衝突したりすれば無断で削除・統合してはならない。Preflightで明示し、出力保留/ユーザー選択/近似手順を要求する。
- `timeline.tempoChanges`は元楽曲の正本。異なるテンポ区間を秒へ変換する場合は区分積分する。テンポ変更を消して定テンポとして再量子化しない。

## 8. レンダリングの権限・互換性

1. MIDI Playback: 4.1 `notes[] + midiEvents[]`のみを使用（Vocal情報は無視してよい）。
2. Voice Synth Export: Voice選択 → Track/Clip/Note選択 → Lyric Alignment → Phonetic Timing → Vocal Pitch/Expression → Target mapping。
3. `VocalPerformance`を持たないBasicファイルでも交換の入力として有効。4.1からのversion-only移行を認める。
4. ターゲットの実装で正確に出せる情報と、近似/未対応/未検証を区別する。元のOSTFを無断書換えしない。
5. 外部アダプターの`unverified`は出力形式の動作保証ではない。実アプリ読み込みとRound-tripを検証した上で`application-tested`へ昇格する。
6. 4.2 Readerは未知の4.3+フィールドを既知4.2として読み飛ばしたまま保存・上書きしてはならない。

## 9. 適合条件と検査の範囲

Reader/WriterはSchemaのほか、定義IDの一意性、型付き参照、Voice→Track、Note所属、音素Unit参照、時間・Curve順序・値域・同Tick順序等の規範意味条件を満たす必要がある。参照オブジェクトに現れる`id`は新しい実体IDの定義ではない。エクスポート時の曖昧さとCoreの構造エラーは区別する。同梱の監査ツールは静的な配布整合性とフィールド網羅性を確認するもので、全意味規則や音声合成動作を認証するものではない。

## 10. JSON入力の厳格性

- `.ostf`の4.2実装はUTF-8のJSONを採用する。重複プロパティ、`NaN`、`Infinity`、非有限数、非ゼロ値のゼロへのunderflow、不正UTF-8および孤立Unicode代理符号を入力エラーとして拒否し、先勝ち/後勝ちの暗黙解決を禁止する。
- 入力を拒否した場合は修正・置換したOSTFや外部ファイルを勝手に保存しない。従来互換のためUTF-8 BOMを読み取りのみ受け付けてもよい。
- Schema適合だけでは、Voice/Note所有権、Alignment、音素順序、PPQ損失などの意味条件を満たしたことにはならない。

## 11. Adapter契約（Coreの追加フィールドではない）

- **エクスポート:** Voiceは`lyrics.voices`/`lyrics.alignments`から明示選択する。MIDI Melodyを歌唱に昇格させない。変換できない音素、Pitch、Expression、Voicebank、Tempo、Time Signature、Noteは損失/近似/曖昧さを報告する。損失を暗黙承認しない。
- **Sidecar:** オプトインの`.vocal-sidecar.json`は元OSTFから歌唱情報を複製する補助記録である。外部歌声ソフトが読めるNativeデータではなく、元OSTFの正本を置き換えない。元OSTF/Native/ReportのSHAと元PPQを照合する。
- **Native編集レビュー:** 元OSTF、Baseline Native、Edited Native、Export Report、Sidecarの5入力を一致検証し、差分を読み取り専用で提示する。Note/Tempo/Meter/Voiceルーティングの改変はブロックする。変更Pitchを自動的にOSTF centsへ変換しない。
- **歌詞書き戻し:** 承認は既定で全件`pending`/`false`。単一Unitと単一Noteの曖昧さのない対応でのみ、承認された`lyrics.units[].text`と`lyrics.phrases[].text`を**新規OSTF**へ反映できる。発音、音素、歌唱表現、MIDIを変更せず保持することは別の明示承認を要する。既存ファイルは上書きしない。
- SHA256は同一性照合であり、ファイル作成者の認証・電子署名ではない。Adapterのローカル検証は実アプリでの合成可能性を証明しない。

外部Adapterの情報保持・損失報告は[適合性](CONFORMANCE.ja.md)と[移行方針](MIGRATION.ja.md)を参照。実装固有の契約はCore外である。

## 12. バージョン・互換性の扱い

- 4.1有効データの最小4.2化は`version`を`4.1.0`から`4.2.0`に変えるだけであり、未指定歌唱情報を推測作成しない。
- 4.2専用項目のあるファイルを4.1に戻す場合、その削除は情報損失を伴う。Readerは未対応Versionや将来の未知フィールドを消した状態で保存しない。
- 4.2の**Core仕様適合**と**Adapterでのローカル出力可能性**と**外部アプリでの読み込み実証**と**歌声の音響的同等性**は相互に独立した合格基準である。
- 4.2.0のリリース後に既存フィールドの意味、時間基準、必須性を変更する場合は互換性評価が必要。4.2.0公開用Coreの意味規則を固定する。

## 13. 規格正式版の公開範囲

本パッケージはOSTF 4.2.0 Coreの正式規格配布物である。データ構造と意味規則を定め、特定の歌声合成ソフトへの対応認証は行わない。Native変換ツール、Voicebank、音声合成エンジンは収録しない。外部アプリ動作検証の実施を主張しない。[適合性と実装範囲](CONFORMANCE.ja.md)を参照。

# Part XV — 実装・編集・AI生成の実務

## 基本データから歌唱を追加する順序

最初に10個のRoot必須項目と共通PPQを決め、曲の構成、和声、Track、Clip、Noteを作ります。歌唱する部分だけにLyric Document/Phrase/Unitを作成し、VoiceでTrackと歌詞文書を関連付けます。Voice付きAlignmentで既存Noteへ対応付け、音素・ピッチ等が実際にある場合にのみVocalPerformanceを追加します。MelodyやLeadという名前から声を推定しません。

歌詞のないハミングでは、Voiceと`noteIds`で担当Noteを明示します。ダミーの歌詞や別の歌唱Note配列を作る必要はありません。通常の楽器のメロディーは従来のNotesとMIDIのままでよく、4.2歌唱情報は不要です。

## Clip/Noteを移動・削除するとき

Clip移動では通常は`clip.start`を変更し、内部のNote・音素・曲線の相対時間を保ちます。ただし前倒し子音など負の相対値について絶対時刻が負にならないか確認します。Note移動/削除ではAlignment、VoiceのnoteIds、Pitch/Expressionの対象、PhonemeのnoteId、Techniqueの対象を同時に整合させます。Clip分割ではイベントの所属とローカル時間を再構築し、正本Noteを重複生成しません。

## 表示歌詞と発音の編集

表示歌詞を変えても既存のpronunciation・phonetics・phonemeEventsを自動的に正しい発音へ更新できるとは限りません。これらは独立した著者データとして保持し、再生成は明示操作で行います。Unit削除では音素の参照を残しません。歌詞書き戻しで他のMIDIや歌唱表現を無断変更してはいけません。

## AIから直接生成する場合

AIは完全なUTF-8 JSONを出力し、許可されていない独自Rootキーを追加しません。IDは表示名とは別に一意化し、時間はすべて同じPPQに従わせます。Unit/Noteを原則1対1にし、メリスマ等だけ明示的に広げます。歌唱ピッチはNoteの基準音からのcent偏差、表現量は抽象0〜1であり、欠損値を0.5で埋めません。コードネームやキーを変えて演奏Noteとの不一致を隠してはいけません。

## 全項目網羅の意味

本版はSchemaから到達可能な名前付きプロパティの宣言位置569件をデモ群で掲載しています。Core481件と互換保存88件の合計です。同じ名前でも別のObject/分岐で定義されるものは別の宣言位置です。すべてのenum値・数値・組合せ・言語・音響結果を試した意味ではありません。未到達の埋込Legacy定義はリファレンスの保管定義として説明し、新しいCore項目として扱いません。

## ダウンコンバートと外部形式

4.2専用フィールドが存在しなければ4.1へversionだけ戻せます。存在する場合の削除は損失であり、コピーとして出力し、削除箇所を報告します。外部形式が表現できない情報は元OSTFに残します。Sidecarは補助記録でありNativeの互換性や音響一致の証明ではありません。
