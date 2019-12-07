# Ten program wyświetla prosty wykres liniowy.
import matplotlib.pyplot as plt

def main():
    # Utworzenie list wraz ze współrzędnymi X i Y każdego punktu danych.
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Utworzenie wykresu.
    plt.plot(x_coords, y_coords)

    # Dodanie tytułu.
    plt.title('Sprzedaż według roku')

    # Dodanie etykiet do osi.
    plt.xlabel('Rok')
    plt.ylabel('Sprzedaż')

    # Dostosowanie znaczników osi do własnych potrzeb.
    plt.xticks([0, 1, 2, 3, 4],
               ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 1, 2, 3, 4, 5],
               ['0 mln', '1 mln', '2 mln', '3 mln', '4 mln', '5 mln'])

    # Dodanie siatki.
    plt.grid(True)

    # Wyświetlenie wykresu.
    plt.show()

# Wywołanie funkcji main().
main()
