# Ten program importuje moduł coin
# i tworzy trzy egzemplarze klasy Coin.

import coin

def main():
    # Utworzenie trzech egzemplarz klasy Coin.
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()

    # Wyświetlenie wyników rzutów monetami.
    print('Oto wyniki rzutów trzema monetami:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

    # Symulacja rzutu monetą.
    print('Symulacja rzutów trzema monetami...')
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()

    # Wyświetlenie wyników rzutów monetami.
    print('Oto wyniki rzutów trzema monetami:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

# Wywołanie funkcji main().
main()
