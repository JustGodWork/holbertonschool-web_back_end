#!/usr/bin/env python3
""" Flask Babel app with template parameterization """

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """
    Configuration class for Babel internationalization.

    Attributes:
        LANGUAGES (list): A list of supported languages for the application.
        Default languages are English ('en') and French ('fr').
        BABEL_DEFAULT_LOCALE (str): The default locale for the application.
                                    Defaults to 'en' (English).
        BABEL_DEFAULT_TIMEZONE (str): The default timezone for the application.
                                      Defaults to 'UTC'.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    """
    Determine the best match for supported languages.

    This function uses the `Accept-Language` header from the request
    to determine the best match for the supported languages defined
    in the app configuration.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """
    Render the index page.

    This function renders the `3-index.html` template, which uses
    translations for the title and header.
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
