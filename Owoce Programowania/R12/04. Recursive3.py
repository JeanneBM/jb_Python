# Ten program pokazuje przykład użycia funkcji range_sum().

def main():
    # Utworzenie listy liczb.
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Zsumowanie elementów
    # o indeksach od 2 do 5.
    my_sum = range_sum(numbers, 2, 5)

    # Wyświetlenie obliczonej sumy.
    print('Suma elementów o indeksach od 2 do 5 wynosi', my_sum)

# Funkcja range_sum() zwraca sumę podanego zakresu
# elementów listy num_list. Parametr start określa indeks
# pierwszego sumowanego elementu. Parametr end
# określa indeks ostatniego sumowanego elementu.
def range_sum(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)

# Wywołanie funkcji main().
main()
