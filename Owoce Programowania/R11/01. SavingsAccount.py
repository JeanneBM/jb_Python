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
