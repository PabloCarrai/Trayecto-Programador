def Potencia():
    print("Ingrese el número que desea calcular su cuadrado:")
    a=int(input())
    a=a**2
    return a

def Saludar():
    print("╔════════════════════════════╗")
    print("║ Bienvenido a Calulator 2.0 ║")
    print("╚════════════════════════════╝")
    return "todo ok"

Saludar()
print(Potencia())