"""
Programar un piedra papel o tijera

#   revisar las conbinaciones, me marie con el horario
"""

j1=int(input("Elija 1)Piedra, 2)Papel, 3)Tijera"))
j2=int(input("Elija 1)Piedra, 2)Papel, 3)Tijera"))

if(j1==j2):
    print("Empate jugador 1 {j1} jugador 2 {j2}")
elif(j1==1 and j2==2): #  Piedra papel
    print("jugador 1 {j1} jugador 2 {j2}")
    print("Gana jugador 2 ")
elif(j1==2 and j2==1): #  Papel Piedra
    print("jugador 1 {j1} jugador 2 {j2}")
    print("Gana jugador 1 ")
elif(j1==2 and j2==3): #  Papel tijera
    print("jugador 1 {j1} jugador 2 {j2}")
    print("Gana jugador 2 ")
elif(j1==3 and j2==2): #  tijera Papel 
    print("jugador 1 {j1} jugador 2 {j2}")
    print("Gana jugador 1 ")
elif(j1==1 and j2==3): #   piedra tijera
    print("jugador 1 {j1}jugador 2 {j2}")
    print("Gana jugador 1 ")
elif(j1==3 and j2==1): #   tijera piedra
    print("jugador 1 {j1}jugador 2 {j2}")
    print("Gana jugador 2 ")



