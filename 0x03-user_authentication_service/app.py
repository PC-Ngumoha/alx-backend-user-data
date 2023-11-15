#!/usr/bin/env python3
"""App Module: Flask App
"""
from auth import Auth
from flask import Flask, jsonify, request

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
