# Ten program wyświetla sumę wszystkich
# wartości zapisanych w pliku sales_data.txt.

def main():
    # Inicjalizacja zmiennej akumulatora.
    total = 0.0

    try:
        # Otworzenie pliku sales_data.txt.
        infile = open('sales_data.txt', 'r')

        # Odczytanie wartości z pliku,
        # a następnie ich zsumowanie.
        for line in infile:
            amount = float(line)
            total += amount

        # Zamknięcie pliku.
        infile.close()

        # Wyświetlenie obliczonej sumy.
        print(format(total, '.2f'))

    except IOError:
        print('Wystąpił błąd podczas odczytu pliku.')

    except ValueError:
        print('W pliku znajdują się dane inne niż liczbowe.')

    except:
        print('Wystąpił błąd.')

# Wywołanie funkcji main().
main()
