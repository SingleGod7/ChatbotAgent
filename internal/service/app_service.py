from dataclasses import dataclass
from injector import inject
from flask_sqlalchemy import SQLAlchemy
from internal.model import App
import uuid

@inject
@dataclass
class AppService:
    db:SQLAlchemy

    def create_app(self):
        app = App(name="javis", account_id = uuid.uuid4(), icon="", description="这是钢铁侠的助手")
        self.db.session.add(app)
        self.db.session.commit()
        return app