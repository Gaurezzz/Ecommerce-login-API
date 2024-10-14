from fastapi import APIRouter, Depends, HTTPException, status
from services.database import get_db
from sqlalchemy.orm import Session
from services.auth_token import create_access_token, decode_access_token
from services.email import send_email
from schemes.defaultAuth import loginSchema, registerSchema, cambiarContrasenaSchema, codigoVerificacionSchema, resendcodeSchema
from models.usuario import Usuario
from models.rol import Rol
from models.rolPermiso import RolPermiso
from models.permiso import Permiso
from models.historialAcceso import HistorialAcceso
from datetime import datetime, timedelta
import random
import bcrypt
import sys

router = APIRouter()

@router.post("/register")
async def register(register: registerSchema, db: Session = Depends(get_db)):

    usuario = Usuario(
        nombre=register.nombre,
        email=register.email,
        password_hash=bcrypt.hashpw(register.password.encode('utf-8'),  bcrypt.gensalt()),
        rolID=register.rolID
    )
    
    token = str(random.randint(100000, 999999))
    usuario.token = create_access_token(dict(token=token), expires_delta=timedelta(hours=1))

    db.add(usuario)

    db.commit()
    db.refresh(usuario)

    db.add(HistorialAcceso(userID=usuario.id, accion="register"))

    db.commit()
    db.refresh(usuario)

    await send_email(subject="Verificacion de correo",
               email_to=usuario.email,
               code=token)

    return {
        "message": "Usuario creado exitosamente",
        "id": usuario.id,
        "nombre": usuario.nombre,
        "email": usuario.email,
        "rolID": usuario.rolID
    }

@router.post("/resendcode")
async def resendcode(resendcode: resendcodeSchema, db: Session = Depends(get_db)):

    print('hola')
    sys.stdout.flush()

    usuario = db.query(Usuario).filter(Usuario.email == resendcode.email).first()
    if not usuario: raise HTTPException(status_code=404, detail="Usuario no encontrado.")

    token = str(random.randint(100000, 999999))
    usuario.token = create_access_token(dict(token=token), expires_delta=timedelta(hours=1))

    db.add(HistorialAcceso(userID=usuario.id, accion="resendcode"))

    db.commit()
    db.refresh(usuario)

    await send_email(subject="Verificacion de correo",
               email_to=usuario.email,
               code=token)

    return {
        "message": "Código de verificación reenviado exitosamente",
        "id": usuario.id,
        "nombre": usuario.nombre,
        "email": usuario.email,
        "rolID": usuario.rolID
    }

@router.post("/verification")
def verification(codigo: codigoVerificacionSchema, db: Session = Depends(get_db)):

    usuario = db.query(Usuario).filter(Usuario.email == codigo.email).first()
    if not usuario: raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    if usuario.is_verified: raise HTTPException(status_code=400, detail="El usuario ya ha sido verificado.")

    print(usuario.token)
    if decode_access_token(usuario.token) == None: raise HTTPException(status_code=400, detail="El token ha expirado.")
    if decode_access_token(usuario.token)['token'] != codigo.codigo: raise HTTPException(status_code=400, detail="El código de verificación es incorrecto.")            

    usuario.token = None
    usuario.is_verified = True

    db.add(HistorialAcceso(userID=usuario.id, accion="verification"))

    db.commit()
    db.refresh(usuario)

    return {
        "message": "Usuario verificado exitosamente",
        "id": usuario.id,
        "nombre": usuario.nombre,
        "email": usuario.email,
        "rolID": usuario.rolID
    }

@router.post("/login")
def login(login: loginSchema, db: Session = Depends(get_db)):

    usuario = db.query(Usuario).filter(Usuario.email == login.email).first()
    if not usuario: raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    if not bcrypt.checkpw(login.password.encode('utf-8'), usuario.password_hash.encode('utf-8')): raise HTTPException(status_code=400, detail="Contraseña incorrecta.")
    if not usuario.is_verified: raise HTTPException(status_code=400, detail="El usuario no ha sido verificado.")

    token = create_access_token(dict(type="acceso",sub=usuario.id), expires_delta=timedelta(hours=1))
    refresh_token = create_access_token(dict(type="refresh",sub=usuario.id), expires_delta=timedelta(hours=1))

    usuario.token = token
    usuario.refresh_token = refresh_token

    db.add(HistorialAcceso(userID=usuario.id, accion="login"))
    db.commit()
    db.refresh(usuario)

    return {
        "message": "Inicio de sesión exitoso",
        "token": token,
        "refresh_token": refresh_token,
        "id": usuario.id,
        "nombre": usuario.nombre,
        "email": usuario.email
    }

@router.post("/changePassword")
def changePassword(cambiarContrasena: cambiarContrasenaSchema, db: Session = Depends(get_db)):

    usuario = db.query(Usuario).filter(Usuario.email == cambiarContrasena.email).first()
    if not usuario: raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    if not usuario.is_verified: raise HTTPException(status_code=400, detail="El usuario no ha sido verificado.")

    if decode_access_token(usuario.token) == None: raise HTTPException(status_code=400, detail="El token ha expirado.")
    if decode_access_token(usuario.token)['token'] != cambiarContrasena.codigo: raise HTTPException(status_code=400, detail="El código de verificación es incorrecto.")

    usuario.token = None
    usuario.password_hash = bcrypt.hashpw(cambiarContrasena.password.encode('utf-8'),  bcrypt.gensalt())

    db.add(HistorialAcceso(userID=usuario.id, accion="changePassword"))

    db.commit()

    return {
        "message": "Contraseña cambiada exitosamente"
    }
