from tkinter import *

class Menu:

    def __init__(self):
        self.raiz = Tk()
        self.width = "1000"
        self.height = "600"
        self.raiz.geometry(f"{self.width}x{self.height}")
        self.raiz.title("Generador de horarios")


        # self.agregarMateriaButton = Button()

        self.raiz.mainloop()
        pass
