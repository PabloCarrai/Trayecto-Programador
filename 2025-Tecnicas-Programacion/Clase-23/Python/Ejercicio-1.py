"""
En una pizzeria se pide ingresar el precio de 10 pizzas, 
Se pide ordenar los precios de menor a mayor y mostrar el promedio de los precios.
"""

#   Creamos la lista vacia
pizzas=[]
#   Ingresamos los valores
for i in range(10):
    pizza=int(input("Ingrese el precio de la pizza   "))
    #   Lo agregamos a la lista
    pizzas.append(pizza)

print(pizzas)

#   Los ordenamos    
pizzas.sort()
#   Los mostramos
for i in range(len(pizzas)):
    #   Ordenados
    print(f"Ordenados quedaria {pizzas[i]}")
