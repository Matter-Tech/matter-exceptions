import json
from typing import Any
from abc import ABC, abstractmethod

from fastapi import HTTPException


class BaseAPIException(HTTPException, ABC):
    def __init__(self, description, detail: Any = None):
        self.description = description
        super().__init__(detail=detail, status_code=self.status_code)

    def as_json(self):
        return json.dumps(
            {
                "status_code": self.status_code,
                "description": self.description,
                "detail": self.detail,
            }
        )

    @property
    @abstractmethod
    def status_code(self):
        pass
