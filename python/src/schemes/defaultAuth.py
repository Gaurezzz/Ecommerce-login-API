from pydantic import BaseModel, EmailStr
from pydantic import field_validator
import re

class loginSchema(BaseModel):
    email: EmailStr
    password: str

    @field_validator('password')
    def validate_password(cls, password):
        # Al menos una letra mayúscula
        if not re.search(r'[A-Z]', password):
            print('La contraseña debe contener al menos una letra mayúscula.')
            raise ValueError('La contraseña debe contener al menos una letra mayúscula.')
        # Al menos una letra minúscula
        if not re.search(r'[a-z]', password):
            print('La contraseña debe contener al menos una letra minúscula.')
            raise ValueError('La contraseña debe contener al menos una letra minúscula.')
        # Al menos un número
        if not re.search(r'\d', password):
            print('La contraseña debe contener al menos un número.')
            raise ValueError('La contraseña debe contener al menos un número.')
        # Al menos un carácter especial
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValueError('La contraseña debe contener al menos un carácter especial.')
        # Mínimo 8 caracteres
        if len(password) < 8:
            print('La contraseña debe contener al menos 8 caracteres.')
            raise ValueError('La contraseña debe contener al menos 8 caracteres.')
        return password

class registerSchema(loginSchema):
    nombre: str
    rolID: int

    @field_validator('nombre')
    def validate_nombre(cls, nombre):
        if not re.match(r'^[a-zA-Z ]+$', nombre):
            print('El nombre solo puede contener letras y espacios.')
            raise ValueError('El nombre solo puede contener letras y espacios.')
        return nombre

    @field_validator('rolID')
    def validate_rolID(cls, rolID):
        if rolID not in [1, 2, 3]:
            print('El rolID debe ser 1, 2 o 3.')
            raise ValueError('El rolID debe ser 1, 2 o 3.')
        return rolID
    
class resendcodeSchema(BaseModel):
    email: EmailStr

    @field_validator('email')
    def validate_email(cls, email):
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            print('El email ingresado no es válido.')
            raise ValueError('El email ingresado no es válido.')
        return email
    
class codigoVerificacionSchema(BaseModel):
    email: EmailStr
    codigo: str

    @field_validator('codigo')
    def validate_codigo(cls, codigo):
        if not re.match(r'^[0-9]{6}$', codigo):
            print('El código de verificación debe contener 6 dígitos.')
            raise ValueError('El código de verificación debe contener 6 dígitos.')
        return codigo
    
class cambiarContrasenaSchema(loginSchema):
    codigo: str

    @field_validator('codigo')
    def validate_codigo(cls, codigo):
        if not re.match(r'^[0-9]{6}$', codigo):
            print('El código de verificación debe contener 6 dígitos.')
            raise ValueError('El código de verificación debe contener 6 dígitos.')
        return codigo