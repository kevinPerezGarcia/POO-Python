import os

# Definición de clase
class MamiferoCuadrupedo:

    # Atributos de clase: idénticos entre distintos objetos
    especie = "Mamífero"
    organos_respiratorios = ["Pulmones", "Fosas nasales"]
    extremidades = 4

    # Atributos de instancia: varían entre distintos objetos
    
    def __init__(self, nombre, edad, peso): # Método constructor
        self.__mi_nombre = nombre
        self.__mi_edad = edad
        self.__mi_peso = peso

    def obtener_datos_privados(self):
        cadena = "NOMBRE: " + self.__mi_nombre + "\n" + \
                 "EDAD  : " + str(self.__mi_edad) + "\n" + \
                 "PESO  : " + str(self.__mi_edad) + "\n"
        return (cadena)

    @property
    def mi_nombre(self):
        return "El nuevo nombre es: " + self.__mi_nombre

    @mi_nombre.setter
    def mi_nombre(self, nuevo_nombre):
        self.__mi_nombre = nuevo_nombre

    @mi_nombre.deleter
    def mi_nombre(self):
        del self.__mi_nombre

# Función principal
def main():

    os.system("cls")

    # Instanciamiento de la clase MamiferoCuadrupedo
    perro = MamiferoCuadrupedo("Bobby", 3, 10)
    gato = MamiferoCuadrupedo("Bobby", 2, 1)
    vaca = MamiferoCuadrupedo("Canela", 8, 600)

    print(perro.mi_nombre)
    perro.mi_nombre = "Scoby Doo"
    print(perro.mi_nombre)
    del perro.mi_nombre
    print(perro.mi_nombre)

# Fin de definición de función main()

# Cuerpo principal del programa
if __name__ == "__main__":
    main()

# Fin de cuerpo principal