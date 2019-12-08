# Ten program przeprowadza serializację obiektów klasy CellPhone.
import pickle
import cellphone

# Stała przechowująca nazwę pliku.
FILENAME = 'cellphones.dat'

def main():
    # Inicjalizacja zmiennej kontrolującej działanie pętli.
    again = 't'

    # Otworzenie pliku.
    output_file = open(FILENAME, 'wb')

    # Pobranie danych od użytkownika.
    while again.lower() == 't':
        # Pobranie danych o telefonie komórkowym.
        man = input('Podaj producenta telefonu: ')
        mod = input('Podaj numer modelu telefonu: ')
        retail = float(input('Podaj cenę detaliczną telefonu: '))

        # Utworzenie obiektu klasy CellPhone.
        phone = cellphone.CellPhone(man, mod, retail)

        # Serializacja obiektu i jego zapis w pliku.
        pickle.dump(phone, output_file)

        # Czy będą podane dane o kolejnym telefonie komórkowym?
        again = input('Czy chcesz podać dane kolejnego telefonu komórkowego? (t/n): ')

    # Zamknięcie pliku.
    output_file.close()
    print('Dane zostały zapisane w pliku ', FILENAME)

# Wywołanie funkcji main().
main()
