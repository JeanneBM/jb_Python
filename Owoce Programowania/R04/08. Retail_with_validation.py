# Ten program oblicza cenę detaliczną produktu.

MARK_UP = 2.5  # Procentowa wysokość marży.
another = 't'  # Zmienna kontrolująca działanie pętli.

# Przetworzenie jednego lub większej liczby produktów.
while another == 't' or another == 'T':
    # Pobranie kosztu całkowitego produktu.
    wholesale = float(input("Podaj cenę hurtową " +
                            "produktu: "))

    # Weryfikacja podanego kosztu produktu.
    while wholesale < 0:
        print('BŁĄD: Koszt produktu nie może być ujemny.')
        wholesale = float(input('Podaj poprawną' +
                                'cenę produktu: '))

    # Obliczenie ceny detalicznej.
    retail = wholesale * MARK_UP

    # Wyświetlenie ceny detalicznej.
    print('Cena detaliczna: ', format(retail, '.2f'), ' zł.', sep='')

    # Czy powtórzyć operację?
    another = input('Czy chcesz obliczyć cenę innego produktu? ' +
                    '(Jeśli tak, wpisz t): ')


