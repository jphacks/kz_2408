# ゲームコネクト

<!-- [![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2024/07/JPHACKS2024_ogp.jpg)](https://www.youtube.com/watch?v=DZXUkEj-CSI) -->
[![IMAGE ALT TEXT HERE](./app_image.png)](https://youtu.be/TZA6EsNIHM0)


# 製品URL
実際に下記のURLでサービスを利用することができます。 

https://anime-create.com/hack/gameconnect.html

> [!IMPORTANT]
> 使用に際して、Google アカウントが必要になります。
> よろしくお願い致します。

## 製品概要
### 背景(製品開発のきっかけ、課題等）

ユーザーは以下の性質を持つ方々としました。
- 10代~20代
- オタク
- 学生
- 男性


現在、2020年1月15日から始まった新型コロナウイルスの影響は収まっています。<br>
しかしながら、コロナ禍で始まったリモートワーク等の習慣から、
ユーザーは孤独や運動不足を抱えるようになりました。<br>
これら課題解決を目指し、ゲームコネクトを開発しました。

### 製品説明（具体的な製品の説明）

#### デモ動画

[![alt text](https://img.youtube.com/vi/TZA6EsNIHM0/0.jpg)](https://youtu.be/TZA6EsNIHM0 "title")

### 特長
#### 1. オフラインのゲームを前提とするため外に出るきっかけを作れる！
#### 2. 人と人とのつながりを深めるため、温かみのある色彩にしました。
#### 3. Webアプリなのでインストールの必要性がない!

### 解決出来ること

このサービスは人と人とのつながりを想像し、ユーザーの孤独と運動不足を解消します！

### 今後の展望

- 実装できていない機能
    - 自己紹介文からプレイヤーがどんな人なのかをグラフで可視化する機能
        HTTPS通信が実現できなかった
    

### 注力したこと（こだわり等）

[@yoshiyuki-140](https://github.com/yoshiyuki-140)
- 仮想ペルソナを明確にし、この機能がどのようにユーザーの課題を解決するのか考えながら実装した。
- 人と人のつながりを深めるため、温かみのある色彩を意識したこと。

[@AniCre0](https://github.com/Anicre0)
- 開発速度を意識し、動作コードは1つのHTMLで完結させた。
- 外部APIをできるだけ少なくしたことにより拡張性と運用費を抑えた。
- ユーザーはもちろん、ボードゲームやパーティーゲームグッズを販売している方々も応援できることを意識した。
- ゲームの開催場所を地図上で可視化できる機能を実装したこと。
- チームに参加した後、レビューやチャットを通じてユーザ間でやり取りできる仕組みを実装した。

[@ura0612](https://github.com/ura0612)
- サービスの世界観を意識し、フォントにこだわった。
- 競合調査を行い、きちんと機能を選定した。
- ユーザー人数、年代、性別などを概算し、運用面できちんとお客さんがいらっしゃるか検討した。
- 孤独な人とそうでない人の致死率の差を調べスケールアップできるか否かを検討した。


## 開発技術
### コンポーネント図

<figure>
    <img width="477" alt="スクリーンショット 2024-10-27 22 06 47" src="https://github.com/user-attachments/assets/994d94b9-f3a9-49ec-8b59-12b79657910f">
    <figcaption>コンポーネント図</figcaption>
</figure>

- Main Component (メインコンポーネント)<br>
メインコンポーネントはアプリケーション全体のUIの切り替えを管理する要素です。

- User Auth Component (ユーザー認証コンポーネント)<br>
ユーザー認証に関連する機能を担当するコンポーネント。

- User Auth Profile Component (ユーザープロフィールコンポーネント)<br>
ユーザーのプロフィール情報を管理し表示するためのコンポーネント。
ユーザーの名前、自己紹介、過去の参加履歴などのデータを扱います。

- Team Management Component (チーム管理コンポーネント)<br>
チームの作成・管理を行うコンポーネントです。
チームの作成時には、ユーザーが指定した情報（場所、人数、日程など）を基にFirebase Realtime Databaseに保存し、チームのマッチングや管理機能を提供します。
UI上では、チーム作成フォームや現在のチーム情報を表示・操作可能である。

- Firebase Realtime Database<br>


### 活用した技術

#### フレームワーク・ライブラリ・モジュール
- Vue.js<br>
- Google Firebase<br>
- Google Firebase Auth<br>
- Google Firebase Realtime Database<br>
- Leaflet.js<br>
- Font Awesome<br>
- Google Fonts (DotGothic16)<br>

#### ハッカソンで開発した独自機能・技術

- Leaflet.jsを用いた直感的な地図操作
- リアルタイムなチーム作成・管理とチャット機能<br>
- ゲーム風のプロフィールステータス管理<br>
- イベント終了後のレビュー機能



> [!NOTE]
> 時間の都合上一部バックエンドの機能を切りました。
> そのため、製品として動作するコードは、./frontend/jphack.htmlのみとなります
