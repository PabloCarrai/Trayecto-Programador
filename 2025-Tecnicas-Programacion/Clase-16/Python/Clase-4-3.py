def saludar(nombre):
    return f"Bienvenido {nombre}"

#   Funciones con parametros
def suma(numero1, numero2): # adentro del parentesis van los parametros
    suma=numero1+numero2
    return suma

#   Envio los argumentos(valores) de cada parametro
print(suma(1,3))
print(saludar("Juan"))


a=int(input("Ingresa un numero "))
b=int(input("Ingresa otro numero "))
print(suma(a,b))