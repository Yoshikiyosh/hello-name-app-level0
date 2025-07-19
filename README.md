# Hello Name App - Level 0

FastAPI + Clean Architecture で実装された「Hello, 名前！」アプリです。

## 🎯 概要

`http://localhost:8000/hello?name=太郎` にアクセスすると `Hello, 太郎!` と返すシンプルなAPIアプリケーションです。

## 🏗️ アーキテクチャ

Clean Architecture の原則に従った4層構造：

- **API層** (`app/api/`): FastAPIエンドポイント
- **Application層** (`app/application/`): ユースケース
- **Domain層** (`app/domain/`): ビジネスロジック
- **Infrastructure層** (`app/infrastructure/`): 外部接続（今回は未使用）

## 📁 ディレクトリ構成

```
app/
├── api/
│   └── hello.py          # FastAPIエンドポイント
├── application/
│   └── use_case.py       # ユースケース層
├── domain/
│   └── model.py          # ドメインモデル
├── infrastructure/       # 今回は未使用
└── main.py              # エントリーポイント
tests/
└── test_hello.py        # テストファイル
requirements.txt         # 依存関係
README.md               # このファイル
```

## 🚀 セットアップと実行

### 1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 2. アプリケーションの起動

```bash
# 方法1: uvicornコマンドで実行
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 方法2: Pythonスクリプトとして実行
python -m app.main
```

### 3. APIの確認

ブラウザまたはcurlで以下にアクセス：

```bash
# 例1: 太郎さんにあいさつ
curl "http://localhost:8000/hello?name=太郎"
# レスポンス: {"message": "Hello, 太郎!"}

# 例2: 英語名でのあいさつ
curl "http://localhost:8000/hello?name=John"
# レスポンス: {"message": "Hello, John!"}
```

### 4. API仕様の確認

FastAPIの自動生成ドキュメントを確認：

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🧪 テストの実行

```bash
pytest tests/
```

## 🎯 目標達成確認

✅ `http://localhost:8000/hello?name=太郎` にアクセスして `{"message": "Hello, 太郎!"}` が返ることを確認 