from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/tiger')
def hello_tiger():
    return '[T] hello tiger'


@app.route('/lion')
def hello_lion():
    return '[T] hello lion'


@app.route('/new/<animal>')
def hello_new(animal):
    return '[A] hello %s' % animal


@app.route('/animal/<kind>')
def hello_animal(kind):
    if kind == 'tiger':
        return redirect(url_for('hello_tiger'))
    if kind == 'lion':
        return redirect(url_for('hello_lion'))
    else:
        return redirect(url_for('hello_new', animal=kind))


if __name__ == '__main__':
    app.run(debug=True)
