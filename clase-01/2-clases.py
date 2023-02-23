class operacion:
    
    def sumar(self, *args):
        suma = 0
        for numero in args:
            suma = suma + numero
        return suma


oper = operacion()
print(oper.sumar(10,20,30,40))