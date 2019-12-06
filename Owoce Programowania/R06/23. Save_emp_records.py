# Ten program pobiera od użytkownika dane pracownika,
# a następnie zapisuje rekordy w pliku employee.txt.

def main():
    # Pobranie liczby rekordów, które mają być utworzone.
    num_emps = int(input('Podaj liczbę rekordów, ' +
                         'które mają zostać utworzone: '))

    # Otworzenie pliku do zapisu.
    emp_file = open('employees.txt', 'w')

    # Pobranie danych o poszczególnych
    # pracownikach i zapisanie ich w pliku.
    for count in range(1, num_emps + 1):
        # Pobranie danych o pracowniku.
        print('Podaj dane o pracowniku nr ', count, sep='')
        name = input('Imię i nazwisko:')
        id_num = input('Numer identyfikacyjny: ')
        dept = input('Dział: ')

        # Zapisanie danych jako rekordu w pliku.
        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

        # Wyświetlenie pustego wiersza.
        print()

    # Zamknięcie pliku.
    emp_file.close()
    print('Rekordy pracowników zostały zapisane w pliku employees.txt.')

# Wywołanie funkcji main().
main()
