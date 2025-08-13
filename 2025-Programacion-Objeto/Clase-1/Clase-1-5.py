class lapicera():
    #   Son opcionales, si no los agrego al instancia toman esos valores
    def __init__(self,marca="Bic",color="Azul",medida="1.5"):
        print(f"La Lapicera es de marca {marca}, y de color {color}. Su medida es {medida}")
        
bic=lapicera()
parker=lapicera("Parker","Negro","2")