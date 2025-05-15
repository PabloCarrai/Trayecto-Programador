"""
Realizar el ingreso de distintos paises hasta que se ingresa
Argentina. Se pide contar la cantidad de paises ingresados y mostrar
la cantidad total y los distintos paises ingresados
"""
mostrar=""
c=1
pais=input("Ingrese un pais ")
while(pais!="Argentina"):
    pais=input("Ingrese un pais ")
    c=c+1
    mostrar=mostrar+f"""{pais}
"""
    
print("La cantidad total de paises ingresados es de {c}")
print(mostrar)