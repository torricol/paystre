from fastapi import APIRouter
from fastapi.responses import JSONResponse
from datetime import datetime
from app.model.platforms import Platform, PlatformCreate, PlatformRead
from app.routes.dependencies.db_session import SessionDep
from app.schemas.responses import SuccessResponse, ErrorResponse
from sqlmodel import select

platform_route = APIRouter(
    prefix="/platforms",
    tags=["Platforms"]
)

@platform_route.get("/", response_model=SuccessResponse[list[PlatformRead]])
def get_platforms(db: SessionDep):
    statement = select(Platform).where(Platform.is_delete == False)
    platforms = db.exec(statement).all()
    return SuccessResponse(data=platforms)


@platform_route.get("/{platform_id}", response_model=SuccessResponse[PlatformRead])
def get_platform(platform_id: int, db: SessionDep):
    platform = db.get(Platform, platform_id)
    if not platform or platform.is_delete:
        error_response = ErrorResponse(error=True, message="Platform not found", codigo_error=404)
        return JSONResponse(status_code=404, content=error_response.model_dump())
    return SuccessResponse(data=platform)


@platform_route.post("/", status_code=201, response_model=SuccessResponse[PlatformRead])
def create_platform(platform: PlatformCreate, db: SessionDep):
    db_platform = Platform(**platform.model_dump())
    db.add(db_platform)
    db.commit()
    db.refresh(db_platform)
    return SuccessResponse(data=db_platform)


@platform_route.put("/{platform_id}", response_model=SuccessResponse[PlatformRead])
def update_platform(platform_id: int, platform_update: PlatformCreate, db: SessionDep):
    platform = db.get(Platform, platform_id)
    if not platform or platform.is_delete:
        error_response = ErrorResponse(error=True, message="Platform not found", codigo_error=10)
        return JSONResponse(status_code=404, content=error_response.model_dump())
    platform.name = platform_update.name
    platform.updated_at = datetime.now()
    platform.active = platform_update.active
    db.add(platform)
    db.commit()
    db.refresh(platform)
    return SuccessResponse(data=platform)


@platform_route.delete("/{platform_id}", response_model=SuccessResponse[PlatformRead])
def delete_platform(platform_id: int, db: SessionDep):
    platform = db.get(Platform, platform_id)
    if not platform or platform.is_delete:
        error_response = ErrorResponse(error=True, message="Platform not found", codigo_error=404)
        return JSONResponse(status_code=404, content=error_response.model_dump())
    platform.is_delete = True
    platform.deleted_at = datetime.now()
    db.add(platform)
    db.commit()
    db.refresh(platform)
    return SuccessResponse(data=platform)