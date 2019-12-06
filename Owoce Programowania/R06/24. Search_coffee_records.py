# Ten program pozwala użytkownikowi na
# wyszukiwanie w pliku coffee.txt rekordów
# dopasowanych do opisu.

def main():
    # Utworzenie zmiennej boolowskiej do użycia jako flagi.
    found = False

    # Pobranie szukanej wartości.
    search = input('Podaj nazwę kawy, której szukasz: ')

    # Otworzenie pliku coffee.txt.
    coffee_file = open('coffee.txt', 'r')

    # Odczytanie pola opisu pierwszego rekordu.
    descr = coffee_file.readline()

    # Odczytanie pozostałej części pliku.
    while descr != '':
        # Odczytanie pola ilości.
        qty = float(coffee_file.readline())

        # Usunięcie sekwencji \n z opisu.
        descr = descr.rstrip('\n')

        # Ustalenie, czy rekord został dopasowany
        # do szukanej wartości.
        if descr == search:
            # Wyświetlenie rekordu.
            print('Opis:', descr)
            print('Ilość:', qty)
            print()
            # Przypisanie wartości True zmiennej found.
            found = True

        # Odczytanie pola opisu następnego rekordu.
        descr = coffee_file.readline()

    # Zamknięcie pliku.
    coffee_file.close()

    # Jeżeli szukana wartość nie została znaleziona
    # w pliku, należy wyświetlić odpowiedni komunikat.
    if not found:
        print('Szukana kawa nie została znaleziona w pliku.')

# Wywołanie funkcji main().
main()
