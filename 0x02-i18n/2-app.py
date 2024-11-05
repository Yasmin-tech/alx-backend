#!/usr/bin/env python3
"""
    Python Flask app.
    """


from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """
        The configuration for the flask app
        and Babel
        """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_local() -> str:
    """
    Get the user local based on the request

    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """
        The base route
        """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
