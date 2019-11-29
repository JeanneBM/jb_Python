# Ten program wyświetla wysokość podatku od nieruchomości.

TAX_FACTOR = 0.0065  # Wysokość stawki podatku.

# Pobranie pierwszego numeru działki.
print('Podaj numer działki')
print('lub 0, aby zakończyć.')
lot = int(input('Numer działki: '))

# Kontynuacja przetwarzania dopóki, dopóty
# użytkownik nie wpisze 0.
while lot != 0:
    # Pobranie wartości nieruchomości.
    value = float(input('Podaj wartość nieruchomości: '))

    # Obliczenie wysokości podatku.
    tax = value * TAX_FACTOR

    # Wyświetlenie wysokości podatku.
    print('Wysokość podatku: ', format(tax, ',.2f'), ' zł.', sep='')

    # Pobranie następnego numeru działki.
    print('Podaj następny numer działki lub')
    print('0, aby zakończyć.')
    lot = int(input('Numer działki: '))

