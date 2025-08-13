class Botella:
    #   Atributos
    color="Negro"
    capacidad="1L"
    contenido="Vino"
    
dia1=Botella()
print(dia1.capacidad)
print(dia1.color)
print(dia1.contenido)

dia2=Botella()
print(dia2.capacidad)
print(dia2.color)
print(dia2.contenido)
#   Aca cambio algunos de los atributos del objeto real
dia3=Botella()
dia3.capacidad="2L"
dia3.contenido="Agua"
print(dia3.capacidad)
print(dia3.color)
print(dia3.contenido)
