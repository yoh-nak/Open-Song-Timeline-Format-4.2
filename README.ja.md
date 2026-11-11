# Open Song Timeline Format 4.2.0

**正式規格版 — 任意の歌唱パフォーマンス交換**

OSTFは曲構成・和声・Track/Clip/Note・MIDI・歌詞・演奏指示を、DAWやアプリに依存せず交換するJSON形式です。4.2は4.1 Coreを維持し、任意の音素候補、Voice Profile、歌唱パフォーマンスを追加します。楽器メロディーを歌唱専用にせず、専用Max for Liveデバイスも前提にしません。

## 主要資料

- [全網羅マニュアル](docs/COMPLETE_MANUAL.ja.md) / [English](docs/COMPLETE_MANUAL.md)
- [全網羅パラメーターリファレンス](docs/PARAMETER_REFERENCE.ja.md) / [English](docs/PARAMETER_REFERENCE.md)
- [規範仕様](docs/SPECIFICATION.ja.md) / [English](docs/SPECIFICATION.md)
- [デモ全一覧](docs/EXAMPLES_GUIDE.ja.md) / [全項目の掲載位置](docs/PARAMETER_COVERAGE.md)

## 収録デモ

`.ostf`は53件です。01〜50は技術リファレンス、51〜53はPop歌唱32小節・Jazz24小節・Electronic32小節の新規楽曲デモです。全て`version: "4.2.0"`です。

Schemaから到達可能な**全569宣言位置（Core481＋互換保存88）**をデモ群で網羅します。同じ名前でも定義Object/分岐が異なれば別位置として数えます。全enum値・数値・組合せを網羅したという意味ではありません。

## 正式版の範囲

これはCore規格の正式配布物であり、特定ソフトの動作認証ではありません。外部アプリの動作検証は行っておらず、Native変換器・Voicebank・音声エンジンは同梱しません。[適合性](docs/CONFORMANCE.ja.md)、[移行](docs/MIGRATION.ja.md)、[リリースノート](RELEASE_NOTES.ja.md)を参照してください。

## 静的監査（任意）

```bash
python -m pip install -r requirements.txt
python tools/audit_release.py
```

JSON・Schema構造、デモの項目網羅、ファイル数、文書リンク、[SHA-256](SHA256SUMS.txt)を確認します。全意味規則や歌声合成を試すものではありません。

## ライセンス

規格・Schema・文書・デモは[CC0-1.0](LICENSE)、Pythonツールは[MIT](LICENSE-CODE)です。4.1と同じ区分を継承しています。[NOTICE](NOTICE.md)に由来と収録範囲を記載しています。

## 配布整備記録

[静的整備記録](STATIC_REPORT.md) / [機械可読レポート](RELEASE_REPORT.json)
