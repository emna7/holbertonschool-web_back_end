#!/usr/bin/env python3
"""Basic babel setup
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import Optional


class Config:
    """configuration
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


def get_user(login_as):
    """look for a user and get it
    """
    if login_as is None:
        return None
    u = users.get(login_as)
    if u:
        return u
    return None


@app.before_request
def before_request():
    """set it global
    """
    login_id = request.args.get('login_as')
    if login_id:
        search_user = get_user(int(login_id))
        g.user = search_user


@babel.localeselector
def get_local() -> Optional[str]:
    """get locale time
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """call index template
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
