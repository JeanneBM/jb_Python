# Ten program oblicza wynagrodzenie pracownika.

def main():
    # Pobranie liczby przepracowanych godzin.
    hours = int(input('Podaj liczbę przepracowanych godzin: '))

    # Pobranie stawki godzinowej.
    pay_rate = float(input('Podaj stawkę godzinową: '))

    # Obliczenie należnego wynagrodzenia.
    gross_pay = hours * pay_rate

    # Wyświetlenie obliczonego wynagrodzenia.
    print('Wynagrodzenie wynosi ', format(gross_pay, '.2f'), ' zł', sep='')

# Wywołanie funkcji main().
main()
