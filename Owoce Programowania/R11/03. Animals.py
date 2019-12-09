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
