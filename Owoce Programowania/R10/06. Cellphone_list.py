# Ten program tworzy pięć obiektów CellPhone
# i przechowuje je na liście.

import cellphone

def main():
    # Pobranie listy obiektów CellPhone.
    phones = make_list()

    # Wyświetlenie danych przechowywanych na liście.
    print('Oto wprowadzone przez Ciebie dane:')
    display_list(phones)

# Funkcja make_list() pobiera od użytkownika dane
# o pięciu telefonach komórkowych. Następnie zwraca
# listę obiektów CellPhone zawierających dane.

def make_list():
    # Utworzenie pustej listy.
    phone_list = []

    # Dodanie pięciu obiektów CellPhone do listy.
    print('Podaj dane pięciu telefonów komórkowych.')
    for count in range(1, 6):
        # Pobranie danych o telefonie komórkowym.
        print('Telefon nr ' + str(count) + ':')
        man = input('Podaj producenta telefonu: ')
        mod = input('Podaj numer modelu telefonu: ')
        retail = float(input('Podaj cenę detaliczną telefonu: '))
        print()

        # Utworzenie w pamięci nowego obiektu CellPhone
        # i przypisanie go zmiennej phone.
        phone = cellphone.CellPhone(man, mod, retail)

        # Dodanie obiektu do listy.
        phone_list.append(phone)

    # Zwrot listy.
    return phone_list

# Funkcja display_list() akceptuje argument w postaci listy
# zawierającej obiekty CellPhone i wyświetla dane przechowywane
# w poszczególnych obiektach.

def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()

# Wywołanie funkcji main().
main()
