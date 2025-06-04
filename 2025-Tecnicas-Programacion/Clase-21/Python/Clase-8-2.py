#   Matriz
filas=[
    ["Nombre y Apellido","Juan"],
    ["Edad",21]]

#   Mostrar la matriz
for i in filas: # recorro las filas
    print(i)
    for j in i: #   veo contenido del vector
        print(j)
        
#   Funciona por ser matriz
for i,j in filas:
    print(i,j)
    
filas1=[["Nombre y Apellido","Edad","Mail"],
        ["Juan Perez,",21,"juanp@gmail.com"],
        ["Juan Rez,",23,"jnp@gmail.com"]
        ]

for i,j,k in filas1:
    print(i,j,k)

#   Union de vectores
