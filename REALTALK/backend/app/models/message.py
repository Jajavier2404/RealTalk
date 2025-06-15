from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db.database import Base

class Mensaje(Base):
    __tablename__ = "mensajes"

    id = Column(Integer, primary_key=True, index=True)
    emisor_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    receptor_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    contenido = Column(Text, nullable=False)
    fecha_envio = Column(DateTime, default=datetime.utcnow)

    # Relaciones ORM (no obligatorias pero recomendadas)
    emisor = relationship("Usuario", foreign_keys=[emisor_id], backref="mensajes_enviados")
    receptor = relationship("Usuario", foreign_keys=[receptor_id], backref="mensajes_recibidos")
