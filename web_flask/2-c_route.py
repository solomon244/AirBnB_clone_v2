#!/usr/bin/python3
"""script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Return Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hnb():
    """Return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Route /c/<text> returns C message"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
