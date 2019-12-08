import random

# Klasa Coin symuluje rzut monetą, w przypadku
# którego może wypaść orzeł lub reszka.

class Coin:

    # Metoda __init__() inicjalizuje atrybut danych
    #  __sideup o wartości 'orzeł'.

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
