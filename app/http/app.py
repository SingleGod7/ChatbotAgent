import sys
import os

import dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from internal.server import Http
from internal.router import Router
from config import Config
from injector import Injector

from pkg.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .module import ExtensionModule

dotenv.load_dotenv()

conf = Config()

# 先创建配置，然后初始化 injector
injector = Injector([ExtensionModule])
app = Http(__name__, 
           router=injector.get(Router), 
           db=injector.get(SQLAlchemy), 
           migrate=injector.get(Migrate),
           config=conf)

if __name__ == "__main__":
    app.run(debug=True)