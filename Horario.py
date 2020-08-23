
class Horario():
    '''Define la estructura de una horario que contendra materias'''
    def __init__(self):
        '''
        @param materias: esta lista donde contendran las materias
        '''
        self.materias = []

    def agregarMateria(self, materia):
        self.materias.append(materia)

    def eliminarMateria(self, materia):
        self.materias.remove(materia)

    def modificarMeteria(self,oldMateria, newMateria):
        self.materias.remove(oldMateria)
        self.materias.append(newMateria)



