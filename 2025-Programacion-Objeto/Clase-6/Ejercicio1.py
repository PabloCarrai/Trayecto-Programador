"""
Realizar un programa que procese 10 clientes de un banco.
Se pide mostrar el tipo de cuenta (sueldo - credito).
Se debe permitir al usuario realizar transferencias y
depósitos en su cuenta mediante un cbu o alias que
es generado por el banco.
"""


class banco:
    def __init__(self):
        self.cbuAlias = []
        self.nombres = []
        self.fondos = 0
        self.nombre = input("Nombre del cliente? ")
        self.cuenta = input("Tipo de cuenta (sueldo/credito)? ")
        self.cbuAlia = input("Su CBU/Alias? ")
        self.nombres.append(self.nombre)
        self.cbuAlias.append(self.cbuAlia)

    def transferencias(self):
        montoTranferir = int(input("Cuanto va a transferir? "))
        for i in range(len(self.cbuAlias)):
            print(f"Titulares {self.nombres[i]} CBU/Alias: {self.cbuAlias[i]}")
            cbu = input("A que cbu va a transferir? ")
            if cbu not in self.cbuAlias:
                print("No reconocemos dicha cuenta. ")
        if (montoTranferir > self.fondos):
            print("No tiene fondos suficientes. ")
        else:
            self.fondos -= montoTranferir
            print(f"Usted cuenta con {self.fondos}")

    def deposito(self):
        montoDepositar = int(input("Cuanto va a depositar? "))
        self.fondos += montoDepositar
        print(f"Usted cuenta con {self.fondos}")


bono = banco()
bono.fondos = 344444444444
bono.deposito()
bono.transferencias()
hermanabono = banco()
hermanabono.fondos = 333333333333
hermanabono.deposito()
hermanabono.deposito()
print(hermanabono.cbuAlias)
hermanabono.deposito()
hermanabono.transferencias()
