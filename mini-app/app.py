# Flaskクラスをimport
from flask import Flask

# Flaskクラスをインスタンス化
app = Flask(__name__)


# URLと実行する関数をマッピングする
@app.route("/")
def index():
    return "Hello, world!"
