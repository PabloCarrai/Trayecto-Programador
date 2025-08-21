""" 
metodos instancia y clases en los objetos
"""
#   instancias estaticas(Metodos sin instancia un objeto)


class Equipo:
    # atributo
    nombrejg = "Pablo"
    posicion = "Defensa"
    altura = "1.80"
    peso = "49"
    pelo = "Rubio"

    def mostrar():
        print("Hola Pablo")

    #   Metodo estatico
    @staticmethod
    def prueba(cls):  # Requisito de referencia al metodo estatico
        print("Hola Mauro")


#   como llamar al metodo estatico para que funcione
cars = Equipo()
#   Aca llamo al metodo estatico sin definir un objeto instanciado
Equipo.prueba(15)
#   Los metodos estaticos no pueden acceder a los atributos.
