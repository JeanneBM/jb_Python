# Ten program przekazuje obiekt Coin
# jako argument funkcji.
import coin

# Funkcja main().
def main():
    # Utworzenie obiektu Coin.
    my_coin = coin.Coin()

    # To polecenie wyświetli ciąg tekstowy 'orzeł'.
    print(my_coin.get_sideup())

    # Przekazanie obiektu funkcji flip().
    flip(my_coin)

    # To polecenie może wyświetlić ciąg tekstowy
    # 'orzeł' lub 'reszka'.
    print(my_coin.get_sideup())

# Funkcja flip() symuluje rzut monetą.
def flip(coin_obj):
    coin_obj.toss()

# Wywołanie funkcji main().
main()
