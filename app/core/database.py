import os
from sqlalchemy import create_engine    
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#URL de conexión a la base de datos
DATABASE_URL = f"postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@db:{os.getenv("POSTGRES_PORT")}/{os.getenv("POSTGRES_DB")}"

#Creación del motor de la base
engine = create_engine(DATABASE_URL)

#Creación de una fabrica de sesionara para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base para la definición de modelos SQLAlchemy
Base = declarative_base()

#Dependencias para obtener una sesión en cada solicitud
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()