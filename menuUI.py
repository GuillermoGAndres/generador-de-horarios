from tkinter import *
from agregarMateriaUI import AgregarMateriaUI

class Menu:

    def __init__(self):
        self.raiz = Tk()
        self.width = "1000"
        self.height = "600"
        self.raiz.geometry(f"{self.width}x{self.height}")
        self.raiz.title("Generador de horarios")

        self.leftFrame = Frame(self.raiz)
        self.leftFrame.pack(side = LEFT)
        self.agregarMateriaButton = Button(self.leftFrame, text = "Agregar materias", command=self.agregarMateriaListener).pack()
        self.actualizarMateriaButton = Button(self.leftFrame, text = "Actualizar materia").pack()
        self.eliminarMateriaButton = Button(self.leftFrame, text = "Eliminar materia").pack()

        self.generarHorarioButton = Button(self.leftFrame, text ="Generar pdf").pack()

        self.raiz.mainloop()
        pass

    def agregarMateriaListener(self):
        self.raiz.destroy()
        AgregarMateriaUI()
        pass
    
    def actualizarMateriaListener(self):
        pass

    def eliminarMateriaListener(self):
        pass
    
    def generarHorarioListener(self):
        pass
