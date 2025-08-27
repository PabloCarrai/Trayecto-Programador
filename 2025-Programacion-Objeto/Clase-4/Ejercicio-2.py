""" 
Realizar un objeto que permita crear 2 jugadores, un jugador va a 
tener 4 X, y el otro jugador va a tener 4 O, el primer jugador que 
logre llegar a 0 gana!
"""


class jugador():
    cantidad = 4
    nombre = "pirulo"

    def cargarNombre(self):
        self.nombre = input("Nombre?  ")

    def mostrarJugador(self):
        print(f"El jugador {self.nombre} tiene {self.cantidad}")

    def consumirCantidad(self, puntos):
        print(f"El jugador {self.nombre} tiene {self.cantidad}")
        self.cantidad = self.cantidad-puntos
        print(f"Acaba de perder {puntos} punto y le queda {self.cantidad}")


ana = jugador()
carlos = jugador()
ana.cargarNombre()
carlos.cargarNombre()
ana.mostrarJugador()
carlos.mostrarJugador()
ana.consumirCantidad(2)
carlos.consumirCantidad(1)
ana.mostrarJugador()
carlos.mostrarJugador()
ana.consumirCantidad(1)
carlos.consumirCantidad(4)
ana.mostrarJugador()
carlos.mostrarJugador()
if (ana.cantidad < carlos.cantidad):
    print("Perdio", ana.nombre)
else:
    print("Gano", ana.nombre)
