class Producto:
    def __init__(self, nombre, precio, cantidad, fec_venc):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.fec_venc = fec_venc
        self.__ganacia = 0.3

    def __prueba(self):
        self.__ganancia
        print(self.__ganancia)
    
    def mostrar_valor_venta(self):
        return {
            'valor_venta': (self.precio * self.__ganacia) + self.precio
        }


