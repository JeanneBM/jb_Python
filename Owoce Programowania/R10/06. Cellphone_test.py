# Ten program testuje klasę CellPhone.

import cellphone

def main():
    # Pobranie danych o telefonie komórkowym.
    man = input('Podaj producenta telefonu: ')
    mod = input('Podaj numer modelu telefonu: ')
    retail = float(input('Podaj cenę detaliczną telefonu: '))

    # Utworzenie egzemplarza klasy CellPhone.
    phone = cellphone.CellPhone(man, mod, retail)

    # Wyświetlenie podanych danych.
    print('Oto podane przez Ciebie dane:')
    print('Producent:', phone.get_manufact())
    print('Numer modelu:', phone.get_model())
    print('Cena detaliczna:', format(phone.get_retail_price(), '.2f'), sep='')

# Wywołanie funkcji main().
main()
