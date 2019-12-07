# Ten program używa funkcji do obliczenia
# sumy wartości elementów listy.

def main():
    # Utworzenie listy.
    numbers = [2, 4, 6, 8, 10]

    # Wyświetlenie sumy wszystkich elementów listy.
    print('Suma wartości elementów listy wynosi', get_total(numbers))

# Funkcja get_total() akceptuje argument
# w postaci listy i zwraca sumę wartości
# wszystkich jej elementów.
def get_total(value_list):
    # Utworzenie zmiennej przeznaczonej do użycia w charakterze akumulatora.
    total = 0

    # Obliczenie sumy wszystkich elementów listy.
    for num in value_list:
        total += num

    # Zwrot wartości zmiennej total.
    return total

# Wywołanie funkcji main().
main()
