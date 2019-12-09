# Ten program używa rekurencji do wyznaczenia
# największego wspólnego dzielnika dwóch liczb.

def main():
    # Pobranie dwóch liczb.
    num1 = int(input('Podaj pierwszą liczbę całkowitą: '))
    num2 = int(input('Podaj drugą liczbę całkowitą: '))

    # Wyświetlenie największego wspólnego dzielnika.
    print('Największy wspólny dzielnik tych')
    print('dwóch liczb wynosi', gcd(num1, num2))

# Funkcja gcd() zwraca największy wspólny
# dzielnik dwóch podanych liczb całkowitych.
def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(x, x % y)

# Wywołanie funkcji main().
main()
