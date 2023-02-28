__all__ = ["BaseAPIException", "DetailedException", "AuthenticationFailedError"]

from http.client import HTTPException


class BaseAPIException(HTTPException):
    def __init__(self, description, payload: dict | None = None, type: str | None = None):
        HTTPException.__init__(self, description)

        self.data = {}
        if payload:
            self.data.update(payload)

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
