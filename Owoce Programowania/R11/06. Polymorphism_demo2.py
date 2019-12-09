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

