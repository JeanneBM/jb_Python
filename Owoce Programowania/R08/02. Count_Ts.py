# Ten program zlicza ilość wystąpień
# litery T (zarówno małej, jak i dużej)
# w podanym ciągu tekstowym.

def main():
    # Utworzenie zmiennej do obsługi licznika pętli.
    # Ta zmienna musi mieć wartość początkową 0.
    count = 0

    # Pobranie ciągu tekstowego od użytkownika.
    my_string = input('Podaj dowolne zdanie: ')

    # Zliczenie wystąpień litery T.
    for ch in my_string:
        if ch == 'T' or ch == 't':
            count += 1

    # Wyświetlenie wyniku.
    print('Litera T wystąpiła', count, 'razy.')

# Wywołanie funkcji main().
main()
