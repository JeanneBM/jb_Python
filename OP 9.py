01. Birthdays.py 	

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

----------------------------------------------------------------------------------------------------------------------------------------------

02. Card_dealer.py 	

# Ten program używa słownika do symulacji talii kart.

def main():
    # Utworzenie talii kart.
    deck = create_deck()

    # Określenie liczby kart, które gracz chce otrzymać.
    num_cards = int(input('Podaj liczbę kart, które chcesz otrzymać:'))

    # Pobranie podanej liczby kart z talii.
    deal_cards(deck, num_cards)

# Funkcja create_deck() zwraca słownik
# przedstawiający talię kart.
def create_deck():
    # Utworzenie słownika, w którym każda karta i jej wartość
    # są przechowywane w postaci par klucz-wartość.
    deck = {'As pik': 1, '2 pik': 2, '3 pik': 3,
            '4 pik': 4, '5 pik': 5, '6 pik': 6,
            '7 pik': 7, '8 pik': 8, '9 pik': 9,
            '10 pik': 10, 'Walet pik': 10,
            'Dama pik': 10, 'Król pik': 10,

            'As kier': 1, '2 kier': 2, '3 kier': 3,
            '4 kier': 4, '5 kier': 5, '6 kier': 6,
            '7 kier': 7, '8 kier': 8, '9 kier': 9,
            '10 kier': 10, 'Walet kier': 10,
            'Dama kier': 10, 'Król kier': 10,

            'As trefl': 1, '2 trefl': 2, '3 trefl': 3,
            '4 trefl': 4, '5 trefl': 5, '6 trefl': 6,
            '7 trefl': 7, '8 trefl': 8, '9 trefl': 9,
            '10 trefl': 10, 'Walet trefl': 10,
            'Dama trefl': 10, 'Król trefl': 10,

            'As karo': 1, '2 karo': 2, '3 karo': 3,
            '4 karo': 4, '5 karo': 5, '6 karo': 6,
            '7 karo': 7, '8 karo': 8, '9 karo': 9,
            '10 karo': 10, 'Walet karo': 10,
            'Dama karo': 10, 'Król karo': 10}

    # Zwrot talii kart.
    return deck

# Funkcja deal_cards() pobiera podaną
# liczbę kart z talii.

def deal_cards(deck, number):
    # Zainicjalizowanie zmiennej działającej jako akumulator.
    hand_value = 0

    # Sprawdzenie, czy liczba pobieranych kart
    # nie jest większa niż liczba kart w talii.
    if number > len(deck):
        number = len(deck)

    # Pobranie kart i obliczenie ich łącznej wartości.
    for count in range(number):
        card, value = deck.popitem()
        print(card)
        hand_value += value

    # Wyświetlenie wartości kart pozostających w ręku gracza.
    print('Wartość pobranych kart:', hand_value)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------	

03. Pickle_objects.py 	

# Ten program przedstawia serializację obiektu.
import pickle

# Funkcja main().
def main():
    again = 't'  # Zmienna kontrolująca działanie pętli.

    # Otworzenie pliku w trybie zapisu binarnego.
    output_file = open('info.dat', 'wb')

    # Pobieranie danych dopóki, dopóty użytkownik nie zdecyduje inaczej.
    while again.lower() == 't':
        # Pobranie danych o osobie i ich zapisanie.
        save_data(output_file)

        # Czy użytkownik chce wprowadzić kolejne dane?
        again = input('Chcesz podać kolejne dane? (t/n): ')

    # Zamknięcie pliku.
    output_file.close()

# Funkcja save_data() pobiera dane o osobie,
# umieszcza je w słowniku, a następnie serializuje
# słownik do podanego pliku.
def save_data(file):
    # Utworzenie pustego słownika.
    person = {}

    # Pobranie danych o osobie
    # i umieszczenie ich w słowniku.
    person['name'] = input('Imię: ')
    person['age'] = int(input('Wiek: '))
    person['weight'] = float(input('Waga: '))

    # Serializacja słownika.
    pickle.dump(person, file)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------
	
04. Sets.py 	

# Ten program pokazuje różne operacje przeprowadzane na zbiorach.
baseball = set(['Justyna', 'Celina', 'Ada', 'Alicja'])
basketball = set(['Ewa', 'Celina', 'Alicja', 'Sara'])

# Wyświetlenie elementów zbioru baseball.
print('Oto osoby grające w drużynie bejsbolowej:')
for name in baseball:
    print(name)

# Wyświetlenie elementów zbioru basketball.
print()
print('Oto osoby grające w drużynie koszykówki:')
for name in basketball:
    print(name)

# Część wspólna zbiorów.
print()
print('Oto osoby grające w obu drużynach:')
for name in baseball.intersection(basketball):
    print(name)

# Unia zbiorów.
print()
print('Oto osoby grające w jednej z drużyn:')
for name in baseball.union(basketball):
    print(name)

# Różnica między zbiorami baseball i basketball.
print()
print('Oto osoby grające w drużynie bejsbolowej, ale nie w drużynie koszykówki:')
for name in baseball.difference(basketball):
    print(name)

# Różnica między zbiorami basketball i baseball.
print()
print('Oto osoby grające w drużynie koszykówki, ale nie w drużynie bejsbolowej:')
for name in basketball.difference(baseball):
    print(name)

# Różnica symetryczna.
print()
print('Oto osoby grające w jednej drużynie, ale nie w obu:')
for name in baseball.symmetric_difference(basketball):
    print(name)

----------------------------------------------------------------------------------------------------------------------------------------------
	
05. Unpickle_objects.py

# Ten program przedstawia deserializację obiektu.
import pickle

# Funkcja main().
def main():
    end_of_file = False  # Ta opcja będzie wskazywała koniec pliku.

    # Otworzenie pliku w trybie odczytu binarnego.
    input_file = open('info.dat', 'rb')

    # Odczyt danych aż do końca pliku.
    while not end_of_file:
        try:
            # Deserializacja następnego obiektu.
            person = pickle.load(input_file)

            # Wyświetlenie obiektu.
            display_data(person)
        except EOFError:
            # Ustawienie opcji oznaczającej
            # dotarcie do końca pliku.
            end_of_file = True

    # Zamknięcie pliku.
    input_file.close()

# Funkcja display_data() wyświetla informacje o osobie,
# której słownik został przekazany jako argument.
def display_data(person):
    print('Imię:', person['name'])
    print('Wiek:', person['age'])
    print('Waga:', person['weight'])
    print()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------
