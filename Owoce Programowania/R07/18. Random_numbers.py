# Ten program umieszcza na liście
# dwuwymiarowej losowo wybrane liczby.
import random

# Stałe określające liczbę wierszy i kolumn.
ROWS = 3
COLS = 4

def main():
    # Utworzenie listy dwuwymiarowej.
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    # Wypełnienie listy losowo wybranymi liczbami.
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1, 100)

    # Wyświetlenie listy.
    print(values)

# Wywołanie funkcji main().
main()
