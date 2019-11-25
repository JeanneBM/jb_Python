# Pobranie wyników trzech sprawdzanów i umieszczenie
# ich w zmiennych o nazwach test1, test2 i test3.
test1 = float(input('Podaj wynik z pierwszego sprawdzianu: '))
test2 = float(input('Podaj wynik z drugiego sprawdzianu: '))
test3 = float(input('Podaj wynik z trzeciego sprawdzianu: '))

# Obliczenie średniej trzech wyników i przypisanie
# wartości średniej do zmiennej average.
average = (test1 + test2 + test3) / 3.0

# Wyświetlenie wartości średniej.
print('Twój średni wynik wynosi', average)
