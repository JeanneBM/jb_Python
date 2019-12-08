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
