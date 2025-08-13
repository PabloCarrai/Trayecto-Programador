"""
Crear un objeto que se llame Parlantes y que tenga de 
atributos material, conector (tipo de conector), color 
y altavoces. Mostrar al menos 10 produciones diarias, 
debe existir por lo menos 2 dias que cambie mínimamente 
2 atributos y luego mostrarlo
"""

class Parlante():
    #   Atributos
    material="Acero"
    conector="RGB"
    altavoz="Redondo"
    #   Metodo
    def Imprimir(self):
        print(f"Material: {self.material} Conector: {self.conector} Altavoz: {self.altavoz}")
        
dia=Parlante()
dia.conector="USB"
dia.altavoz="Rectangular"
dia.Imprimir()

dia1=Parlante()
dia1.material="Madera"
dia1.Imprimir()

dia2=Parlante()
dia2.material="Goma"
dia2.Imprimir()

dia3=Parlante()
dia3.material="Caucho"
dia3.conector="HDMI"
dia3.Imprimir()

dia4=Parlante()
dia4.material="Plastico blando"
dia4.altavoz="Elicoidal"
dia4.Imprimir()

dia5=Parlante()
dia5.altavoz=6
dia5.Imprimir()

dia6=Parlante()
dia6.conector="RGB"
dia6.Imprimir()

dia7=Parlante()
dia7.material="Caucho"
dia7.Imprimir()

dia8=Parlante()
dia8.altavoz="Triangular"
dia8.Imprimir()

dia9=Parlante()
dia9.conector="USB3.0"
dia9.Imprimir()