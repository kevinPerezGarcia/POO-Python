class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_atributos(self):
        print(f'Soy {self.nombre} con {self.edad} años.')

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        print(f"Estoy en el {self.grado} grado.")

mi_estudiante = Estudiante("Fulanito", 18, 5)
mi_estudiante.mostrar_atributos()
mi_estudiante.mostrar_grado()