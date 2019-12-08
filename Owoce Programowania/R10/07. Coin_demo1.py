import random

# Klasa Coin symuluje rzut monetą, w przypadku
# której może wypaść orzeł lub reszka.

class Coin:

    # Metoda __init__() inicjalizuje atrybut
    # danych sideup o wartości 'orzeł'.

    def __init__(self):
        self.sideup = 'orzeł'

    # Metoda toss() generuje liczbę losową w przedziale
    # od 0 do 1. Jeżeli liczba to 0, wówczas atrybut danych
    # sideup ma wartość 'orzeł'. W przeciwnym razie jego
    # wartością jest 'reszka'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'orzeł'
        else:
            self.sideup = 'reszka'

    # Metoda get_sideup() zwraca wartość
    # przechowywaną przez atrybut danych sideup.

    def get_sideup(self):
        return self.sideup

# Funkcja main().
def main():
    # Utworzenie obiektu na podstawie klasy Coin.
    my_coin = Coin()

    # Wyświetlenie wyniku rzutu monetą.
    print('Wynik rzutu monetą:', my_coin.get_sideup())

    # Symulacja rzutu monetą.
    print('Symulacja rzutu monetą...')
    my_coin.toss()

    # Wyświetlenie wyniku rzutu monetą.
    print('Wynik rzutu monetą:', my_coin.get_sideup())

# Wywołanie funkcji main().
main()
