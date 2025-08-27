""" 
Herencia

Se hereran los metodos/atributos de una clase principal

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


toto = Animal()
toto.GetReino()

toti = Gato()
toti.SetDatos()
toti.GetPatas()
