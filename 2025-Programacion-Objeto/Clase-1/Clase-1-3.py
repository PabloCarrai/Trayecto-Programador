class Mesa:
    #   Atributos
    material="Madera"
    patas="4"
    forma="Rectangular"
    color="Caoba"
    
    #   Metodo(Funcion de una clase)
    def Mostrar(self):
        print(f"La mesa es de material: {self.material}. tiene {self.patas}.Posee forma {self.forma} Su color es {self.color} ")
        
dia1=Mesa()
dia1.Mostrar()
dia2=Mesa()
dia2.Mostrar()
dia3=Mesa()
dia3.material="plastico"
dia3.color="azul"
dia3.Mostrar()