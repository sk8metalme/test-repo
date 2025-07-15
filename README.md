# 電卓Webアプリ（オニオンアーキテクチャ設計）

## 動作確認手順

1. 必要なパッケージのインストール

Python 3.xがインストールされていることを確認してください。

```
pip install Flask
```

2. サーバの起動

```                                                             


    
python main.py
```

3. ブラウザでアクセス

下記URLにアクセスしてください。

```
http://localhost:5000/
```

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
```