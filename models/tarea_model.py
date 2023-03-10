from sqlalchemy import Column, types
from enum import Enum
from sqlalchemy.sql.schema import ForeignKey
from bd import conexion

class EstadoTareaEnum(Enum):
    PENDIENTE = 'PENDIENTE'
    REALIZANDOSE = 'REALIZANDOSE'
    REALIZADA = 'REALIZADA'
    CANCELADA = 'CANCELADA'

class Tarea(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    descripcion = Column(type_=types.Text, default='No tiene descripcion')
    fechaVencimiento = Column(type_=types.DateTime, name='fecha_vencimiento')
    estado = Column(type_=types.Enum(EstadoTareaEnum), default=EstadoTareaEnum.PENDIENTE)

    usuarioId = Column(ForeignKey(column='usuario.id'), type_=types.Integer, nullable=False)

    __tablename__ = 'tareas'