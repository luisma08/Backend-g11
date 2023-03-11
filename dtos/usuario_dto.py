from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import Schema, fields
from models.usuario_model import Usuario

class UsuarioDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario

class LoginDto(Schema):
    correo = fields.Email(required=True, error_messages= {'required': 'El correo debe ser requerido'})
    password = fields.Str(required=True, error_messages= {'required': 'El password debe ser requerido'})