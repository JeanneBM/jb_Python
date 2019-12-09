# Ten program symuluje grę „Wieże Hanoi”.

def main():
    # Zdefiniowanie pewnych wartości początkowych.
    num_discs = 3
    from_peg = 1
    to_peg = 3
    temp_peg = 2

    # Symulacja gry.
    move_discs(num_discs, from_peg, to_peg, temp_peg)
    print('Wszystkie krążki zostały przeniesione!')

# Funkcja moveDiscs() wyświetla ruch, który
# należy wykonać w grze „Wieże Hanoi”.
# Parametry funkcji są następujące:
#    num:        liczba krążków do przeniesienia,
#    from_peg:   słupek, z którego należy zdjąć krążek,
#    to_peg:     słupek, na którym należy umieścić krążek,
#    temp_peg:   słupek tymczasowy.
def move_discs(num, from_peg, to_peg, temp_peg):
    if num > 0:
        move_discs(num - 1, from_peg, temp_peg, to_peg)
        print('Przeniesienie krążka ze słupka', from_peg, '. na słupek', to_peg)
        move_discs(num - 1, temp_peg, to_peg, from_peg)

# Wywołanie funkcji main().
main()
