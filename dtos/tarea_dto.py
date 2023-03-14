from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models.tarea_model import Tarea

class TareaDto(SQLAlchemyAutoSchema):

    estado = fields.Method("obtener_valor_estado")

    def obtener_valor_estado(self, obj):
        return obj.estado.value
    
    class Meta:
        model = Tarea