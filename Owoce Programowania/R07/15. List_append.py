# Ten program pokazuje przykład użycia metody append()
# podczas dodawania nowych elementów do listy.

def main():
    # Najpierw trzeba utworzyć pustą listę.
    name_list = []

    # Utworzenie zmiennej kontrolującej działanie pętli.
    again = 't'

    # Dodanie imion do listy.
    while again == 't':
        # Pobranie imienia od użytkownika.
        name = input('Podaj imię: ')

        # Dodanie elementu do listy.
        name_list.append(name)

        # Czy dodać kolejny element?
        print('Czy chcesz dodać kolejne imię?')
        again = input('Jeśli tak, wpisz t, w przeciwnym razie wpisz inny znak: ')
        print()

    # Wyświetlenie wpisanych imion.
    print('Oto wpisane imiona:')

    for name in name_list:
        print(name)

# Wywołanie funkcji main().
main()
