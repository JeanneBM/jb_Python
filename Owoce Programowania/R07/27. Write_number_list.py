# Ten program zapisuje w pliku listę liczb.

def main():
    # Utworzenie listy liczb.
    numbers = [1, 2, 3, 4, 5, 6, 7]

    # Otworzenie pliku do odczytu.
    outfile = open('numberlist.txt', 'w')

    # Zapisanie listy w pliku.
    for item in numbers:
        outfile.write(str(item) + '\n')

    # Zamknięcie pliku.
    outfile.close()

# Wywołanie funkcji main().
main()
