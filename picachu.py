class Picachu():
    tipo = 'Electrico'

    def __init__(self, nombre, nivel, salud):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud

    def atacar(self):
        return f"Picachu ataca y genera {self.nivel / 4} puntos de daño."

picachu_1 = Picachu('Pepe', 750, 500)
picachu_2 = Picachu('Roco', 1200, 1000)

print(picachu_1.tipo, picachu_1.nombre, picachu_1.nivel, picachu_1.salud)
print(picachu_1.atacar())
print(picachu_2.tipo, picachu_2.nombre, picachu_2.nivel, picachu_2.salud)
print(picachu_2.atacar())