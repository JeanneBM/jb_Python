# Ten program używa metody writelines() do
# zapisania w pliku listy ciągów tekstowych.

def main():
    # Utworzenie listy ciągów tekstowych.
    cities = ['Nowy Jork', 'Boston', 'Atlanta', 'Dallas']

    # Otworzenie pliku do odczytu.
    outfile = open('cities.txt', 'w')

    # Zapisanie listy w pliku.
    outfile.writelines(cities)

    # Zamknięcie pliku.
    outfile.close()

# Wywołanie funkcji main().
main()
