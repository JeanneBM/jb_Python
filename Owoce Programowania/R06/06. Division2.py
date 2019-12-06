# Ten program dzieli jedną liczbę przez drugą.

def main():
    # Pobranie dwóch liczb.
    num1 = int(input('Podaj liczbę : '))
    num2 = int(input('Podaj następną liczbę: '))

    # Jeżeli wartość num2 jest inna niż 0, następuje
    # podzielenie num1 przez num2 i wyświetlenie wyniku.
    if num2 != 0:
        result = num1 / num2
        print(num1, 'dzielone przez', num2, 'daje', result)
    else:
        print('Nie można dzielić przez zero.')

# Wywołanie funkcji main().
main()
