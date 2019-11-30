# Ten program symuluje 10 rzutów monetą.
import random

# Definicje stałych.
HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        # Symulacja rzutu monetą.
        if random.randint(HEADS, TAILS) == HEADS:
            print('orzeł')
        else:
            print('reszka')

# Wywołanie funkcji main().
main()


