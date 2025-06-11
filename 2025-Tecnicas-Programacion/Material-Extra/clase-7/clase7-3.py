Nombre = "Juan"
Numero1 = 2
Numero2 = 3
#¿Cómo hago para mostrar un mensaje previamente del valor que tengo en la variable?
print("Mirá que lindo está el día me comentó el vecino "+Nombre)#En este caso se utiliza el signo + porque tengo un texto como mensaje y le voy a concatenar otro texto. Porque la variable nombre almacena un tipo de dato texto. Si fuese numérico no voy a poder concatenar, ya que el tipo de dato texto, y el tipo de dato numérico son distintos entre si.
#¿Qué pasa si concateno este mismo mensaje con un número?
#print("Mirá que lindo está el día me comentó el vecino "+Numero1)#Aparece el siguiente error: TypeError: can only concatenate str (not "int") to str. Qué me indica que no se puede CONCATENAR texto con un número.
#¿Cómo lo muestro?
print("Mirá que linda está el día me comento el vecino ",Numero1)#En lugar del signo +, utilizamos el signo ,. Que permite distinguir entre texto y número. En este caso podrá mostrar el mensaje
#Ahora bien, esto también se puede mostrar de otra manera, que es utilizando el printf
print(f"Mirá que linda está el día me comento el vecino {Numero1}")#El printf nos permite mostrar cualquier tipo de dato, sin importar cual sea, y también me permite no salir del mensaje, es decir, no tengo que estar entrando y saliendo para poder informar el valor que está almacenado dentro de una variable