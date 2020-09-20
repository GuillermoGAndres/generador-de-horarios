from dia import Dia

class Horario():
    '''Define la estructura de una horario que contendra materias'''
    self.lunes = Dia("Lunes")
    self.martes = Dia("Martes")
    self.miercoles = Dia("Miercoles")
    self.jueves = Dia("Jueves")
    self.viernes = Dia("Viernes")
    self.sabado = Dia("Sabado")
    self.domingo = Dia("Domingo")

    def __init__(self):
        '''
        Uno horario tendra muchos dias
        @param materias: esta lista donde contendran las materias
        '''
        pass

    def agregarMateria(self,materia):

    def eliminarMateria(self, materia):
        self.materias.remove(materia)

    def modificarMeteria(self,oldMateria, newMateria):
        self.materias.remove(oldMateria)
        self.materias.append(newMateria)



