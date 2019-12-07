# Ten program wyświetla prosty wykres kołowy.
import matplotlib.pyplot as plt

def main():
    # Utworzenie listy wielkości sprzedaży.
    sales = [100, 400, 300, 600]

    # Utworzenie listy etykiet dla poszczególnych części wykresu.
    slice_labels = ['Kwartał 1', 'Kwartał 2', 'Kwartał 3', 'Kwartał 4']

    # Utworzenie wykresu kołowego na podstawie listy wartości.
    plt.pie(sales, labels=slice_labels)

    # Dodanie tytułu.
    plt.title('Sprzedaż według kwartałów')

    # Wyświetlenie wykresu kołowego.
    plt.show()

# Wywołanie funkcji main().
main()
