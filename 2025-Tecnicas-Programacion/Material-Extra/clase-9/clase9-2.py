#Vamos a ver otras funciones en listas
Colores = ["rojo", "Azul", "Amarillo"]
for x in Colores:
    print(x)
#Para agregar a un array esta la función append, es para agregar al final de la lista un valor
Colores.append("Verde")
#["rojo","Azul","Amarillo","Verde"]
for x in Colores:
    print(x)
#Para eliminar un valor, hay dos funciones. La primera es remove()
Colores.remove("Verde")#Aca el remove, elimina como argumento a un valor, siempre y cuando coincida con el argumento que enviamos en los parentesis
#   0      1       2         3 
#["rojo","Azul","Amarillo","Verde"]
#Elimino el "verde"
#["rojo","Azul","Amarillo"]
for x in range(len(Colores)):
    print(x,Colores[x])
#Otra funcion que sirve para eliminar un elemento de la lista. La otra se llama pop().
#Colores.pop()#Asi sin ningun valor, por defecto va a eliminar el ultimo elemento de la lista.
#Lo que va a eliminar es el valor "Amarillo", porque es el ultimo valor de nuestro vector
#["rojo","Azul","Amarillo"]
#Esti queda
#["rojo","Azul"]
#El pop tiene una cuestion que es la siguiente, si se le introduce un valor numerico va a ir hasta ese indice y borarrá el valor que se encuentra en ese indice y pondra el otro valor que se encuentre en nuestro array después del indice 1 y lo colocará alli. Osea:
#["rojo","Azul","Amarillo"]
Colores.pop(1)
#   0      1      2
#["rojo","Azul","Amarillo"]
#Osea nuestro array va a quedar solo el rojo
#   0        1
#["rojo", "Amarillo"]
for x in range(len(Colores)):
    print(x,Colores[x])

#Agregar en un indice o posicion especifica se utiliza en python el insert()
Colores.insert(1,"Gris")
Colores.insert(2,"Negro")
for x in range(len(Colores)):
    print(x,Colores[x])