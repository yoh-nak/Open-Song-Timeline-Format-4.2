# OSTF 4.2.0 — Static Release Report / 静的整備記録

Prepared: 2026-11-11. Formal Core specification release package; GitHub upload has not been performed.

| Item / 項目 | Result / 結果 |
|---|---|
| Files in release / 配布ファイル数 | 87 / 100 maximum |
| `.ostf` files / デモ | 53; all version 4.2.0 |
| Strict JSON + declared Schema / 構造 | 53 / 53 |
| Reachable parameter declarations / 宣言位置 | 569 / 569 covered |
| Core / 旧形式保存 | 481 / 88 |
| Broken local Markdown links / リンク切れ | 0 |
| Frozen Core `properties` + `$defs` | Unchanged / 不変 |
| Inherited 4.1 base schema bytes | Unchanged / 不変 |
| Existing reference semantic subsets / 参照関係の部分診断 | 53 documents; no remaining diagnostics |
| External application execution / 実アプリ | Not performed / 実施していない |

A field witness means a named property is stored in a matching schema branch at the documented JSON Pointer. It does not mean all enum values, all possible numbers, every semantic rule, every engine or every combination was tested. The existing reference checks are not complete normative semantic validators.

The inherited wordless-humming demo had a stale primary lyric document reference. It now points to its actual `doc-wordless` object. No Core field or constraint was changed to accept a demo.

The [machine-readable report](RELEASE_REPORT.json) records exact counts and hashes. [SHA256SUMS.txt](SHA256SUMS.txt) covers every other shipped file; the manifest cannot hash itself. `python tools/audit_release.py` performs the shipped read-only package audit. Final ZIP CRC and manifest verification are performed after packaging and recorded in the delivery summary, not claimed as an external application test.

本書の確認は配布物の静的な整備範囲です。過去の657件等の回帰テストを今回実行したという主張はありません。規格の正式版であることと外部アプリの動作対応済みは区別します。
