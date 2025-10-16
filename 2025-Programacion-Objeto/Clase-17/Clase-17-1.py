import tkinter as tk


class menu:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Menu en tkinter")

        menubar = tk.Menu(self.ventana)
        menu_Archivo = tk.Menu(menubar)
        menu_Archivo.add_command(label="Nuevo", command=self.imprimir_nombre)
        menu_Archivo.add_command(label="Abrir", command=self.imprimir_nombre)
        menu_Archivo.add_command(label="Guardar", command=self.imprimir_nombre)
        menu_Archivo.add_command(label="Guardar Como", command=self.imprimir_nombre)
        menu_Archivo.add_command(label="Cerrar", command=self.salir)
        self.ventana.bind_all("<Control-n>", self.imprimir_nombre)

        menubar.add_cascade(label="Archivo", menu=menu_Archivo)
        self.ventana.config(menu=menubar)
        self.ventana.mainloop()

    def imprimir_nombre(self,evento=None):
        print("Pablo")

    def salir(self):
        print("Adios")
        self.ventana.destroy()


menu = menu()
