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
