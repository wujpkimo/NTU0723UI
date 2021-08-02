from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def index():
    message = 'pass some data to javascript'
    return render_template("./hello.html", message=message)


if __name__ == '__main__':
    app.run(debug=True)
