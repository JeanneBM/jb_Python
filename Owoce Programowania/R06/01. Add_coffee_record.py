# Ten program dodaje nowy
# rekord do pliku coffee.txt.

def main():
    # Utworzenie zmiennej kontrolującej działanie pętli.
    another = 't'

    # Otworzenie pliku coffee.txt w trybie dołączania danych.
    coffee_file = open('coffee.txt', 'a')

    # Dodanie rekordów do pliku.
    while another == 't' or another == 'T':
        # Pobranie rekordu danych.
        print('Podaj dane kawy:')
        descr = input('Opis: ')
        qty = int(input('Ilość (w kilogramach): '))

        # Dołączenie danych do pliku.
        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')

        # Ustalenie, czy użytkownik chce
        # dodać kolejny rekord do pliku.
        print('Czy chcesz dodać kolejny rekord?')
        another = input('Jeśli tak, wpisz t, w przeciwnym razie wpisz inny znak: ')

    # Zamknięcie pliku.
    coffee_file.close()
    print('Dane zostały dołączone do pliku coffee.txt.')

# Wywołanie funkcji main().
main()
