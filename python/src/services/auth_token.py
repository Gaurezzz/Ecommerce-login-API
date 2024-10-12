from datetime import datetime, timedelta, timezone
import jwt
from decouple import config
import sys
from fastapi import HTTPException

# Crear un access token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(tz=timezone.utc) + expires_delta
    else:
        expire = datetime.now(tz=timezone.utc) + timedelta(minutes=int(config('ACCESS_TOKEN_EXPIRE_MINUTES')))
    to_encode.update({"exp": expire})
    print(to_encode)
    sys.stdout.flush()
    encoded_jwt = jwt.encode(to_encode, config('SECRET_KEY'), algorithm=config('ALGORITHM'))
    return encoded_jwt

# Decodificar un access token
def decode_access_token(token: str):
    print(datetime.now(tz=timezone.utc))
    try:
        payload = jwt.decode(token, config('SECRET_KEY'), algorithms=[config('ALGORITHM')])

        print(payload)
        sys.stdout.flush()

        # Verificar la expiración
        if "exp" in payload:
            expiration = datetime.fromtimestamp(payload['exp'],tz=timezone.utc)
            print(expiration, datetime.now(tz=timezone.utc))
            sys.stdout.flush()
            if datetime.now(tz=timezone.utc)> expiration:
                return None
        
        return payload
    except jwt.ExpiredSignatureError:
        # Token expirado
        HTTPException(status_code=400, detail="Token expirado.")
    except jwt.InvalidTokenError:
        # Token inválido
        HTTPException(status_code=400, detail="Token inválido.")
    except Exception as e:
        # Error desconocido
        HTTPException(status_code=400, detail="Error desconocido.")
