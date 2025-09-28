import sys
import os

import dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from internal.server import Http
from internal.router import Router
from config import Config
from injector import Injector, Module, Binder, singleton

from flask_sqlalchemy import SQLAlchemy
from internal.extension.database_extension import db

dotenv.load_dotenv()

conf = Config()

class ExtensionModule(Module):
    def configure(self, binder: Binder):
        # 直接绑定已经创建的 db 实例
        binder.bind(SQLAlchemy, to=db)

# 先创建配置，然后初始化 injector
injector = Injector([ExtensionModule()])
app = Http(__name__, router=injector.get(Router), db=injector.get(SQLAlchemy), config=conf)

if __name__ == "__main__":
    app.run(debug=True)