# Stała NUM_DAYS przechowuje liczbę dni,
# dla których będą pobierane dane sprzedaży.
NUM_DAYS = 5

def main():
    # Utworzenie listy przechowującej wartość
    # sprzedaży w poszczególnych dniach.
    sales = [0] * NUM_DAYS

    # Utworzenie zmiennej przechowującej indeks.
    index = 0

    print('Podaj wartość sprzedaży w poszczególnych dniach.')

    # Pobranie wartości sprzedaży dla każdego dnia.
    while index < NUM_DAYS:
        print('Dzień nr ', index + 1, ': ', sep='', end='')
        sales[index] = float(input())
        index += 1

    # Wyświetlenie podanych wartości.
    print('Oto podane wartości:')
    for value in sales:
        print(value)

# Wywołanie funkcji main().
main()
