# Ten program odczytuje zawartość pliku i umieszcza ją na liście.

def main():
    # Otworzenie pliku do odczytu.
    infile = open('cities.txt', 'r')

    # Odczytanie zawartości pliku i umieszczenie jej na liście.
    cities = infile.readlines()

    # Zamknięcie pliku.
    infile.close()

    # Usunięcie znaku \n z każdego elementu.
    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1

    # Wyświetlenie zawartości listy.
    print(cities)

# Wywołanie funkcji main().
main()
