from typing import Any, Generic, TypeVar, Optional
from pydantic import BaseModel, Field

T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    """Estructura estándar para respuestas exitosas"""
    success: bool = Field(True)
    data: T


class ErrorResponse(BaseModel):
    """Estructura estándar para respuestas de error"""
    error: bool = Field(True)
    message: str
    codigo_error: int
