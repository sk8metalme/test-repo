# 電卓Webアプリ（オニオンアーキテクチャ設計）

## 概要
- オニオンアーキテクチャで設計したシンプルかつリッチな電卓Webアプリです。
- ダーク＆カラフルなUI、ボタン式の直感的な操作性。
- ドメイン層・アプリケーション層・プレゼンテーション層を明確に分離。
- ユニットテスト・カバレッジ100%（主要ロジック）

---

## 動作確認手順

1. 必要なパッケージのインストール

Python 3.xがインストールされていることを確認してください。

```sh
pip install Flask coverage
```

2. サーバの起動

```sh
python main.py
```

3. ブラウザでアクセス

```
http://localhost:5000/
```

---

## テスト実行・カバレッジ計測

1. ユニットテスト実行

```sh
python -m unittest discover -s tests
```

2. カバレッジ計測付きでテスト実行

```sh
coverage run -m unittest discover -s tests
```

3. カバレッジレポート表示（ターミナル）

```sh
coverage report
```

4. HTMLカバレッジレポート生成

```sh
coverage html
```

`htmlcov/index.html` をブラウザで開くと詳細なカバレッジが確認できます。

---

## ディレクトリ構成（抜粋）

```
app/
  ├── presentation/
  │   ├── views.py
  │   └── templates/
  │       └── calculator.html
  ├── application/
  │   └── calculator_service.py
  ├── domain/
  │   ├── calculator_entity.py
  │   └── value_object/
  │       ├── operator.py
  │       └── operand.py
  └── infrastructure/
      └── __init__.py
main.py
README.md

# テスト

tests/
  ├── test_operator.py
  ├── test_operand.py
  ├── test_calculator_entity.py
  └── test_calculator_service.py
```

---

## PR・ブランチ運用

- 実装内容は `feature/calculator-onion-arch` ブランチで管理し、PRでレビュー・マージ運用しています。
- PR例：[PR #7: 電卓Webアプリ（オニオンアーキテクチャ）実装](https://github.com/sk8metalme/test-repo/pull/7)

---

## その他
- ご質問・ご要望はPRまたはIssueでお気軽にどうぞ。
