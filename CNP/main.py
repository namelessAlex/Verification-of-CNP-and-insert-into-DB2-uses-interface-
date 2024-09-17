from cnp import CNP, Persoana, Angajat, MainFunction
  
def main():
# Obiect de tip Persoana
    persoana1 = Persoana("1900102410020", "Popescu", "Ion")
    MainFunction.show_details_for_person(persoana1)

# Obiect de tip Angajat
    angajat1 = Angajat("1900102410022", "Ionescu", "Maria", "Programator")
    MainFunction.show_details_for_person(angajat1)

main()