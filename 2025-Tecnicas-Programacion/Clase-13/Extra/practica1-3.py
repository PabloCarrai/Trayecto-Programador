"""for I in range (1,11): Todos los numeros
    print("Número: ",I)
for I in range (2,21,2): Numeros Pares
    print("Número: ",I)
for I in range (1,21,2): Numeros Impares
    print("Número: ",I)
for x in range (1,11):
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido de "+nombre)
    Nota1 = int(input("Ingrese la primer nota de "+nombre+" "+apellido))
    Nota3 = int(input("Ingrese la segunda nota de "+nombre+" "+apellido))
    Nota2 = int(input("Ingrese la tercer nota de "+nombre+" "+apellido))
    Promedio=(Nota1+Nota2+Nota3)/3
    print("El promedio de "+nombre+" "+apellido+" es: ",Promedio)"""

for x in range (1,11):
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input(f"Ingrese el apellido de {nombre}: ")
    Nota1 = int(input(f"Ingrese la primer nota de {nombre} {apellido}: "))
    Nota3 = int(input(f"Ingrese la segunda nota de {nombre} {apellido}: "))
    Nota2 = int(input(f"Ingrese la tercer nota de {nombre} {apellido}: "))
    Promedio=(Nota1+Nota2+Nota3)/3
    print(f"El promedio de {nombre} {apellido} es de: {Promedio}")
    if(Promedio>=7 and Promedio<=10):
        print(f"El alumno {nombre} {apellido} está Aprobado!")
    elif(Promedio>=4 and Promedio<7):
        print(f"El alumno {nombre} {apellido} está DICIEMBRE☺")
    else:
        print(f"El alumno {nombre} {apellido} está FEBRERO☻")
        