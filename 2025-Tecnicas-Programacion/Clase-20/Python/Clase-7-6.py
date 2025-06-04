#   Ciclos
for i in range(1,6):
    print(i)


#   Necesitamos que solo ingrese y al final mostrar las temperaturas ingresadas

#   Acumulador
acu=""

for i in range(1,6):
    print("Vamos a ingresar la temperatura de los dias de la semana ")
    print(f"Necesito que ingrese la temperatura del {i} dia habil")
    dia=input()
    acu=acu+dia+"\n"

print(acu)

#   Contador
c=0
#   Ciclo while
print("Ingrese la letra a para ingresar")
letra=input()
while(letra=="a"):
    print("Esta dentro del ciclo y estas en la vuelva numero")
    print(c)
    c=c+1
    print("Ingrese la letra a para ingresar")
    letra=input()

print("cantidad de vuelvas realizadas ")
print(c)

