#!/usr/bin/python3
""" Script that starts a Flask web application """


from flask import Flask, request
from markupsafe import escape


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    It returns the string `Hello HBNB!`
    """
    return f'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    It returns the string `HBNB`
    """
    return f'HBNB'

app.run(host='0.0.0.0', port=5000)
