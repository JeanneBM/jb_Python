# Ten program odczytuje zawartość pliku
# philosophers.txt wiersz po wierszu.
def main():
    # Otworzenie pliku o nazwie philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Odczyt trzech wierszy z pliku.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Zamknięcie pliku.
    infile.close()

    # Wyświetlenie danych
    # wczytanych do pamięci.
    print(line1)
    print(line2)
    print(line3)

# Wywołanie funkcji main().
main()
