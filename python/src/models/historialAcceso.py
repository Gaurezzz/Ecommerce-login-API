from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from services.database import Base
import re

class HistorialAcceso(Base):
    __tablename__ = 'historialAccesos'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    userID = Column(Integer, ForeignKey('usuarios.id'))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    accion = Column(String(255), nullable=True)
    ip_address = Column(String(255), nullable=True)

    def __init__(self, userID, accion, ip_address=None):
        self.userID = userID
        self.accion = accion
        if ip_address:
            self.ip_address = ip_address

    def __repr__(self):
        return f'<HistorialAcceso userID:{self.userID} timeStamp: {self.timestamp} Accion: {self.accion}>'