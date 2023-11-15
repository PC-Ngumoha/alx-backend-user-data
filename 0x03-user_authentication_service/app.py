#!/usr/bin/env python3
"""App Module: Flask App
"""
from auth import Auth
from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)
AUTH = Auth()


@app.route('/', strict_slashes=False)
def root_route_handler() -> str:
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
