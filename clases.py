oper_value = input('Ingresa el tipo de operacion: ')
a = int(input('Ingresa primer valor: '))
b = int(input('Ingresa segundo valor: '))

class Oper():
    def suma(self, numero_1, numero_2):
        return numero_1 + numero_2

    def resta(self, numero_1, numero_2):
        return numero_1 - numero_2
operaciones=Oper()

if oper_value == 'S':
    resultado = operaciones.suma(a, b)
elif oper_value == 'R':
    resultado = operaciones.resta(a, b)
else:
    resultado = 'ESTA OPERACION NO EXISTE'


print(f'El resultado es {resultado}')