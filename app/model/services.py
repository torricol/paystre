from datetime import datetime
from typing import Optional
from sqlmodel import Relationship, SQLModel, Field
from app.model.platforms import Platform


class Service(SQLModel, table=True):
    __tablename__ = "services"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(..., max_length=100)
    pay_date: int = Field(default=0)
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())
    deleted_at: Optional[datetime] = None
    active: bool = Field(default=True)
    is_delete: bool = Field(default=False)

    # La Clave Foránea (FK)
    platform_id: Optional[int] = Field(default=None, foreign_key="platforms.id")
    
    # Relación: Un servicio pertenece a una plataforma
    platform: Optional[Platform] = Relationship(back_populates="services")

    model_config = {
        "from_attributes": True
    }


class ServiceCreate(SQLModel):
    name: str = Field(..., max_length=100)
    active: bool = Field(default=True)


class ServiceRead(SQLModel):
    id: int
    name: str
    active: bool

    model_config = {
        "from_attributes": True
    }