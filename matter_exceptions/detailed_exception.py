from typing import Any
from abc import ABC, abstractmethod


class DetailedException(Exception, ABC):
    def __init__(self, message: str, detail: Any = None):
        self.message = message if self.topic in message else f"{self.topic}: {message}"
        self.detail = detail
        self.type = self.topic.replace(" ", "_").lower()

    def __reduce__(self):
        return self.__class__, (
            self.message,
            self.detail,
        )

    def __eq__(self, other):
        return other.__reduce__() == self.__reduce__()

    @property
    @abstractmethod
    def topic(self):
        pass
