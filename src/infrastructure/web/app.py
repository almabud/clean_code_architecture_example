from flask import Flask

from .views.user import user
from .views.post import post


def create_app(config_name):

    app = Flask(__name__)

    config_module = "src.infrastructure.web.config.{}Config".format(
        config_name.capitalize()
    )

    app.config.from_object(config_module)

    app.register_blueprint(user)
    app.register_blueprint(post)

    return app
