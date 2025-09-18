import typing as t

import pendulum
from pydantic import BaseModel, Field


class ErrorBody(BaseModel):
    message: str | None = Field(None)
    errors: t.Any | None = Field(None)


class ErrorResponse(BaseModel):
    details: ErrorBody


class AppException(Exception):
    def __init__(
        self,
        status_code: int,
        message: str | None = None,
        errors: dict[str, t.Any] | None = None,
        headers: dict[str, str] | None = None,
    ):
        self.status_code = status_code
        self.message = message
        self.errors = errors
        self.headers = headers


class NotFoundException(AppException):
    def __init__(self, message: str | None = None):
        super().__init__(status_code=404, message=message or "Resource not found.")
