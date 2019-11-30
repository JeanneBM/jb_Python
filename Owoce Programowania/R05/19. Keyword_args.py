# Ten program pokazuje przykład użycia argumentów w postaci słów kluczowych.

def main():
    # Wyświetlenie wysokości odsetek. Wartość 0.01 określa
    # stopę procentową, 10 określa przedział czasu,
    # a 10000 zł to zdeponowana kwota.
    show_interest(rate=0.01, periods=10, principal=10000.0)

# Funkcja show_interest() wyświetla wysokość odsetek
# dla zdeponowanej kwoty, uwzględniając podaną
# stopę procentową i czas trwania lokaty.

def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print('Wysokość odsetek wynosi ',
          format(interest, '.2f'),
          sep='')

# Wywołanie funkcji main().
main()


