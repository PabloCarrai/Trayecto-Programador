"""
Permitir el ingreso de 30 paises con sus respectivas capitales
y presidentes
"""
mostrar=""
for i in range(1,31):
    nombrep=input("Ingrese nombre del pais ")
    capitalp=input(f" Ingrese la capital de {nombrep} ")
    presidentep=(f"Ingrese el presidente del pais {nombrep}")
    #acumulo las entradas en una variable para mostrar todo junto
    mostrar=mostrar+f"""El nombre del pais es: {nombrep}, 
    la capital es {capitalp} 
    Su presidente es {presidentep}"""
    
mostrar