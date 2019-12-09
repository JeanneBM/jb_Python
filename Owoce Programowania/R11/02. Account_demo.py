# Ten program tworzy egzemplarze
# klas SavingsAccount i CD.

import accounts

def main():
    # Pobranie numeru konta, oprocentowania,
    # i salda konta oszczędnościowego.
    print('Podaj dane dotyczące konta oszczędnościowego.')
    acct_num = input('Numer konta: ')
    int_rate = float(input('Oprocentowanie: '))
    balance = float(input('Saldo: '))

    # Utworzenie obiektu klasy SavingsAccount.
    savings = accounts.SavingsAccount(acct_num, int_rate,
                                      balance)

    # Pobranie numeru konta, oprocentowania,
    # salda i daty wykupu certyfikatu depozytowego.
    print('Podaj dane dotyczące certyfikatu depozytowego.')
    acct_num = input('Numer konta: ')
    int_rate = float(input('Oprocentowanie: '))
    balance = float(input('Saldo: '))
    maturity = input('Data wykupu:')

    # Utworzenie obiektu klasy CD.
    cd = accounts.CD(acct_num, int_rate, balance, maturity)

    # Wyświetlenie wprowadzonych danych.
    print('Oto wprowadzone dane:')
    print()
    print('Konto oszczędnościowe')
    print('---------------------')
    print('Numer konta:', savings.get_account_num())
    print('Oprocentowanie:', savings.get_interest_rate())
    print('Saldo: ',
          format(savings.get_balance(), '.2f'),
          sep='')
    print()
    print('CD')
    print('---------------------')
    print('Numer konta:', cd.get_account_num())
    print('Oprocentowanie:', cd.get_interest_rate())
    print('Saldo: ',
          format(cd.get_balance(), '.2f'),
          sep='')
    print('Data wykupu:', cd.get_maturity_date())

# Wywołanie funkcji main().
main()
