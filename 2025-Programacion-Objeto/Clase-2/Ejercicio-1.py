"""
Realizar un objeto llamado auricular con atributo: 
marca, color, material y conector. Debe mostrar al 
menos 5 veces la marca ryzen y otras 5 la marca logitech
"""


class auricular:
    marca = "Logitech"
    color = "Negro"
    conector = "USB"

    def imprimirDatos(self):
        print(
            f"Auricular Marca:{self.marca} Color:{self.color} Conector:{self.conector} ")


auricular1 = auricular()
auricular1.imprimirDatos()
auricular2 = auricular()
auricular2.color = "Naranja"
auricular2.imprimirDatos()
auricular3 = auricular()
auricular3.marca = "ryzen"
auricular3.conector = "RG"
auricular3.imprimirDatos()
auricular4 = auricular()
auricular4.conector = "jack3.5"
auricular4.marca = "ryzen"
auricular4.imprimirDatos()
auricular5 = auricular()
auricular5.marca = "ryzen"
auricular5.color = "Rosado"
auricular5.imprimirDatos()
auricular6 = auricular()
auricular6.color = "Violeta"
auricular6.imprimirDatos()
auricular7 = auricular()
auricular7.color = "Violeta"
auricular7.imprimirDatos()
auricular8 = auricular()
auricular8.conector = "USB3.0"
auricular8.imprimirDatos()
auricular9 = auricular()
auricular9.marca = "ryzen"
auricular9.conector = "Serial"
auricular9.imprimirDatos()
auricular10 = auricular()
auricular10.marca = "ryzen"
auricular10.imprimirDatos()
