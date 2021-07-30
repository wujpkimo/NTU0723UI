from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def index():
    title = "flask template"
    course = {'name': 'bdpy',
              'description': 'Python and big data',
              "duration": 35}
    series = ['loop', 'bdpy', 'pykt']
    return render_template("./hello.html", course=course, series=series, title=title)


if __name__ == '__main__':
    app.run(debug=True)
