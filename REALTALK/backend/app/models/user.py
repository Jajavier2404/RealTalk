from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from db.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre_usuario = Column(String(500), unique=True, nullable=False)
    correo = Column(String(500), unique=True, nullable=False)
    clave_hash = Column(Text, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
