# Ten program oblicza wysokość wynagrodzenia
# każdego z pracowników Małgorzaty.

# NUM_EMPLOYEES to jest stała
# określająca wielkość listy.
NUM_EMPLOYEES = 6

def main():
    # Utworzenie listy do przechowywania godzin przepracowanych przez pracowników.
    hours = [0] * NUM_EMPLOYEES

    # Pobranie liczby godzin przepracowanych przez poszczególnych pracowników.
    for index in range(NUM_EMPLOYEES):
        print('Podaj liczbę godzin przepracowanych przez pracownika nr ',
              index + 1, ': ', sep='', end='')
        hours[index] = float(input())

    # Pobranie stawki godzinowej.
    pay_rate = float(input('Podaj stawkę godzinową: '))

    # Wyświetlenie wynagrodzenia należnego poszczególnym pracownikom.
    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print('Wynagrodzenie dla pracownika nr ', index + 1,
              format(gross_pay, ' .2f'), ' zł', sep='')

# Wywołanie funkcji main().
main()
