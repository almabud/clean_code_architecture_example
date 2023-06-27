import json

from flask import Blueprint, request, Response, jsonify

from src.interface_adapter.user_list_controller import UserListController

user = Blueprint("user", __name__)


@user.route("/users", methods=["GET"])
def urser_list():

    res = UserListController(request.__dict__).dispatch()

    return jsonify(res.dict()), res.status_code
