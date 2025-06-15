from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db.database import Base

class SesionActiva(Base):
    __tablename__ = "sesiones_activas"

    usuario_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    socket_id = Column(String(500), nullable=False)
    conectado_en = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", backref="sesion_activa", uselist=False)
