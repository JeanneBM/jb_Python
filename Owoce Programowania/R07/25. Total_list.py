# Ten program oblicza sumę
# wartości wszystkich elementów listy.

def main():
    # Utworzenie listy.
    numbers = [2, 4, 6, 8, 10]

    # Utworzenie zmiennej przeznaczonej do użycia w charakterze akumulatora.
    total = 0

    # Obliczenie sumy wartości wszystkich elementów listy.
    for value in numbers:
        total += value

    # Wyświetlenie obliczonej sumy.
    print('Suma wartości wszystkich elementów listy wynosi', total)

# Wywołanie funkcji main().
main()
