#Librerias
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta
#Archivos locales
from bd import conexion
from controllers.usuario_controller import UsuariosController, LoginController, PerfilController


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:masterPGsql15*@localhost:5432/tareas'
# variable de configuracion JWT
app.config['JWT_SECRET_KEY'] = 'ultrasupersecreto'

# Modificamos el tiempo de expiracion en 1h y 10 min
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1, minutes=10)

Flask_api = Api(app=app)

conexion.init_app(app)

Migrate(app=app, db=conexion)
JWTManager(app)

#Definir mis rutas del proyecto

Flask_api.add_resource(UsuariosController, '/registro')

Flask_api.add_resource(LoginController, '/login')

Flask_api.add_resource(PerfilController, '/perfil')

if __name__ == '__main__':
    app.run(debug=True)