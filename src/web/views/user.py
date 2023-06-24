import json

from flask import Blueprint, request, Response


user = Blueprint("user", __name__)


@user.route("/users", methods=["GET"])
def urser_list():
    return Response(json.dumps({"status": "success", "data": "hello"}), status=200)
