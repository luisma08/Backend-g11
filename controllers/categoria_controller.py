from flask_restful import Resource, request
from flask import send_file
from werkzeug.utils import secure_filename
from os import path
# universal unique indentifier
from uuid import uuid4

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