from .base_api_exception import BaseAPIException
from .detailed_exception import DetailedException


class ValidationError(BaseAPIException):
    @property
    def status_code(self):
        return 400


class AccessDeniedError(BaseAPIException):
    @property
    def status_code(self):
        return 403


class NotFoundError(BaseAPIException):
    @property
    def status_code(self):
        return 404


class ConflictError(BaseAPIException):
    @property
    def status_code(self):
        return 409


class UnprocessableError(BaseAPIException):
    @property
    def status_code(self):
        return 422


class ServerError(BaseAPIException):
    @property
    def status_code(self):
        return 500


class UnauthorizedError(BaseAPIException):
    @property
    def status_code(self):
        return 401


class AuthenticationFailedError(DetailedException):
    @property
    def topic(self):
        return "Authentication Failed Error"
