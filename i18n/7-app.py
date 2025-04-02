#!/usr/bin/env python3
""" Flask Babel app with inferred time zone """

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError


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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale():
    """
    Determine the best match for supported languages.
    Priority:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request headers
    4. Default locale
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.get('user') and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone():
    """
    Determine the appropriate time zone.
    Priority:
    1. Timezone from URL parameters
    2. Timezone from user settings
    3. Default to UTC

    Returns:
        str: A valid time zone string.
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except UnknownTimeZoneError:
            pass
    if g.get('user') and g.user.get('timezone'):
        try:
            return pytz.timezone(g.user['timezone']).zone
        except UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


def get_user():
    """Retrieve a user dictionary based on the login_as parameter."""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Set the logged-in user in the global context."""
    g.user = get_user()


@app.route('/')
def index():
    """
    Render the index page for the application.

    This function handles the root URL of the application and renders
    the '7-index.html' template, which serves as the main page of the app.

    Returns:
        str: The rendered HTML content of the '7-index.html' template.
    """
    return render_template('7-index.html', current_timezone=get_timezone())


if __name__ == "__main__":
    app.run()
