from flask import Flask, render_template


app = Flask(__name__)


# 各URLに応じた関数(アプリパスの定義)
@app.route('/')
def index():

	return """
            <html>
            <head>
                <title>Top</title>
            </head>
            <body>
                <h1>Hello from Flask</h1>
                <a href="ryosei">Hello from ryosei</a>
            </body>
            </html>
			"""


@app.route('/ryosei')
def ryosei():
	return """
            <html>
            <head>
                <title>Top</title>
            </head>
            <body>
                <h1>Hello from Ryosei</h1>
                <a href="./">Hello from anaconda</a>
            </body>
            </html>
			"""

@app.route('/diary')
def diary():
	return render_template("diary.html")

#アプリ実行
if __name__ == "__main__":
    #Flaskアプリの実行
    app.run(debug=True)


