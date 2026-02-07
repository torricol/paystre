from datetime import datetime
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlmodel import select
from app.model.clients import Client, ClientCreate, ClientRead
from app.routes.dependencies.db_session import SessionDep
from app.schemas.responses import ErrorResponse, SuccessResponse

client_route = APIRouter(
    prefix="/clients",
    tags=["Clients"]
)

@client_route.get("/", response_model=SuccessResponse[list[ClientRead]])
def get_clients(db: SessionDep):
    statement = select(Client).where(Client.is_delete == False)
    clients = db.exec(statement).all()
    return SuccessResponse(data=clients)

@client_route.get("/{client_id}", response_model=SuccessResponse[ClientRead])
def get_client(client_id: int, db: SessionDep):
    client = db.get(Client, client_id)
    if not client or client.is_delete:
        error_response = ErrorResponse(error=True, message="Client not found", codigo_error=404)
        return JSONResponse(status_code=404, content=error_response.model_dump())
    return SuccessResponse(data=client)


@client_route.post("/", status_code=201, response_model=SuccessResponse[ClientRead])
def create_client(client: ClientCreate, db: SessionDep):
    db_client = Client(**client.model_dump())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return SuccessResponse(data=db_client)


@client_route.put("/{client_id}", response_model=SuccessResponse[ClientRead])
def update_client(client_id: int, client_update: ClientCreate, db: SessionDep):
    client = db.get(Client, client_id)
    if not client or client.is_delete:
        error_response = ErrorResponse(error=True, message="Client not found", codigo_error=10)
        return JSONResponse(status_code=404, content=error_response.model_dump())
    client.name = client_update.name
    client.updated_at = datetime.now()
    client.active = client_update.active
    db.add(client)
    db.commit()
    db.refresh(client)
    return SuccessResponse(data=client)


@client_route.delete("/{client_id}", response_model=SuccessResponse[ClientRead])
def delete_client(client_id: int, db: SessionDep):
    client = db.get(Client, client_id)
    if not client or client.is_delete:
        error_response = ErrorResponse(error=True, message="Client not found", codigo_error=404)
        return JSONResponse(status_code=404, content=error_response.model_dump())
    client.is_delete = True
    client.deleted_at = datetime.now()
    db.add(client)
    db.commit()
    db.refresh(client)
    return SuccessResponse(data=client)