# Ten program oblicza i wyświetla wynagrodzenie.
# Pobranie liczby przepracowanych godzin.
hours = int(input('Podaj liczbę godzin przepracowanych w tym tygodniu: '))

# Pobranie stawki godzinowej.
pay_rate = float(input('Podaj stawkę godzinową: '))

# Obliczenie wynagrodzenia.
gross_pay = hours * pay_rate

# Wyświetlenie wynagrodzenia.
print('Wynagrodzenie wynosi ', format(gross_pay, '.2f'), ' zł')
