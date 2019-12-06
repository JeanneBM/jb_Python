# Ten program używa pętli for do odczytania
# wszystkich wartości zapisanych w pliku sales.txt.

def main():
    # Otworzenie pliku sales.txt do odczytu.
    sales_file = open('sales.txt', 'r')

    # Odczytanie wszystkich wierszy z pliku.
    for line in sales_file:
        # Konwersja wiersza na postać wartości typu float.
        amount = float(line)
        # Sformatowanie i wyświetlenie wartości liczbowej.
        print(format(amount, '.2f'))

    # Zamknięcie pliku.
    sales_file.close()

# Wywołanie funkcji main().
main()
