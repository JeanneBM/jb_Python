# Ten program pokazuje, jak użyć metody remove()
# do usunięcia elementu z listy.

def main():
    # Utworzenie listy wraz z przykładowymi elementami.
    food = ['pizza', 'burgery', 'chipsy']

    # Wyświetlenie listy.
    print('Oto lista elementów znajdujących się na liście:')
    print(food)

    # Pobranie elementu, który ma zostać zmieniony.
    item = input('Który element powinien zostać usunięty? ')

    try:
        # Usunięcie elementu.
        food.remove(item)

        # Wyświetlenie listy.
        print('Oto zmodyfikowana lista:')
        print(food)

    except ValueError:
        print('Podany element nie został znaleziony na liście.')

# Wywołanie funkcji main().
main()
