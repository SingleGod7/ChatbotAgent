from dataclasses import field, dataclass
from typing import Any
from pkg.response.response import HttpCode

@dataclass
class CustomException(Exception):
    status_code: HttpCode = HttpCode.FAIL
    message: str = ""
    data: any = field(default_factory=dict)


class FailException(CustomException):
    pass

class UnauthorizedException(CustomException):
    status_code = HttpCode.UNAUTHORIZED

class ForbiddenException(CustomException):
    status_code = HttpCode.FORBIDDEN

class NotFoundException(CustomException):
    status_code = HttpCode.NOT_FOUND

class ValidationErrorException(CustomException):
    status_code = HttpCode.VALIDATION_ERROR
