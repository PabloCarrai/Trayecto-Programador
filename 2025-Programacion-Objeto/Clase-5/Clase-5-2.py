""" 
Elaborar un objeto que permita mostrar por pantalla
10 usuarios de una plataforma de suscripcion de 
peliculas
"""


class pelicula:
    def __init__(self, nombre, anio, genero, suscripcion):
        nombre = input("Pelicula? ")
        anio = int(input("Año?  "))
        genero = input("Genero? ")
        suscripcion = input("Suscripcion? ")
        self.nombre = nombre
        self.anio = anio
        self.genero = genero
        self.suscripcion = suscripcion
        print(
            f"Nombre {self.nombre} Año: {self.anio} Genero: {self.genero} Suscripcion: {self.suscripcion}")


class usuarios:
    def __init__(self, id_usuario, nombre, mail, suscripcion):
        id_usuario += 1
        nombre = input("Nombre?  ")
        mail = input("Mail? ")
        suscripcion = input("Suscripcion? ")
        self.nombre = nombre
        self.mail = mail
        self.suscripcion = suscripcion
        print(
            f"Usuario {self.nombre} Mail {self.mail} Suscripcion {self.suscripcion}")


class alquiler:
    def __init__(self):
        pelicula = pelicula()
        usuario = usuarios()
        if (pelicula.suscripcion == usuario.suscripcion):
            print("Felicitaciones podes ver la pelicula")
        else:
            print("No podes verla ")


# ironman = pelicula()
# pepito = usuarios()

# if (ironman.suscripcion == pepito.suscripcion):
#     print("Felicitaciones podes ver la pelicula")
# else:
#     print("No podes ver la pelicula")


pocahonta = pelicula()
