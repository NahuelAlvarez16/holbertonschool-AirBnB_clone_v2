#!/usr/bin/python3
# save this as app.py
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return f'Hello HBNB!'

app.run(host='0.0.0.0', port=5000)
