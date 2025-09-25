import sys
import os

import dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from internal.server import Http
from internal.router import Router
from config import Config
from injector import Injector

dotenv.load_dotenv()

injector = Injector()
app = Http(__name__, router=injector.get(Router), config=Config())

if __name__ == "__main__":
    app.run(debug=True)