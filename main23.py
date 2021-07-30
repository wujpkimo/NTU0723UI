from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'hello world! using flask executable'


def create_app():
    return app
