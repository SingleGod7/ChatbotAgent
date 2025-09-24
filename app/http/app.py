import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from internal.server import Http
from internal.router import Router
from injector import Injector

injector = Injector()
app = Http(__name__, router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)