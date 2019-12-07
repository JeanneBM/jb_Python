# Ten program pokazuje przykład użycia operatora powtarzania.

def main():
    # Wyświetlenie dziewięciu wierszy, z których każdy jest coraz dłuższy.
    for count in range(1, 10):
        print('Z' * count)

    # Wyświetlenie dziewięciu wierszy, z których każdy jest coraz krótszy.
    for count in range(8, 0, -1):
        print('Z' * count)

# Wywołanie funkcji main().
main()
