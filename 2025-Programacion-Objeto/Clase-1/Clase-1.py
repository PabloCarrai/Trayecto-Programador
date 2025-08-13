#   Definimos un objeto llamado Persona
class Persona:
    # aca van los metodos y atributos    
    nombre = "Pepe"   #   atributo(Caracteristicas)
    pelo = "negro"    #   atributo(Caracteristicas)
    
    
#   Instancio(creo) un objeto
persona1=Persona()

#   Muestro los atributos de este objeto persona1
print(persona1.nombre)
persona2=Persona()
print(persona2.pelo)
#   Cambiar atributo(Sobrescribir el atributo)
persona2.pelo="Rubio"
print(persona2.pelo)

