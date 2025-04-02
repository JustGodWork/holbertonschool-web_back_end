#!/usr/bin/env python3
""" Flask Babel app setup """

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Render the index page."""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
