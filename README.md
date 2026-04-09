# Garage Manager（整備予約・顧客管理アプリ）

## アプリ概要
Django を用いて作成した整備予約・顧客管理アプリです。  
顧客・車両・予約を一元管理できるようにし、自動車整備の現場で必要になりやすい情報を整理して確認できるようにしました。  
自動車整備士としての現場感覚を活かし、実務で使うことを意識して設計しています。

---

## 主な機能

### 顧客管理
- 顧客一覧表示
- 顧客登録
- 顧客詳細表示
- 顧客編集
- 顧客削除

### 車両管理
- 車両一覧表示
- 車両登録
- 車両詳細表示
- 車両編集
- 車両削除

### 予約管理
- 予約一覧表示
- 予約登録
- 予約詳細表示
- 予約編集
- 予約削除

### 関連表示
- 顧客詳細ページで登録車両を表示
- 顧客詳細ページで予約履歴を表示
- 車両詳細ページで予約履歴を表示

---

## 使用技術
- Python
- Django
- SQLite
- HTML
- Bootstrap
- Django Template

---

## モデル構成

### Customer
- 顧客名
- 電話番号
- メールアドレス
- 住所
- メモ

### Vehicle
- 顧客（Customer と関連）
- 車名
- ナンバー

### Reservation
- 顧客（Customer と関連）
- 車両（Vehicle と関連）
- 日付
- 時間
- 作業内容

---

## 工夫した点
- 顧客・車両・予約を別モデルで管理し、ForeignKey を使って関連付けを行いました。
- 顧客詳細ページから登録車両と予約履歴を確認できるようにしました。
- 車両詳細ページからも予約履歴を確認できるようにし、整備履歴の確認がしやすい構成にしました。
- CRUD（一覧・詳細・登録・編集・削除）をすべて自分で実装し、データの流れを理解しながら作成しました。
- Bootstrap を利用して、見やすく操作しやすい画面構成を意識しました。

---

## 学習を通じて理解したこと
- Django の URL / View / Template の流れ
- Model を使ったデータ設計
- ForeignKey によるモデル同士の関連付け
- templates継承（`{% extends %}`）
- templates構文
  - `{{ }}` はデータ表示
  - `{% %}` は Django の命令
- 逆方向アクセス
  - `customer.vehicle_set.all`
  - `vehicle.reservation_set.all`
  - `customer.reservation_set.all`

---

## 今後の改善点
- ユーザー認証機能の追加
- 顧客に紐づく車両のみを予約画面で選択できる機能
- 検索・絞り込み機能の追加
- バリデーションの強化
- UI / UX の改善
- デプロイ対応



## 起動方法

### 1. 仮想環境を有効化
```powershell
.\venv\Scripts\Activate.ps1

## 画像イメージ

### 整備予約・顧客管理アプリ
![整備予約・顧客管理アプリ](./images/customer.png)

### 顧客詳細
![顧客詳細1](./images/customer2.png)
![顧客詳細2](./images/customer3.png)

### 車両一覧
![車両一覧](./images/vehicle3.png)
### 車両詳細
![車両詳細1](./images/vehicle.png)
![車両詳細2](./images/vehicle2.png)

### 予約一覧
![予約一覧](./images/reservation4.png)
### 予約詳細
![予約詳細1](./images/reservation.png)
![予約詳細2](./images/reservation2.png)                                   
![予約詳細3](./images/reservation3.png)
          
