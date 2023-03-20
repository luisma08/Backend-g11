from flask_restful import Resource, request
from os import path
from werkzeug.utils import secure_filename
from uuid import uuid4

from db import conexion
from models.producto_model import Producto
from dtos.producto_dto import ProductoDto, MostrarProductoDto

class ProductosController(Resource):
    def post(self):
        mimetype_valido = 'image/'
        data = request.form.to_dict()
        # TODO: validar que tengamos esa llave en el formulario llamada 'imagen' +
        # TODO: validar que solo sean imagenes +
        # TODO: agregar un uuid al nombre de la imagen y sea un nombre valido
        # TODO: no recibir imagenes que pesen mas de 10Mb
        try:
            # obtener imagen por medio de la llave imagen
            imagen = request.files.get('imagen')
            if mimetype_valido not in imagen.mimetype:
                raise Exception('El tipo de archivo no es valido')
            
            dto = ProductoDto()
            # Agregando identificador
            nombre = secure_filename(uuid4().hex +'_'+ imagen.filename)
            # Agregamos el nombre de la carpeta donde se guardara la imagen
            data['imagen'] = 'imagenes-producto/' + nombre

            data_serializada = dto.load(data)
            nuevo_producto = Producto(**data_serializada)

            conexion.session.add(nuevo_producto)
            imagen.save(path.join('imagenes-producto', nombre))

            conexion.session.commit()

            return {
                'message': 'Producto creado exitosamente'
                }
        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'Error al crear el producto',
                'content': error.args
            }
        
    def get(self):
        resultado = conexion.session.query(Producto).all()
        dto = MostrarProductoDto()
        data = dto.dump(resultado, many=True)
        return {
            'content': data
        }