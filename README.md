# ゲームコネクト

<!-- [![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2024/07/JPHACKS2024_ogp.jpg)](https://www.youtube.com/watch?v=DZXUkEj-CSI) -->
[![IMAGE ALT TEXT HERE](./app_image.png)](https://youtu.be/TZA6EsNIHM0)


# 製品URL
実際に下記のURLでサービスを利用することができます。 

https://anime-create.com/hack/gameconnect.html

## 製品概要
### 背景(製品開発のきっかけ、課題等）

コロナ禍で人と人とのつながりが減ってきました。
特に、今回ユーザー層として定めた以下の特徴を持つ人たちは、孤独や運動不足という課題を抱えています。
今回はユーザーとして、仮想ペルソナを以下の特徴を持つ方にしました。
- 10代~20代
- オタク
- 学生
- 男性

すなわち、我々です！
我々技術オタクは、その性質上、孤独になりやすいです。
孤独は寿命を短めます。

### 製品説明（具体的な製品の説明）

<!-- ここは岡崎さんに説明してもらう。もしくはヒアリングをしながら書き起こす -->
#### デモ動画

[![alt text](https://img.youtube.com/vi/TZA6EsNIHM0/0.jpg)](https://youtu.be/TZA6EsNIHM0 "title")

### 特長
#### 1. オフラインのゲームを前提とするため外に出るきっかけを作れる！
#### 2. 人と人とのつながりを深めるため、温かみのある色彩にしました。
#### 3. Webアプリなのでインストールの必要性がない!

### 解決出来ること

このサービスは人と人とのつながりを想像し、ユーザーの孤独と運動不足を解消します！
<!-- ここにボードゲーム業界の活性化の旨を入れる -->

### 今後の展望

- 実装できていない機能
    - 自己紹介文からプレイヤーがどんな人なのかをグラフで可視化する機能
        HTTPS通信が実現できなかった
    

### 注力したこと（こだわり等）

<!-- 黒瀬 -->

- 仮想ペルソナを明確にし、この機能がどのようにユーザーの課題を解決するのか考えながら実装した。
- 人と人のつながりを深めるため、温かみのある色彩を意識した。

<!-- 岡崎さん -->
- 今回のデモで動作するコードは１つのhtmlで完結させた
- オープンソースの地図をはじめ、外部APIを最小限にとどめたことにより拡張性とサーバ費を少なく済ませた
- 私たちだけでなく、トランプやボードゲームなどのゲーム会社にとってメリットがあるアプリを開発した
- Leaflet.jsを使って、チームの開催場所を地図上で確認できる機能を実装した
- チームに参加した後、レビューやチャットを通じてフィードバックを提供できる仕組みを取り入れた

<!-- 浦澤さん -->

- アプリ内の文字のフォントや競合調査をし、ユーザーの人数を数値化した
- 孤独な人とそうでない人の致死率、人数、年代、性別などを調べ、製品背景を意識した




 ;





<!-- これより下は岡崎さんにお願いする -->

## 開発技術
*注意
デモアプリ並び実際の発表時にはフロントエンドの
jphack.htmlのみで動作しfirebaseの設定を除き２日間のみで
完全に０から開発した。

高速開発を実現する為、外部ライブラリHTMLのみを用い
ライブラリも全てCDNの読み込みのみで完結した
加えて、デザインcssもhtmlの１つのファイルで完結した.

以下はデモ発表時に使用したjphack.htmlについて説明する


<img width="477" alt="スクリーンショット 2024-10-27 22 06 47" src="https://github.com/user-attachments/assets/994d94b9-f3a9-49ec-8b59-12b79657910f">

Main Component (メインコンポーネント)<br>
メインコンポーネントはアプリケーション全体のUIの切り替えを管理する中心的な要素である。

2. User Auth Component (ユーザー認証コンポーネント)<br>
ユーザー認証に関連する機能を担当する。Firebase Authenticationを使用し、ユーザーのサインイン・サインアウトや認証情報の管理を行う。

3. User Auth Profile Component (ユーザープロフィールコンポーネント)<br>
ユーザーのプロフィール情報を管理し表示するためのコンポーネント。認証後のユーザー情報をFirebase Realtime Databaseから取得し、ユーザーの名前、自己紹介、過去の参加履歴などのデータを表示・更新する役割を持つ。

4. Team Management Component (チーム管理コンポーネント)<br>
チームの作成・管理を行うコンポーネント。チームの作成時には、ユーザーが指定した情報（場所、人数、日程など）を基にFirebase Realtime Databaseに保存し、チームのマッチングや管理機能を提供する。UI上では、チーム作成フォームや現在のチーム情報を表示・操作可能である。

5. Firebase Realtime Database<br>


### 活用した技術

#### フレームワーク・ライブラリ・モジュール
・Vue.js<br>
・Google Firebase<br>
・Google Firebase Auth<br>
・Google Firebase Realtime Database<br>
・Leaflet.js<br>
・Font Awesome<br>
・Google Fonts (DotGothic16)<br>

#### ハッカソンで開発した独自機能・技術

・Leaflet.jsを用いた直感的な地図操作
・リアルタイムなチーム作成・管理とチャット機能<br>
・ゲーム風のプロフィールステータス管理<br>
・イベント終了後のレビュー機能

