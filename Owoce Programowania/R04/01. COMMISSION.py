# Ten program oblicza wysokość premii ze sprzedaży.

# Utworzenie zmiennej kontrolującej działanie pętli.
keep_going = 't'

# Obliczenie serii premii.
while keep_going == 't':
    # Pobranie wielkości sprzedaży i premii.
    sales = float(input('Podaj wielkość sprzedaży: '))
    comm_rate = float(input('Podaj wysokość premii: '))

    # Obliczenie premii.
    commission = sales * comm_rate

    # Wyświetlenie premii.
    print('Premia wynosi ',
          format(commission, '.2f'), ' zł.', sep='')

    # Czy użytkownik chce obliczyć kolejną premię?
    keep_going = input('Czy chcesz obliczyć kolejną ' +
                       'premię? (Jeśli tak, wpisz t): ')


