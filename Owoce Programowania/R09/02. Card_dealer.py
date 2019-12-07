# Ten program używa słownika do symulacji talii kart.

def main():
    # Utworzenie talii kart.
    deck = create_deck()

    # Określenie liczby kart, które gracz chce otrzymać.
    num_cards = int(input('Podaj liczbę kart, które chcesz otrzymać:'))

    # Pobranie podanej liczby kart z talii.
    deal_cards(deck, num_cards)

# Funkcja create_deck() zwraca słownik
# przedstawiający talię kart.
def create_deck():
    # Utworzenie słownika, w którym każda karta i jej wartość
    # są przechowywane w postaci par klucz-wartość.
    deck = {'As pik': 1, '2 pik': 2, '3 pik': 3,
            '4 pik': 4, '5 pik': 5, '6 pik': 6,
            '7 pik': 7, '8 pik': 8, '9 pik': 9,
            '10 pik': 10, 'Walet pik': 10,
            'Dama pik': 10, 'Król pik': 10,

            'As kier': 1, '2 kier': 2, '3 kier': 3,
            '4 kier': 4, '5 kier': 5, '6 kier': 6,
            '7 kier': 7, '8 kier': 8, '9 kier': 9,
            '10 kier': 10, 'Walet kier': 10,
            'Dama kier': 10, 'Król kier': 10,

            'As trefl': 1, '2 trefl': 2, '3 trefl': 3,
            '4 trefl': 4, '5 trefl': 5, '6 trefl': 6,
            '7 trefl': 7, '8 trefl': 8, '9 trefl': 9,
            '10 trefl': 10, 'Walet trefl': 10,
            'Dama trefl': 10, 'Król trefl': 10,

            'As karo': 1, '2 karo': 2, '3 karo': 3,
            '4 karo': 4, '5 karo': 5, '6 karo': 6,
            '7 karo': 7, '8 karo': 8, '9 karo': 9,
            '10 karo': 10, 'Walet karo': 10,
            'Dama karo': 10, 'Król karo': 10}

    # Zwrot talii kart.
    return deck

# Funkcja deal_cards() pobiera podaną
# liczbę kart z talii.

def deal_cards(deck, number):
    # Zainicjalizowanie zmiennej działającej jako akumulator.
    hand_value = 0

    # Sprawdzenie, czy liczba pobieranych kart
    # nie jest większa niż liczba kart w talii.
    if number > len(deck):
        number = len(deck)

    # Pobranie kart i obliczenie ich łącznej wartości.
    for count in range(number):
        card, value = deck.popitem()
        print(card)
        hand_value += value

    # Wyświetlenie wartości kart pozostających w ręku gracza.
    print('Wartość pobranych kart:', hand_value)

# Wywołanie funkcji main().
main()
