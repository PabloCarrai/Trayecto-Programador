colores=[]
print("Necesito que ingrese la cantidad de colores que va a ingresar")
ccolores=int(input())
for i in range(0,ccolores):
    print("Ingrese los colores ")
    colores.append(input()) #   asi agrego un elemento
    
for i in colores:
    print(i)