
"""
Vayan armando un programa que permita calcular el total 
de una compra para 20 clientes. Sabiendo que los productos 
son: televisores y smartv. Se necesita saber el mínimo gastado
y el promedio gastado
"""


class hipermercado:
    total_compra = 0
    televisores = 10000
    smartv = 15000

    def compra(self, cant_Compras):
        for i in range(cant_Compras):
            compra = int(input(
                f"Que producto desea comprar? (1)televisores {self.televisores} /(2)Smartv {self.smartv}?"))
            if compra == 1:
                print(
                    f"Usted acaba de adquirir un televisor al precio de {self.televisores}")
                self.total_compra = self.total_compra+self.televisores
            else:
                if compra == 2:
                    print(
                        f"Usted acaba de adquirir un smartv al precio de {self.smartv}")
                self.total_compra = self.total_compra+self.smartv

    def gastoTotal(self):
        print(f"Usted ha gastado {self.total_compra}")


comprador = hipermercado()
comprador.compra(3)
comprador.gastoTotal()
