# Ten program pokazuje przykład użycia metody insert().

def main():
    # Utworzenie listy wraz z przykładowymi imionami.
    names = ['Jakub', 'Katarzyna', 'Bartosz']

    # Wyświetlenie listy.
    print('Lista przed wstawieniem nowego elementu:')
    print(names)

    # Wstawienie nowego elementu w indeksie 0.
    names.insert(0, 'Janusz')

    # Ponowne wyświetlenie listy.
    print('Lista po wstawieniu nowego elementu:')
    print(names)

# Wywołanie funkcji main().
main()
