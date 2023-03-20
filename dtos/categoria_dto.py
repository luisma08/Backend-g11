from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.categoria_model import Categoria

class CategoriaDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Categoria