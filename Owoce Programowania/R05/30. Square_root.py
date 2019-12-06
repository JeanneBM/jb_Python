# Ten program pokazuje przykład użycia funkcji sqrt().
import math

def main():
    # Pobranie liczby.
    number = float(input('Podaj liczbę: '))

    # Obliczenie pierwiastka kwadratowego tej liczby.
    square_root = math.sqrt(number)

    # Wyświetlenie obliczonej wartości.
    print('Pierwiastek kwadratowy liczby', number, 'wynosi', square_root)

# Wywołanie funkcji main().
main()
