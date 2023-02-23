def saludar(nombre):
    print(f'Hola {nombre}')


saludar('Jorge')

def saldudar_varios(*args):
    #Cuando se coloca en un parametro el '*' significa que no hay limites de ese parametro, este parametro debe de ir al ultimo
    #Todos los valores que le pasemos a este parametro se almacenaran en un tupla
    #Nota: las tuplas, a diferencia de los arreglos, no se pueden modificar osea una vez creadas sus valores no pueden cambiar
    print(args)
    for nombre in args:
        saludo = 'Hola {}'.format(nombre)
        print(saludo)

saldudar_varios('Roxana', 'Juana', 'Martin', 'Roberto')
saldudar_varios('Pedro', 'Luis')

def informacion_usuario(**kwargs):
    print(kwargs)
    # .get('llave') > devolver el valor si es que existe la llave, 
    # sino existe entonces devolvera None o el segundo parametro que le colocaremos (opcional)
    print(kwargs.get('estatura', 'No existe'))
    try:
        print(kwargs['estatura'])
    except:
        print('No existe la llave estatura')

informacion_usuario(nombre='Eduardo', edad=30, estado_civil='soltero', estatura=1.88)
informacion_usuario(nombre='Pamela', apellido='Juarez', nacionalidad='Colombiana', fec_nac='31/06/1999')

#
def dividir(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        return 'No puede haber division entre 0'
    except TypeError:
        return 'Las divisiones solamente pueden ser entre dos numeros'
    except:
        return 'Erros desconocido'

valor = dividir(10,5)
print(valor)

valor = dividir(10,0)
print(valor)

valor = dividir('a', 'b')
print(valor)