""" 
Herencia

Se hereran los metodos/atributos de una clase principal


Solo hereda el que hace el cambio. No los otros
"""

#   Clase padre


class Animal:
    reino = "vegetal"

    def GetReino(self):
        print(self.reino)

#   Clase hijo


class Gato(Animal):  # entre parentesis de quien hereda
    patas = 4

    def GetPatas(self):
        print(f"Reino: {self.reino} {self.patas} Patas")

    def SetDatos(self):
        self.patas = 5
        self.reino = "Carnivoro"


class Perro(Animal):
    def GetCambios(self):
        print(f"El reino {self.reino}")


toto = Animal()
toto.GetReino()

toti = Gato()
toti.SetDatos()
toti.GetPatas()

titi = Perro()
titi.GetReino()
titi.GetCambios()
