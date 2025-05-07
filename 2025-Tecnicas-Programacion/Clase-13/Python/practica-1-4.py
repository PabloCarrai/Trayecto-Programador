"""
Codificar un programa en python que ingrese 10 
productos y permita comprar a 10 clientes. 
Mostrar el total por cada cliente y 
el total en el día
"""


#   Acumulador gasto por dia
tdia = 0
for i in range(10):
    #   Acumulador gasto por cliente
    tcliente = 0
    #   cliente
    nombre = input("Su nombre: ")
    apellido = input(f"{nombre} su apellido ")
    for e in range(10):
        producto = input("Producto  ")
        precio = float(input("Precio $ "))
        #   Acumulo lo gastado por el cliente
        tcliente = tcliente+precio
    #   El gasto por total por cliente
    print(f"El total gastado por {nombre} {apellido} es de ${tcliente}")
    tdia = tdia+tcliente
#   Imprimo el gasto por dia
print(f"El total gastado por dia es ${tdia}")
