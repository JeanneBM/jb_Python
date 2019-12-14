01. SavingsAccount.py 	

# Klasa SavingsAccount przedstawia
# konto oszczędnościowe.

class SavingsAccount:

    # Metoda __init__() akceptuje argumenty w postaci
    # numeru konta, oprocentowania i salda.

    def __init__(self, account_num, int_rate, bal):
        self.__account_num = account_num
        self.__interest_rate = int_rate
        self.__balance = bal

    # Tutaj znajdują się metody mutatorów dla
    # atrybutów danych.

    def set_account_num(self, account_num):
        self.__account_num = account_num

    def set_interest_rate(self, int_rate):
        self.__interest_rate = int_rate

    def set_balance(self, bal):
        self.__balance = bal

    # Tutaj znajdują się metody akcesorów dla
    # atrybutów danych.

    def get_account_num(self):
        return self.__account_num

    def get_interest_rate(self):
        return self.__interest_rate

    def get_balance(self):
        return self.__balance

# Klasa CD przedstawia certyfikat
# depozytowy. To jest podklasa klasy
# SavingsAccount.

class CD(SavingsAccount):

    # Metoda __init__() akceptuje argumenty w postaci
    # numeru konta, oprocentowania, salda
    # i daty wykupu.

    def __init__(self, account_num, int_rate, bal, mat_date):
        # Wywołanie metody __init__() superklasy.
        SavingsAccount.__init__(self, account_num, int_rate, bal)

        # Inicjalizacja atrybutu __maturity_date.
        self.__maturity_date = mat_date

    # Metoda set_maturity_date() to mutator
    # dla atrybutu __maturity_date.

    def set_maturity_date(self, mat_date):
        self.__maturity_date = mat_date

    # Metoda get_maturity_date() to akcesor
    # dla atrybutu __maturity_date.

    def get_maturity_date(self):
        return self.__maturity_date
      
----------------------------------------------------------------------------------------------------------------------------------------------

02. Account_demo.py 

# Ten program tworzy egzemplarze
# klas SavingsAccount i CD.

import accounts

def main():
    # Pobranie numeru konta, oprocentowania,
    # i salda konta oszczędnościowego.
    print('Podaj dane dotyczące konta oszczędnościowego.')
    acct_num = input('Numer konta: ')
    int_rate = float(input('Oprocentowanie: '))
    balance = float(input('Saldo: '))

    # Utworzenie obiektu klasy SavingsAccount.
    savings = accounts.SavingsAccount(acct_num, int_rate,
                                      balance)

    # Pobranie numeru konta, oprocentowania,
    # salda i daty wykupu certyfikatu depozytowego.
    print('Podaj dane dotyczące certyfikatu depozytowego.')
    acct_num = input('Numer konta: ')
    int_rate = float(input('Oprocentowanie: '))
    balance = float(input('Saldo: '))
    maturity = input('Data wykupu:')

    # Utworzenie obiektu klasy CD.
    cd = accounts.CD(acct_num, int_rate, balance, maturity)

    # Wyświetlenie wprowadzonych danych.
    print('Oto wprowadzone dane:')
    print()
    print('Konto oszczędnościowe')
    print('---------------------')
    print('Numer konta:', savings.get_account_num())
    print('Oprocentowanie:', savings.get_interest_rate())
    print('Saldo: ',
          format(savings.get_balance(), '.2f'),
          sep='')
    print()
    print('CD')
    print('---------------------')
    print('Numer konta:', cd.get_account_num())
    print('Oprocentowanie:', cd.get_interest_rate())
    print('Saldo: ',
          format(cd.get_balance(), '.2f'),
          sep='')
    print('Data wykupu:', cd.get_maturity_date())

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

03. Animals.py 	

# Klasa Mammal przedstawia zwierzę.

class Mammal:

    # Metoda __init__() akceptuje argument
    # określający gatunek zwierzęcia.

    def __init__(self, species):
        self.__species = species

    # Metoda show_species() wyświetla komunikat
    # podający gatunek zwierzęcia.

    def show_species(self):
        print('To jest', self.__species)

    # Metoda make_sound() symuluje
    # wydanie dźwięku.

    def make_sound(self):
        print('Grrrrr')

# Klasa Dog jest podklasą klasy Mammal.

class Dog(Mammal):

    # Metoda __init__() wywołuje metodę __init__()
    # superklasy i przekazuje argument 'pies'.

    def __init__(self):
        Mammal.__init__(self, 'pies')

    # Metoda make_sound() nadpisuje metodę
    # o tej samej nazwie w superklasie.

    def make_sound(self):
        print('Hau! Hau!')

# Klasa Cat jest podklasą klasy Mammal.

class Cat(Mammal):

    # Metoda __init__() wywołuje metodę __init__()
    # superklasy i przekazuje argument 'kot'.

    def __init__(self):
        Mammal.__init__(self, 'Cat')

    # Metoda make_sound() nadpisuje metodę
    # o tej samej nazwie w superklasie.

    def make_sound(self):
        print('Miau')
        
----------------------------------------------------------------------------------------------------------------------------------------------

04. Wrong_type.py 

def main():
    # Przekazanie ciągu tekstowego funkcji show_mammal_info()…
    show_mammal_info('To jest ciąg tekstowy')

# Funkcja show_mammal_info() akceptuje
# argument w postaci obiektu, a następnie
# wywołuje jego metody show_species() i make_sound().

def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

05. Polymorphism_demo1.py 	

# Ten program pokazuje przykład zastosowania polimorfizmu.

import animals

def main():
    # Utworzenie obiektów klas
    # Mammal, Dog i Cat.
    mammal = animals.Mammal('zwierzę')
    dog = animals.Dog()
    cat = animals.Cat()

    # Wyświetlenie informacji o każdym zwierzęciu.
    print('Oto kilka przykładów zwierząt')
    print('i wydawanych przez nie dźwięków.')
    print('--------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)

# Funkcja show_mammal_info() akceptuje
# argument w postaci obiektu, a następnie
# wywołuje jego metody show_species() i make_sound().

def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

06. Polymorphism_demo2.py 

# Ten program pokazuje przykład zastosowania polimorfizmu.

import animals

def main():
    # Utworzenie obiektów klas
    # Mammal, Dog i Cat.
    mammal = animals.Mammal('zwierzę')
    dog = animals.Dog()
    cat = animals.Cat()

    # Wyświetlenie informacji o każdym zwierzęciu.
    print('Oto kilka przykładów zwierząt')
    print('i wydawanych przez nie dźwięków.')
    print('--------------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
    print()
    show_mammal_info('To jest ciąg tekstowy')

# Funkcja show_mammal_info() akceptuje
# argument w postaci obiektu, a następnie
# wywołuje jego metody show_species() i make_sound().

def show_mammal_info(creature):
    if isinstance(creature, animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print('To nie jest zwierzę!')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

07. Vehicles.py 	

# Klasa Automobile przechowuje ogólne dane
# dotyczące samochodu w posiadaniu dealera.

class Automobile:
    # Metoda __init__() akceptuje argumenty
    # w postaci marki, modelu, przebiegu i ceny. Inicjalizuje
    # atrybuty danych z podanymi wartościami.

    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    # Tutaj znajdują się metody mutatorów
    # dla atrybutów danych klasy.

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    # Tutaj znajdują się metody akcesorów
    # dla atrybutów danych klasy.

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

# Klasa Car przedstawia samochód osobowy. To jest
# podklasa klasy Automobile.

class Car(Automobile):
    # Metoda __init__() akceptuje argumenty w postaci
    # marki, modelu, przebiegu, ceny i liczby drzwi.

    def __init__(self, make, model, mileage, price, doors):
        # Wywołanie metody __init__() superklasy i przekazanie
        # wymaganych argumentów. Zwróć uwagę na
        # przekazanie również self jako argumentu.
        Automobile.__init__(self, make, model, mileage, price)

        # Inicjalizacja atrybutu __doors.
        self.__doors = doors

    # Metoda set_doors() jest mutatorem
    # dla atrybutu __doors.

    def set_doors(self, doors):
        self.__doors = doors

    # Metoda get_doors() jest akcesorem
    # dla atrybutu __doors.

    def get_doors(self):
        return self.__doors

# Klasa Truck przedstawia samochód terenowy. To jest
# podklasa klasy Automobile.

class Truck(Automobile):
    # Metoda __init__() akceptuje argumenty w postaci
    # marki, modelu, przebiegu, ceny i rodzaju napędu samochodu.

    def __init__(self, make, model, mileage, price, drive_type):
        # Wywołanie metody __init__() superklasy i przekazanie
        # wymaganych argumentów. Zwróć uwagę na
        # przekazanie również self jako argumentu.
        Automobile.__init__(self, make, model, mileage, price)

        # Inicjalizacja atrybutu __drive_type.
        self.__drive_type = drive_type

    # Metoda set_drive_type() jest mutatorem
    # dla atrybutu __drive_type.

    def set_drive_type(self, drive_type):
        self.__drive = drive_type

    # Metoda get_drive_type() jest akcesorem
    # dla atrybutu __drive_type.

    def get_drive_type(self):
        return self.__drive_type

# Klasa SUV przedstawia samochód typu SUV. Jest to
# podklasa klasy Automobile class.

class SUV(Automobile):
    # Metoda __init__() akceptuje argumenty
    # w postaci marki, modelu, przebiegu, ceny
    # i liczby miejsc.

    def __init__(self, make, model, mileage, price, pass_cap):
        # Wywołanie metody __init__() superklasy i przekazanie
        # wymaganych argumentów. Zwróć uwagę na
        # przekazanie również self jako argumentu.
        Automobile.__init__(self, make, model, mileage, price)

        # Inicjalizacja atrybutu __pass_cap.
        self.__pass_cap = pass_cap

    # Metoda set_pass_cap() jest mutatorem
    # dla atrybutu __pass_cap.

    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap

    # Metoda get_pass_cap() jest akcesorem
    # dla atrybutu __pass_cap.

    def get_pass_cap(self):
        return self.__pass_cap
      
----------------------------------------------------------------------------------------------------------------------------------------------

08. Car_demo.py 

# Ten program pokazuje przykład użycia klasy Car.

import vehicles

def main():
    # Utworzenie obiektu na podstawie klasy Car.
    # Samochodem jest Audi z 2007 roku o przebiegu 12500
    # w cenie 21500. Ten samochód jest czterodrzwiowy.
    used_car = vehicles.Car('Audi', 2007, 12500, 21500.0, 4)

    # Wyświetlenie danych samochodu.
    print('Marka:', used_car.get_make())
    print('Model:', used_car.get_model())
    print('Przebieg:', used_car.get_mileage())
    print('Cena:', used_car.get_price())
    print('Liczba drzwi:', used_car.get_doors())

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

09. Car_truck_suv_demo.py

# Ten program tworzy obiekty
# klas Car, Truck i SUV.

import vehicles

def main():
    # Utworzenie obiektu Car przedstawiającego
    # używane czterodrzwiowe BMW z roku 2001
    # o przebiegu 70000 i cenie 15000.
    car = vehicles.Car('BMW', 2001, 70000, 15000.0, 4)

    # Utworzenie obiektu Truck przedstawiającego
    # używaną Toyotę o przebiegu 40000 w cenie
    # 12000 oraz z napędem na cztery koła.
    truck = vehicles.Truck('Toyota', 2002, 40000, 12000.0, '4WD')

    # Utworzenie obiektu SUV przedstawiającego
    # używane pięciomiejscowe Volvo z roku 2000
    # o przebiegu 30000 i cenie 18500.
    suv = vehicles.SUV('Volvo', 2000, 30000, 18500.0, 5)

    print('DOSTĘPNE SAMOCHODY UŻYWANE')
    print('==========================')

    # Wyświetlenie danych samochodu osobowego.
    print('W ofercie jest następujący samochód osobowy:')
    print('Marka:', car.get_make())
    print('Model:', car.get_model())
    print('Przebieg:', car.get_mileage())
    print('Cena:', car.get_price())
    print('Liczba drzwi:', car.get_doors())
    print()

    # Wyświetlenie danych samochodu terenowego.
    print('W ofercie jest następujący samochód terenowy:')
    print('Marka:', truck.get_make())
    print('Model:', truck.get_model())
    print('Przebieg:', truck.get_mileage())
    print('Cena:', truck.get_price())
    print('Drive type:', truck.get_drive_type())
    print()

    # Wyświetlenie danych samochodu typu SUV.
    print('W ofercie jest następujący samochód typu SUV:')
    print('Marka:', suv.get_make())
    print('Model:', suv.get_model())
    print('Przebieg:', suv.get_mileage())
    print('Cena:', suv.get_price())
    print('Passenger Capacity:', suv.get_pass_cap())

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------
