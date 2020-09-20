
class Materia():
    '''Representa un materia'''
    def __init__(self, nombreMateria, hora):
        '''
        Cada materia le correspondra un objet hora.
        nombreMateria -> str
        inia -> str
        acaba -> str
        '''
        self.nombreMateria = nombreMateria
        self.hora = hora

    def __str__(self):
        return f'Materia: {self.nombreMateria}\nInicia: {self.hora.horaInicio}\nAcaba: {self.hora.horaFinal}\n'

