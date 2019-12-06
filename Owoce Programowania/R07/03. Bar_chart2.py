# Ten program wyświetla prosty wykres słupkowy.
import matplotlib.pyplot as plt

def main():
    # Utworzenie listy wraz ze współrzędnymi X lewej krawędzi wszystkich słupków.
    left_edges = [0, 10, 20, 30, 40]

    # Utworzenie listy wraz z wysokością wszystkich słupków.
    heights = [100, 200, 300, 400, 500]

    # Utworzenie zmiennej określającej szerokość słupka.
    bar_width = 5

    # Utworzenie wykresu słupkowego.
    plt.bar(left_edges, heights, bar_width)

    # Wyświetlenie wykresu słupkowego.
    plt.show()

# Wywołanie funkcji main().
main()
