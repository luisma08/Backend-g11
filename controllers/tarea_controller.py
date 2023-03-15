# librerias
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import and_, or_, Enum
from sqlalchemy.orm import Query
from datetime import datetime
# archivos locales
from models.tarea_model import Tarea, EstadoTareaEnum
from bd import conexion
from dtos.tarea_dto import TareaDto

class TareasController(Resource):
    @jwt_required()
    def post(self):
        usuario_id = get_jwt_identity()
        data = request.json
        dto = TareaDto()

        try:
            data_validada = dto.load(data)
            nueva_tarea = Tarea(**data_validada, usuarioId = usuario_id)
            conexion.session.add(nueva_tarea)
            conexion.session.commit()

            return {
                'message': 'Se agrego la tarea exitosamente'
            }, 201
        except Exception as error:
            return{
                'message': 'Error al crear la tarea',
                'content': error.args
            }
        
    @jwt_required()
    def get(self):
        # TODO: devolver todas las tareas del usuario
        usuario_id = get_jwt_identity()
        query: Query = conexion.session.query(Tarea)
        print('id de usuario para el get')
        print(usuario_id)

        tareas_usuario_activado: Tarea = query.filter_by(usuarioId = usuario_id).all()
        print(tareas_usuario_activado)

        dto = TareaDto()

        data = dto.dump(tareas_usuario_activado, many=True)

        return{
            'content': data
        }
        
class TareaController(Resource):
    @jwt_required()
    def get(self):
        usuario_id = get_jwt_identity()
        print(usuario_id)
        # Obtengo los parametros de la url
        nombre = request.args.get('nombre')
        estado = request.args.get('estado')
        fecha_vencimiento = request.args.get('fecha_vencimiento')

        nombre_str = "%{}%".format(nombre)
        fec_ven_str = "%{}%".format(fecha_vencimiento)
        print(fec_ven_str)

        query: Query = conexion.session.query(Tarea)
        filtro_tarea: Tarea = query.filter(and_(Tarea.usuarioId == usuario_id, 
                                                Tarea.estado == EstadoTareaEnum(estado), 
                                                Tarea.fechaVencimiento == fecha_vencimiento, 
                                                Tarea.nombre.like(nombre_str))).all()

        print(filtro_tarea)

        dto = TareaDto()

        data = dto.dump(filtro_tarea, many=True)

        return{
            'content': data
        }