from flask import Flask
from flask_cors import CORS
from internal.router import Router
from config import Config

from internal.exception import CustomException
from pkg.response import Response, json, HttpCode
import os
from pkg.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from internal.model import App


class Http(Flask):

    def __init__(
            self, 
            *args, 
            config: Config, 
            db: SQLAlchemy, 
            migrate : Migrate,
            router: Router, 
            **kwargs):
        super().__init__(*args, **kwargs)
        router.register_routes(self)

        self.config.from_object(config)  # Load configuration settings

        self.register_error_handler(Exception, self._register_error_handler)

        db.init_app(self)
        migrate.init_app(self, db, directory="internal/migration")
        CORS(self, resources={
            r"/*" : {
                "origins" : "*",
                "supports_credentials" : True,
                "method" : ["GET", "POST"],
                "allow_headers" : ["Content-Type"]
            }
        })

    def _register_error_handler(self, error):
        """Custom error handler"""
        if isinstance(error, CustomException):
            return json(Response(code=error.status_code, 
                                 message=error.message, 
                                 data=error.data if error.data else {}))
        if self.debug or os.getenv("FLASK_ENV") == "development":
            raise error
        else:
            return json(Response(code=Http, message="Internal Server Error", data={}))