# Ten program pokazuje przykład zastosowania klasy BankAccount.

import bankaccount

def main():
    # Określenie salda początkowego.
    start_bal = float(input('Podaj początkową wysokość salda: '))

    # Utworzenie obiektu BankAccount.
    savings = bankaccount.BankAccount(start_bal)

    # Zdeponowanie pewnej kwoty na koncie.
    pay = float(input('Jaką kwotę zarobiłeś w tym tygodniu? '))
    print('Ta kwota została zdeponowana na koncie.')
    savings.deposit(pay)

    # Wyświetlenie salda bieżącego.
    print('Wysokość salda wynosi ',
          format(savings.get_balance(), '.2f'),
          sep='')

    # Pobranie kwoty, która ma zostać wypłacona.
    cash = float(input('Jaką kwotę chcesz wypłacić? '))
    print('Ta kwota zostanie odjęta od bieżącej wysokości salda.')
    savings.withdraw(cash)

    # Wyświetlenie salda bieżącego.
    print('Wysokość salda wynosi ',
          format(savings.get_balance(), '.2f'),
          sep='')

# Wywołanie funkcji main().
main()
