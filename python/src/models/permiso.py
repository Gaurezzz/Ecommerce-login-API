from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from services.database import Base
import re

class Permiso (Base):
    __tablename__ = 'permisos'
    id = Column(Integer, primary_key=True, index=True)
    nombre_permiso = Column(String(255), index=True)
    descripcion = Column(String(255), nullable=True)

    def __init__(self, id, nombre_permiso, descripcion=None):
        self.id = id
        self.nombre_permiso = nombre_permiso
        if descripcion:
            self.descripcion = descripcion
    
    def __repr__(self):
        return f'<Permiso {self.nombre_permiso}>'
    