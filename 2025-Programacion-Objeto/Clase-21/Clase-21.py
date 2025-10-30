#   Creamos un archivo

nombredelArchivo = input("Dime como quieres llamar al archivo ")
contenidoArchivo = input("Ingresa un contenido para dicho archivo  ")

with open(nombredelArchivo, "a") as archivo:
    archivo.write(contenidoArchivo)
    print(f"Hemos creado el archivo {nombredelArchivo}")
    print(f"Y agregamos el contenido {contenidoArchivo}")


with open(nombredelArchivo, "r") as archivo1:
    print(archivo1.read())

with open("Probando.txt", "a") as f:
    f.write("Queremos mas sueldo \n")
    f.write("Si no tenemos mas sueldo se pudre todo  \n")
    f.write("Hemos contratado al minotauro para hacer de fuerza de choque  \n")

with open("Probando.txt", "r") as f:
    print(f.read())



with open("audio.mp3", "r") as archivo1:
    print(archivo1.read())
