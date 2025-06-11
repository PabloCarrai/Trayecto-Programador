print("\033[3;34;47m"+"Bienvenido a Piedra ✊ Papel ✋ o Tijera ✌ 1.0")
print("\x1b[;37;m"+"Bienvenido a Piedra ✊ Papel ✋ o Tijera ✌ 1.0")
print("""Elija una opción:
1) Piedra ✊
2) Papel ✋
3) Tijera ✌""")
j1=input()
while(j1!="1" and j1!="2" and j1!="3"):
    print ("""Ingrese una opción válida
1) Piedra ✊
2) Papel ✋
3) Tijera ✌""")
    j1=input()
if(j1=="1" or j1=="2"):
    j2="2"
else:
    j2="1"

if(j1=="1" and j2=="1" or j1=="2" and j2=="2" or j1=="3" and j2=="1"):
    print("Empate")
elif(j1=="2" and j2=="1" or j1=="3" and j2=="2"):
    print("Has ganado")
else:
    print("Has perdido")