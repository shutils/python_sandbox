# python_sandbox

# 参考動作環境
- OS: Ubuntu 20.04
- 要求ソフトウェア
  - python3
  - pipenv

# 実行方法
1. プロジェクトルートで`pipenv shell`を実行し仮想環境へ入る
    ```
    $ pipenv shell
    ```
2. `pipenv sync`を実行し必要パッケージをインストール
    ```
    $ pipenv sync
    ```
3. `flask run`を実行しサーバーを起動
    ```
    $ flask run
    ```
4. http://localhost:5000 へアクセス