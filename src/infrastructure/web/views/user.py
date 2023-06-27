from flask import Blueprint, request, jsonify

from src.interface_adapter.login_controller import LoginController
from src.interface_adapter.signup_controller import SignUpController
from src.interface_adapter.user_list_controller import UserListController

user = Blueprint("user", __name__)


@user.route("/users/", methods=["GET"])
def urser_list():
    res = UserListController(request.__dict__).dispatch()

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
