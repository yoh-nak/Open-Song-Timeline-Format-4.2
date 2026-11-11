# OSTF 4.2.0 — 全網羅規範仕様

正式規格版: 2026-11-11。構造の正本は[4.2 Schema](../schema/ostf-4.2.0.schema.json)、継承Core全体の意味規則は[全網羅マニュアル](COMPLETE_MANUAL.ja.md)、全フィールドの型・条件は[全網羅リファレンス](PARAMETER_REFERENCE.ja.md)。MUST / MUST NOT / SHOULD / MAYは規範用語。

4.1 Coreの意味を保持し、Part Aに継承したTrack Direction規則、Part Bに4.2歌唱交換規則をまとめる。Part Aの4.1表記は仕様の導入版を示す歴史的な説明で、配布物の現在版は4.2.0である。4.2追加情報はPart Bに従う。

# Part A — 継承するTrack Directionsと正本の境界

## 1. 目的・範囲・拡張に依存しない原則

OSTFは曲情報、構成、和声、確定した演奏、歌詞、共有可能な編集関係を交換する形式です。DAWセッションや音源状態の代用品ではありません。

4.0では、3.5までのキー、転調、スケール、構成、和声、歌詞、実演奏Note、Sound Slot、Note Off Velocity、Mute、Probability、Velocity Deviation、固定MIDIトリガー、共有編集関係をそのまま継承します。その上に、MIDI Channel、Control Change、Program Change、Bank Selectを構成するCC、Pitch Bend、Channel Pressure、Polyphonic Key Pressure、Channel Mode、MPE、Logical MIDI Bus、複数メロディー宣言、複数歌詞声部を**名前の決まった型付きCore項目**として追加します。`extensions`をこれらの標準機能の正本にしてはなりません。

`extensions`は任意です。省略した文書だけで全標準機能を記述できます。既存・第三者拡張の保持能力は残しますが、3.5で標準化された現在の曲情報の正本にしてはなりません。未知拡張を削除することも要求しません。既知の旧拡張を移行できない場合も原本を保持し、不明な内容を推測で新Coreへ流し込みません。

音源プリセット、DSP、生成モデル内部状態、Liveの一時的なウィンドウ位置等はアプリ／Live Setに保持します。今回の標準項目を任意JSONの`appData`や`settings`へ逃がす保存方式は採用しません。将来、共通交換が必要な新情報が判明した場合は、意味と型を定義した新しいOSTF版で追加します。

4.0.0はMIDI 1.0互換のChannel Voice／Channel Mode相当の演奏制御とMPEの意味的構成までを担当します。System Exclusive、MIDI Clock、MIDI Time Code、MIDI Machine Control、MIDI Show Control、MIDI 2.0 UMP、音声クリップ、歌唱エンジン状態、プラグインの完全復元、物理MIDI Port割当、DAW Track/Audio Routing、連続テンポカーブ、完全な楽譜組版は4.0.0 Coreの範囲外です。Logical MIDI Busは曲内の論理的な出力空間であり、実機PortやOSデバイス名を正本にしません。

## 2. 保存形式・版・数値

UTF-8のJSONオブジェクト一つとします。BOM、同一オブジェクトの重複キー、孤立サロゲート、不正UTF-8、NaN/Infinity、末尾の非空白を禁止します。Core整数はJSON整数トークンで記載し、`1.0`、`1e0`、`true`を整数の代わりに使用しません。最大整数の絶対値は`9007199254740991`です。整数の加算・乗算後もこの範囲を満たす必要があります。

有限の十進JSON数値をbinary64の限界だけで不正としません。未知情報の数値を無損失保存すると表明する実装は、元の数値トークンまたは同等の精度を保持します。表現できなければ読取専用／保存拒否／明示的な損失確認とし、黙って丸めません。キー順・空白のバイト一致と意味上の保持は別です。

ルート必須項目は3.5から変えず、`format`, `version`, `ppq`, `song`, `timeline`, `harmony`, `tracks`, `soundSlots`, `lyrics`, `resources`の10個です。`format="OSTF"`、`version="4.2.0"`。MIDI演奏制御を使わない4.2文書へ空のMIDI設定を強制しません。

任意のルート項目は`extensions`, `drumKits`, `contributors`, `document`, `relativePhrases`, `generation`, `presentation`, `phraseLibrary`, `clipChoices`, `localization`, `provenance`, **`midi`**です。`midi`はLogical MIDI Busだけを宣言します。追加の未定義Coreフィールドは禁止します。SchemaのURLは識別子であり、読込時の取得要求ではありません。

3.0.0～4.1.0は各原版のSchemaと意味で読みます。単に読んだだけで4.2へ書き換えません。4.3.0や5.0.0等の未知の将来版は未対応と明示し、編集を拒否するか、原文のまま保存する限定モードにします。未来の項目を4.2の既知項目と推測して変更しません。

## 3. 時間軸・ID・参照

`ppq`は四分音符当たりの整数tickで1～960000、推奨960です。全トラック、全標準編集項目に同じ値を用います。拍子変更によってtickの単位は変わりません。Core時刻は0以上、ゲート長は1以上。NoteおよびMIDI Eventのクリップ内開始は負を許し、絶対開始は0以上です。

区間は`[start, start+duration)`です。変更イベントはその`at`から有効です。Clip内のNoteとMIDI EventはClipローカル`start`を使い、絶対時刻は`clip.start + local start`です。NoteとMIDI Eventのローカルstartは負を許しますが、絶対時刻は0以上でなければなりません。

同一絶対tickではNote Offの暗黙`order=0`、MIDI Eventの省略時`order=1`、Note Onの暗黙`order=2`を用います。数値orderの小さいものを先に処理し、同値では**Note Off → MIDI Event → Note On**の順とします。同一tick・同一orderのMIDI Eventは保存配列順を維持し、Note Off/On群はnoteIdの辞書順とします。MIDI Eventは負のorderでNote Offより前、2より大きいorderでNote Onより後へ明示配置できます。表示の小節・拍、秒数、MIDI番号、配列番号を時刻やIDの代わりにしません。

IDは`^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$`。Core対象のIDは種別をまたいで文書内で一意です。フレーズ原型、インスタンス、候補グループ、候補、役割定義、生成Process、履歴Record、初期スケール、キー変更に加え、4.0のMIDI Bus、MIDI Event、Lyric Voice、および4.1のTrack Directionも含みます。例外は**各原型の中のsource note ID**で、その原型内だけのIDです。`document.id/revisionId`は別の文書識別空間です。未知拡張や過去版の局所IDをCoreの登録簿へ再帰的に取り込みません。

Refは`{type,id}`。Schemaに列挙した正しい種類へ解決します。同じ文字列の異種別対象、同名の別対象、配列の同じ場所にある対象へ付け替えません。移動ではIDを維持、独立コピーでは新IDを付けます。関連参照を更新できない操作は中止するか、対象が標準編集関係なら後述の状態を更新します。

## 4. 曲情報の正本

| 情報 | 正式な保存先 | 読み手がしてはならないこと |
|---|---|---|
| 原文曲名・副題・説明 | `song.title/subtitle/description` | UI言語に合わせて原文を上書き |
| 代表的な初期キー | `song.key` | 先頭コード・先頭scale・旧拡張から黙って補完 |
| 曲中のキー変更 | `timeline.keyChanges` | ノートを読み込み時に移調 |
| 既定スケール | `song.scale` | キーと同じ情報とみなす |
| 時間付きスケール文脈 | `harmony.scales` | そのたびに全体キーを変更 |
| 初期テンポ・拍子 | `tempoChanges[0]`、`meterChanges[0]`（tick 0） | `song.bpm`等の別正本を作る |
| ジャンル・ムード | `song.genres`、`song.moods` | 認識できない名前をPop等へ置換 |
| 作者等 | `contributors`＋`song.credits` | ソフトの開発者／データ編集者を作曲者にする |
| 主旋律・主歌詞 | `song.primaryMelodyTrackId/primaryLyricDocumentId` | 未指定を先頭要素と同一視 |
| 複数メロディー集合 | `song.melodyTrackIds` | Track名やroleから黙って追加 |
| 複数歌詞声部 | `lyrics.voices`＋任意`alignments[].voiceId` | 同じ歌詞本文を声部ごとに不要複製 |
| 論理MIDI出力 | `midi.buses`＋`tracks[].midi.busId` | OS/DAWの物理Port名を正本化 |
| MIDI制御演奏 | `tracks[].clips[].midiEvents` | Note配列や任意拡張へ混在 |
| ボイシング | `harmony.chords[].voicing` | 実演奏を勝手に生成／二重再生 |
| 実演奏 | `tracks[].clips[].notes` | 生成設定を実行して再構成 |
| Track固有の時間付き演奏・生成指示 | `tracks[].directions` | HarmonyやNote/MIDIの第二の正本にする |
| 楽器の演奏可能Pitch能力 | `tracks[].instrument.playablePitchRange` | 一時的な演奏音域Directionと混同 |

`title`だけはsong内必須で、未命名の空文字を許します。その他の任意フィールドがないことは有効な未完成状態です。未指定をC major、120 BPM、Pop、English等へ書き換えてはいけません。ただしテンポ・拍子は後述のとおり元々必須であり、欠落した不正文書を補完して正常扱いしません。

`primaryMelodyTrackId`は既存トラック、`primaryLyricDocumentId`は既存歌詞文書へ解決します。未指定時には特定しません。4.0の任意`melodyTrackIds`は重複なしの順序付きTrack参照で、複数の旋律・対旋律・ボーカルハーモニー等を明示できます。配列先頭をPrimaryとは解釈せず、Primaryは従来どおり`primaryMelodyTrackId`だけで指定します。`primaryMelodyTrackId`と`melodyTrackIds`を併記するとき、Primaryはその集合に含めます。主旋律指定は追加の発音命令ではなく、主歌詞指定も他の歌詞文書を削除する指示ではありません。

## 5. キー・転調・スケール

### 5.1 キー値

`key.state`は`tonal`, `atonal`, `unspecified`。`tonal`では`tonic`と`mode`が必須、他の二状態ではその両方を禁止します。`label`は任意の原文表示注記です。未指定と明示的なunspecifiedを保存上区別し、どちらも推定キーに置換しません。無調をC majorと表示してはいけません。

`tonic`は`{step,alter}`。stepはA～G、alterは−2～2。自然音C=0,D=2,E=4,F=5,G=7,A=9,B=11にalterを加え12で正規化します。C#とDbの綴りは別に保持します。

`mode`は非空の原文識別文字列です。共通に認識する正確な識別子を`major`, `minor`, `dorian`, `phrygian`, `lydian`, `mixolydian`, `locrian`とします。majorは通常の長調、minorは通常の短調という調性の記述であり、許可ノートの閉集合ではありません。minorを自然短音階のみへの強制指定としません。未知のモードや`blues`などもそのまま保存・表示し、major/minorへ丸めません。未知の意味を解釈しない実装は名称と主音の保持だけでもよいものとします。

`label`はmodeやtonicを変更する別正本ではありません。labelから反対の主音が読み取れるなどの疑義は診断できますが、自動修復しません。Camelot番号、五度圏上の位置、調号は派生表示であり保存する正本を増やしません。対応しないモードをmajor/minorと偽って正確表示しません。

### 5.2 初期キーと変更マップ

初期キーの保存場所は**song.keyだけ**です。`timeline.keyChanges[]`は`id`, `at`, `key`が必須、`label`が任意です。`at`は**1以上**、厳密昇順、同じ時刻の複数変更は禁止します。`at:0`でsong.keyを二重定義しません。

時刻tの有効キーは、`at <= t`を満たす最後の変更、なければsong.key、どちらもなければ未指定です。戻り転調は戻るキー値を別の変更として明示します。局所的な借用和音やコードごとのスケールから転調を自動認定しません。変更は次の変更まで持続し、セクション境界で勝手に初期キーへ戻しません。無調・未指定への遷移も同じマップで記述できます。

時間付きの複数調性を同時に自動合成する機能はありません。多調の解析は複数のスケール文脈等で保持できるものの、このマップは一つの共有調性記述です。多調を単一キーに黙って押し込めません。

### 5.3 全体スケールと局所文脈

任意の`song.scale`は`id, tonic, intervals`必須、label任意の既定スケールです。intervalsは0～11の整数、0を含む厳密昇順・重複なしです。キーのmodeから自動で作ったり、キー変更によって自動で主音をずらしたりしません。初期スケールは時間付きscaleと区別されます。

`harmony.scales[]`は従来の`id,start,duration,tonic,intervals,label?`を維持します。3.5の任意`targets`はsection/track/clip/chord/noteへの明示的Ref配列です。指定対象のいずれかに該当する文脈として扱い、参照の実在を要求します。track対象はその所属clip/note、clip対象は所属note、section対象はその時間範囲との共通部分に適用可能な文脈です。chord/note対象は当該対象への注記です。targetなしは一般の時間付き文脈で、特定のトラック所有を意味しません。

明示的contextIdがある操作はそれを用います。時刻と対象に一致する時間付き文脈が一つならそれを候補に、複数なら複数候補のまま提示します。配列先頭だけを正解としません。一致する文脈がなく、song.scaleがあればそれが既定候補です。実装固有の選択は明示操作として行い、元データの複数文脈を削除しません。

スケールとキーが異なる主音・音集合を持っても、それだけで文書を不正にしません。分析注記と作曲意図は演奏ノートを制限しません。全体キー変更時にも確定済みメロディー、ボイシング、スケール、ドラムを自動更新しません。

### 5.4 読込時キー・一時移調・確定移調

Playerの「Original」は**読み込んだ文書の基準**です。過去の作者の原調を保証しません。初期表示はsong.key、再生位置での表示は有効キーを用い、どちらを表示しているかUIで区別します。

再生だけのTranspose、印刷だけのTranspose、試聴テンポ倍率はアプリの一時状態であり、OSTFの現在の曲情報へ書き込みません。一時移調値を保存して読込時に再適用することは禁止します。

確定移調は明示的な一括編集です。選択した対象の`pitchRole=musical`のpitch Note、コードroot/bass・voicing、キー、スケール等を整合するよう更新するか、更新できない関係をstale/unverifiedとして示します。`pitchRole=fixedTrigger`、Sound Slot ID、ドラムMIDI割当は移調しません。0～127等を外れる値はクリップ／折返しで黙って修正しません。ラベルを安全に更新できない場合も不一致を隠しません。コードのintervals、スケールのintervalsそのものは半音移調では不変です。

フレーズ原型と実体化ノートを両方ずらして二重移調しないよう、リンク関係を再計算するかstaleにします。履歴を記録する場合はprovenanceへ以前のキー等を残せますが、過去情報を現在のsong.keyより優先しません。

## 6. テンポ・拍子・構成・曲長・弱起

`timeline.tempoChanges`は空でなくtick 0から厳密昇順、bpmは有限で0超1000以下。四分音符毎分であり、6/8等でも付点四分音符毎分へ読み替えません。変化はstepで、次の変更点まで一定です。一定区間の秒数は`tick差 × 60 / ppq / bpm`。変更をまたぐ場合は区分積分します。

`meterChanges`もtick 0から厳密昇順、numeratorは1～64、denominatorは1,2,4,8,16,32,64。小節途中の変更を丸めて移動しません。任意`beatGroups`は分母音符単位の正整数列で、合計がnumeratorに一致します。7/8の[2,2,3]等を保持できますが、アクセントやノート時刻の自動変更ではありません。

sectionsは開始順で重複区間なし、隙間・空配列を許します。`id,name,start,duration`必須、roleは自由文字列、localizedNamesは既存の任意表示です。nameをVerse/Chorus判定用のIDにしません。未知roleやセクションを削除しません。セクション境界で演奏ノートを切りません。

任意の`timeline.duration`は名目的な曲配置長（tick、0も可）です。無音の前後区間・空の構成の長さを保存できます。イベントの削除／クロップ命令ではありません。記載長を超えるノートやゲートも保持し、表示・書出では「指定配置長」「配置内容の範囲」「有効ノートの終了」を区別します。未指定なら長さ不明と、素材から算出した表示長を混同しません。旧仕様同様、実演奏終端は有効なノートgateEndの最大値、ノートがなければ0です。

任意`barOrigin`は最初の完全小節の始点です。省略時は0として小節を計算するだけで、保存値を補完しません。0より大きいとき、初期拍子の一小節長`ppq*4*numerator/denominator`未満とし、0とbarOriginの間に拍子変更を置きません。区間[0,barOrigin)は弱起表示、barOriginを小節1の先頭とします。負の絶対時刻を作りません。

barOrigin以降は現在の拍子で小節を積算します。小節途中の拍子変更では直前の小節を部分小節として終え、変更位置から次の小節番号を開始します。元々小節境界なら余分な空小節を増やしません。小節長が分数tickでも計算は有理数のまま行い、実イベントのtickは整数のまま保持します。

## 7. 和声・ボイシング・実演奏の分離

chordsとscalesは空でもよく、それぞれstartの非減少順、重なりを許します。Chordの必須項目はid,start,duration,非空label。rootとintervalsは両方あるか両方なし。bassは任意。intervalsは0～35の整数、0を含む厳密昇順・重複なしで、14を2へ丸めません。

labelだけのコードも有効です。各ソフトの独自コード解析を標準の構造化解釈と偽りません。root/intervals/bassとlabelやvoicingの差は診断できても、自動的に書き換えません。

`voicing.pitches`は順序と同音の重複を保持する0～127の非空配列です。velocitiesは省略でき、ある場合はpitchesと同じ長さ・同じ位置対応、要素は1～127またはnull。nullは未指定であり0ではありません。並べ替えるなら音高とVelocityを対で移動します。

ボイシングはGate/trackを持たないスナップショットです。Coreノートの代わりではありません。コード試聴や伴奏実体化は明示操作に限定し、保存済みトラックと重ねて自動発音させません。voicing.velocitiesと実ノートvelocityも別の値です。

## 8. トラック・クリップ・ノート・打楽器

Trackはid,name,clips必須。role、instrument（name必須・family任意）、enabled、trackType、preferredView、soundSource、localizedNames、drumKitId、4.0の`midi`は任意です。enabledの解釈既定はtrue。trackTypeはmelodic/drum/mixedで、melodicにはpitchノート、drumにはsoundSlotIdノート、mixedには両種類を許します。未指定の空トラックを勝手にdrum等と断定しません。trackTypeはDAWトラックの種類ではありません。

Clipはid,start,duration,notes必須、name,enabled,localizedNames、4.0の`midiEvents`任意。startは絶対tick、notesとmidiEventsのstartはローカルtickです。各配列はstart非減少を基本とし、同時刻のMIDI Eventはeffective order、その後保存配列順を維持します。`onset = clip.start + note.start`、`eventAt = clip.start + midiEvent.start`、`gateEnd = onset + duration`。絶対onset/eventAtは0以上、演算結果はMAX以内。弱起、clip後方の発音、clipをまたぐゲート、同音重複、clip境界外の明示MIDI Eventを黙って省略・短縮しません。

Noteはid,start,durationと、pitchまたはsoundSlotIdの**どちらか一つ**が必須。pitchは0～127（60=C4、69=A4）。任意velocityは1～127、4.0の任意`channel`は1～16です。未指定値を保存時に推測で埋めません。NoteのchannelはNote Onと対応Note Offの両方に適用し、途中で別Channelへ移動する意味にはしません。ゲートは音源のリリース時間・一発音のサンプル長・楽譜上の音価ではありません。3.5ではNote自身にも任意`enabled`を持ち、省略時trueと解釈します。実効有効状態は`track.enabled && clip.enabled && note.enabled`です。falseのNoteは削除せず保持し、Note On/Offを発生させません。

### 8.1 Note On / Note Offの完結

任意`velocity`はNote On Velocityです。3.5の任意`releaseVelocity`は0～127のNote Off／Release Velocityです。未指定は「値がない」であり0や64を自動挿入しません。DAW／MIDI出力先がRelease Velocityを保持できない場合は損失として報告します。Note On Velocity 0を保存済み演奏Noteの代用品にせず、鳴らさない編集状態は`enabled:false`を使用します。

### 8.2 Note ProbabilityとVelocity Deviation

任意`probability`は0.0～1.0で、省略時1.0。0.0は抽選上必ず発音しないが、編集Muteである`enabled:false`とは区別します。抽選は実効enabledなNoteにだけ適用します。PRNG、乱数系列、複数Note間の相関は4.0でも標準化しません。完全に決定的な交換が必要なら、明示操作で結果を通常Noteへ実体化し、probabilityを省略します。読込だけで再抽選して保存内容を書き換えません。

任意`velocityDeviation`は整数で、`velocity`がある場合だけ許します。値は基準velocityからもう一方の端点までの差で、意味規則として`1 <= velocity + velocityDeviation <= 127`を満たします。実際の発音Velocityはその二端点の間からホストが選べますが、選択アルゴリズムは規格化しません。完全再現が必要なら明示的に通常velocityへ実体化します。省略時0と解釈するだけで保存時に0を書き足しません。

### 8.3 Musical PitchとFixed MIDI Trigger

pitch Noteの任意`pitchRole`は`musical`または`fixedTrigger`で、省略時`musical`です。`soundSlotId` Noteには`pitchRole`を付けません。`musical`は通常の音楽音高としてキー・スケール・コード・相対音・移調・メロディー解析の対象になります。`fixedTrigger`はKeyswitch、Articulation selector、Sampler／Pattern trigger等の**そのMIDIキー番号自体を固定して送るNote**です。

`fixedTrigger`は通常Noteと同じstart/duration/velocity/releaseVelocity/enabled/probability/velocityDeviationを持てますが、半音移調、Key変更、Chord/Scale追従、相対音割当、メロディー音域解析、歌詞alignmentの対象にしません。確定Transposeでもpitchを変更せず、DAWへは保存された0～127のMIDI Note番号をそのまま貼り付けます。音源固有の「pizzicato」等の意味をCoreへ推測登録せず、Triggerの意味は音源側の契約です。CC等で実現する奏法切替は4.0の`midiEvents`で表します。

SoundSlotはid/name必須、role/midiNote/midiMapping/localizedNamesは既存の任意項目です。IDが音楽上の発音対象、midiMappingは外部MIDI対応です。gm1は35～81、customは0～127。customの36をGM Kickと断定しません。midiNoteとmidiMappingを併記するときは番号一致を要求します。番号が同じでも異なるSlotを統合しません。

DrumKitはid,name,soundSlotIds必須、localizedNames任意。順序付きの所属であり音源プリセットではありません。track.drumKitIdを使うときはそのtrack中の全Slot参照がキットに所属し、参照自体も存在することを要求します。Slotを複数Kitで共有することは可能です。

SoundSourceはunassigned/gm1/externalMidi/plugin/hostManagedという情報上のヒントで、identifierを許す種類もSchemaどおりです。音源の自動実行、プリセット復元、機器への自動送信を要求しません。プレビュー用音源を選んでもCoreのInstrumentやSlotを書き換えません。

Mixedのpitch:36とSlotのGM36は別対象です。外部MIDI出力で合流する場合、分離ルーティングまたは情報損失確認が必要です。同音同chの重複、Slot ID消失、PPQ丸め、未対応マッピングも黙って解消しません。未割当SlotからGM番号を推測して正式書出ししません。Player内の近似試聴音とMIDI互換性は別です。

### 8.4 MIDI ChannelとTrack MIDI Mode

MIDI Channelの保存値は**1～16**です。MIDI 1.0 wireのstatus下位4bitへ変換するときだけ`channel - 1`とします。0～15をOSTF Channel値として保存しません。

Trackの任意`midi`は`mode`必須で、`busId`任意です。modeは`singleChannel`, `multiChannel`, `mpe`です。

- `singleChannel`では`channel`必須。Note/MIDI Eventのchannel省略時はTrack channelを継承し、明示値を持つ場合はTrack channelと一致させます。
- `multiChannel`ではTrack-level channelを置きません。**全Concrete Noteと全MIDI Eventにchannelを明示**します。
- `mpe`ではTrack-level channelを置かず`mpe`設定必須。**全Concrete Noteと全MIDI Eventにchannelを明示**します。`pitchRole=musical`のpitch Noteは当該ZoneのMember Channelを使用します。Master ChannelはZone共通制御用です。

Track MIDI設定自体がないことは、MIDI Channelを推定してよい意味ではありません。4.0で定義するMIDI EventはすべてChannel Voice/Mode相当なので、自身のchannelまたはsingleChannelの継承により**有効Channelが一意に決まることを意味適合要件**とします。ReaderはC1等を勝手に補完して正常扱い・保存しません。Track MIDI設定なしでもEvent自身がchannelを持てば有効です。

### 8.5 Logical MIDI Busと複数Port境界

任意ルート`midi.buses[]`の各Busは`id,name`必須です。表示名の翻訳は既存`localization`を使用します。Busは**文書内の論理的なMIDI出力空間**で、各Busが独立した1～16 Channel空間を持ちます。同じChannel 1でも異なるBusなら別の論理出力です。

`track.midi.busId`は存在するBusへ解決します。省略は「Bus未指定」であり、配列先頭BusやMain Portを自動選択する意味ではありません。同じBus/Channelを複数Trackが共有することは可能で、その場合Program/CC/Pitch Bend等のChannel stateも共有される実演奏として扱います。衝突が疑われても別Channelへ自動移動しません。

BusにはOSのPort名、USB Device ID、MIDI Interfaceの物理Port番号、Ableton Live/Cubase等のTrack番号、Plugin instance、Audio outputを保存しません。Hostは読込後に`Logical MIDI Bus → local physical/virtual destination`を別設定として対応付けられます。3.5から残る`soundSource.identifier`は情報上のopaque hintであり、4.0の物理Port正本には昇格しません。

### 8.6 MIDI Event共通規則

`clips[].midiEvents[]`はNote以外の演奏制御です。全Eventは`id,start,type`必須。`start`はClipローカルsigned tick、`order`は任意signed整数で省略時1です。Channelを持つEventの有効Channelは前節の規則で決定します。

対応するtypeは次の6種です。

| type | 追加必須値 | 範囲・意味 |
|---|---|---|
| `controlChange` | `controller`, `value` | controller 0～119, value 0～127 |
| `channelMode` | `controller`, `value` | controller 120～127, value 0～127 |
| `programChange` | `program` | wire値0～127。UIは1～128表示可 |
| `pitchBend` | `value14` | 0～16383、中央8192 |
| `channelPressure` | `value` | 0～127。Channel Aftertouch |
| `polyPressure` | `pitch`, `value` | pitch/valueとも0～127。Poly Aftertouch |

Control Change 120～127を`controlChange`として保存せず`channelMode`を使用します。未知／未定義Controller番号も0～119の範囲なら番号を保持し、既知の別Controllerへ変換しません。

Bank Selectは専用の`bank`フィールドを新たな正本にしません。MIDIと同じくCC0（Bank Select MSB）、CC32（Bank Select LSB）、Program Changeのイベント列で表します。同様にRPN/NRPN、14-bit CC pair、Data Entry等も4.0.0では意味をまとめた別Eventへ変換せず、元のControl Change列として保存できます。Program/BankのUI上のまとめ表示は派生表示です。Program Changeを受け取っただけで`track.instrument`や`soundSource`を現在の音源名へ自動書換えず、これらは別の情報層として保持します。

Pitch Bendの`value14`はBend幅の半音数ではありません。Pitch Bend Sensitivity等はRPNとして保存されるReceiver stateです。`value14`から±2 semitone等を推定してCoreへ書きません。

### 8.7 targetNoteIdとPer-note Expression

`controlChange`, `pitchBend`, `channelPressure`, `polyPressure`は任意`targetNoteId`を持てます。これはOSTF上の意味的な関連付けで、wire上のChannel/Pitchを置換しません。参照先は同一文書の**pitch Note**とします。MPEのper-note表現として使う場合は`pitchRole=musical`のNoteを対象にします。Sound Slot NoteをtargetNoteIdへ割り当ててmidiMappingからpitchを推測しません。

`targetNoteId`はEventと同じTrackに属するNoteへ解決します。`polyPressure.targetNoteId`を持つ場合、Eventのpitchと対象Note.pitchを一致させます。EventとNoteの有効Channelも一致させます。MPE等でtargetNoteIdを使っても、Event channelを省略してよい根拠にはしません（singleChannel継承を除く）。

MIDI Event自身には4.0.0でevent-local muteを設けません。Eventは親Track/Clipが有効なときだけscheduleします。さらに`targetNoteId`を持つEventは、対象Noteが`enabled`および`probability`の結果としてその再生回に実際にscheduleされた場合だけ送ります。対象Noteが発音しない回に、そのNote専用のPitch Bend/CC/Pressureを別Noteへ漏らしません。targetNoteIdを持たないraw Channel EventはNote抽選とは独立してscheduleします。Noteを鳴らさない回でも必ず送る必要があるPitch Bend Reset等は、意味的にNote専用でなければtargetNoteIdを付けずraw Eventとして保存します。

### 8.8 MPE

MPEは独自の`mpePitch`等のEvent型を作りません。通常のNote、Pitch Bend、Channel Pressure、Control Change等を個別Channelへ割り当てる方式として表します。

`track.midi.mode="mpe"`では`mpe.zone`と`mpe.memberChannelCount`を必須とします。`zone="lower"`のMaster Channelは1、Memberは2から昇順にcount個。`zone="upper"`のMaster Channelは16、Memberは15から降順にcount個です。masterChannel/memberChannelsを別フィールドへ重複保存しません。

MPE ZoneのProgram Change、Pedal等の共通制御は必要に応じてMaster Channel上の通常MIDI Eventとして保存し、Note固有のPitch Bend/Pressure/CCは対象Member Channelへ保存します。MPE設定そのものをMIDIへ送るためのRPN列を保持する場合も通常CC Eventとして保存できますが、Trackの`mpe`設定はOSTF上の意味的なZone宣言です。両方が矛盾する場合は警告し、黙って片方を書換えません。

同じLogical Bus上で同じ`zone`を複数Trackが宣言する場合、`memberChannelCount`は一致させます。同一Bus上のLower ZoneとUpper ZoneはMember/Masterを含む占有Channelが重複してはなりません。複数Trackが同一Zone宣言を共有すること自体は可能ですが、具体Note/EventのChannel競合を別Channelへ自動修復しません。

### 8.9 同一tickのGlobal MIDI順序

同じLogical Busへ複数Track/Clipからイベントが集まる場合も、絶対tickとorderを使用します。基本順序は`absolute tick → numeric order → event kind tie rule`です。Note Offはimplicit order 0、MIDI Event省略値は1、Note Onはimplicit order 2です。MIDI Event同士でtick/orderが同じ場合、同一Clip内は保存配列順、異なるClip/Track間は`trackId → clipId → eventId`の辞書順を決定的なtie-breakerとします。

作者が同tickのCC0→CC32→Program Change等の厳密順を必要とする場合、同一Clip内の配列順または異なるorderを使用します。実装は同tickだからという理由でController/Program/Pitch Bendを種類別に勝手に並べ替えません。

## 9. 歌詞・言語・主歌詞

lyricsはdocuments,phrases,units,alignmentsの4配列必須で、4.0の`voices`は任意です。空でも有効です。documentはid必須、title/language任意。phraseはid,documentId,text必須、unitはid,phraseId,text必須。どちらもpronunciationと、start/durationの対を任意に持ちます。時間を持つなら絶対tickで終端もMAX以内です。

textが表示原文、pronunciationが発音注記です。自動分割・自動転写・歌唱エンジンの命令ではありません。unitの連結がphrase本文と一致することを要求しません。alignmentのunitIds/noteIdsはそれぞれ非空・重複なしの順序付き配列、実在する`pitchRole=musical`のNote等の正しい対象へ解決します。`fixedTrigger`を歌詞音として割り当てません。複数単位と複数音の関係を保存でき、alignmentから追加ノートを生成しません。4.0の任意`voiceId`を持つalignmentでは、unit側のdocumentが当該Voice.documentId、note側の所属TrackがVoice.trackIdに一致しなければなりません。

`song.languages`は楽曲全体の言語メタデータ、歌詞document.languageは当該文書の言語です。混在を許し、一方から他方へ自動複写しません。song.languagesの省略は不明、空配列は登録なしであり、器楽曲や英語を推測しません。BCP 47表記を推奨しますが、認識できない原文を破棄・正規化しません。言語配列の大文字小文字だけが違う重複は不正です。

代表歌詞は明示されたprimaryLyricDocumentIdのみ。複数言語・複数版の歌詞を一つに結合しません。訳詞は別文書と割当として扱い、名称の翻訳機能で歌詞本文を置換しません。ノートの移動・削除でalignmentを壊す操作は参照を明示的に更新するか、損失を確認するか、中止します。4.0の`targetNoteId`付きMIDI Eventも同じくCore参照なので、対象Noteを削除・別文書へ分離する操作ではEvent参照を一緒に更新／削除するか操作を中止します。CoreのalignmentやtargetNoteIdはstaleフラグで不正参照を許容しません。

### 9.1 複数ボーカル・コーラス歌詞

`lyrics.voices[]`は`id,trackId,documentId`必須、`name,role`任意です。roleは開いた文字列で、共通推奨値として`lead`, `harmony`, `backing`, `unison`, `double`, `counter`, `adlib`, `response`を認識できますが、未知roleを削除・別roleへ丸めません。

同じLyric Documentを複数Voiceが参照できます。LeadとHarmonyが同じ本文を歌うだけならDocument/Phrase/Unitを複製せず、それぞれのVoiceとAlignmentで別のNote集合へ対応付けます。別の歌詞を歌うBacking/Response等は別Documentを参照します。

Voice.trackIdは存在するTrack、documentIdは存在するLyric Documentへ解決します。VoiceのTrackを`melodyTrackIds`へ含めることを推奨しますが、歌詞Voiceであることだけを理由にWriterが自動追加しません。既存`primaryMelodyTrackId`と`primaryLyricDocumentId`の両方に一致するVoiceが一意ならUIはLead候補として提示できますが、4.0は新しい第三のPrimary正本を作りません。


## 10. ジャンル・ムード・クレジット・権利・素材

song.genresとsong.moodsは任意で、要素はid,name,externalUri?。固定のジャンル／ムード表を設けません。配列順は著者の表示順、同名の異なるIDも保持します。未指定・空・未知名をPopや既定Moodに変換しません。externalUriがあっても読み込み時に取得せず、原文nameを上書きしません。URIは絶対URIとし、その実在を形式適合要件にはしません。

contributorsはid,name,kind?,localizedNames?、song.creditsはid,contributorId,role,label?。roleは既存の開いたASCII意味識別子。参照は実在のcontributorへ解決します。data-editor、software-developer、composer等を同一視しません。氏名の一致で人物を統合しません。

song.rightsはnotice/licenseUri/rightsHolderIdsの任意集合で一つ以上を持ちます。rightsHolderIdsはcontributorsへの重複なし参照です。licenseUriは著者が記載した絶対URI。形式への保存は権利の認証・付与ではありません。未記載のライセンスや著作者を補いません。

resourcesはid,kind,uri必須、name,sha256任意。kindはaudio/midi/text/other。uriは素材参照であり、音声トラックの発音や自動ダウンロード命令ではありません。相対URIは当該OSTFファイル位置を基準に、利用者の明示操作時に解決します。外部取得・プラグイン実行・スクリプト実行は読込だけでは行いません。素材未取得はノート内容の不正を意味しません。

## 11. 共通編集情報のCore化と状態

旧標準拡張の機能を次の正式ルート項目へ移します。名前空間や拡張version/data層はありません。構造・意味は3.4.0に含まれます。

| 3.4 Core | 保存する型付き情報 | 旧保存先（移行元のみ） |
|---|---|---|
| relativePhrases | assignments | org.ostf.relative-phrase.v1 |
| generation | processes | org.ostf.generation-context.v1 |
| presentation | roleDefinitions,sectionRoleAssignments,appearance | org.ostf.appearance.v1 |
| phraseLibrary | templates,instances | org.ostf.phrase-library.v1 |
| clipChoices | groups | org.ostf.clip-choices.v1 |
| localization | entries | org.ostf.localization.v1 |

各Core項目にはstatusとdependenciesが必須です。status=currentは現在のCoreとの対応一致、staleは不一致が判明、unverifiedは未確認です。成熟度や実行成功を意味しません。dependenciesはscope=none/document/objects（objectsなら非空・重複なしrefs）です。

currentではすべての参照を解決し、意味上の対応を満たします。objectsなら当該項目から参照するCore対象をすべて列挙します。列挙できない場合はdocument。親clip/trackの移動やenabled変更による子の絶対位置・有効状態の変化も依存対象の変更です。翻訳・表示・生成・フレーズに参照があるのにnoneと宣言してはいけません。songの翻訳など、Refで対象を列挙できない関係にはscope=documentを用います。

関連するCoreを編集するとき、関係を再計算して一致を確かめるか、stale/unverifiedへ変更します。未対応の編集関係をcurrentのまま残しません。状態の書換えだけを新しい音楽編集として再帰的に無効化しません。stale/unverifiedの参照・内容不一致は警告として保持しますが、型不正・ID重複・管理対象の二重所有は許しません。Core本体の不正参照にもこの緩和を適用しません。

読み込み時には再生成・再抽選・候補の適用・原型の同期を行いません。現在の演奏は常にCoreトラックです。

### 11.1 相対音

assignmentはnoteId,basis,contextId,anchorPitch,index,chromaticOffset。basisはchordTone/scaleDegree。同一noteIdへ重複assignmentを作りません。assignment対象は`pitchRole=musical`のpitch Noteだけで、`fixedTrigger`やSound Slot Noteを参照しません。contextIdはChordまたはScale（song.scaleもScale）で、anchorPitchのピッチクラスはroot/tonicに一致します。

`note.pitch = anchorPitch + context.intervals[index-1] + chromaticOffset`。indexは1始まりで実際の配列長以内、offsetは−24～24。結果は0～127。コード記号の「5th」と配列の5番目を同一視しません。文脈区間外の弱起でも明示的ID参照の関係だけで拒否しません。

staleな相対情報で実ノートを上書きしません。最適な声部進行や新しいコードへの追従方法は、標準の自動実行としては定めません。

### 11.2 生成履歴と生成意図

generation.processesの要素はid,generator,inputs,outputs,protectedNoteIds必須。targetRangeとintentは任意。generatorは非空id/version。inputsはrole,ref,readRange?、outputsは非空Ref配列、保護IDは重複なしです。inputsは空も複数も許します。

intentはgenreNames,moodNames,groove,prompt,seedの明示した項目だけを許します。seedは文字列で精度を保持します。これらは生成意図の記録で、エンジンをまたぐ同一結果を保証しません。promptを自動実行・外部送信してはいけません。標準化していない内部パラメーター辞書やvendorExtensionは3.4のgenerationに設けません。

Grooveにはname、およびunitTicks/longWeight/shortWeightの三つ組を記録できます。三つ組は全部あるか全部なし。unitTicksは元の一分割のtick長、隣接二分割を対とし、比率L:Sなら対の2*unitTicks内の二つ目の開始は`2*unitTicks*L/(L+S)`という生成意図を表します。確定演奏へ再適用しません。明示的に生成する場合に整数tickで表現できなければ、PPQを正確に変更するか損失を確認します。nameから固有グルーヴの音楽的意味を自動推測しません。

生成Genreはsong.genresの代わりではありません。Moodも同様です。適用範囲はinputs/targetRange/outputsで記述し、セクションの名前から推測しません。

保護するnote集合は操作前に固定します。ID、発音対象、pitchRole、絶対onset、duration、velocity、releaseVelocity、probability、velocityDeviation、4.0のchannelの有無と値、およびtrack/clip/noteを合わせた実効enabled状態を比較します。保護リストを操作後に削除して保護を回避してはいけません。PPQの変更は有理時間として正確比較できる場合以外は保護比較を拒否します。テンポによる実秒数・音源音色は別の編集対象であり、tick保護と同じ保証にしません。

### 11.3 表示と役割

presentationのroleDefinitionsはid/name/baseRole?、sectionRoleAssignmentsはsection ID→roleDefinition ID。appearanceはroleColors/customRoleColors/objectColors。色は#RRGGBB、objectColorsはtarget/color、同一target重複は禁止です。

色の優先順は、sectionでは自身のobjectColor→割当役割のcustomRoleColor→そのbaseRoleのroleColor→section.roleのroleColor→ホスト既定。track/slotは自身→roleColor→既定。clipは自身→親track、noteは自身→親clip。その他は自身→既定。名前・色から音楽的なroleや発音を決定しません。未解決の色参照を同名対象へ付け替えません。

### 11.4 再利用フレーズとVelocity

Templateはid,duration,notes必須、name任意。durationは反復周期。source notesは具体Noteと同じくid/start/durationとpitchまたはsoundSlotId、任意velocity/releaseVelocity/enabled/probability/velocityDeviation/pitchRoleを持てます。IDはそのTemplate内でのみ一意、source notes自体は発音しません。

Instanceはid/templateId/clipId/repeatCount/transpose/noteMap必須、velocityModeと3.5のnoteStateModeは任意。Template/InstanceのIDは4.0でもグローバルCore IDです。一つのclipを複数Instanceで所有できません。noteMapはtemplateNoteId/repeatIndex/noteId。繰返しごとのsource note発生と全Core clip noteが過不足なく一対一に対応します。

```
clip.duration = template.duration * repeatCount
note.start = repeatIndex * template.duration + sourceNote.start
note.duration = sourceNote.duration
if sourceNote.pitchRole is omitted or musical:
    note.pitch = sourceNote.pitch + instance.transpose
if sourceNote.pitchRole == fixedTrigger:
    note.pitch = sourceNote.pitch                         # 絶対MIDIキー、移調しない
note.soundSlotId = sourceNote.soundSlotId                 # Sound Slotも移調しない
```

source pitch Noteとmapped concrete Noteの実効`pitchRole`は常に一致させます。`fixedTrigger`をmaterialize/refreshしただけで別MIDIキーへ移動してはいけません。

repeatIndexは0以上repeatCount未満。同一発生の重複、mapped noteの二重所有、clipの二重所有は禁止です。音高・演算後時刻も範囲内とします。弱起・テールを省略しません。currentの整合検査で巨大な直積を生成する必要はなく、件数と各mapを調べられます。

velocityModeの解釈既定はindependent。これは実ノートのVelocityが原型と独立で、原型の明示更新後も存続note IDのVelocityを保持するモードです。新たなノートを実体化する明示操作では原型のVelocityを初期値として複写できますが、その後は自動同期しません。linkedでは、mapped noteとsource noteのVelocityについて、未指定か否かと数値が完全に一致する必要があります。モード変更だけで実ノートを書き換えず、必要な更新を一括操作として提示します。

3.5の`noteStateMode`も省略時`independent`です。対象は`enabled`, `releaseVelocity`, `probability`, `velocityDeviation`です。independentでは原型の明示更新後も既存Concrete Noteのこれらの値を維持し、新規materialize時にだけ原型の明示値を初期複写できます。linkedでは各フィールドの「省略か明示か」と値をSource NoteとConcrete Noteで一致させます。`velocity`は従来どおりvelocityModeの責任で、pitchRoleは両モードと独立して常に構造的に一致させます。

4.0の`channel`はPhrase Source Noteへ追加しません。特にMPE Channelはmaterialize後のConcrete Performance配置であり、再利用フレーズの音楽原型の正本ではありません。Phrase refreshで存続するConcrete Noteのchannelを保持します。multiChannel/MPE Trackへ新しいConcrete Noteをmaterializeする操作は、確定前に有効channelを明示割当し、原型やpitchからChannelを推測しません。

原型置換は影響する全Instance・Core notes・依存関係を原子的に更新するか失敗します。存続する(repeatIndex,templateNoteId)は既存noteIdを維持します。リンク解除は該当Instanceだけを取り除きCore clip/notesを保持します。勝手に未使用Templateを削除しません。無限反復・確率的な読込時展開は扱いません。

### 11.5 クリップ候補

Groupはid/candidates/selectedCandidateId必須、name任意。Candidateはid/clipIds必須、name任意。グループは候補を一つ以上持ち、候補のclipIdsは重複なしで空の無音候補も可。選択IDは当該候補IDかnull。3.4ではGroupとCandidateのIDもCore全体で一意です。

一つのgroup内で同じclipを複数候補が共有できますが、異なるgroupの管理集合を重ねません。currentでは管理clip自身のenabledが選択候補への所属と一致し、nullならすべて無効です。親track.enabledと各note.enabledは別のミュートで変更しません。

選択を変更する操作は全管理clipと選択IDを一括更新します。読み込んだだけでは選択を適用せず、矛盾を診断します。4.0ではclip.enabledがそのClipのNoteだけでなく`midiEvents`のscheduleにも適用されるため、候補切替時にController/Program等だけが無効Clipから漏れないようにします。これは既に実体化された演奏clipの組合せであり、曲構成・和声・歌詞を含む全曲シーンではありません。

### 11.6 多言語表示

localization.entriesはtarget/field/values。targetはkindと、song以外ではグローバルCore id。旧profile指定はありません。valuesは言語タグ→非空翻訳です。タグの大文字小文字だけが違う重複を禁止します。SchemaがBCP 47全体を検証するとは主張しません。原文の値を残し、翻訳のない場合は原文に戻します。

| kind | 翻訳可能なfield |
|---|---|
| song | title,subtitle,description,key.label,rights.notice |
| alternateTitle | title |
| contributor,section,track,clip,soundSlot,drumKit,resource,phraseTemplate,clipCandidate,clipChoiceGroup,roleDefinition,genre,mood,**midiBus,lyricVoice** | name |
| track（追加） | instrument.name |
| credit | label |
| lyricDocument | title |
| keyChange | label,key.label |
| scale | label |

currentでは原文フィールドの存在を要求します。同一対象・field・言語は重複禁止。既存localizedNames/localizedTitlesと同じ翻訳を併記する場合は文字列が完全一致しなければなりません。新規作成はlocalizationへ集約を推奨しますが、旧フィールドも保持します。歌詞本文、音名、コード値、ID、URI、role、modeの意味を翻訳機能で変更しません。

## 12. 文書同一性・履歴・マージ

任意documentはid/revisionId必須、parents/createdBy/modifiedBy任意。idは同じ作業文書の系列、revisionIdは内容が変わるごとに新たに割り当てる不透明な識別子です。単なる再保存で意味内容が変わらなければ維持できます。新たな独立コピーでは新id、元から派生する場合はparentsへ元の組を記録します。同一idの分岐は異なるrevisionIdで区別します。再編集・Undo後の新保存も新しいrevisionとし、過去の組を再利用しません。

parentsの要素はdocumentId/revisionId必須、sha256任意。自分自身と同じ組を親にしません。同一組の重複を禁止し、同一組に異なるhashを付けることも禁止します。IDや親の宣言だけで改変防止・本人認証・安全な自動マージを保証しません。履歴グラフ全体の検証は利用可能な履歴がある場合だけです。

provenance.recordsはid/action必須、description/tool/sources/semitones/beforeKey/afterKey任意。actionはcreate/import/conversion/edit/transpose/merge/generation/other。semitonesを記載できるのはtransposeだけです。現在の音楽値を上書きする命令ではなく、過去の自己申告履歴です。sourcesのdocumentId等は過去文書を指すため、現在のCore IDへ解決しません。resourceIdだけは現在のresourcesへ解決します。ハッシュは入力原本の正確なバイト列で、出力自身のハッシュを自分に埋め込みません。

マージは次の契約で行います。フォーマット自体がどのアプリにも全曲を書き換える権限を与えるものではありません。

- **既定は担当対象だけ。** Drumは明示選択したdrum/mixed対象、Song Writerは明示選択した主旋律等。トラック名や配列位置だけで担当を決めません。未指定primaryMelodyTrackIdを勝手に新しいトラックへ振り替えません。
- **共有情報を別途比較。** 構成、テンポ、拍子、キー、スケール、ジャンル、クレジット、歌詞は独立の差分・承認対象。ノートのマージに便乗して上書きしません。Baseがない場合は安全な三者マージができると主張しません。
- **4.0 Track MIDIも担当対象と参照を分離。** 担当Trackをマージするとき、そのTrackのConcrete Note `channel`、Clip `midiEvents`、Track `midi`設定は担当演奏データとして一緒に比較できます。ただしRoot `midi.buses`は共有参照情報です。取り込むTrackが未知`busId`を参照する場合、対応Busを明示的に取り込むか利用者が既存Busへ対応付けます。同名Busや同じ配列位置へ黙って付け替えません。
- **文書IDを越えて同一IDを盲信しない。** 独立文書の同じnote/slot IDは衝突し得ます。新しいID対応表を作り、既知の全参照を一緒に更新します。未知拡張の内部参照を推測で変更しません。必要な参照を安全に維持できなければ統合を中止します。
- **PPQは有理数で整合。** `tick / ppq`を正確な時間として比較し、整数に正確変換できる共通PPQを使います。LCMが960000超、演算後MAX超、または丸めが必要なら黙って処理せず拒否か明示的な損失確認。ノートだけでなく全時間フィールド、range、フレーズ周期、Groove単位も対象です。
- **位置移動とテンポ変更は分離。** セクションやclipを移動しても、関連するキー/テンポ/拍子が自動で追従するとは限りません。移動対象・取り残す対象と新境界をプレビューし、一括で確定します。
- **全体を原子的に保存。** 操作中の失敗で一部変更された正本を残しません。参照・保護・依存状態を確認してから別名または一括保存します。Unsupported Coreの保持ができないWriterはその編集を拒否します。

マージ時に未知データや未解釈のCore値を失わず保持する要件は、生成機能への対応とは別です。特定デバイスが各標準編集機能を実行できることまでは要求しませんが、非対応を理由に消去してはなりません。

## 13. 旧版・独自拡張との移行境界と3.5→4.0

3.5以前を直接4.0として扱いません。既存原版の読込、旧データの意味を示した移行プレビュー、明示的な4.0保存を分離します。

3.5→4.0の最小移行では既存Core値を変更する必要はありません。`version`を4.0.0として保存する明示操作時にも、MIDI情報が存在しない曲へ`midi`, `track.midi`, `note.channel`, `clip.midiEvents`, `lyrics.voices`, `song.melodyTrackIds`を推測で追加しません。

既存`primaryMelodyTrackId`から`melodyTrackIds:[primary]`を作ることは意味を増やさない移行候補として提示できますが、自動追記は必須ではありません。Track名、role、歌詞Alignment、音域から他のMelody Trackを推測追加しません。既存複数Lyric DocumentからVoiceを推測せず、Lead/Harmony/Backingの関係がユーザーまたは移行元の明示情報から分かる場合だけ`lyrics.voices`を作成します。

MIDI／DAW／旧拡張から4.0 Eventを移行する場合は、元データが明示したChannel、Controller番号、Program、Pitch Bend 14-bit値、Pressure値、同tick順序を保持します。Program番号のUI 1～128表示を保存値へ取り込むときはwire値0～127へ明示変換し、どちらの番号体系か不明なら推測変換しません。Bank SelectはCC0/32として保持します。

3.5 `soundSource.identifier`にPortらしい文字列があってもLogical MIDI Busや物理Portへ自動昇格しません。Logical Busはユーザー／移行元が同一出力空間だと明示できる場合だけ作ります。物理Port名はHost設定へ残します。

旧拡張に4.0相当の情報がある場合、既知の意味と版が確認できるものだけCoreへ移行します。移行できない未知拡張は原本を保持し、不明なCC/Aftertouch/MPE意味を推測しません。4.0 Coreと旧拡張が矛盾するときはCoreを現在の正本とし、旧データあり・未移行／矛盾として警告します。

4.0から3.5以下へ保存すると、少なくともMIDI Event、Note Channel、Track MIDI Mode/Bus、MPE宣言、複数Melody集合、Lyric Voice、Alignment.voiceIdを失う可能性があります。削除されるパス・参照・関係を提示し、確認なしのダウングレードを禁止します。MIDI Eventを3.5 extensionsへ押し戻すことを標準の下位互換とは定義しません。

3.5→4.0の詳細な移行意味は本節と4.0確定仕様を継承します。4.0→4.1は[本版の移行方針](MIGRATION.ja.md)を参照します。

## 14. 継承Coreの責任範囲と将来版への境界

4.2.0は4.1.0と4.0.0のCore演奏正本を継承します。Concrete Note、Logical MIDI Bus、MIDI Channel、Control Change、Channel Mode、Program Change、Pitch Bend、Channel/Poly Pressure、MPE Zone宣言と同tick順序、複数Melody Track、複数Lyric Voiceに加えて、4.1ではTrack DirectionsとInstrument Playable Pitch CapabilityをCoreへ追加します。

OSTFはMIDIファイルのJSON化やDAW Projectの代替を目的にしません。Noteは引き続き`notes[]`が音楽・演奏Noteの正本で、Note On/Offを`midiEvents[]`へ二重保存しません。MIDI EventはNoteを補助する時系列制御です。Program/CC/Pitch Bend等をNote属性へ埋め込まず、逆にNoteをController streamへ解体しません。

Logical BusまでをPortableな曲情報とし、その先のPhysical/Virtual MIDI Port、USB device、DAW destination、Plugin instance、Audio routingはHost設定です。Busから実環境へのMappingがなくてもOSTF文書自体は有効です。

System Exclusive、MIDI Clock/MTC/MMC、MIDI Show Control、MIDI 2.0 UMP/Per-Note Controllers、Audio Clip、Plugin state、Automation Lane一般化を4.0.0へ含めません。将来これらを共通交換する必要が生じても4.0.0の既存フィールドの意味を黙って変更せず、4.xの追加または次期Majorで型と移行規則を定義します。

## 15. 適合区分・リリース判定

構造適合はSchema、意味適合は本書のID/参照/時間/関係規則、編集適合は保持・非破壊・損失報告の契約で判断します。Readerは表示できない標準機能を未対応と示せます。Writerは未対応情報を保持できなければ保存を拒否します。音色一致、生成結果の優劣、DAW接続の成功は形式適合とは別です。

本版の策定ではユーザー指定によりAbleton Live/Max for Live、Player、Composer、Editor、各Arranger、実機MIDI機器、音源、UI等の**動作検証をリリース条件にしません**。仕様書・Schema・移行規則・サンプル間の静的整合性確認は仕様策定作業として行えますが、それは実機相互運用性を検証した意味ではありません。

公開可否は[リリースノート](../RELEASE_NOTES.ja.md)に記載します。4.0はMIDI Performanceと複数Melody/Voiceを標準化したMajor版で、4.1はその意味を変更せずTrack Directionsを追加するMinor版です。


## 16. OSTF 4.1 Track Directions

### 16.1 位置付け

4.1では各Trackへ任意の`directions[]`を追加します。これはTrack専用の第二Timelineではありません。全DirectionはOSTF文書共通のPPQ・絶対tickを使用します。Range型は`start`と`duration`、Vendor Point型は`at`を使用します。

Directionは「そのTrackをどう演奏・解釈・生成してほしいか」という意味情報です。Concrete Note、CC、Program Change、Pitch Bend、Aftertouch等の実演奏正本を置き換えません。ファイルを開いただけでDirectionをNote/MIDIへ自動Materializeしてはなりません。

### 16.2 `improvisation`

区間型Directionです。`pitchSource`と`adherence`を必須とします。

`pitchSource.type`は次の4種です。

- `effectiveKeyScale` — 現在有効な`song.key`＋`timeline.keyChanges`から標準ModeのPitch集合を解決
- `songScale` — 明示された`song.scale`を利用
- `harmonyScales` — `harmony.scales[].id`を参照し、Jazz等のChord Scale追従に利用
- `explicitScale` — Direction内部だけのPitch Collection。PentatonicやBlues等の演奏材料に利用

`effectiveKeyScale`の標準Mode解決は、major=`[0,2,4,5,7,9,11]`、minor=`[0,2,3,5,7,8,10]`、dorian=`[0,2,3,5,7,9,10]`、phrygian=`[0,1,3,5,7,8,10]`、lydian=`[0,2,4,6,7,9,11]`、mixolydian=`[0,2,4,5,7,9,10]`、locrian=`[0,1,3,5,6,8,10]`です。未知Mode、atonal、unspecifiedは未解決とし、別Scaleを推測しません。

`adherence`は`strict`または`preferred`。`strict`は生成Pitchを原則Pitch Source内に制限し、`preferred`は主材料としながら経過音・Approach・Ornament等を許容します。既存Concrete NoteがDirectionと一致しなくても再生上のNote正本を自動修正しません。

### 16.3 `playingRole`

指定区間だけ`track.role`を演奏・生成解釈上で上書きします。区間終了後はTrack-wideの`track.role`へ戻ります。代表値は`solo`, `lead`, `accompaniment`, `comping`, `fill`, `counter`, `response`, `unison`, `double`, `bassline`, `pad`, `drone`です。語彙はOpenで、未知値を保持します。

### 16.4 `pitchRange`と`instrument.playablePitchRange`

`pitchRange`は時間付きの一時的な演奏Register指示です。`lowPitch`, `highPitch`, `constraint`を持ち、`lowPitch <= highPitch`。`constraint`は`strict`または`preferred`です。

`instrument.playablePitchRange`は時間に依存しない楽器能力です。5弦BassのLow B等を表現できます。Timed `pitchRange`は宣言済み`playablePitchRange`の内側でなければなりません。4.1では弦数、フレット数、Tuning、Fingering、物理構造までは標準化しません。

### 16.5 Vendor Direction

`type="vendor"`はSoftware独自の演奏指示を安全に保持するための拡張点です。`namespace`, `name`, 任意`version`, `data`を持ち、namespaceはreverse-domain形式を推奨します。`org.ostf`およびその子名前空間はOSTF標準用に予約します。

Vendor DirectionはRange型とPoint型を許します。Breath Point、特殊Gesture、独自AI phrase mode等をSoftware側で実験し、複数Softwareで意味が安定した概念だけ将来Coreへ昇格できます。未知Vendor Directionは動作上無視してよい一方、非破壊Round Tripでは保持します。

### 16.6 `instruction`

任意の自然言語補助指示です。人間やAI対応Softwareが利用できますが、AIサービス実行やNetwork接続を要求するものではありません。構造化Coreパラメータと矛盾した場合は構造化パラメータが正本です。

`instruction`は文書データであり、実行コード、権限付与、外部操作の承認、ApplicationのSystem/Developer命令として扱ってはいけません。AI対応Softwareはこれを非信頼の音楽メタデータとして扱い、外部送信・ファイル操作・ネットワーク操作等を`instruction`だけを根拠に自動実行してはなりません。Vendor `data`も同様にデータであり、コードとして実行しません。

### 16.7 重複・優先順位

異なるStandard Direction typeは同時にActiveで構いません。同一Trackで`improvisation`同士、`playingRole`同士、`pitchRange`同士の区間重複は禁止します。4.1では`priority`、Last Wins、配列順による勝敗を導入しません。

### 16.8 Version・Compatibility

4.0-only Readerが`4.1.0`を4.0として推測解釈してはなりません。4.1を明示認識するCompatibility Playerは、未対応Directionの動作を再生時に無視してConcrete Note/MIDIを再生できます。ただし保存時に未対応4.1 Coreデータを黙って削除してはなりません。

4.0→4.1の最小MigrationはVersion変更だけで成立し、DirectionやPlayable Rangeを推測追加しません。4.1-only情報を含む文書の4.0 DowngradeはLossyです。


# Part B — OSTF 4.2 Vocal Performance

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
