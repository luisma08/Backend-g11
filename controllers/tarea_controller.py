# librerias
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm import Query
# archivos locales
from models.tarea_model import Tarea
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
        pass