import os
from .default_config import DEFAULT_CONFIG

def _get_env(key):
    return os.getenv(key, DEFAULT_CONFIG.get(key))

def _get_bool_env(key):
    value = _get_env(key)
    return value.lower() == "True" if value is not None else False

class Config:
    def __init__(self):
        self.WTF_CSRF_ENABLED = False

        #database 
        self.SQLALCHEMY_DATABASE_URI = _get_env("SQLALCHEMY_DATABASE_URI")
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_size": int(_get_env("SQLALCHEMY_POOL_SIZE")),
            "pool_recycle": int(_get_env("SQLALCHEMY_POOL_RECYCLE")),
        }
        self.SQLALCHEMY_ECHO = _get_bool_env("SQLALCHEMY_ECHO")