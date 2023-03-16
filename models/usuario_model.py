from sqlalchemy import Column, types
from enum import Enum
from db import conexion

class TipoUsuario(Enum):
    ADMIN = 'ADMIN'
    PERSONA = 'PERSONA'

class Usuario(conexion.Model):
    id = Column(type_= types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    apellido = Column( type_=types.Text)
    correo = Column(type_= types.Text, unique=True, nullable=False)
    password = Column(type_=types.Text, nullable=False)
    tipo = Column(type_=types.Enum(TipoUsuario), default=TipoUsuario.PERSONA)

    __tablename__ = 'usuarios'