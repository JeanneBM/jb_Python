# Ten program oblicza średni wynik z kilku sprawdzianów. Prosi użytkownika
# o podanie liczby uczniów i sprawdzianów.

# Pobranie liczby uczniów.
num_students = int(input('Podaj liczbę uczniów: '))

# Pobranie liczby sprawdzianów.
num_test_scores = int(input('Podaj liczbę sprawdzianów: '))

# Obliczenie średniego wyniku ze sprawdzianów uczniów.
for student in range(num_students):
    # Inicjalizacja akumulatora wyników sprawdzianów.
    total = 0.0
    # Pobranie wyników sprawdzianów danego ucznia.
    print('Uczeń numer', student + 1)
    print('–––––––––––––––––')
    for test_num in range(num_test_scores):
        print('Podaj wynik ze sprawdzianu numer', test_num + 1, end='')
        score = float(input(': '))
        # Dodanie wyniku do akumulatora.
        total += score

    # Obliczenie średniego wyniku ze sprawdzianów danego ucznia.
    average = total / num_test_scores

    # Wyświetlenie obliczonej wartości.
    print('Średni wynik ucznia', student + 1,
          'to', average)
    print()

