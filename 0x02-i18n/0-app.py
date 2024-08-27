#!/usr/bin/env python3
""" Web Framework app """
from flask import Flask, render_template


# create flask instance
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def simple() -> str:
    """ A route that render an html content
     from template directory """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
