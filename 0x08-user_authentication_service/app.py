#!/usr/bin/env python3
""" Set up and run Flask app"""

from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)

AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """Return: Message"""
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user() -> str:
    """ POST /users
        Register a new user.
        JSON Body:
            email - user email
            password - user password
        Return: User email"""
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'message': 'please use json'}), 400
    except Exception:
        return jsonify({'message': 'bad request'}), 400
    if 'email' in data and 'password' in data:
        try:
            print(data)
            new_user = AUTH.register_user(data['email'], data['password'])
            return jsonify({
                'email': new_user.email,
                'message': 'user created'
                }), 201
        except ValueError:
            return jsonify({'message': 'email already registered'}), 400
    return jsonify({'message': 'please provide an email and password'}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /sessions
        JSON Body:
            email - user email
            password - user password
        Return: User email
    """
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'message': 'please use json'}), 400
    except Exception:
        abort(400)
    if 'email' and 'password' in data:
        if AUTH.valid_login(data['email'], data['password']):
            session_id = AUTH.create_session(data['email'])

            res = jsonify({
                    'email': data['email'],
                    'message': 'logged in'
                    })
            res.set_cookie('session_id', session_id)

            return res
        else:
            abort(401)
    return jsonify({'message': 'please provide an email and password'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
