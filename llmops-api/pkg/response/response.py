from dataclasses import dataclass, field
from typing import  Any

from flask import jsonify

from .http_code import HttpCode


@dataclass
class Response:
    code : HttpCode = HttpCode.SUCCESS
    message : str = ""
    data : Any = field(default_factory=dict)

def json(data: Response):
    return jsonify(data), 200

def success_json(data: Any = None):
    return json(Response(code=HttpCode.SUCCESS,message="", data=data))

def fail_json(data: Any = None):
    return json(Response(code=HttpCode.FAIL, message="", data=data))

def validation_error_json(error: Any = None):
    first_key = next(iter(error))
    if first_key:
        msg = error[first_key][0]
    else:
        msg = ""
    return json(Response(code=HttpCode.VALIDATION_ERROR, message=msg, data=error))

def message(code: HttpCode = None,message: str = ""):
    return json(Response(code=code, message=message, data={}))

def success_message(msg: str = ""):
    return message(HttpCode.SUCCESS, message=msg)

def fail_message(msg: str = ""):
    return message(HttpCode.FAIL, message=msg)

def not_found_message(msg: str = ""):
    return message(HttpCode.NOT_FOUND, message=msg)

def unauthorized_message(msg: str = ""):
    return message(HttpCode.UNAUTHORIZED, message=msg)

def forbidden_message(msg: str = ""):
    return message(HttpCode.FORBIDDEN, message=msg)

