# Ten program pozwala na zarządzanie informacjami o osobach.
import contact
import pickle

# Stałe globalne obsługujące opcje menu.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Stała globalna przechowująca nazwę pliku.
FILENAME = 'contacts.dat'

# Funkcja main().
def main():
    # Wczytanie istniejącego słownika
    # i przypisanie go zmiennej mycontacts.
    mycontacts = load_contacts()

    # Inicjalizacja zmiennej przechowującej opcję wybraną przez użytkownika.
    choice = 0

    # Przetwarzanie wybranej opcji menu aż do chwili
    # gdy użytkownik zdecyduje się na zakończenie programu.
    while choice != QUIT:
        # Pobranie opcji wybranej przez użytkownika.
        choice = get_menu_choice()

        # Przetworzenie opcji wybranej przez użytkownika.
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)

    # Zapisanie słownika mycontacts w pliku.
    save_contacts(mycontacts)

def load_contacts():
    try:
        # Otworzenie pliku contacts.dat.
        input_file = open(FILENAME, 'rb')

        # Deserializacja słownika.
        contact_dct = pickle.load(input_file)

        # Zamknięcie pliku contacts.dat.
        input_file.close()
    except IOError:
        # Podany plik nie istnieje, więc
        # został utworzony pusty słownik.
        contact_dct = {}

    # Zwrot słownika.
    return contact_dct

# Funkcja get_menu_choice() wyświetla menu,
# pobiera i sprawdza opcję wybraną przez użytkownika.
def get_menu_choice():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Wyszukanie osoby')
    print('2. Dodanie nowej osoby')
    print('3. Zmiana istniejącej osoby')
    print('4. Usunięcie osoby')
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
# podane imię i nazwisko w słowniku.
def look_up(mycontacts):
    # Pobranie imienia i nazwiska do wyszukania.
    name = input('Podaj imię i nazwisko: ')

    # Wyszukanie imienia i nazwiska w słowniku.
    print(mycontacts.get(name, 'Nie znaleziono osoby.'))

# Funkcja add() dodaje nową osobę,
# wpis do słownika.
def add(mycontacts):
    # Pobranie informacji o osobie.
    name = input('Imię i nazwisko: ')
    phone = input('Numer telefonu: ')
    email = input('Adres e-mail ')

    # Utworzenie obiektu klasy Contact o nazwie entry.
    entry = contact.Contact(name, phone, email)

    # Jeżeli osoba nie znajduje się w słowniku,
    # zostanie dodana jako klucz wraz z wartością
    # w postaci obiektu entry.
    if name not in mycontacts:
        mycontacts[name] = entry
        print('Osoba została dodana.')
    else:
        print('Podana osoba już istnieje.')

# Funkcja change() zmienia
# obiekt istniejący w słowniku.
def change(mycontacts):
    # Pobranie imienia i nazwiska do wyszukania.
    name = input('Podaj imię i nazwisko: ')

    if name in mycontacts:
        # Pobranie nowego numeru telefonu.
        phone = input('Podaj nowy numer telefonu: ')

        # Pobranie nowego adresu e-mail.
        email = input('Podaj nowy adres e-mail: ')

        # Utworzenie obiektu klasy Contact o nazwie entry.
        entry = contact.Contact(name, phone, email)

        # Uaktualnienie informacji o osobie.
        mycontacts[name] = entry
        print('Informacje zostały uaktualnione.')
    else:
        print('Nie znaleziono osoby.')

# Funkcja delete() usuwa ze słownika
# dane wskazanej osoby.
def delete(mycontacts):
    # Pobranie imienia i nazwiska do wyszukania.
    name = input('Podaj imię i nazwisko: ')

    # Jeżeli osoba została znaleziona, przedstawiający ją element będzie usunięty.
    if name in mycontacts:
        del mycontacts[name]
        print('Osoba została usunięta.')
    else:
        print('Nie znaleziono osoby.')

# Funkcja save_contacts() serializuje podany
# obiekt i zapisuje go w pliku contacts.dat.
def save_contacts(mycontacts):
    # Otworzenie pliku w trybie zapisu binarnego.
    output_file = open(FILENAME, 'wb')

    # Serializacja słownika i jego zapis w pliku.
    pickle.dump(mycontacts, output_file)

    # Zamknięcie pliku.
    output_file.close()

# Wywołanie funkcji main().
main()
