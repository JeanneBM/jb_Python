# Ten program wyświetla
# zawartość pliku.

def main():
    # Pobranie nazwy pliku.
    filename = input('Podaj nazwę pliku: ')

    # Otworzenie pliku.
    infile = open(filename, 'r')

    # Odczytanie zawartości pliku.
    contents = infile.read()

    # Wyświetlenie zawartości pliku.
    print(contents)

    # Zamknięcie pliku.
    infile.close()

# Wywołanie funkcji main().
main()
