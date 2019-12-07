# Ten program wyświetla prosty wykres liniowy.
import matplotlib.pyplot as plt

def main():
    # Utworzenie list wraz ze współrzędnymi X i Y każdego punktu danych.
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Utworzenie wykresu.
    plt.plot(x_coords, y_coords)

    # Wyświetlenie wykresu.
    plt.show()

# Wywołanie funkcji main().
main()
