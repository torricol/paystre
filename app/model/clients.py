from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class Client(SQLModel, table=True):
    __tablename__ = "clients"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(..., max_length=100)
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())
    deleted_at: Optional[datetime] = None
    active: bool = Field(default=True)
    is_delete: bool = Field(default=False)

    model_config = {
        "from_attributes": True
    }


class ClientCreate(SQLModel):
    name: str = Field(..., max_length=100)
    active: bool = Field(default=True)


class ClientRead(SQLModel):
    id: int
    name: str
    active: bool

    model_config = {
        "from_attributes": True
    }