from datetime import datetime, timezone, timedelta
from typing import List, Optional
from sqlmodel import Relationship, SQLModel, Field


class Platform(SQLModel, table=True):
    __tablename__ = "platforms"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(..., max_length=50)
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())
    deleted_at: Optional[datetime] = None
    active: bool = Field(default=True)
    is_delete: bool = Field(default=False)

    # Relación: una plataforma puede tener muchos servicios
    services: List["Service"] = Relationship(back_populates="platform")

    model_config = {
        "from_attributes": True
    }


class PlatformCreate(SQLModel):
    name: str = Field(..., max_length=50)
    active: bool = Field(default=True)


class PlatformRead(SQLModel):
    id: int
    name: str
    active: bool

    model_config = {
        "from_attributes": True
    }