# Stałe nazwane przedstawiające zwykłą stawkę
# za godzinę i mnożnik za nadgodziny.
BASE_HOURS = 40  # Standardowa stawka godzinowa.
OT_MULTIPLIER = 1.5  # Mnożnik za nadgodziny.

# Pobranie liczby przeprowadzonych godzin i stawki godzinowej.
hours = float(input('Podaj liczbę przepracowanych godzin: '))
pay_rate = float(input('Podaj stawkę godzinową: '))

# Obliczenie i wyświetlenie wynagrodzenia.
if hours > BASE_HOURS:
    # Obliczenie wynagrodzenia wraz z nadgodzinami.
    # Najpierw należy pobrać liczbę nadgodzin.
    overtime_hours = hours - BASE_HOURS

    # Obliczenie wynagrodzenia za nadgodziny.
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER

    # Obliczenie całkowitego wynagrodzenia.
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
    # Obliczenie wynagrodzenia bez nadgodzin.
    gross_pay = hours * pay_rate

# Wyświetlenie obliczonego wynagrodzenia.
print('Wynagrodzenie wynosi', format(gross_pay, ',.2f'), sep='')

