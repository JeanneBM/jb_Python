# Ten program dzieli jedną liczbę przez drugą.

def main():
    # Pobranie dwóch liczb.
    num1 = int(input('Podaj liczbę: '))
    num2 = int(input('Podaj następną liczbę: '))

    # Podzielenie liczby num1 przez num2 i wyświetlenie wyniku.
    result = num1 / num2
    print(num1, 'dzielone przez', num2, 'daje', result)

# Wywołanie funkcji main().
main()
