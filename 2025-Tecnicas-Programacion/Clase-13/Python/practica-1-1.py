persona = "Juan"
edad = 21
persona = input("Ingresa tu nombre ")
edad = float(input("Ingrese su edad: "))
#Para los ingresos con numeros, se tiene que indicar
#el tipo de numero que espera ingresar, int() float()
#edad=float(input("Ingrese su edad:")) float es para decimales
print("La persona es: ", persona)
if (edad > 18):
    print(persona, " Es mayor de 18")
else:
    print("Es menor a 18")
