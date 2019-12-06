# Ten program pokazuje, jak liczby odczytane z pliku muszą
# zostać skonwertowane z ciągu tekstowego, zanim będą
# mogły być użyte w operacjach matematycznych.

def main():
    # Otworzenie pliku do odczytu.
    infile = open('numbers.txt', 'r')

    # Odczytanie trzech liczb z pliku.
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    # Zamknięcie pliku.
    infile.close()

    # Dodanie trzech odczytanych liczb.
    total = num1 + num2 + num3

    # Wyświetlenie liczb i ich sumy.
    print('Odczytane liczby to:', num1, num2, num3)
    print('Suma liczb wynosi:', total)

# Wywołanie funkcji main().
main()
