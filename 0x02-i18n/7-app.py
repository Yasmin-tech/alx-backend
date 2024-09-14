#!/usr/bin/env python3
"""A Basic Flask app with internationalization support."""

from flask_babel import Babel, gettext
from typing import Dict, Union
from flask import Flask, render_template, request, g
import pytz


class Config:
    """Represents a Flask Babel configuration."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page."""
    supported_lang = app.config["LANGUAGES"]

    # Priority is given to the locale in the query string
    user_local = request.args.get("locale")
    if user_local and user_local in supported_lang:
        return user_local

    # Fall back to the user's locale setting if available
    user_local = getattr(request, "user_locale", None)
    if user_local and user_local in supported_lang:
        return user_local

    # Finally, use the best match from the accepted languages
    return request.accept_languages.best_match(supported_lang)


@babel.timezoneselector
def get_timezone() -> str:
    """Retrieves the timezone for a web page."""
    # the priority is given to the timezone in the query string
    timezone = request.args.get("timezone")
    if not timezone and g.user:
        # get the timezone from the query user settings
        timezone = getattr(request, 'user_timezone')
    try:
        pytz.timezone(timezone)
        return timezone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config["BABEL_DEFAULT_TIMEZONE"]


def get_user() -> Union[Dict, None]:
    """
        If the variable login_as is set
        and found in users, this function return
        the related dictionary.Otherwise, return None
        """
    login_as = request.args.get("login_as")
    if login_as:
        return users.get(int(login_as))
    return None


@app.before_request
def before_request() -> None:
    """
        This function runs before everything to check if the
        user is logged in
        """
    logged_user = get_user()
    if logged_user:
        request.user_locale = logged_user['locale']
        request.user_timezone = logged_user['timezone']
    g.user = logged_user


@app.route("/")
def get_index() -> str:
    """The home/index page."""
    message = None
    if g.user:
        message = gettext("logged_in_as") % {'username': g.user['name']}
    return render_template("5-index.html", message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
