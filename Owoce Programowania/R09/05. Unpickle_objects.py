# Ten program przedstawia deserializację obiektu.
import pickle

# Funkcja main().
def main():
    end_of_file = False  # Ta opcja będzie wskazywała koniec pliku.

    # Otworzenie pliku w trybie odczytu binarnego.
    input_file = open('info.dat', 'rb')

    # Odczyt danych aż do końca pliku.
    while not end_of_file:
        try:
            # Deserializacja następnego obiektu.
            person = pickle.load(input_file)

            # Wyświetlenie obiektu.
            display_data(person)
        except EOFError:
            # Ustawienie opcji oznaczającej
            # dotarcie do końca pliku.
            end_of_file = True

    # Zamknięcie pliku.
    input_file.close()

# Funkcja display_data() wyświetla informacje o osobie,
# której słownik został przekazany jako argument.
def display_data(person):
    print('Imię:', person['name'])
    print('Wiek:', person['age'])
    print('Waga:', person['weight'])
    print()

# Wywołanie funkcji main().
main()
