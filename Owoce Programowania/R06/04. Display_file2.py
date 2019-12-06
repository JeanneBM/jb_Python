# Ten program wyświetla
# zawartość pliku.

def main():
    # Pobranie nazwy pliku.
    filename = input('Podaj nazwę pliku: ')

    try:
        # Otworzenie pliku.
        infile = open(filename, 'r')

        # Odczytanie zawartości pliku.
        contents = infile.read()

        # Wyświetlenie zawartości pliku.
        print(contents)

        # Zamknięcie pliku.
        infile.close()
    except IOError:
        print('Wystąpił błąd podczas próby odczytania')
        print('pliku o nazwie', filename)

# Wywołanie funkcji main().
main()
