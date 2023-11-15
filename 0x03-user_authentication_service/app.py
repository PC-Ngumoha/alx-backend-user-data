#!/usr/bin/env python3
"""App Module: Flask App
"""
from auth import Auth
from flask import Flask, jsonify, request, abort, make_response, redirect, \
                  url_for

app = Flask(__name__)
AUTH = Auth()


@app.route('/', strict_slashes=False)
def root() -> str:
    """The root route of the API
    """
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', strict_slashes=False, methods=['POST'])
def users() -> str:
    """Registers a new user on the app.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            AUTH.register_user(email, password)
        except ValueError:
            return jsonify({'message': 'email already registered'}), 400
        return jsonify({
            'email': '{}'.format(email),
            'message': 'user created'
        })


@app.route('/sessions', strict_slashes=False, methods=['POST'])
def login() -> str:
    """Logs users into the the app and creates a new session
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if not AUTH.valid_login(email, password):
            abort(401)
        else:
            session_id = AUTH.create_session(email)
            response = make_response(jsonify({
                'email': '{}'.format(email),
                'message': 'logged in'
            }))
            response.set_cookie('session_id', session_id)
            return response


@app.route('/sessions', strict_slashes=False, methods=['DELETE'])
def logout() -> str:
    """Logs out the user with the current session
    """
    if request.method == 'DELETE':
        session_id = request.cookies.get('session_id')
        session_user = AUTH.get_user_from_session_id(session_id)
        if session_user:
            AUTH.destroy_session(session_user.id)
            return redirect(url_for('root'))
        else:
            abort(403)


@app.route('/profile', strict_slashes=False, methods=['GET'])
def profile() -> str:
    """Gets the logged in user's profile information
    """
    if request.method == 'GET':
        session_id = request.cookies.get('session_id')
        session_user = AUTH.get_user_from_session_id(session_id)
        if session_user:
            return jsonify({'email': '{}'.format(session_user.email)}), 200
        else:
            abort(403)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
