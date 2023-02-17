operacion = input('Ingresa el tipo de operacion: ')
a = int(input('Ingresa primer valor: '))
b = int(input('Ingresa segundo valor: '))

def suma(numero_1, numero_2):
    return numero_1 + numero_2

def resta(numero_1, numero_2):
    return numero_1 - numero_2

if operacion == 'S':
    resultado = suma(a, b)
elif operacion == 'R':
    resultado = resta(a, b)
else:
    resultado = 'ESTA OPERACION NO EXISTE'

print(resultado)