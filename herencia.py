class Animal():
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("Soy un animal del tipo", type(self).__name__)

class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzz!")
    def moverse(self):
        print("Volando")
    def picar(self):
        print("Picar!")

class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        super().__init__(especie, edad)
        self.dueño = dueño

if __name__ == "__main__":
    #mi_perro = Perro('mamífero', 10)
    #mi_vaca = Vaca("mamífero", 23)
    #mi_abeja = Abeja("insecto", 1)

    #mi_perro.hablar()
    #mi_vaca.hablar()

    #mi_vaca.describeme()
    #mi_abeja.describeme()

    #mi_abeja.picar()

    mi_perro = Perro('mamífero', 7, 'Luis')
    print(mi_perro.especie)
    print(mi_perro.edad)
    print(mi_perro.dueño)