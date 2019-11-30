# Ten program oblicza długość przeciwprostokątnej
# trójkąta prostokątnego.
import math

def main():
    # Pobranie długości dwóch przyprostokątnych.
    a = float(input('Podaj długość przyprostokątnej A: '))
    b = float(input('Podaj długość przyprostokątnej B: '))

    # Obliczenie długości przeciwprostokątnej.
    c = math.hypot(a, b)

    # Wyświetlenie obliczonej wartości.
    print('Długość przeciwprostokątnej wynosi', c)

# Wywołanie funkcji main().
main()


