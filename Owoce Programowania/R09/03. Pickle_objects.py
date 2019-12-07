# Ten program przedstawia serializację obiektu.
import pickle

# Funkcja main().
def main():
    again = 't'  # Zmienna kontrolująca działanie pętli.

    # Otworzenie pliku w trybie zapisu binarnego.
    output_file = open('info.dat', 'wb')

    # Pobieranie danych dopóki, dopóty użytkownik nie zdecyduje inaczej.
    while again.lower() == 't':
        # Pobranie danych o osobie i ich zapisanie.
        save_data(output_file)

        # Czy użytkownik chce wprowadzić kolejne dane?
        again = input('Chcesz podać kolejne dane? (t/n): ')

    # Zamknięcie pliku.
    output_file.close()

# Funkcja save_data() pobiera dane o osobie,
# umieszcza je w słowniku, a następnie serializuje
# słownik do podanego pliku.
def save_data(file):
    # Utworzenie pustego słownika.
    person = {}

    # Pobranie danych o osobie
    # i umieszczenie ich w słowniku.
    person['name'] = input('Imię: ')
    person['age'] = int(input('Wiek: '))
    person['weight'] = float(input('Waga: '))

    # Serializacja słownika.
    pickle.dump(person, file)

# Wywołanie funkcji main().
main()
