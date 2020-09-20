from tkinter import *
from menuUI import Menu


class GeneradorHorariosGUI:
    """Administra la pantalla principal de la aplicacion"""

    def __init__(self):
        self.raiz = Tk()
        self.width = "1000"
        self.height = "600"
        self.raiz.geometry(f"{self.width}x{self.height}")
        self.raiz.title("Generador de horarios")
        self.raiz.config(bg='#254d74')
        self.hacerHorarioBtton = Button(self.raiz, text = "Hacer horario",
                command = self.hacerHorarioListenner,
                bg = "#4CAF50",
                activebackground = '#45a049',
                font = 'Verdana 13 bold ',
                width = 35,
                height = 2,
                bd = 0,
                fg = 'white',
                activeforeground = 'white', 
                cursor="hand1",
                relief = FLAT).place(
                x=int(self.width)/2 - 210, y=int(self.height)/2 - 80)

        self.salir = Button(self.raiz, text = "Salir", 
                command=self.raiz.destroy,
                bg = "#ff4d4d",
                activebackground = '#ff3333',
                font = 'Verdana 13 bold italic',
                width = 35,
                height = 2,
                bd = 0,
                fg = 'white',
                cursor="hand1",
                relief = "flat").place(
                x=int(self.width)/2 - 210, y=int(self.height)/2)
        self.raiz.mainloop()

    def hacerHorarioListenner(self):
        self.raiz.destroy()
        Menu()



if __name__ == "__main__":
    app = GeneradorHorariosGUI()
