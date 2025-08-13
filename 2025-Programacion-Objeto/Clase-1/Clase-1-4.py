# Constructor(es un metodo que permite darle valor al atributo del objeto)
#class Cubierto():
    # Atributos
    #forma="cuchara"
    #marca="tramontina"
    #color="negro"
    #material="aluminio"
 
class Cubierto():
    #   Metodo con atributos que luego tengo que asignar
    def __init__(self,forma,marca,color,material):
        print(f" Se creo correctamente el cubierto con forma de {forma} de la marca {marca} y de color {color} con el material {material}")   

#   Objeto con constructor obligatorio
#   tengo que enviarle los valores de los atributos
cuchara=Cubierto("cuchara","tramontina","azul","plastico")
cuchara