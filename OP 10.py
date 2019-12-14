01. BankAccount.py 

# Klasa BankAccount symuluje konto w banku.

class BankAccount:

    # Metoda __init__() akceptuje argument
    # w postaci salda konta. Ta wartość
    # zostanie przypisana atrybutowi __balance.

    def __init__(self, bal):
        self.__balance = bal

    # Metoda deposit() symuluje
    # utworzenie depozytu.

    def deposit(self, amount):
        self.__balance += amount

    # Metoda withdraw() symuluje
    # wypłatę środków z konta.

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Błąd: niewystarczająca ilość środków')

    # Metoda get_balance() zwraca
    # bieżącą wysokość salda.

    def get_balance(self):
        return self.__balance
      
----------------------------------------------------------------------------------------------------------------------------------------------

02. Account_test.py 

# Ten program pokazuje przykład zastosowania klasy BankAccount.

import bankaccount

def main():
    # Określenie salda początkowego.
    start_bal = float(input('Podaj początkową wysokość salda: '))

    # Utworzenie obiektu BankAccount.
    savings = bankaccount.BankAccount(start_bal)

    # Zdeponowanie pewnej kwoty na koncie.
    pay = float(input('Jaką kwotę zarobiłeś w tym tygodniu? '))
    print('Ta kwota została zdeponowana na koncie.')
    savings.deposit(pay)

    # Wyświetlenie salda bieżącego.
    print('Wysokość salda wynosi ',
          format(savings.get_balance(), '.2f'),
          sep='')

    # Pobranie kwoty, która ma zostać wypłacona.
    cash = float(input('Jaką kwotę chcesz wypłacić? '))
    print('Ta kwota zostanie odjęta od bieżącej wysokości salda.')
    savings.withdraw(cash)

    # Wyświetlenie salda bieżącego.
    print('Wysokość salda wynosi ',
          format(savings.get_balance(), '.2f'),
          sep='')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

03. BankAccount2.py 

# Klasa BankAccount symuluje konto w banku.

class BankAccount:

    # Metoda __init__() akceptuje argument
    # w postaci salda konta. Ta wartość
    # zostanie przypisana atrybutowi __balance.

    def __init__(self, bal):
        self.__balance = bal

    # Metoda deposit() symuluje
    # utworzenie depozytu.

    def deposit(self, amount):
        self.__balance += amount

    # Metoda withdraw() symuluje
    # wypłatę środków z konta.

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Błąd: niewystarczająca ilość środków')

    # Metoda get_balance() zwraca
    # bieżącą wysokość salda.

    def get_balance(self):
        return self.__balance

    # Metoda __str__() zwraca ciąg tekstowy
    # informujący o bieżącym stanie obiektu.

    def __str__(self):
        return 'Wysokość salda wynosi ' + format(self.__balance, '.2f')
      
----------------------------------------------------------------------------------------------------------------------------------------------

04. Account_test2.py 	

# Ten program pokazuje przykład zastosowania klasy BankAccount
# wraz z dodaną do niej metodą __str__().

import bankaccount2

def main():
    # Określenie salda początkowego.
    start_bal = float(input('Podaj początkową wysokość salda: '))

    # Utworzenie obiektu BankAccount.
    savings = bankaccount2.BankAccount(start_bal)

    # Zdeponowanie pewnej kwoty na koncie.
    pay = float(input('Jaką kwotę zarobiłeś w tym tygodniu? '))
    print('Ta kwota została zdeponowana na koncie.')
    savings.deposit(pay)

    # Wyświetlenie salda bieżącego.
    print(savings)

    # Pobranie kwoty, która ma zostać wypłacona.
    cash = float(input('Jaką kwotę chcesz wypłacić? '))
    print('Ta kwota zostanie odjęta od bieżącej wysokości salda.')
    savings.withdraw(cash)

    # Wyświetlenie salda bieżącego.
    print(savings)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

05. Car.py 	

# Klasa Car.
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year
      
----------------------------------------------------------------------------------------------------------------------------------------------

06. Cellphone.py 

# Klasa CellPhone przechowuje dane dotyczące telefonu komórkowego.

class CellPhone:

    # Metoda __init__() inicjalizuje atrybuty.

    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    # Metoda set_manufact() akceptuje argument
    # przedstawiający producenta telefonu komórkowego.

    def set_manufact(self, manufact):
        self.__manufact = manufact

    # Metoda set_model() akceptuje argument
    # przedstawiający numer modelu telefonu komórkowego.

    def set_model(self, model):
        self.__model = model

    # Metoda set_retail_price() akceptuje argument
    # przedstawiający cenę detaliczną telefonu komórkowego.

    def set_retail_price(self, price):
        self.__retail_price = price

    # Metoda get_manufact() zwraca
    # producenta telefonu komórkowego.

    def get_manufact(self):
        return self.__manufact

    # Metoda get_model() zwraca
    # numer modelu telefonu komórkowego.

    def get_model(self):
        return self.__model

    # Metoda get_retail_price() zwraca
    # cenę detaliczną telefonu komórkowego.

    def get_retail_price(self):
        return self.__retail_price
      
----------------------------------------------------------------------------------------------------------------------------------------------

06. Cellphone_list.py 	

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

----------------------------------------------------------------------------------------------------------------------------------------------

06. Cellphone_test.py 	

# Ten program testuje klasę CellPhone.

import cellphone

def main():
    # Pobranie danych o telefonie komórkowym.
    man = input('Podaj producenta telefonu: ')
    mod = input('Podaj numer modelu telefonu: ')
    retail = float(input('Podaj cenę detaliczną telefonu: '))

    # Utworzenie egzemplarza klasy CellPhone.
    phone = cellphone.CellPhone(man, mod, retail)

    # Wyświetlenie podanych danych.
    print('Oto podane przez Ciebie dane:')
    print('Producent:', phone.get_manufact())
    print('Numer modelu:', phone.get_model())
    print('Cena detaliczna:', format(phone.get_retail_price(), '.2f'), sep='')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

06. Pickle_cellphone.py 

# Ten program przeprowadza serializację obiektów klasy CellPhone.
import pickle
import cellphone

# Stała przechowująca nazwę pliku.
FILENAME = 'cellphones.dat'

def main():
    # Inicjalizacja zmiennej kontrolującej działanie pętli.
    again = 't'

    # Otworzenie pliku.
    output_file = open(FILENAME, 'wb')

    # Pobranie danych od użytkownika.
    while again.lower() == 't':
        # Pobranie danych o telefonie komórkowym.
        man = input('Podaj producenta telefonu: ')
        mod = input('Podaj numer modelu telefonu: ')
        retail = float(input('Podaj cenę detaliczną telefonu: '))

        # Utworzenie obiektu klasy CellPhone.
        phone = cellphone.CellPhone(man, mod, retail)

        # Serializacja obiektu i jego zapis w pliku.
        pickle.dump(phone, output_file)

        # Czy będą podane dane o kolejnym telefonie komórkowym?
        again = input('Czy chcesz podać dane kolejnego telefonu komórkowego? (t/n): ')

    # Zamknięcie pliku.
    output_file.close()
    print('Dane zostały zapisane w pliku ', FILENAME)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

06. Unpickle_cellphone.py 	

# Ten program przeprowadza deserializację obiektów klasy CellPhone.
import pickle
import cellphone

# Stała przechowująca nazwę pliku.
FILENAME = 'cellphones.dat'

def main():
    end_of_file = False    # Ta opcja będzie wskazywała koniec pliku.

    # Otworzenie pliku.
    input_file = open(FILENAME, 'rb')

    # Odczyt danych aż do końca pliku.
    while not end_of_file:
        try:
            # Deserializacja następnego obiektu.
            phone = pickle.load(input_file)

            # Wyświetlenie danych telefonu komórkowego.
            display_data(phone)
        except EOFError:
            # Ustawienie opcji oznaczającej
            # dotarcie do końca pliku.
            end_of_file = True

    # Zamknięcie pliku.
    input_file.close()

# Funkcja display_data() wyświetla dane pochodzące
# z obiektu CellPhone przekazanego jej jako argument.
def display_data(phone):
    print('Producent:', phone.get_manufact())
    print('Numer modelu:', phone.get_model())
    print('Cena detaliczna:',
          format(phone.get_retail_price(), '.2f'),
          sep='')
    print()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

07. Coin.py 	

import random

# Klasa Coin symuluje rzut monetą, w przypadku
# którego może wypaść orzeł lub reszka.

class Coin:

    # Metoda __init__() inicjalizuje atrybut danych
    #  __sideup o wartości 'orzeł'.

    def __init__(self):
        self.__sideup = 'orzeł'

    # Metoda toss() generuje liczbę losową w przedziale
    # od 0 do 1. Jeżeli liczba to 0, wówczas atrybut danych
    # __sideup ma wartość 'orzeł'. W przeciwnym razie jego
    # wartością jest 'reszka'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'orzeł'
        else:
            self.__sideup = 'reszka'

    # Metoda get_sideup() zwraca wartość
    # przechowywaną przez atrybut __sideup.

    def get_sideup(self):
        return self.__sideup
      
----------------------------------------------------------------------------------------------------------------------------------------------

07. Coin_argument.py

# Ten program przekazuje obiekt Coin
# jako argument funkcji.
import coin

# Funkcja main().
def main():
    # Utworzenie obiektu Coin.
    my_coin = coin.Coin()

    # To polecenie wyświetli ciąg tekstowy 'orzeł'.
    print(my_coin.get_sideup())

    # Przekazanie obiektu funkcji flip().
    flip(my_coin)

    # To polecenie może wyświetlić ciąg tekstowy
    # 'orzeł' lub 'reszka'.
    print(my_coin.get_sideup())

# Funkcja flip() symuluje rzut monetą.
def flip(coin_obj):
    coin_obj.toss()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

07. Coin_demo1.py 	

import random

# Klasa Coin symuluje rzut monetą, w przypadku
# której może wypaść orzeł lub reszka.

class Coin:

    # Metoda __init__() inicjalizuje atrybut
    # danych sideup o wartości 'orzeł'.

    def __init__(self):
        self.sideup = 'orzeł'

    # Metoda toss() generuje liczbę losową w przedziale
    # od 0 do 1. Jeżeli liczba to 0, wówczas atrybut danych
    # sideup ma wartość 'orzeł'. W przeciwnym razie jego
    # wartością jest 'reszka'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'orzeł'
        else:
            self.sideup = 'reszka'

    # Metoda get_sideup() zwraca wartość
    # przechowywaną przez atrybut danych sideup.

    def get_sideup(self):
        return self.sideup

# Funkcja main().
def main():
    # Utworzenie obiektu na podstawie klasy Coin.
    my_coin = Coin()

    # Wyświetlenie wyniku rzutu monetą.
    print('Wynik rzutu monetą:', my_coin.get_sideup())

    # Symulacja rzutu monetą.
    print('Symulacja rzutu monetą...')
    my_coin.toss()

    # Wyświetlenie wyniku rzutu monetą.
    print('Wynik rzutu monetą:', my_coin.get_sideup())

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

07. Coin_demo2.py 	

import random

# Klasa Coin symuluje rzut monetą, w przypadku
# której może wypaść orzeł lub reszka.

class Coin:

    # Metoda __init__() inicjalizuje atrybut
    # danych sideup o wartości 'orzeł'.

    def __init__(self):
        self.sideup = 'orzeł'

    # Metoda toss() generuje liczbę losową w przedziale
    # od 0 do 1. Jeżeli liczba to 0, wówczas atrybut danych
    # sideup ma wartość 'orzeł'. W przeciwnym razie jego
    # wartością jest 'reszka'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'orzeł'
        else:
            self.sideup = 'reszka'

    # Metoda get_sideup() zwraca wartość
    # przechowywaną przez atrybut danych sideup.

    def get_sideup(self):
        return self.sideup

# Funkcja main().
def main():
    # Utworzenie obiektu na podstawie klasy Coin.
    my_coin = Coin()

    # Wyświetlenie wyniku rzutu monetą.
    print('Wynik rzutu monetą:', my_coin.get_sideup())

    # Symulacja rzutu monetą.
    print('Symulacja rzutu monetą...')
    my_coin.toss()

    # A teraz małe oszustwo! Zamierzam
    # bezpośrednio zmienić wartość
    # atrybutu sideup na 'orzeł'.
    my_coin.sideup = 'orzeł'

    # Wyświetlenie wyniku rzutu monetą.
    print('Wynik rzutu monetą:', my_coin.get_sideup())

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

07. Coin_demo3.py 	

import random

# Klasa Coin symuluje rzut monetą, w przypadku
# którego może wypaść orzeł lub reszka.

class Coin:

    # Metoda __init__() inicjalizuje atrybut
    # danych __sideup o wartości 'orzeł'.

    def __init__(self):
        self.__sideup = 'orzeł'

    # Metoda toss() generuje liczbę losową w przedziale
    # od 0 do 1. Jeżeli liczba to 0, wówczas atrybut danych
    # __sideup ma wartość 'orzeł'. W przeciwnym razie jego
    # wartością jest 'reszka'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'orzeł'
        else:
            self.__sideup = 'reszka'

    # Metoda get_sideup() zwraca wartość
    # przechowywaną przez atrybut __sideup.

    def get_sideup(self):
        return self.__sideup

# Funkcja main().
def main():
    # Utworzenie obiektu na podstawie klasy Coin.
    my_coin = Coin()

    # Wyświetlenie wyniku rzutu monetą.
    print('Wynik rzutu monetą:', my_coin.get_sideup())

    # Symulacja rzutu monetą.
    print('Symulacja dziesięciu rzutów monetą:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

07. Coin_demo4.py 	

# Ten program importuje moduł coin,
# a następnie tworzy egzemplarz klasy Coin.

import coin

def main():
    # Utworzenie obiektu na podstawie klasy Coin.
    my_coin = coin.Coin()

    # Wyświetlenie wyniku rzutu monetą.
    print('Wynik rzutu monetą:', my_coin.get_sideup())

    # Symulacja rzutu monetą.
    print('Symulacja dziesięciu rzutów monetą:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

07. Coin_demo5.py 	

# Ten program importuje moduł coin
# i tworzy trzy egzemplarze klasy Coin.

import coin

def main():
    # Utworzenie trzech egzemplarz klasy Coin.
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()

    # Wyświetlenie wyników rzutów monetami.
    print('Oto wyniki rzutów trzema monetami:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

    # Symulacja rzutu monetą.
    print('Symulacja rzutów trzema monetami...')
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()

    # Wyświetlenie wyników rzutów monetami.
    print('Oto wyniki rzutów trzema monetami:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

07. Klasa_Coin.py 	

import random

# Klasa Coin symuluje rzut monetą, w przypadku
# której może wypaść orzeł lub reszka.

class Coin:

    # Metoda __init__() inicjalizuje atrybut
    # danych sideup o wartości 'orzeł'.

    def __init__(self):
        self.sideup = 'orzeł'

    # Metoda toss() generuje liczbę losową w przedziale
    # od 0 do 1. Jeżeli liczba to 0, wówczas atrybut danych
    # sideup ma wartość 'orzeł'. W przeciwnym razie jego
    # wartością jest 'reszka'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'orzeł'
        else:
            self.sideup = 'reszka'

    # Metoda get_sideup() zwraca wartość
    # przechowywaną przez atrybut danych sideup.

    def get_sideup(self):
        return self.sideup
      
----------------------------------------------------------------------------------------------------------------------------------------------

08. Contact.py 	

# Klasa Contact przechowuje informacje o osobie.

class Contact:
    # Metoda __init__() inicjalizuje atrybuty.
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    # Metoda set_name() przypisuje wartość atrybutu name.
    def set_name(self, name):
        self.__name = name

    # Metoda set_phone przypisuje wartość atrybutu phone.
    def set_phone(self, phone):
        self.__phone = phone

    # Metoda set_email przypisuje wartość atrybutu email.
    def set_email(self, email):
        self.__email = email

    # Metoda get_name() zwraca wartość atrybutu name.
    def get_name(self):
        return self.__name

    # Metoda get_phone() zwraca wartość atrybutu phone.
    def get_phone(self):
        return self.__phone

    # Metoda get_email() zwraca wartość atrybutu email.
    def get_email(self):
        return self.__email

    # Metoda __str__() zwraca ciąg tekstowy
    # przedstawiający informacje o stanie obiektu.
    def __str__(self):
        return "Imię i nazwisko: " + self.__name + \
               "\nNumer telefonu: " + self.__phone + \
               "\nAdres e-mail " + self.__email
      
----------------------------------------------------------------------------------------------------------------------------------------------

08. Contact_manager.py 

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

----------------------------------------------------------------------------------------------------------------------------------------------

09. Customer.py 	

# Klasa Customer.
class Customer:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone
      
----------------------------------------------------------------------------------------------------------------------------------------------

10. ServiceQuote.py 	

# Stała określająca procentową wysokość podatku.
TAX_RATE = 0.05

# Klasa ServiceQuote.
class ServiceQuote:
    def __init__(self, pcharge, lcharge):
        self.__parts_charges = pcharge
        self.__labor_charges = lcharge

    def set_parts_charges(self, pcharge):
        self.__parts_charges = pcharge

    def set_labor_charges(self, lcharge):
        self.__labor_charges = lcharge

    def get_parts_charges(self):
        return self.__parts_charges

    def get_labor_charges(self):
        return self.__labor_charges

    def get_sales_tax(self):
        return self.__parts_charges * TAX_RATE

    def get_total_charges(self):
        return self.__parts_charges + self.__labor_charges + \
               (self.__parts_charges * TAX_RATE)
      
----------------------------------------------------------------------------------------------------------------------------------------------
