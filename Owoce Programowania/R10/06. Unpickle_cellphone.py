# Ten program przeprowadza deserializację obiektów klasy CellPhone.
import pickle
import cellphone

# Stała przechowująca nazwę pliku.
FILENAME = 'cellphones.dat'

def main():
    end_of_file = False    # Ta opcja będzie wskazywała koniec pliku.

    # Otworzenie pliku.
    input_file = open(FILENAME, 'rb')

    # Odczyt danych aż do końca pliku.
    while not end_of_file:
        try:
            # Deserializacja następnego obiektu.
            phone = pickle.load(input_file)

            # Wyświetlenie danych telefonu komórkowego.
            display_data(phone)
        except EOFError:
            # Ustawienie opcji oznaczającej
            # dotarcie do końca pliku.
            end_of_file = True

    # Zamknięcie pliku.
    input_file.close()

# Funkcja display_data() wyświetla dane pochodzące
# z obiektu CellPhone przekazanego jej jako argument.
def display_data(phone):
    print('Producent:', phone.get_manufact())
    print('Numer modelu:', phone.get_model())
    print('Cena detaliczna:',
          format(phone.get_retail_price(), '.2f'),
          sep='')
    print()

# Wywołanie funkcji main().
main()
