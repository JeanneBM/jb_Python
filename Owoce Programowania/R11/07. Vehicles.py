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

