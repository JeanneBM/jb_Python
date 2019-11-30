# Utworzenie zmiennej globalnej.
number = 0

def main():
    global number
    number = int(input('Podaj liczbę: '))
    show_number()

def show_number():
    print('Podana liczba to', number)

# Wywołanie funkcji main().
main()


