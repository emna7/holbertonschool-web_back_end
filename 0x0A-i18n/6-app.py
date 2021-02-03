#!/usr/bin/env python3
""" flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)


class Config(object):
    """ Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
app.config.from_object(Config)
babel = Babel(app)


@app.before_request
def before_request():
    """determine if a user is logged in"""
    if (request.args.get('login_as')):
        id = int(request.args.get('login_as'))
        user = get_user(id)
        if user:
            g.user = user


def get_user(id):
    """get user"""
    if id in users:
        return users[id]
    return None


@app.route('/')
def hello():
    """ render html file """
    login = False
    if g.get('user') is not None:
        login = True
    return render_template('6-index.html', login=login)


@babel.localeselector
def get_locale():
    """ best match with the supported languages """
    x = request.args.get('locale')
    if x in app.config['LANGUAGES']:
        return x
    if (g.get('user') and g.user["locale"] in app.config['LANGUAGES']):
        return g.user["locale"]
    return(request.accept_languages.best_match(app.config['LANGUAGES']))


if __name__ == '__main__':
    app.run()
