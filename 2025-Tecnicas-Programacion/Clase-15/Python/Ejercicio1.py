"""
Realizar el ingreso de distintos presidentes del
mundo. Se pide contar y mostrar la cantidad de
presidentes ingresados y mostrar todos los
presidentes
"""

#   Contador de presidentes
cpre=0
#   Acumulador de los nombres de los presidentes
tpre=""
#   Variable para iniciar el ciclo
iniciamos=input("Arrancamos? (si/no)")
while(iniciamos!="no"):
    presidente=input("Ingrese nombre del presidente ")
    cpre=cpre+1
    tpre=tpre+f"""{presidente}
"""
    #   De alguna forma tenemos que salir o continuar
    iniciamos=input("Seguimos? (si/no)")

#   Imprimimos los presidentes y la cantidad
print(" Todos los presidentes: ")
print(f"{tpre}")
print(f" Cantidad de presidentes: {cpre}")