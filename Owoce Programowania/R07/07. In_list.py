# Ten program pokazuje przykład
# użycia operatora in wraz z listą.

def main():
    # Utworzenie listy numerów produktów.
    prod_nums = ['V475', 'F987', 'Q143', 'R688']

    # Pobranie szukanego numeru produktu.
    search = input('Podaj numer produktu: ')

    # Ustalenie, czy podany numer produktu znajduje się na liście.
    if search in prod_nums:
        print(search, 'został znaleziony na liście.')
    else:
        print(search, 'nie został znaleziony na liście.')

# Wywołanie funkcji main().
main()
