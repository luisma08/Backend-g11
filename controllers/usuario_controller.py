from flask_restful import Resource, request
from bcrypt import gensalt, hashpw

from db import conexion
from dtos.usuario_dto import UsuarioDto
from models.usuario_model import Usuario

class RegistroController(Resource):
    def post(self):
        data = request.json
        try:
            dto = UsuarioDto()
            data_serializada = dto.load(data)
            # HASH DEL PASSWORD
            salt = gensalt()
            password = bytes(data_serializada.get('password'), 'urf-8')
            hashed_password = hashpw(password, salt).decode('utf-8')
            data_serializada['password'] = hashed_password
            nuevo_usuario = Usuario(**data_serializada)

            conexion.session.add(nuevo_usuario)
            conexion.session.commit()

            return {
                'message': 'Usuario creado exitosamente'
            }
        except Exception as error:
            return {
                'message': 'Error al registrar el usuario',
                'content': error.args
            }