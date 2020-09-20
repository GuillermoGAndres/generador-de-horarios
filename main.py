from hora import Hora
from materia import Materia
from dia import Dia

def main():
    hora =  Hora("7:00", " 9:00")
    materia1 = Materia("Bases Datos", hora)
    materia2 = Materia("Sistemas", Hora("9:00", "11:00"))
    materias = [materia1, materia2]
    oneday = Dia("Lunes")
    print(oneday)




    pass

if __name__ == "__main__":
    main()

