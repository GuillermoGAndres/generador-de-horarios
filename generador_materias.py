
''' Generador de materias CLI '''

def add_materia():
    name_materia = input("Escriba el nombre de la meteria: ")
    print("Dias en los que se imparten:")
    print("1.- Monday")
    print("2.- Turday")
    print("3.- Wedsday")
    print("4.- Thursday")
    print("5.- Friday")
    print("6.- Satardy")
    

    pass

def delete_materia():
    pass

def update():
    pass


print(" \tGenerador de materias CLI ")  
#Se tiene que verificar que esta en el rango dado
choice=-1;
while( not (choice > 0 and choice < 4 ) ):
    print("\tHorario")
    print("1.- Agregar materia")
    print("2.- Eliminar materia")
    print("3.- Actualizar materia")
    choice = int(input("Escoje una opcion: "))

if choice == 1:
    add_materia()
elif choice == 2:
    delete_materia()
elif choice == 3:
    update_materia()





