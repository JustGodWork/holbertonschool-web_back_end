#!/usr/bin/env python3
""" Flask Babel app with forced locale via URL parameter """

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
    Determine the best match for
    supported languages or force locale via URL.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """
    Render the index page for the application.

    This function handles the root URL of the application and renders
    the '4-index.html' template, which serves as the main page of the app.

    Returns:
        str: The rendered HTML content of the '4-index.html' template.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
