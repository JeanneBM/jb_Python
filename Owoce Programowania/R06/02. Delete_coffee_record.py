# Ten program pozwala użytkownikowi
# na usunięcie rekordu w pliku coffee.txt.

import os  # To polecenie jest niezbędne do wywołania funkcji remove() i rename().

def main():
    # Utworzenie zmiennej boolowskiej do użycia jako flagi.
    found = False

    # Pobranie kawy przeznaczonej do usunięcia.
    search = input('Podaj nazwę kawy, którą chcesz usunąć: ')

    # Otworzenie pierwotnego pliku coffee.txt.
    coffee_file = open('coffee.txt', 'r')

    # Otworzenie pliku tymczasowego.
    temp_file = open('temp.txt', 'w')

    # Odczytanie pola opisu pierwszego rekordu.
    descr = coffee_file.readline()

    # Odczytanie pozostałej części pliku.
    while descr != '':
        # Odczytanie pola ilości.
        qty = float(coffee_file.readline())

        # Usunięcie sekwencji \n z opisu.
        descr = descr.rstrip('\n')

        # Jeżeli to nie jest rekord przeznaczony do usunięcia,
        # zapisz go w pliku tymczasowym.
        if descr != search:
            # Zapisanie rekordu w pliku tymczasowym.
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')
        else:
            # Przypisanie wartości True zmiennej found.
            found = True

        # Odczytanie pola opisu następnego rekordu.
        descr = coffee_file.readline()

    # Zamknięcie plików pierwotnego i tymczasowego.
    coffee_file.close()
    temp_file.close()

    # Usunięcie pierwotnego pliku coffee.txt.
    os.remove('coffee.txt')

    # Zmiana nazwy pliku tymczasowego.
    os.rename('temp.txt', 'coffee.txt')

    # Jeżeli szukana wartość nie została znaleziona
    # w pliku, należy wyświetlić odpowiedni komunikat.
    if found:
        print('Plik został uaktualniony.')
    else:
        print('Szukana kawa nie została znaleziona w pliku.')

# Wywołanie funkcji main().
main()
