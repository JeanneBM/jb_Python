import random

# Klasa Coin symuluje rzut monetą, w przypadku
# którego może wypaść orzeł lub reszka.

class Coin:

    # Metoda __init__() inicjalizuje atrybut
    # danych __sideup o wartości 'orzeł'.

    def __init__(self):
        self.__sideup = 'orzeł'

    # Metoda toss() generuje liczbę losową w przedziale
    # od 0 do 1. Jeżeli liczba to 0, wówczas atrybut danych
    # __sideup ma wartość 'orzeł'. W przeciwnym razie jego
    # wartością jest 'reszka'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'orzeł'
        else:
            self.__sideup = 'reszka'

    # Metoda get_sideup() zwraca wartość
    # przechowywaną przez atrybut __sideup.

    def get_sideup(self):
        return self.__sideup

# Funkcja main().
def main():
    # Utworzenie obiektu na podstawie klasy Coin.
    my_coin = Coin()

    # Wyświetlenie wyniku rzutu monetą.
    print('Wynik rzutu monetą:', my_coin.get_sideup())

    # Symulacja rzutu monetą.
    print('Symulacja dziesięciu rzutów monetą:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

# Wywołanie funkcji main().
main()
