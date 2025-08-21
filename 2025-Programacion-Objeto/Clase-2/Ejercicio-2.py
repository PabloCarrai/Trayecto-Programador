"""
Realizar un objeto con un constructor que permita 
comprar entradas de una funcion de teatro. 
Debe permitir ingresar la cantidad de butacas, 
sector, precio y fecha. Debe mostrar las 5 funciones. 
Las fechas son: 30/08 - 11/09 - 21/09 - 14/10 y 25/12
"""


class reservas:
    def __init__(self, cButacas, sector, precio, fecha):
        print(
            f"Cantidad de Butacas Vendidas: {cButacas}, Sectores: {sector}, Precio:{precio}, Fecha:{fecha}")


r1 = reservas(3, "Campo", "2560", "30/08")
r2 = reservas(4, "Vip", "3000", "11/09")
r3 = reservas(5, "Centro", "2340", "21/09")
r4 = reservas(6, "Vip", "5400", "14/10")
r5 = reservas(4, "Pulman", "5600", "25/12")
