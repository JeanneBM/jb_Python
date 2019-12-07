# Ten program pokazuje, jak pobrać indeks
# elementu listy, a następnie zastąpić go
# nowym elementem.

def main():
    # Utworzenie listy wraz z przykładowymi elementami.
    food = ['pizza', 'burgery', 'chipsy']

    # Wyświetlenie listy.
    print('Oto lista elementów znajdujących się na liście:')
    print(food)

    # Pobranie elementu, który ma zostać zmieniony.
    item = input('Który element powinien zostać zmieniony? ')

    try:
        # Pobranie indeksu elementu listy.
        item_index = food.index(item)

        # Pobranie nowej wartości.
        new_item = input('Podaj nową wartość: ')

        # Zastąpienie starej wartości nową.
        food[item_index] = new_item

        # Wyświetlenie listy.
        print('Oto zmodyfikowana lista:')
        print(food)
    except ValueError:
        print('Podany element nie został znaleziony na liście.')

# Wywołanie funkcji main().
main()
