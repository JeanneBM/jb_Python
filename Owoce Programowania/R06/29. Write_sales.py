# Ten program prosi użytkownika o podanie wartości sprzedaży,
# a następnie zapisuje te informacje w pliku sales.txt.

def main():
    # Pobranie liczby dni.
    num_days = int(input('Z ilu dni chcesz ' +
                         'podać dane? '))

    # Otworzenie nowego pliku o nazwie sales.txt.
    sales_file = open('sales.txt', 'w')

    # Pobranie wartości sprzedaży dla poszczególnych dni
    # i zapisanie tych danych w pliku.
    for count in range(1, num_days + 1):
        # Pobranie wartości sprzedaży dla danego dnia.
        sales = float(input('Podaj wartość sprzedaży w dniu nr ' +
                            str(count) + ': '))

        # Zapisanie informacji w pliku.
        sales_file.write(str(sales) + '\n')

    # Zamknięcie pliku.
    sales_file.close()
    print('Dane zostały zapisane w pliku sales.txt.')

# Wywołanie funkcji main().
main()
