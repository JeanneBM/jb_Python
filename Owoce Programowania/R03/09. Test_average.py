# Ten program pobiera wyniki trzech sprawdzianów
# i wyświetla ich średnią. Jeżeli średnia jest wyższa niż
# pewna wartość, wówczas program składa uczniowi gratulacje..

# HIGH_SCORE to stała nazwana przechowująca wartość
# po przekroczeniu której uczeń otrzymuje gratulacje.
HIGH_SCORE = 95

# Pobranie wyników z trzech testów.
test1 = int(input('Podaj wynik ze sprawdzanu nr 1: '))
test2 = int(input('Podaj wynik ze sprawdzanu nr 2: '))
test3 = int(input('Podaj wynik ze sprawdzanu nr 3: '))

# Obliczenie średniego wyniku.
average = (test1 + test2 + test3) / 3

# Wyświetlenie średniego wyniku.
print('Średni wynik wynosi', average)

# Jeżeli średnia jest powyżej wartości HIGH_SCORE,
# należe pogratulować uczniowi.
if average >= HIGH_SCORE:
    print('Gratulacje!')
    print('Świetny wynik!')
    
    
