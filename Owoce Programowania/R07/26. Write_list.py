# Ten program zapisuje listę ciągów tekstowych w pliku

def main():
    # Utworzenie listy ciągów tekstowych.
    cities = ['Nowy Jork', 'Boston', 'Atlanta', 'Dallas']

    # Otworzenie pliku do odczytu.
    outfile = open('cities.txt', 'w')

    # Zapisanie listy w pliku.
    for item in cities:
        outfile.write(item + '\n')

    # Zamknięcie pliku.
    outfile.close()

# Wywołanie funkcji main().
main()
