#vamos a crear un minijuego en el que se va a realizar 10 preguntas, por cada respuesta correcta, se sumaran 5 puntos, en caso de responder incorrectamente se restaran 2 puntos.

ctotal=0
# a="h2O"
def rta(a):
    # rta1=="h2O"
    if(rta1==a):
        ctotal=ctotal+5
    else:
        ctotal=ctotal-2

print("""Pregunta 1
¿Qué elementos químicos se necesitan para generar agua?
""")
rta1=input()
rta("h20")
print("""Pregunta 2
¿Cuál es el idioma que era predominante en la antigua roma?
""")
rta1=input()
rta("latin")
print("""Pregunta 3
¿Qué estado tiene el agua cuando es hielo?
""")
rta1=input()
rta("solido")
print("""Pregunta 4
¿Cuál es el nombre del árbol nacional de argentina?
""")
rta1=input()
if(rta1=="Ceibo"):
    ctotal=ctotal+5
else:
    ctotal=ctotal-2
print("""Pregunta 5
¿Quién inventó la transfusión de sangre?
""")
rta1=input()
if(rta1=="Agote"):
    ctotal=ctotal+5
else:
    ctotal=ctotal-2
print("""Pregunta 6
¿Quién inventó la penisilina?
""")
rta1=input()
if(rta1=="Fleming"):
    ctotal=ctotal+5
else:
    ctotal=ctotal-2
print("""Pregunta 7
¿Qué famoso corredor argentino fue el único campeón de f1?
""")
rta1=input()
if(rta1=="Fangio"):
    ctotal=ctotal+5
else:
    ctotal=ctotal-2
print("""Pregunta 8
¿Qué famoso corredor argentino fue el único campeón de f1?
""")
rta1=input()
if(rta1=="H2O"):
    ctotal=ctotal+5
else:
    ctotal=ctotal-2
print("""Pregunta 9
¿De qué color es el caballo blanco de San Martin?
""")
rta1=input()
if(rta1=="Blanco"):
    ctotal=ctotal+5
else:
    ctotal=ctotal-2
print("""Pregunta 10
¿Qué famoso procer argentino cruzó los andes?
""")
rta1=input()
if(rta1=="San Martin"):
    ctotal=ctotal+5
else:
    ctotal=ctotal-2

print(f"puntuación final : {ctotal}")
if(ctotal>=25 and ctotal<50):
    print("Felicitaciones ganaste humildemente")
elif(ctotal==50):
    print("Felicitaciones ganaste y sos el campeón del mundo")
else:
    print("Has perdido por afano!")