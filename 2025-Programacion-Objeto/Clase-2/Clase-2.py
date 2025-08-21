""" 
Metodos y constructores. 
"""
#   Con el constructor me ahorro la creacion de los atributos


class llave:
    material = "Oro"
    #   Constructor

    def __init__(self, tamanio, color, forma):
        print(
            f"La llave ha sido creada con el tamaño {tamanio} posee el color: {color} por ultimo su forma {forma}")


llave = llave("ancho", "rojo", "restangular")
