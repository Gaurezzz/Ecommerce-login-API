from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from services.database import Base, SessionLocal
from fastapi import HTTPException
import re

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(255), index=True)
    email = Column(String(255), index=True, unique=True)
    password_hash = Column(String(255))
    token = Column(String(255), nullable=True)
    refresh_token = Column(String(255), nullable=True)
    rolID = Column(Integer, ForeignKey('roles.id'))
    GoogleID = Column(String(255), nullable=True, index=True)
    FechaCreacion = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)

    def __init__(self, nombre, email, password_hash, rolID, GoogleID=None):
        self.nombre = nombre
        self.email = self.unique_email(email)
        self.password_hash = password_hash
        self.rolID = rolID
        if (GoogleID): self.GoogleID = GoogleID

    #validamos que el email no este en la base de datos
    def unique_email(self, email):
        db = SessionLocal()
        usuario = db.query(Usuario).filter(Usuario.email == email).first()
        if usuario: raise HTTPException(status_code=400, detail="El correo ingresado ya se encuentra en uso.")
        return email


    def __repr__(self):
        return f'<Usuario {self.nombre}>'