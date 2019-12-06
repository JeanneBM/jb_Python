# Ten program oblicza średnią
# wartość elementów listy.

def main():
    # Utworzenie listy.
    scores = [2.5, 7.3, 6.5, 4.0, 5.2]

    # Utworzenie zmiennej przeznaczonej do użycia w charakterze akumulatora.
    total = 0.0

    # Obliczenie sumy wszystkich elementów listy.
    for value in scores:
        total += value

    # Obliczenie średniej wartości elementów listy.
    average = total / len(scores)

    # Wyświetlenie sumy wszystkich elementów listy.
    print('Średnia wartość elementów listy wynosi', average)

# Wywołanie funkcji main().
main()
