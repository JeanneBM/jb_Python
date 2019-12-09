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

