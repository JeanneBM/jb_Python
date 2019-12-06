# Ten program wyświetla sumę wszystkich
# wartości zapisanych w pliku sales_data.txt.

def main():
    # Inicjalizacja zmiennej akumulatora.
    total = 0.0

    try:
        # Otworzenie pliku sales_data.txt.
        infile = open('sales_data.txt', 'r')

        # Odczytanie wartości z pliku,
        # a następnie ich zsumowanie.
        for line in infile:
            amount = float(line)
            total += amount

        # Zamknięcie pliku.
        infile.close()
    except Exception as err:
        print(err)
    else:
        # Wyświetlenie obliczonej sumy.
        print(format(total, '.2f'))

# Wywołanie funkcji main().
main()
