from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from .models import Usuario

class SoloClientes(BasePermission):
    message = 'Solo los clientes pueden realizar esta peticion'
    def has_permission(self, request: Request, view):
        # request.user > toda la informacion del usuario autenticado
        usuario : Usuario = request.user

        if usuario.tipoUsuario == 'CLIENTE':
            # SI RETORNAMOS TRUE INDICA QUE EL USUARIO TIENE LOS PERMISOS CORRESPONDIENTES
            return True
        else:
            return False