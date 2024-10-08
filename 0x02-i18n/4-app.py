#!/usr/bin/env python3
"""A Basic Flask app with internationalization support."""

from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Represents a Flask Babel configuration."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page."""
    supported_lang = app.config["LANGUAGES"]
    user_local = request.args.get("locale")
    if user_local and user_local in supported_lang:
        return user_local
    return request.accept_languages.best_match(supported_lang)


@app.route("/")
def get_index() -> str:
    """The home/index page."""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
