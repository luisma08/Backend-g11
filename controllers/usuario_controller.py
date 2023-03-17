from flask_restful import Resource, request
from bcrypt import gensalt, hashpw

from db import conexion
from dtos.usuario_dto import UsuarioDto
from models.usuario_model import Usuario
from utils.enviar_correo import enviar_correo

class RegistroController(Resource):
    def post(self):
        data = request.json
        try:
            dto = UsuarioDto()
            data_serializada = dto.load(data)
            # HASH DEL PASSWORD
            salt = gensalt()
            password = bytes(data_serializada.get('password'), 'utf-8')
            hashed_password = hashpw(password, salt).decode('utf-8')
            data_serializada['password'] = hashed_password
            nuevo_usuario = Usuario(**data_serializada)

            conexion.session.add(nuevo_usuario)
            
            enviar_correo(nuevo_usuario.correo, 
                          'Bienvenido a LibreriaAPP',
                          ''' Bienvenido a esta nueva plataforma.
                          Donde podras encontrar todo lo necesario para tus utiles de escritorio''')
            
            conexion.session.commit()
            return {
                'message': 'Usuario creado exitosamente'
            }
        except Exception as error:
            # Si algo fallo todo los inserts, updates y deletes quedaran sin efecto y no se guardara nada en la base de datos
            conexion.session.rollback()
            return {
                'message': 'Error al registrar el usuario',
                'content': error.args
            }