# Ten program używa wartości zwrotnej funkcji.

def main():
    # Pobranie wieku użytkownika.
    first_age = int(input('Podaj swój wiek: '))

    # Pobranie wieku najlepszego przyjaciela użytkownika.
    second_age = int(input('Podaj wiek najlepszego przyjaciela: '))

    # Obliczenie sumy obu pobranych wartości.
    total = sum(first_age, second_age)

    # Wyświetlenie obliczonej wartości.
    print('Razem macie', total, 'lat.')

# Funkcja sum() akceptuje dwa argumenty
# liczbowe i zwraca ich sumę.
def sum(num1, num2):
    result = num1 + num2
    return result

# Wywołanie funkcji main().
main()
