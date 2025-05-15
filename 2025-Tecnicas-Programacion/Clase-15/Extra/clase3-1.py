#Ingreso de 30 paises con sus respectivas capitales y presidentes.
mostrar=""
for P in range(1,31):
    nombrep=input("Ingrese el nombre del país a ingresar: ")
    capitalp=input(f"Ingrese la capital de {nombrep}: ")
    presidentep=input(f"Ingrese el presidente de {nombrep}: ")
    mostrar=mostrar+f"""El nombre del país es: {nombrep}.
La capital del país {nombrep} es: {capitalp}.
Su presidente es: {presidentep}.
"""
print(mostrar)