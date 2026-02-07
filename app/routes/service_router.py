from fastapi import APIRouter

service_route = APIRouter(
    prefix="/services",
    tags=["Services"]
)