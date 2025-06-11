Colores=[]

print("necesito que ingrese la cantidad de colores que desea ingresar: ")
CantColores=int(input())

for I in range(0,CantColores):
    print("Ingrese el color que desea guardar: ")
    Colores.append(input())

for I in Colores:
    print(I)