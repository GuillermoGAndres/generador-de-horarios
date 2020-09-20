

class Dia:
    """Representa el dia"""

    def __init__(self, nameDay, materias=list()):
        """Inicializa el nombre del dia y con sus respectivas materias 
        Un dia contendra muchas materias
        materias - sera una list
        dayName -  string
        """
        self.nameDay =  nameDay
        self.materias = materias

    def agregarMateria(self, materia):
        self.materias.append(materia)


    def __str__(self):
        string = self.nameDay + "\n"
        for materia in self.materias:
            string += str(materia)
        return string






