# Ten program symuluje rzut kośćmi.
import random

# Stałe określające minimalną i maksymalną liczbę losową.
MIN = 1
MAX = 6

def main():
    # Utworzenie zmiennej kontrolującej działanie pętli.
    again = 't'

    # Symulacja rzutu kośćmi.
    while again == 't' or again == 'T':
        print('Rzucam kośćmi . . .')
        print('Oto wynik:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        # Czy chcesz rzucić jeszcze raz?
        again = input('Czy chcesz rzucić jeszcze raz (t = tak): ')

# Wywołanie funkcji main().
main()


