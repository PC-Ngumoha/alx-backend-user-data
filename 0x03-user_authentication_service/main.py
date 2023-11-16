#!/usr/bin/env python3
""" Main module: Integration test for the app
"""
import requests

API_URL = 'http://0.0.0.0:5000'


def register_user(email: str, password: str) -> None:
    """Tests the ability to register new users on the app.
    """
    data = {'email': email, 'password': password}
    expected_output = {'email': '{}'.format(email),
                       'message': 'user created'}
    expected_status_code = 200

    response = requests.post('{}/users'.format(API_URL), data=data)

    assert response.status_code == expected_status_code
    assert response.json() == expected_output


def log_in_wrong_password(email: str, password: str) -> None:
    """Tests Login attempt with wrong password
    """
    data = {'email': email, 'password': password}
    expected_status_code = 401

    response = requests.post('{}/sessions'.format(API_URL), data=data)

    assert response.status_code == expected_status_code


def log_in(email: str, password: str) -> str:
    """Tests Login attempt with correct details
    """
    data = {'email': email, 'password': password}
    expected_status_code = 200

    response = requests.post('{}/sessions'.format(API_URL), data=data)

    assert response.status_code == expected_status_code
    assert response.cookies.get('session_id') is not None
    return response.cookies.get('session_id')


def profile_unlogged() -> None:
    """Tests attempt to access the profile as an anonymous user
    """
    expected_status_code = 403

    response = requests.get('{}/profile'.format(API_URL))

    assert response.status_code == expected_status_code


def profile_logged(session_id: str) -> None:
    """Tests attempt to access the profile as a logged-in user
    """
    cookies = {'session_id': session_id}
    expected_status_code = 200

    response = requests.get('{}/profile'.format(API_URL), cookies=cookies)

    assert response.status_code == expected_status_code


def log_out(session_id: str) -> None:
    """Tests attempt to logout the user.
    """
    cookies = {'session_id': session_id}
    unexpected_status_code = 403

    response = requests.delete('{}/sessions'.format(API_URL), cookies=cookies)

    assert response.status_code != unexpected_status_code


def reset_password_token(email: str) -> str:
    """Tests attempt to request a new "reset password token"
    """
    data = {'email': email}
    expected_status_code = 200

    response = requests.post('{}/reset_password'.format(API_URL), data=data)

    assert response.status_code == expected_status_code
    return response.json().get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Tests attempt to update user password using previously retrived token.
    """
    data = {'email': email,
            'reset_token': reset_token,
            'new_password': new_password}
    expected_output = {'email': '{}'.format(email),
                       'message': 'Password updated'}
    expected_status_code = 200

    response = requests.put('{}/reset_password'.format(API_URL), data=data)

    assert response.status_code == expected_status_code
    assert response.json() == expected_output


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
