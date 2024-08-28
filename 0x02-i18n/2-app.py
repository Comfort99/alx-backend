#!/usr/bin/env python3
""" Flask Babel app """
from flask import Flask, request, render_template
from flask_babel import Babel


class Config:
    """ A class to Configure Babel
    attributes """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# create flask instance
# configure babel and instatiate babel app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ A function that uses a location decorator
     to return a language based on the web page  location """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def Home() -> str:
    """ A simple flask object """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
