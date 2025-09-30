from dataclasses import dataclass
from injector import inject
from pkg.sqlalchemy import SQLAlchemy
from internal.model import App
import uuid

@inject
@dataclass
class AppService:
    db:SQLAlchemy

    def create_app(self):
        with self.db.auto_commit():
            app = App(name="javis", account_id = uuid.uuid4(), icon="", description="这是钢铁侠的助手")
            self.db.session.add(app)
        return app
    
    def get_app(self, id:uuid.UUID):
        app = self.db.session.query(App).get(id)
        return app
    
    def update_app(self, id:uuid.UUID):
        with self.db.auto_commit():
            app = self.get_app(id)
            app.name = "慕课聊天机器人"
        return app
    
    def delete_app(self, id:uuid.UUID):
        with self.db.auto_commit():
            app = self.get_app(id)
            self.db.session.delete(app)
        return app