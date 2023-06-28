from flask import Blueprint, request, jsonify

from src.interface_adapter.create_post_controller import CreatePostController
from src.interface_adapter.list_post_controller import ListPostController
from src.interface_adapter.retrieve_post_controller import RetrievePostController

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


@post.route("/posts/<string:identifier>/", methods=["GET"])
def retrieve_post(identifier):
    res = RetrievePostController(
        {"kwargs": request.view_args, **request.__dict__}
    ).dispatch()

    return jsonify(res.dict()), res.status_code
