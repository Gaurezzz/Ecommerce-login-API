from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from services.database import Base
import re

class Rol (Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    nombre_rol = Column(String(255), index=True)

    def __init__(self, id, nombre_rol):
        self.id = id
        self.nombre_rol = nombre_rol

    def __repr__(self):
        return f'<Rol {self.nombre_rol}>'