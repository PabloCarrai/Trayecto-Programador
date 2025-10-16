import tkinter as tk


class menu:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Menu en tkinter")
        menu = tk.Menu()
        menu_archivo = tk.Menu(menu, tearoff=False)
        menu_archivo.add_command(
            label="Nuevo Archivo", accelerator="CTRL+N", command=self.imprimir_nombre
        )
        menu.add_cascade(menu=menu_archivo,label="Archivo")
        self.ventana.config(menu=menu)
        self.ventana.mainloop()

    def imprimir_nombre(self):
        print("Pablo")


menu = menu()
