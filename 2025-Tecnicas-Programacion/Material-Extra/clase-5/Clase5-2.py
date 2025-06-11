#Realizar un programa que permita ingresar los equipos de una liga de futbol, sus jugadores y sus entrenadores.
def Equipos(nombre="",fundacion="",presidente=""):
    nombre=input("Ingrese el nombre del equipo: ")
    fundacion=input(f"Ingrese el año que fue fundado el equipo {nombre}: ")
    presidente=input(f"Ingrese el presidente actual del equipo {nombre}: ")
    MostrarEquipo=f"""{nombre} {fundacion} {presidente}"""
    return MostrarEquipo
def Entrenador(nombre="",edad="",esquema="",contrato=""):
    nombre=input("Ingrese el nombre del entrenador del equipo:")
    edad=input(f"Ingrese la edad del entrenador {nombre}: ")
    esquema=input(f"Ingrese el esquema del entrenador {nombre}: ")
    contrato=input(f"Ingrese el contrato que posee el entrenador {nombre}: ")
    MostrarEntrenador=f"""{nombre} {edad} {esquema} {contrato}"""
    return MostrarEntrenador
def Jugadores(nombre="",edad="",posicion="",contrato=""):
    nombre=input("Ingrese el nombre del jugador del equipo:")
    edad=input(f"Ingrese la edad del jugador {nombre}: ")
    posicion=input(f"Ingrese la posicion del jugador {nombre}: ")
    contrato=input(f"Ingrese el contrato que posee el jugador {nombre}: ")
    MostrarJugador=f"""{nombre} {posicion} {edad} {contrato}"""
    return MostrarJugador

print("Necesito que ingreses el nombre de la liga que vamos a ingresar: ")
NombreLiga=input()
print(f"Necesito que ingreses la cantidad de equipos que juegan en la liga {NombreLiga}:")
CEquipos=int(input())
for I in range(0,CEquipos):
    print(f"Ingrese el {I+1} equipo de la liga {NombreLiga}: ")
    print("Ingrese la cantidad de jugadores que posee ese equipo: ")
    CJugadores=int(input())
    MostrarJugadores=""
    for J in range(0,CJugadores):
        #MostrarJugadores=Mostrarjugadores+Jugadores()
        MostrarJugadores+=Jugadores()
    print(MostrarJugadores)
    print(Equipos())
    print(Entrenador())
