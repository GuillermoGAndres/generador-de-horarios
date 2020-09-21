from tkinter import *

class AgregarMateriaUI:

    def __init__(self):
        self.raiz = Tk()
        self.width = "1000"
        self.height = "600"
        self.raiz.geometry(f"{self.width}x{self.height}")
        self.raiz.title("Generador de horarios")

        self.agregarMeteriaLabel = Label(self.raiz, text="Nombre de la materia",
                font = 'Verdana 18'
                ).pack()
        self.nombreMateria = StringVar()
        self.agregarMeteriaText = Entry(self.raiz, textvariable=self.nombreMateria,
                font = 'Verdana 18').pack()

        self.nombreProfesorLabel = Label(self.raiz, text="Nombre del profesor", font='Verdana 18').pack()
        self.nombreProfesor = StringVar()
        self.nombreProfesorText = Entry(self.raiz, textvariable=self.nombreProfesor, font='Verdana 18').pack()

        self.horaInicioLabel = Label(self.raiz, text="Hora que inicia", font='Verdana 18').pack()
        self.horaInicio = StringVar()
        self.horaInicioText = Entry(self.raiz, textvariable=self.horaInicio, font='Verdana 18').pack()

        self.horaFinalLabel = Label(self.raiz, text="Hora que acaba", font='Verdana 18').pack()
        self.horaFinal = StringVar()
        self.horaFinalText = Entry(self.raiz, textvariable=self.horaFinal, font='Verdana 18').pack()

        self.diasSemanaLabel = Label(self.raiz, text="Dias en las que se imparte", font='Verdana 18').pack()
        self.lunes = IntVar()
        self.martes = IntVar()
        self.miercoles = IntVar()
        self.jueves = IntVar()
        self.viernes = IntVar()
        self.sabado = IntVar()
        self.domingo = IntVar()

        self.chkbtnLunes = Checkbutton(self.raiz, text="Lunes", variable=self.lunes, onvalue=1, offvalue=0, font='Verdana 18').pack()
        self.chkbtnMartes = Checkbutton(self.raiz, text="Martes", variable=self.martes, onvalue=1, offvalue=0, font='Verdana 18').pack()
        self.chkbtnMiercoles = Checkbutton(self.raiz, text="Miercoles", variable=self.miercoles, onvalue=1, offvalue=0, font='Verdana 18').pack()
        self.chkbtnJueves = Checkbutton(self.raiz, text="Jueves", variable=self.jueves, onvalue=1, offvalue=0, font='Verdana 18').pack()
        self.chkbtnViernes = Checkbutton(self.raiz, text="Viernes", variable=self.viernes, onvalue=1, offvalue=0, font='Verdana 18').pack()
        self.chkbtnSabado = Checkbutton(self.raiz, text="Sabado", variable=self.sabado, onvalue=1, offvalue=0, font='Verdana 18').pack()
        self.chkbtnDomingo = Checkbutton(self.raiz, text="Domingo", variable=self.domingo, onvalue=1, offvalue=0, font='Verdana 18').pack()
        
        self.agregarMeteriaBtn = Button(self.raiz, text="Agregar materia", command=self.agregarMateriaListener, font='Verdana 18').pack()

        self.raiz.mainloop();
        pass

    def agregarMateriaListener(self):
        """Va tener a accesso a los campos escritos por el usuario"""
        print(self.nombreMateria.get())
        print(self.nombreProfesor.get())
        print("Lunes: ")
        print(self.lunes.get())



# Test
AgregarMateriaUI()
