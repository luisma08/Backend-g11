from flask_restful import Resource, request
from flask import send_file
from werkzeug.utils import secure_filename
from os import path
from sqlalchemy.orm import Query
# universal unique indentifier
from uuid import uuid4
from dtos.categoria_dto import CategoriaDto
from models.categoria_model import Categoria
from db import conexion

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
        # mimetype_validos = ['image/svg+xml', 'image/webp', 'image/png', 'image/jpeg']
        mimetype_valido = 'image/'
        data = request.form.to_dict()
        try:
            # vamos a recibir la imagen mediante la llave llamada imagen
            imagen = request.files.get('imagen') 
            print(imagen.filename)
            if  mimetype_valido not in imagen.mimetype:
                raise Exception('El archivo no es un archivo valido')

            dto = CategoriaDto()
            # modifica la imagen agregando un identificador para evitar sobre escrituras
            nombre = secure_filename(uuid4().hex +'_'+ imagen.filename)

            # agrego a mi formulario el nombre de la imagen que me envia el cliente
            # agregamos la carpeta donde se almacenara la imagen y con el nuevo nombre
            data['imagen'] = 'imagenes/' + nombre
            data_serializada = dto.load(data)

            nueva_categoria = Categoria(**data_serializada)
            conexion.session.add(nueva_categoria)

            # guardo la imagen en nuestro servidor
            imagen.save(path.join('imagenes', nombre))

            conexion.session.commit()
            return {
                'message': 'Categoria creada exitosamente'
            }
        except Exception as error:
            conexion.session.rollback()
            return {
                    'message': 'Error al crear la categoria',
                    'content': error.args
                }

    def get(self):
        query: Query = conexion.session.query(Categoria)
        resultado = query.all()
        dto = CategoriaDto()
        
        data = dto.dump(resultado, many=True)

        return {
            'content': data
        }