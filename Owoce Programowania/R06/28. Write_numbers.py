# Ten program pokazuje, że liczba musi być
# skonwertowana na postać ciągu tekstowego
# przed jej zapisaniem w pliku tekstowym.

def main():
    # Otworzenie pliku do zapisu.
    outfile = open('numbers.txt', 'w')

    # Pobranie trzech liczb od użytkownika.
    num1 = int(input('Podaj liczbę: '))
    num2 = int(input('Podaj następną liczbę: '))
    num3 = int(input('Podaj następną liczbę: '))

    # Zapisanie liczb w pliku.
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    # Zamknięcie pliku.
    outfile.close()
    print('Dane zostały zapisane w pliku numbers.txt')

# Wywołanie funkcji main().
main()
