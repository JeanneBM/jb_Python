# Ten program wyświetla prosty wykres kołowy.
import matplotlib.pyplot as plt

def main():
    # Utworzenie listy wartości.
    values = [20, 60, 80, 40]

    # Utworzenie wykresu kołowego na podstawie listy wartości.
    plt.pie(values)

    # Wyświetlenie wykresu kołowego.
    plt.show()

# Wywołanie funkcji main().
main()
