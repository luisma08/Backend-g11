#Librerias
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
#Archivos locales
from bd import conexion
from controllers.usuario_controller import UsuariosController


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:masterPGsql15*@localhost:5432/tareas'

Flask_api = Api(app=app)

conexion.init_app(app)

Migrate(app=app, db=conexion)

#Definir mis rutas del proyecto

Flask_api.add_resource(UsuariosController, '/registro')

if __name__ == '__main__':
    app.run(debug=True)