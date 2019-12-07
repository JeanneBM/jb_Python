# Ten program używa słownika do przechowywania
# imion osób i ich dat urodzenia.

# Stałe globalne obsługujące opcje menu.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Funkcja main().
def main():
    # Utworzenie pustego słownika.
    birthdays = {}

    # Inicjalizacja zmiennej przechowującej opcję wybraną przez użytkownika.
    choice = 0

    while choice != QUIT:
        # Pobranie opcji wybranej przez użytkownika.
        choice = get_menu_choice()

        # Przetworzenie opcji wybranej przez użytkownika.
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)

# Funkcja get_menu_choice() wyświetla menu,
# pobiera i sprawdza opcję wybraną przez użytkownika.
def get_menu_choice():
    print()
    print('Przyjaciele i ich daty urodzenia')
    print('--------------------------------')
    print('1. Wyszukanie daty urodzenia')
    print('2. Dodanie daty urodzenia')
    print('3. Zmiana daty urodzenia')
    print('4. Usunięcie daty urodzenia')
    print('5. Zakończenie programu')
    print()

    # Pobranie opcji wybranej przez użytkownika.
    choice = int(input('Wybierz opcję: '))

    # Sprawdzenie opcji wybranej przez użytkownika.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Wybierz prawidłową opcję: '))

    # Zwrot opcji wybranej przez użytkownika.
    return choice

# Funkcja look_up() wyszukuje
# podane imię w słowniku birthdays.
def look_up(birthdays):
    # Pobranie imienia do wyszukania.
    name = input('Podaj imię: ')

    # Wyszukanie imienia w słowniku.
    print(birthdays.get(name, 'Nie znaleziono imienia.'))

# Funkcja add() dodaje nowy
# wpis do słownika birthdays.
def add(birthdays):
    # Pobranie imienia i daty urodzenia.
    name = input('Podaj imię: ')
    bday = input('Podaj datę urodzenia: ')

    # Jeżeli imię nie znajduje się w słowniku, zostanie dodane.
    if name not in birthdays:
        birthdays[name] = bday
    else:
        print('Osoba o podanym imieniu już znajduje się w słowniku.')

# Funkcja change() zmienia istniejący
# wpis w słowniku birthdays.
def change(birthdays):
    # Pobranie imienia do wyszukania.
    name = input('Podaj imię: ')

    if name in birthdays:
        # Pobranie nowej daty urodzenia.
        bday = input('Podaj nową datę urodzenia: ')

        # Uaktualnienie wpisu.
        birthdays[name] = bday
    else:
        print('Nie znaleziono osoby o podanym imieniu.')

# Funkcja delete() usuwa wpis
# ze słownika birthdays.
def delete(birthdays):
    # Pobranie imienia do wyszukania.
    name = input('Podaj imię: ')

    # Jeżeli imię zostało znalezione, wpis będzie usunięty.
    if name in birthdays:
        del birthdays[name]
    else:
        print('Nie znaleziono osoby o podanym imieniu.')

# Wywołanie funkcji main().
main()
