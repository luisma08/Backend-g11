class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        return 'Buenos dias'

class Alumno(Persona):
    def __init__(self, nombre, apellido, grado):
        self.grado = grado
        # llamando al construcotr de la clase que estoy heredando
        super().__init__(nombre, apellido)

    def saludar(self):
        saludo_padre = super().saludar()
        print(saludo_padre + ' Yo soy un alumno')

    def dar_vueltas(Self):
        print('Dando vueltas...')

class Docente(Persona):
    def __init__(self, nombre, apellido, seguro_social):
        self.seguro_social = seguro_social
        super().__init__(nombre, apellido)

    def evaluar(Self):
        print('Evaluando...')

eduardo = Alumno('Eduardo', 'De Rivero', 'Quinto')
paolo = Docente('Paolo', 'Soncco', '123456789')

eduardo.saludar()
print(paolo.saludar())

print(eduardo.nombre)