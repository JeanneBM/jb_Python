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
