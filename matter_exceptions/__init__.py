__all__ = ["BaseAPIException", "DetailedException", "AuthenticationFailedError"]

from http.client import HTTPException


class BaseAPIException(HTTPException):
    def __init__(self, description, payload=None, type=None):
        HTTPException.__init__(self, description)

        if payload:
            self.data = payload
        else:
            self.data = {}

        self.data["type"] = type
        self.data["message"] = description
        self.data["success"] = False


class DetailedException(Exception):
    TOPIC = "Error"

    def __init__(self, message: str, data=None):
        self.message = message if self.TOPIC in message else f"{self.TOPIC}: {message}"
        self.data = data
        self.type = self.TOPIC.replace(" ", "_").lower()

    def __reduce__(self):
        return type(self), (
            self.message,
            self.data,
        )


class AuthenticationFailedError(DetailedException):
    TOPIC = "Authentication Failed Error"
