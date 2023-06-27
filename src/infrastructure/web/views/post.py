from flask import Blueprint, request, jsonify

from src.interface_adapter.create_post_controller import CreatePostController
from src.interface_adapter.login_controller import LoginController
from src.interface_adapter.list_post_controller import ListPostController
from src.interface_adapter.signup_controller import SignUpController
from src.interface_adapter.list_user_controller import ListUserController

post = Blueprint("post", __name__)


@post.route("/posts/", methods=["GET"])
def post_list():
    res = ListPostController(request.__dict__).dispatch()

    return jsonify(res.dict()), res.status_code


@post.route("/posts/", methods=["POST"])
def create_post():
    res = CreatePostController(
        {'data': request.json, **request.__dict__}
    ).dispatch()

    return jsonify(res.dict()), res.status_code
