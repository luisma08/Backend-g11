from flask_restful import Resource, request
from sqlalchemy.orm import Query
from base_de_datos import conexion
from models.maestro_model import Maestro
from dtos.maestro_dto import MaestroDto

class MaestroController(Resource):
    # GET, POST, PUT
    def get(self):
        query: Query = conexion.session.query(Maestro)
        # SELECT * FROM maestros;
        resultado = query.all()

        dto = MaestroDto()

        maestros = dto.dump(resultado, many=True)

        return {
            'content': maestros
        }
    
    def post(self):
        data = request.json
        dto = MaestroDto()
        # load >  aca le pasamos un diccionario y lo convertira y validara si toda la informacion es correcta, si no lo es, 
        # emitira un error y si la informacion esta bien, entonces devolvera un diccionario con la data correcta
        try:
            data_validada = dto.load(data)
            print(data_validada)

            nuevo_maestro = Maestro(nombre=data_validada.get('nombre'), apellido=data_validada.get('apellido'), correo=data_validada.get('correo'), direccion=data_validada.get('direccion'))
            # con el metodo add indicamos que queremos guardar ese nuevo registro
            conexion.session.add(nuevo_maestro)
            # Indicamos a la base de datos que guarde los cambios (insert) de manera permanente
            conexion.session.commit()
            return {
                'message': 'MAESTRO CREADO EXITOSAMENTE'
            }, 201

        except Exception as error:
            return {
                'message': 'ERRR AL CREAR MAESTRO',
                'content': error.args
            }