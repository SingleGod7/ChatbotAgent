from injector import Module, Binder

from pkg.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from internal.extension.database_extension import db
from internal.extension.migrate_extension import migrate

class ExtensionModule(Module):
    def configure(self, binder: Binder):
        binder.bind(SQLAlchemy, to=db)
        binder.bind(Migrate, to=migrate)