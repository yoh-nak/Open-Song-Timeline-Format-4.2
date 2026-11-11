# OSTF 4.2.0 — 正式版リリースノート

規格配布物作成日: 2026-11-11。リリースタグ: `v4.2.0`。

## 規格の追加

`lyrics.units[].phonetics`、`lyrics.voices[].vocalProfile`、`tracks[].clips[].vocalPerformances`の3箇所に任意情報を追加します。音素候補/タイミング、Voice担当Note、Note基準cent曲線、抽象表現曲線、技法、ブレスを扱います。音符の正本は従来のNotesのままです。

## 維持する内容

4.1のTrack Directions、Playable Pitch Range、曲情報、Timeline、Harmony、Lyrics、MIDI CC/Bend/AT/MPE、論理Routing、履歴、編集関係を維持します。楽器ファイルへ歌唱情報を要求しません。

## 配布構成

日英全網羅マニュアル/リファレンス、正式Schema、53件の`.ostf`、全569項目の掲載位置、CC0/MITライセンス、読取専用監査ツールを同梱します。準備版の`properties`/`$defs`は維持し、Schema最上位の説明コメントだけ正式版向けに更新しました。

## 確認の範囲

外部アプリの読み込み、再生、合成、音響一致は検証していません。過去の回帰テスト件数を今回の実施結果として使いません。静的Schema適合と項目網羅は全意味条件の証明ではありません。Native変換器は別配布です。GitHubへのアップロード自体は実施しておらず、このZIPが公開する内容です。
