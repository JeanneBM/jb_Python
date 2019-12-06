# Ten program odczytuje i wyświetla
# zawartość pliku philosophers.txt.
def main():
    # Otworzenie pliku o nazwie philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Odczytanie zawartości pliku.
    file_contents = infile.read()

    # Zamknięcie pliku.
    infile.close()

    # Wyświetlenie danych
    # wczytanych do pamięci.
    print(file_contents)

# Wywołanie funkcji main().
main()

