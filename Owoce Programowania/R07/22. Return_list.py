# Ten program używa funkcji do utworzenia listy.
# Wartością zwrotną funkcji jest odwołanie do listy.

def main():
    # Pobranie listy wraz z przechowywanymi na niej wartościami.
    numbers = get_values()

    # Wyświetlenie wartości znajdujących się na liście.
    print('Oto wartości znajdujące się na liście:')
    print(numbers)

# Funkcja get_values() pobiera od użytkownika
# serię liczb i umieszcza je na liście. Wartością
# zwrotną funkcji jest odwołanie do listy.
def get_values():
    # Utworzenie pustej listy.
    values = []

    # Utworzenie zmiennej kontrolującej działanie pętli.
    again = 't'

    # Pobranie wartości od użytkownika
    # i umieszczenie ich na liście.
    while again == 't':
        # Pobranie liczby i umieszczenie jej na liście.
        num = int(input('Podaj liczbę: '))
        values.append(num)

        # Czy będzie podana kolejna liczba?
        print('Czy chcesz podać kolejną liczbę?')
        again = input('Jeśli tak, wpisz t, w przeciwnym razie wpisz inny znak: ')
        print()

    # Zwrot listy.
    return values

# Wywołanie funkcji main().
main()
