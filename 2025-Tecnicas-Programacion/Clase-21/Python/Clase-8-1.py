#   Declaracion de vectores
colores=[]   #Declaro un vector(Lista) vacio
#   Asignarle un valor, al declarar la lista
colores=["Rojo","Amarillo",33,37,22] #  valores separados por ,
#   Ingresar valores a una lista mediante for
for i in range(0,9):
    print("Ingrese un valor para almacenar   ")
    valor=input()
    colores.append(valor)   #  Guardo lo que almaceno en valor en la lista colores
#   Mostrar los valores de la lista
#   por uso de indices
print(colores[3])   #   Solo se ve el 4 elemento de la lista
#   Otra manera usando un for
for i in colores:
    print(i)
#   Borrar todo en la lista
for i in colores:
    colores="" 
#   Otra forma igual
colores.clear() # vacia el vector/lista
