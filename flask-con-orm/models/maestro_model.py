from base_de_datos import conexion
from sqlalchemy import Column, types

class Seccion(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    apellido = Column(type_=types.Text)
    correo = Column(type_=types.Text, unique=True, nullable=False)
    direccion = Column(type_=types.Text)

    __tablename__ = 'maestros'