# Primero se importan las librerias
from flask import Flask
from dotenv import load_dotenv
from os import environ
from flask_migrate import Migrate
from flask_restful import Api
# Luego se importan los archivos del proyecto
from base_de_datos import conexion
from models.nivel_model import Nivel
from models.maestro_model import Maestro
from models.seccion_model import Seccion
from controllers.nivel_controller import NivelController, UnNivelController
from controllers.maestro_controller import MaestroController

# Es el encargado de leer el archivo .env si es que existe y agregar las variables en ese archivo como si fueran variables de entorno
load_dotenv()

app = Flask(__name__)
# dialect://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

# Es una inicializacion de mi clase Api
flask_api = Api(app=app)

# Si quiero crear mi conexion en otro archivo e inicializar la configuracion de mi conexion, 
# tengo que utilizar el metodo init_app y es aca donde le pasare el parametro de mi instancia
# de la clase Flask
conexion.init_app(app)

#AHORA REALIZAMOS LA INICIALIZACION DE MI CLASE MIGRATE
# SE LE PASA LA APLICACION COMO PRIMER PARAMETRO Y LA CONEXION (INSTANCIA DE SQLMIGRATE) COMO SEGUNDO PARAMETRO
Migrate(app=app, db=conexion)

# DEFINO LAS RUTAS DE MI API

flask_api.add_resource(NivelController, '/nivel')
flask_api.add_resource(UnNivelController, '/nivel/<id>')

# Creando ruta para maestros

flask_api.add_resource(MaestroController, '/maestro')

if __name__ == '__main__':
    app.run(debug=True)