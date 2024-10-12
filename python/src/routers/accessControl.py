from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from services.auth_token import create_access_token, decode_access_token
from schemes.accessControl import refresh_token
from services.database import get_db
from sqlalchemy.orm import Session
from models.usuario import Usuario
from datetime import timedelta


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.get("/protected")
async def protected(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):

    token_info = decode_access_token(token)
    print(token_info)

    try:
        if token_info["type"] != "acceso":
            raise HTTPException(status_code=400, detail="El token no es de acceso")
        
        usuario = db.query(Usuario).filter(Usuario.id == token_info["sub"]).first()

        if usuario is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

    except Exception as e:  # Captura cualquier excepción
        raise HTTPException(status_code=400, detail="El token es inválido") from e

    if not usuario:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")

    return {
        "message": "usuario tiene acceso a la ruta protegida",
        "id": usuario.id,
        "email": usuario.email
    }

@router.post("/refresh")
def refresh(refresh_token: refresh_token, db: Session = Depends(get_db)):
    token_info = decode_access_token(refresh_token)
    print(token_info["type"], token_info["sub"])

    try:
        if token_info["type"] != "refresh":
            raise HTTPException(status_code=400, detail="El token no es de acceso")
        
        usuario = db.query(Usuario).filter(Usuario.id == token_info["sub"]).first()

        if usuario is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

    except Exception as e:  # Captura cualquier excepción
        raise HTTPException(status_code=400, detail="El token es inválido") from e

    if not usuario:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    
    token = create_access_token(dict(type="acceso",sub=usuario.id), expires_delta=timedelta(hours=1))
    refresh_token = create_access_token(dict(type="refresh",sub=usuario.id), expires_delta=timedelta(hours=1))

    usuario.token = token
    usuario.refresh_token = refresh_token

    db.commit()
    db.refresh(usuario)

    return {
        "message": "nuevos tokens generados exitosamente",
        "token": token,
        "refresh_token": refresh_token
    }

@router.get("/logout")
def logout(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_info = decode_access_token(token)
    print(token_info)

    try:
        if token_info["type"] != "acceso":
            raise HTTPException(status_code=400, detail="El token no es de acceso")
        
        # Asegúrate de que se llamen los paréntesis en first()
        usuario = db.query(Usuario).filter(Usuario.id == token_info["sub"]).first()

        # Si no se encuentra el usuario, lanzar una excepción
        if usuario is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

    except Exception as e:  # Captura cualquier excepción
        raise HTTPException(status_code=400, detail="El token es inválido") from e

    if not usuario:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    
    usuario.token = None
    usuario.refresh_token = None

    db.commit()
    db.refresh(usuario)

    return {
        "message": "sesion ha expirado exitosamente"
    }
    