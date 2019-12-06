# Ten program odczytuje wszystkie
# wartości zapisane w pliku sales.txt.

def main():
    # Otworzenie pliku sales.txt do odczytu.
    sales_file = open('sales.txt', 'r')

    # Odczytanie pierwszego wiersza z pliku, ale jeszcze
    # nie będzie skonwertowany na liczbę. Wciąż trzeba
    # sprawdzić, czy wartość to pusty ciąg tekstowy.
    line = sales_file.readline()

    # Jeżeli metoda readline() nie zwróciła pustego ciągu
    # tekstowego, można kontynuować przetwarzanie danych.
    while line != '':
        # Konwersja wiersza na postać wartości typu float.
        amount = float(line)

        # Sformatowanie i wyświetlenie wartości liczbowej.
        print(format(amount, '.2f'))

        # Odczytanie następnego wiersza z pliku.
        line = sales_file.readline()

    # Zamknięcie pliku.
    sales_file.close()

# Wywołanie funkcji main().
main()

