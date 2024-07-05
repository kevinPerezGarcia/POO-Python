import os

# Definición de clase
class MamiferoCuadrupedo:

    # Atributos de clase: idénticos entre distintos objetos
    especie = "Mamífero"
    organos_respiratorios = ["Pulmones", "Fosas nasales"]
    extremidades = 4

    # Atributos de instancia: varían entre distintos objetos
    
    def __init__(self, nombre, edad, peso): # Método constructor
        self.mi_nombre = nombre
        self.mi_edad = edad
        self.mi_peso = peso
        self.initialize_mamifero()

    def initialize_mamifero(self):
        print(f"Initializing mamífero cuadrúpedo: {self.mi_nombre}")
        self.greeting()

    def greeting(self):
        print(f'Hola, soy {self.mi_nombre}')

# Fin de definición de clase

# Función que muestra los atributos de clase en diversas instancias

def mostrar_atributos_de_clase(perro, gato, vaca):

    # Acess a atributos de clase
    print("\n\033[32m -- ATRIBUTOS DE CLASE --\033[0m")
    print("-------- Perro --------")
    print(perro.especie)
    print(perro.organos_respiratorios)
    print(perro.extremidades)

    # Acess a atributos de clase
    print("\n-------- gato --------")
    print(gato.especie)
    print(gato.organos_respiratorios)
    print(gato.extremidades)

    # Acess a atributos de clase
    print("\n-------- vaca --------")
    print(vaca.especie)
    print(vaca.organos_respiratorios)
    print(vaca.extremidades)

# Fin de la función: mostrar_atributos_de_clase()

# Función que muestra los atributos de instancia en diversos objetos

def mostrar_atributos_de_instancia(perro, gato, vaca):

    # Acess a atributos de instancia
    print("\n\033[32m -- ATRIBUTOS DE INSTANCIA --\033[0m")
    print("-------- Perro --------")
    print(f"NOMBRE: {perro.mi_nombre}")
    print(f"EDAD  : {perro.mi_edad}")
    print(f"PESO  : {perro.mi_peso}")

    # Acess a atributos de instancia
    print("\n-------- gato --------")
    print(f"NOMBRE: {gato.mi_nombre}")
    print(f"EDAD  : {gato.mi_edad}")
    print(f"PESO  : {gato.mi_peso}")

    # Acess a atributos de instancia
    print("\n-------- vaca --------")
    print(f"NOMBRE: {vaca.mi_nombre}")
    print(f"EDAD  : {vaca.mi_edad}")
    print(f"PESO  : {vaca.mi_peso}")

# Fin de la función: mostrar_atributos_de_instancia()

# Función principal
def main():

    os.system("cls")

    # Instanciamiento de la clase MamiferoCuadrupedo
    perro = MamiferoCuadrupedo("Bobby", 3, 10)
    gato = MamiferoCuadrupedo("Bobby", 2, 1)
    vaca = MamiferoCuadrupedo("Canela", 8, 600)

    mostrar_atributos_de_clase(perro, gato, vaca)
    print("\n\n")
    mostrar_atributos_de_instancia(perro, gato, vaca)

# Fin de definición de función main()

# Cuerpo principal del programa
if __name__ == "__main__":
    main()

# Fin de cuerpo principal