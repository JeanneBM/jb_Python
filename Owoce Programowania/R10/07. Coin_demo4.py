# Ten program importuje moduł coin,
# a następnie tworzy egzemplarz klasy Coin.

import coin

def main():
    # Utworzenie obiektu na podstawie klasy Coin.
    my_coin = coin.Coin()

    # Wyświetlenie wyniku rzutu monetą.
    print('Wynik rzutu monetą:', my_coin.get_sideup())

    # Symulacja rzutu monetą.
    print('Symulacja dziesięciu rzutów monetą:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

# Wywołanie funkcji main().
main()
