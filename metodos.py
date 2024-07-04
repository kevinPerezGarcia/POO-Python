class Rectangulo():
    _forma = "Rectangulo"

    def __init__(self, ancho, largo):
        self.ancho = ancho
        self.largo = largo

    def area(self):
        return self.ancho * self.largo

    @classmethod
    def get_forma(cls):
        return cls._forma

    @staticmethod
    def sumar_areas(rectangulo_1, rectangulo_2):
        return rectangulo_1.area() + rectangulo_2.area()

if __name__ == "__main__":
    r1 = Rectangulo(10, 20)
    r2 = Rectangulo(10, 20)
    print(r1.area())
    print(r1.get_forma())
    print(Rectangulo.sumar_areas(r1, r2))