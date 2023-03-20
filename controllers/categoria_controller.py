from flask_restful import Resource, request
from flask import send_file
from werkzeug.utils import secure_filename
from os import path
# universal unique indentifier
from uuid import uuid4
from dtos.categoria_dto import CategoriaDto
from models.categoria_model import Categoria

class ImagenesController(Resource):
    def post(self):
        print(request.json)
        print(request.files)
        imagen = request.files.get('imagen')
        print(imagen.filename)

        nombre_seguro = secure_filename(uuid4().hex + '-' + imagen.filename)

        imagen.save(path.join('imagenes', nombre_seguro))
        return {
            'message': 'Categoria creada existosamente'
        }
    def get(self, nombre):
        try:
            return send_file(path.join('imagenes', nombre))
        except FileNotFoundError as error:
            return send_file(path.join('imagenes', 'not_found.jpg'))
        
class CategoriasController(Resource):
    def post(self):
        data = request.form
        # Vamos a recibir la imagen mediante la llave llamada imagen
        imagen = request.files.get('imagen')
        pass

    def get(self):
        pass