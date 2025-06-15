from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Obtener la URL de la base de datos desde el archivo .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el motor de conexión (engine) a PostgreSQL
engine = create_engine(DATABASE_URL, echo=True)

# Crear una clase base para los modelos
Base = declarative_base()

# Crear la sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
