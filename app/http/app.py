import sys
import os

import dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from internal.server import Http
from internal.router import Router
from config import Config
from injector import Injector, Module, Binder

from flask_sqlalchemy import SQLAlchemy
from internal.extension.database_extension import db

dotenv.load_dotenv()

conf = Config()

class ExtensionModule(Module):
    def configure(self, binder: Binder):
        binder.bind(SQLAlchemy, to=db)

injector = Injector()
app = Http(__name__, router=injector.get(Router), db=injector.get(SQLAlchemy), config=conf)

if __name__ == "__main__":
    app.run(debug=True)