# Ten program pokazuje przekazanie funkcji dwóch
# argumentów w postaci ciągów tekstowych.

def main():
    first_name = input('Podaj imię: ')
    last_name = input('Podaj nazwisko: ')
    print('Twoje nazwisko i imię to')
    reverse_name(first_name, last_name)

def reverse_name(first, last):
    print(last, first)

# Wywołanie funkcji main().
main()
