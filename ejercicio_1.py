class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando.")

if __name__ == "__main__":
    nombre = input("¿Cuál es su nombre?: ")
    edad = input("¿Cuál es su edad?: ")
    grado = input("¿Cuál es su grado?: ")
    Estudiante = Estudiante(nombre, edad, grado)

    print(
        f"""
        DATOS DEL ESTUDIANTE: \n
        Nombre: {Estudiante.nombre}
        Edad: {Estudiante.edad}
        Grado: {Estudiante.grado}
        """
    )

    estudiar = input('¿Desea estudiar? (S: Sí/N: No): ')
    if estudiar == 'S':
        Estudiante.estudiar()
