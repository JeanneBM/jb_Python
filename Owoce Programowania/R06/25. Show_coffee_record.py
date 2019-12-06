# Ten program wyświetla rekordy
# zapisane w pliku coffee.txt.

def main():
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

        # Wyświetlenie rekordu.
        print('Opis:', descr)
        print('Ilość:', qty)

        # Odczytanie pola opisu następnego rekordu.
        descr = coffee_file.readline()

    # Zamknięcie pliku.
    coffee_file.close()

# Wywołanie funkcji main().
main()
