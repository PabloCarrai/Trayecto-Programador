#   desde donde arranco y hasta donde -1
for i in range(1, 20):
    print("Numero: ", i)
#   Numeros pares
#   Desde donde hasta donde y cada cuanto
for i in range(2, 21, 2):
    print("Numero: ", i)
#   Numeros impares
for i in range(3, 21, 3):
    print("Numeros: ", i)

for x in range(1, 21):
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input(f"Ingrese el apellido de " + nombre)
    nota1 = int(input(f"Ingrese la nota de {nombre}, {apellido} "))
    nota2 = int(input(f"Ingrese la nota de {nombre}, {apellido} "))
    nota3 = int(input(f"Ingrese la nota de {nombre}, {apellido} "))
    promedio = (nota1+nota2+nota3)/3
    print(f"El promedio de "+nombre+" "+apellido+" es: ", promedio)
    # otra forma mas practica
    print(f"El promedio de {nombre} {apellido} es {promedio}")
    if (promedio >= 7 and promedio <= 10):
        print(f"El alumno {nombre} {apellido} aprobo")
    elif (promedio >= 4 and promedio < 7):
        print(f"El alumno {nombre} {apellido} a diciembre")
    else:
        print(f"El alumno {nombre} {apellido} Desaprobo")
