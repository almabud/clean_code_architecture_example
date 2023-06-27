from flask import Blueprint, request, jsonify

from src.interface_adapter.login_controller import LoginController
from src.interface_adapter.signup_controller import SignUpController
from src.interface_adapter.list_user_controller import ListUserController

user = Blueprint("user", __name__)


@user.route("/users/", methods=["GET"])
def urser_list():
    res = ListUserController(request.__dict__).dispatch()

    return jsonify(res.dict()), res.status_code


@user.route("/users/", methods=["POST"])
def create_user():
    res = SignUpController(
        {'data': request.json, **request.__dict__}
    ).dispatch()

    return jsonify(res.dict()), res.status_code


@user.route("/login/", methods=["POST"])
def login():
    res = LoginController({'data': request.json, **request.__dict__}).dispatch()

    return jsonify(res.dict()), res.status_code
