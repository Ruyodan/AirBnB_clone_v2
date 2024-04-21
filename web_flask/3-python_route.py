#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ returns Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ returns HBNB """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ Print a char C followed by the value of the text variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ Print Python, followed by the value of the text variable """
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
