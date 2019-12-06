# Ten program pobiera od użytkownika trzy
# elementy danych, a następnie zapisuje je w pliku.

def main():
    # Pobranie trzech imion.
    print('Podaj imiona trójki przyjaciół.')
    name1 = input('Przyjaciel #1: ')
    name2 = input('Przyjaciel #2: ')
    name3 = input('Przyjaciel #3: ')

    # Otworzenie pliku o nazwie friends.txt.
    myfile = open('friends.txt', 'w')

    # Zapis danych w pliku.
    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')

    # Zamknięcie pliku.
    myfile.close()
    print('Imiona zostały zapisane w pliku friends.txt.')

# Wywołanie funkcji main().
main()
