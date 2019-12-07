# Ten program odczytuje liczby z pliku i umieszcza je na liście.

def main():
    # Otworzenie pliku do odczytu.
    infile = open('numberlist.txt', 'r')

    # Odczytanie zawartości pliku i umieszczenie jej na liście.
    numbers = infile.readlines()

    # Zamknięcie pliku.
    infile.close()

    # Konwersja każdego elementu na postać liczby całkowitej.
    index = 0
    while index < len(numbers):
        numbers[index] = int(numbers[index])
        index += 1

    # Wyświetlenie zawartości listy.
    print(numbers)

# Wywołanie funkcji main().
main()
