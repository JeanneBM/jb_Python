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
