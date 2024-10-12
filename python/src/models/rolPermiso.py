from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from services.database import Base
import re

class RolPermiso (Base):
    __tablename__ = 'rolesPermisos'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rolID = Column(Integer, ForeignKey('roles.id'))
    permisoID = Column(Integer, ForeignKey('permisos.id'))

    def __init__(self, rolID, permisoID):
        self.rolID = rolID
        self.permisoID = permisoID
    
    def __repr__(self):
        return f'<RolPermiso rolID:{self.rolID} permisoID:{self.permisoID}>'