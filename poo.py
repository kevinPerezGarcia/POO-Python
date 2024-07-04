class Perro():
    # Atributo de clase
    especie = 'mamífero'

    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f'Creando perro {nombre}, {raza}')

        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza

    def ladra(self):
        print('Guau')

    def camina(self, pasos):
        print(f'Caminando {pasos} pasos')

mi_perro = Perro("Toby", "Bulldog")
print(type(mi_perro))

print(mi_perro.nombre)
print(mi_perro.raza)
print(Perro.especie)
print(mi_perro.especie)
mi_perro.ladra()
mi_perro.camina(10)
