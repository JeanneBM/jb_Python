# Ten program przedstawia przykład pętli działającej w nieskończoność.
# Utworzenie zmiennej kontrolującej działanie pętli.
keep_going = 't'

# Uwaga! Pętla działająca w nieskończoność!
while keep_going == 't':
    # Pobranie wielkości sprzedaży i premii.
    sales = float(input('Podaj wielkość sprzedaży: '))
    comm_rate = float(input('Podaj wysokość premii: '))

    # Obliczenie premii.
    commission = sales * comm_rate

    # Wyświetlenie premii.
    print('Premia wynosi ',
          format(commission, '.2f'), ' zł.', sep='')

