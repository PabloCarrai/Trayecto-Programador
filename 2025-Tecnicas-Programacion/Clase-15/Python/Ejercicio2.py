"""
Piedra Papel Tijera
"""
cganados=0
jugamos=input("Arrancamos un Piedra Papel Tijera? (Si/No)")
while(jugamos!="No"):
    epc=input("La pc elije Piedra Papel Tijera ")
    eus=input("Elije tu mano Piedra Papel Tijera ")
    if (epc==eus):
        print("Empate")
        print(f"Vos elejiste {eus} yo eleji {epc}")
        jugamos=input("Seguimos? (Si/No)  ")
    elif(epc=="Piedra" and eus=="Papel"):
        print("Ganaste")
        cganados=cganados+1
        print(f"Vos elejiste {eus} yo eleji {epc}")
        jugamos=input("Seguimos? (Si/No)  ")
    elif(epc=="Piedra" and eus=="Tijera"):
        print("Gane")
        print(f"Vos elejiste {eus} yo eleji {epc}")    
        jugamos=input("Seguimos? (Si/No)  ")
    elif(epc=="Tijera" and eus=="Papel"):
        print("Gane")
        print(f"Vos elejiste {eus} yo eleji {epc}")
        jugamos=input("Seguimos? (Si/No)  ")
    elif(epc=="Tijera" and eus=="Piedra"):
        print("Ganaste")
        cganados=cganados+1
        print(f"Vos elejiste {eus} yo eleji {epc}")
        jugamos=input("Seguimos? (Si/No)  ")    
    elif(epc=="Papel" and eus=="Piedra"):
        print("Gane")
        print(f"Vos elejiste {eus} yo eleji {epc}")
        jugamos=input("Seguimos? (Si/No)  ")
    elif(epc=="Papel" and eus=="Tijera"):
        print("Ganaste")
        cganados=cganados+1
        print(f"Vos elejiste {eus} yo eleji {epc}")    
        jugamos=input("Seguimos? (Si/No)  ")
print(f" Ganastes {cganados} manos")