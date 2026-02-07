from fastapi import FastAPI
from sqlmodel import SQLModel
from app.config.settings import settings
from app.config.db import engine
from app import model
from app.routes import client_route, platform_route
from app.routes.movie_router import movie_route

# Crear todas las tablas
SQLModel.metadata.create_all(engine)

app = FastAPI(
    title="Gestion Streaming LMTF - PayStre",
    description="API para la gestión de pagos y suscripciones",
    version=settings.API_VERSION
);

# Apis de Plataformas
app.include_router(platform_route, prefix=settings.API_V1_STR)

# Apis de Clientes
app.include_router(client_route, prefix=settings.API_V1_STR)

# Apis de Movies
# app.include_router(movie_route, prefix=settings.API_V1_STR)