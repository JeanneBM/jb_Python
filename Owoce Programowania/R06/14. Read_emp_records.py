# Ten program wyświetla rekordy
# zapisane w pliku employees.txt.

def main():
    # Otworzenie pliku employees.txt.
    emp_file = open('employees.txt', 'r')

    # Odczyt z pliku pierwszego wiersza, którym
    # jest pole imienia i nazwiska w pierwszym rekordzie.
    name = emp_file.readline()

    # Jeżeli pole zostało odczytane, należy kontynuować przetwarzanie.
    while name != '':
        # Odczytanie pola numeru identyfikacyjnego.
        id_num = emp_file.readline()

        # Odczytanie pola działu, w którym jest zatrudniony pracownik.
        dept = emp_file.readline()

        # Pozbycie się z pól znaków nowego wiersza.
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        # Wyświetlenie rekordu.
        print('Imię i nazwisko:', name)
        print('ID:', id_num)
        print('Dział:', dept)
        print()

        # Odczytanie pola imienia i nazwiska następnego rekordu.
        name = emp_file.readline()

    # Zamknięcie pliku.
    emp_file.close()

# Wywołanie funkcji main().
main()
