from flask import Flask, Blueprint
from internal.handler import AppHandler
from injector import inject
from dataclasses import dataclass


@inject
@dataclass
class Router:
    """Router class to manage application routes."""
    app_handler: AppHandler

    def register_routes(self, app: Flask) -> None:
        bp = Blueprint("llmops", __name__)

        bp.add_url_rule("/app", methods=["POST"], view_func=self.app_handler.create_app)
        bp.add_url_rule("/ping", "ping", self.app_handler.ping, methods=["GET"])
        bp.add_url_rule("/app/<uuid:id>/debug", "debug", self.app_handler.completion, methods=["POST"])
        bp.add_url_rule("/app/<uuid:id>", "get_app", self.app_handler.get_app)
        bp.add_url_rule("/app/<uuid:id>", "update_app", self.app_handler.update_app, methods=["POST"])
        bp.add_url_rule("/app/<uuid:id>/delete", "delete_app", self.app_handler.delete_app, methods=["POST"])
        app.register_blueprint(bp)
