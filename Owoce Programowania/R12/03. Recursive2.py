# Ten program używa rekurencji
# do obliczenia silni.

def main():
    # Pobranie liczby od użytkownika.
    number = int(input('Podaj nieujemną liczbę całkowitą: '))

    # Obliczenie silni podanej liczby.
    fact = factorial(number)

    # Wyświetlenie obliczonej silni.
    print('Silnia liczby', number, 'wynosi', fact)

# Funkcja factorial() używa rekurencji do obliczenia
# silni liczby przekazanej jej jako argument. Zakładamy,
# że argument jest liczbą nieujemną.
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Wywołanie funkcji main().
main()
