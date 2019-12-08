# Ten program pokazuje przykład zastosowania klasy BankAccount
# wraz z dodaną do niej metodą __str__().

import bankaccount2

def main():
    # Określenie salda początkowego.
    start_bal = float(input('Podaj początkową wysokość salda: '))

    # Utworzenie obiektu BankAccount.
    savings = bankaccount2.BankAccount(start_bal)

    # Zdeponowanie pewnej kwoty na koncie.
    pay = float(input('Jaką kwotę zarobiłeś w tym tygodniu? '))
    print('Ta kwota została zdeponowana na koncie.')
    savings.deposit(pay)

    # Wyświetlenie salda bieżącego.
    print(savings)

    # Pobranie kwoty, która ma zostać wypłacona.
    cash = float(input('Jaką kwotę chcesz wypłacić? '))
    print('Ta kwota zostanie odjęta od bieżącej wysokości salda.')
    savings.withdraw(cash)

    # Wyświetlenie salda bieżącego.
    print(savings)

# Wywołanie funkcji main().
main()
