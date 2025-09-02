productos = [
    [0, "televisor JBL", "JBL", 2000],
    [1, "televisor Sansung", "sansung", 4000],
    [2, "smartv JBL", "JBL", 10000],
    [3, "smartv motorola", "motorola", 150000],
]


class cliente:
    id_cliente = 0
    id_cliente += 1

    def __init__(self, nomcliente, direccion):
        nomcliente = input("Nombre del cliente: ")
        direccion = input("Direccion? ")


class carrito:
    id_carrito=0
    id_carrito+=1
    def __init__(self,idproducto):
        idproducto=int(input("Ingrese id producto"))
        
        
for i in range(10):
    cliente=cliente()
    print("Este es el catalogo de nuestros productos ")
    for e in range(len(productos)):
        for z in range(4):
            print(productos[e][z])