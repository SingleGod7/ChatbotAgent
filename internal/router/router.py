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

        bp.add_url_rule("/ping", "ping", self.app_handler.ping, methods=["GET"])
        bp.add_url_rule("/app/completion", "completion", self.app_handler.completion, methods=["POST"])
        app.register_blueprint(bp)
