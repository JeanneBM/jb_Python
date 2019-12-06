# Ten program zapisuje w pliku
# trzy wiersze danych.
def main():
    # Otworzenie pliku o nazwie philosophers.txt.
    outfile = open('philosophers.txt', 'w')

    # Zapisanie w pliku informacji
    # o trzech sławnych filozofach.
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # Zamknięcie pliku.
    outfile.close()

# Wywołanie funkcji main().
main()
