# Ten program displays a sales chart.
import matplotlib.pyplot as plt

def main():
    # Utworzenie listy wraz ze współrzędnymi X lewej krawędzi wszystkich słupków.
    left_edges = [0, 10, 20, 30, 40]

    # Utworzenie listy wraz z wysokością wszystkich słupków.
    heights = [100, 200, 300, 400, 500]

    # Utworzenie zmiennej określającej szerokość słupka.
    bar_width = 10

    # Utworzenie wykresu słupkowego.
    plt.bar(left_edges, heights, bar_width, color=('r', 'g', 'b', 'w', 'k'))

    # Dodanie tytułu.
    plt.title('Sprzedaż według roku')

    # Dodanie etykiet do osi.
    plt.xlabel('Rok')
    plt.ylabel('Sprzedaż')

    # Dostosowanie znaczników osi do własnych potrzeb.
    plt.xticks([5, 15, 25, 35, 45],
               ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 100, 200, 300, 400, 500],
               ['0 mln', '1 mln', '2 mln', '3 mln', '4 mln', '5 mln'])

    # Wyświetlenie wykresu słupkowego.
    plt.show()

# Wywołanie funkcji main().
main()
