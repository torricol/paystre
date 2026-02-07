from sqlmodel import create_engine
from app.config.settings import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URL), echo=True)