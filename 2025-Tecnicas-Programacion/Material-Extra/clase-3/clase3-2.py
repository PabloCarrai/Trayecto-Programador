#Realizar el ingreso de distintos paises hasta que se ingresa Argentina. Se pide contar la cantidad de países ingresados y mostrar la cantidad total y los distintos paises ingresados.
c=1
mostrar=""
pais=input("Ingrese un país:")
while(pais!="Argentina"):
    pais=input("Ingrese un país:")
    c=c+1
    mostrar=mostrar+f"""{pais}
"""
print("La cantidad total de paises ingresados es de:",c)
print(mostrar)