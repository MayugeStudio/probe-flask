#  r02.py
#  flaskの練習用プログラム
#    →テンプレートエンジンの利用

import threading, webbrowser
from flask import Flask, render_template, request


app = Flask(__name__)

# 各URLに応じた関数(アプリパスの定義)
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route("/tmp_sample2/<data>")
def tmp_sample2(data):
    return render_template("tmp_sample2.html", name=data)

@app.route("/method_sample")
def method_sample():
    return render_template("method_sample.html")

@app.route("/method_sample2", methods=["GET", "POST"])
def method_sample2():
    if request.method == "POST":
        data = request.form.get("namep")
        data += "(post)"
        return render_template("tmp_sample2.html", name=data)
    else:
        data = request.args.get("nameg")
        data += "(get)"
        return render_template("tmp_sample2.html", name=data)

#アプリ実行
if __name__ == "__main__":

    #ブラウザの自動起動
    #threading.Timer(1.0 , lambda: webbrowser.open('http://127.0.0.1:5000') ).start()
    #Flaskアプリの実行
    app.run(debug=True)

