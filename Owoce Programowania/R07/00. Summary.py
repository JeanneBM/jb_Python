01. Average_list.py 	

# Ten program oblicza średnią
# wartość elementów listy.

def main():
    # Utworzenie listy.
    scores = [2.5, 7.3, 6.5, 4.0, 5.2]

    # Utworzenie zmiennej przeznaczonej do użycia w charakterze akumulatora.
    total = 0.0

    # Obliczenie sumy wszystkich elementów listy.
    for value in scores:
        total += value

    # Obliczenie średniej wartości elementów listy.
    average = total / len(scores)

    # Wyświetlenie sumy wszystkich elementów listy.
    print('Średnia wartość elementów listy wynosi', average)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

02. Bar_chart1.py 	

# Ten program wyświetla prosty wykres słupkowy.
import matplotlib.pyplot as plt

def main():
    # Utworzenie listy wraz ze współrzędnymi X lewej krawędzi wszystkich słupków.
    left_edges = [0, 10, 20, 30, 40]

    # Utworzenie listy wraz z wysokością wszystkich słupków.
    heights = [100, 200, 300, 400, 500]

    # Utworzenie wykresu słupkowego.
    plt.bar(left_edges, heights)

    # Wyświetlenie wykresu słupkowego.
    plt.show()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

03. Bar_chart2.py 	

# Ten program wyświetla prosty wykres słupkowy.
import matplotlib.pyplot as plt

def main():
    # Utworzenie listy wraz ze współrzędnymi X lewej krawędzi wszystkich słupków.
    left_edges = [0, 10, 20, 30, 40]

    # Utworzenie listy wraz z wysokością wszystkich słupków.
    heights = [100, 200, 300, 400, 500]

    # Utworzenie zmiennej określającej szerokość słupka.
    bar_width = 5

    # Utworzenie wykresu słupkowego.
    plt.bar(left_edges, heights, bar_width)

    # Wyświetlenie wykresu słupkowego.
    plt.show()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

04. Bar_chart3.py 	

# Ten program displays a sales chart.
import matplotlib.pyplot as plt

def main():
    # Utworzenie listy wraz ze współrzędnymi X lewej krawędzi wszystkich słupków.
    left_edges = [0, 10, 20, 30, 40]

    # Utworzenie listy wraz z wysokością wszystkich słupków.
    heights = [100, 200, 300, 400, 500]

    # Utworzenie zmiennej określającej szerokość słupka.
    bar_width = 10

    # Utworzenie wykresu słupkowego.
    plt.bar(left_edges, heights, bar_width, color=('r', 'g', 'b', 'w', 'k'))

    # Dodanie tytułu.
    plt.title('Sprzedaż według roku')

    # Dodanie etykiet do osi.
    plt.xlabel('Rok')
    plt.ylabel('Sprzedaż')

    # Dostosowanie znaczników osi do własnych potrzeb.
    plt.xticks([5, 15, 25, 35, 45],
               ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 100, 200, 300, 400, 500],
               ['0 mln', '1 mln', '2 mln', '3 mln', '4 mln', '5 mln'])

    # Wyświetlenie wykresu słupkowego.
    plt.show()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

05. Barista_pay.py 	

# Ten program oblicza wysokość wynagrodzenia
# każdego z pracowników Małgorzaty.

# NUM_EMPLOYEES to jest stała
# określająca wielkość listy.
NUM_EMPLOYEES = 6

def main():
    # Utworzenie listy do przechowywania godzin przepracowanych przez pracowników.
    hours = [0] * NUM_EMPLOYEES

    # Pobranie liczby godzin przepracowanych przez poszczególnych pracowników.
    for index in range(NUM_EMPLOYEES):
        print('Podaj liczbę godzin przepracowanych przez pracownika nr ',
              index + 1, ': ', sep='', end='')
        hours[index] = float(input())

    # Pobranie stawki godzinowej.
    pay_rate = float(input('Podaj stawkę godzinową: '))

    # Wyświetlenie wynagrodzenia należnego poszczególnym pracownikom.
    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print('Wynagrodzenie dla pracownika nr ', index + 1,
              format(gross_pay, ' .2f'), ' zł', sep='')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

06. Drop_lowest_score.py 

# Ten program pobiera serię wyników ze sprawdzianów,
# a następnie oblicza średnią po wcześniejszym odrzuceniu
# najniższego wyniku.

def main():
    # Pobranie od użytkownika wyników sprawdzianów.
    scores = get_scores()

    # Obliczenie sumy wszystkich wyników.
    total = get_total(scores)

    # Pobranie najniższego wyniku ze sprawdzianu.
    lowest = min(scores)

    # Odjęcie od obliczonej sumy najniższego wyniku ze sprawdzianu.
    total -= lowest

    # Obliczenie średniej. Zwróć uwagę na podzielenie
    # sumy przez liczbę o jeden mniejszą od liczby wyników,
    # ponieważ został odrzucony najniższy.
    average = total / (len(scores) - 1)

    # Wyświetlenie obliczonej średniej.
    print('Po odrzuceniu najniższego wyniku',
          'średnia wynosi:', average)

# Funkcja get_scores() pobiera od użytkownika serię
# wyników ze sprawdzianów i umieszcza je na liście.
# Wartością zwrotną funkcji jest odwołanie do listy.
def get_scores():
    # Utworzenie pustej listy.
    test_scores = []

    # Utworzenie zmiennej kontrolującej działanie pętli.
    again = 't'

    # Pobranie od użytkownika wyników ze
    # sprawdzianów i umieszczenie ich na liście.
    while again == 't':
        # Pobranie wyniku ze sprawdzianu i umieszczenie go na liście.
        value = float(input('Podaj wynik ze sprawdzianu: '))
        test_scores.append(value)

        # Czy będzie podany kolejny wynik?
        print('Czy chcesz podać kolejny wynik?')
        again = input('Jeśli tak, wpisz t, w przeciwnym razie wpisz inny znak: ')
        print()

    # Zwrot listy.
    return test_scores

# Funkcja get_total() akceptuje argument
# w postaci listy i zwraca wartość całkowitą
# elementów znajdujących się na liście.
def get_total(value_list):
    # Utworzenie zmiennej przeznaczonej do użycia w charakterze akumulatora.
    total = 0.0

    # Obliczenie sumy wszystkich elementów listy.
    for num in value_list:
        total += num

    # Zwrot wartości zmiennej total.
    return total

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

07. In_list.py 	

# Ten program pokazuje przykład
# użycia operatora in wraz z listą.

def main():
    # Utworzenie listy numerów produktów.
    prod_nums = ['V475', 'F987', 'Q143', 'R688']

    # Pobranie szukanego numeru produktu.
    search = input('Podaj numer produktu: ')

    # Ustalenie, czy podany numer produktu znajduje się na liście.
    if search in prod_nums:
        print(search, 'został znaleziony na liście.')
    else:
        print(search, 'nie został znaleziony na liście.')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

08. Index_list.py 	

# Ten program pokazuje, jak pobrać indeks
# elementu listy, a następnie zastąpić go
# nowym elementem.

def main():
    # Utworzenie listy wraz z przykładowymi elementami.
    food = ['pizza', 'burgery', 'chipsy']

    # Wyświetlenie listy.
    print('Oto lista elementów znajdujących się na liście:')
    print(food)

    # Pobranie elementu, który ma zostać zmieniony.
    item = input('Który element powinien zostać zmieniony? ')

    try:
        # Pobranie indeksu elementu listy.
        item_index = food.index(item)

        # Pobranie nowej wartości.
        new_item = input('Podaj nową wartość: ')

        # Zastąpienie starej wartości nową.
        food[item_index] = new_item

        # Wyświetlenie listy.
        print('Oto zmodyfikowana lista:')
        print(food)
    except ValueError:
        print('Podany element nie został znaleziony na liście.')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

09. Insert_list.py 	

# Ten program pokazuje przykład użycia metody insert().

def main():
    # Utworzenie listy wraz z przykładowymi imionami.
    names = ['Jakub', 'Katarzyna', 'Bartosz']

    # Wyświetlenie listy.
    print('Lista przed wstawieniem nowego elementu:')
    print(names)

    # Wstawienie nowego elementu w indeksie 0.
    names.insert(0, 'Janusz')

    # Ponowne wyświetlenie listy.
    print('Lista po wstawieniu nowego elementu:')
    print(names)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

10. Line_graph1.py 	

# Ten program wyświetla prosty wykres liniowy.
import matplotlib.pyplot as plt

def main():
    # Utworzenie list wraz ze współrzędnymi X i Y każdego punktu danych.
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Utworzenie wykresu.
    plt.plot(x_coords, y_coords)

    # Wyświetlenie wykresu.
    plt.show()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

11. Line_graph2.py 	

# Ten program wyświetla prosty wykres liniowy.
import matplotlib.pyplot as plt

def main():
    # Utworzenie list wraz ze współrzędnymi X i Y każdego punktu danych.
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Utworzenie wykresu.
    plt.plot(x_coords, y_coords)

    # Dodanie tytułu.
    plt.title('Przykładowe dane')

    # Dodanie etykiet do osi.
    plt.xlabel('To jest oś X')
    plt.ylabel('To jest oś Y')

    # Dodanie siatki.
    plt.grid(True)

    # Wyświetlenie wykresu.
    plt.show()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

12. Line_graph3.py 

# Ten program wyświetla prosty wykres liniowy.
import matplotlib.pyplot as plt

def main():
    # Utworzenie list wraz ze współrzędnymi X i Y każdego punktu danych.
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Utworzenie wykresu.
    plt.plot(x_coords, y_coords)

    # Dodanie tytułu.
    plt.title('Przykładowe dane')

    # Dodanie etykiet do osi.
    plt.xlabel('To jest oś X')
    plt.ylabel('To jest oś Y')

    # Dodanie siatki.
    plt.grid(True)

    # Wyświetlenie wykresu.
    plt.show()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

13. Line_graph4.py 	

# Ten program wyświetla prosty wykres liniowy.
import matplotlib.pyplot as plt

def main():
    # Utworzenie list wraz ze współrzędnymi X i Y każdego punktu danych.
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Utworzenie wykresu.
    plt.plot(x_coords, y_coords)

    # Dodanie tytułu.
    plt.title('Sprzedaż według roku')

    # Dodanie etykiet do osi.
    plt.xlabel('Rok')
    plt.ylabel('Sprzedaż')

    # Dostosowanie znaczników osi do własnych potrzeb.
    plt.xticks([0, 1, 2, 3, 4],
               ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 1, 2, 3, 4, 5],
               ['0 mln', '1 mln', '2 mln', '3 mln', '4 mln', '5 mln'])

    # Dodanie siatki.
    plt.grid(True)

    # Wyświetlenie wykresu.
    plt.show()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

14. Line_graph5.py 	

# Ten program wyświetla prosty wykres liniowy.
import matplotlib.pyplot as plt

def main():
    # Utworzenie list wraz ze współrzędnymi X i Y każdego punktu danych.
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Utworzenie wykresu.
    plt.plot(x_coords, y_coords, marker='o')

    # Dodanie tytułu.
    plt.title('Sprzedaż według roku')

    # Dodanie etykiet do osi.
    plt.xlabel('Rok')
    plt.ylabel('Sprzedaż')

    # Dostosowanie znaczników osi do własnych potrzeb.
    plt.xticks([0, 1, 2, 3, 4],
               ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 1, 2, 3, 4, 5],
               ['0 mln', '1 mln', '2 mln', '3 mln', '4 mln', '5 mln'])

    # Dodanie siatki.
    plt.grid(True)

    # Wyświetlenie wykresu.
    plt.show()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

15. List_append.py 	

# Ten program pokazuje przykład użycia metody append()
# podczas dodawania nowych elementów do listy.

def main():
    # Najpierw trzeba utworzyć pustą listę.
    name_list = []

    # Utworzenie zmiennej kontrolującej działanie pętli.
    again = 't'

    # Dodanie imion do listy.
    while again == 't':
        # Pobranie imienia od użytkownika.
        name = input('Podaj imię: ')

        # Dodanie elementu do listy.
        name_list.append(name)

        # Czy dodać kolejny element?
        print('Czy chcesz dodać kolejne imię?')
        again = input('Jeśli tak, wpisz t, w przeciwnym razie wpisz inny znak: ')
        print()

    # Wyświetlenie wpisanych imion.
    print('Oto wpisane imiona:')

    for name in name_list:
        print(name)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

16. Pie_chart1.py 	

# Ten program wyświetla prosty wykres kołowy.
import matplotlib.pyplot as plt

def main():
    # Utworzenie listy wartości.
    values = [20, 60, 80, 40]

    # Utworzenie wykresu kołowego na podstawie listy wartości.
    plt.pie(values)

    # Wyświetlenie wykresu kołowego.
    plt.show()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

17. Pie_chart2.py 

# Ten program wyświetla prosty wykres kołowy.
import matplotlib.pyplot as plt

def main():
    # Utworzenie listy wielkości sprzedaży.
    sales = [100, 400, 300, 600]

    # Utworzenie listy etykiet dla poszczególnych części wykresu.
    slice_labels = ['Kwartał 1', 'Kwartał 2', 'Kwartał 3', 'Kwartał 4']

    # Utworzenie wykresu kołowego na podstawie listy wartości.
    plt.pie(sales, labels=slice_labels)

    # Dodanie tytułu.
    plt.title('Sprzedaż według kwartałów')

    # Wyświetlenie wykresu kołowego.
    plt.show()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

18. Random_numbers.py 	

# Ten program umieszcza na liście
# dwuwymiarowej losowo wybrane liczby.
import random

# Stałe określające liczbę wierszy i kolumn.
ROWS = 3
COLS = 4

def main():
    # Utworzenie listy dwuwymiarowej.
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    # Wypełnienie listy losowo wybranymi liczbami.
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1, 100)

    # Wyświetlenie listy.
    print(values)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

19. Read_list.py 

# Ten program odczytuje zawartość pliku i umieszcza ją na liście.

def main():
    # Otworzenie pliku do odczytu.
    infile = open('cities.txt', 'r')

    # Odczytanie zawartości pliku i umieszczenie jej na liście.
    cities = infile.readlines()

    # Zamknięcie pliku.
    infile.close()

    # Usunięcie znaku \n z każdego elementu.
    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1

    # Wyświetlenie zawartości listy.
    print(cities)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

20. Read_number_list.py 

# Ten program odczytuje liczby z pliku i umieszcza je na liście.

def main():
    # Otworzenie pliku do odczytu.
    infile = open('numberlist.txt', 'r')

    # Odczytanie zawartości pliku i umieszczenie jej na liście.
    numbers = infile.readlines()

    # Zamknięcie pliku.
    infile.close()

    # Konwersja każdego elementu na postać liczby całkowitej.
    index = 0
    while index < len(numbers):
        numbers[index] = int(numbers[index])
        index += 1

    # Wyświetlenie zawartości listy.
    print(numbers)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

21. Remove_item.py 

# Ten program pokazuje, jak użyć metody remove()
# do usunięcia elementu z listy.

def main():
    # Utworzenie listy wraz z przykładowymi elementami.
    food = ['pizza', 'burgery', 'chipsy']

    # Wyświetlenie listy.
    print('Oto lista elementów znajdujących się na liście:')
    print(food)

    # Pobranie elementu, który ma zostać zmieniony.
    item = input('Który element powinien zostać usunięty? ')

    try:
        # Usunięcie elementu.
        food.remove(item)

        # Wyświetlenie listy.
        print('Oto zmodyfikowana lista:')
        print(food)

    except ValueError:
        print('Podany element nie został znaleziony na liście.')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

22. Return_list.py 	

# Ten program używa funkcji do utworzenia listy.
# Wartością zwrotną funkcji jest odwołanie do listy.

def main():
    # Pobranie listy wraz z przechowywanymi na niej wartościami.
    numbers = get_values()

    # Wyświetlenie wartości znajdujących się na liście.
    print('Oto wartości znajdujące się na liście:')
    print(numbers)

# Funkcja get_values() pobiera od użytkownika
# serię liczb i umieszcza je na liście. Wartością
# zwrotną funkcji jest odwołanie do listy.
def get_values():
    # Utworzenie pustej listy.
    values = []

    # Utworzenie zmiennej kontrolującej działanie pętli.
    again = 't'

    # Pobranie wartości od użytkownika
    # i umieszczenie ich na liście.
    while again == 't':
        # Pobranie liczby i umieszczenie jej na liście.
        num = int(input('Podaj liczbę: '))
        values.append(num)

        # Czy będzie podana kolejna liczba?
        print('Czy chcesz podać kolejną liczbę?')
        again = input('Jeśli tak, wpisz t, w przeciwnym razie wpisz inny znak: ')
        print()

    # Zwrot listy.
    return values

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

23. Sales_list.py 

# Stała NUM_DAYS przechowuje liczbę dni,
# dla których będą pobierane dane sprzedaży.
NUM_DAYS = 5

def main():
    # Utworzenie listy przechowującej wartość
    # sprzedaży w poszczególnych dniach.
    sales = [0] * NUM_DAYS

    # Utworzenie zmiennej przechowującej indeks.
    index = 0

    print('Podaj wartość sprzedaży w poszczególnych dniach.')

    # Pobranie wartości sprzedaży dla każdego dnia.
    while index < NUM_DAYS:
        print('Dzień nr ', index + 1, ': ', sep='', end='')
        sales[index] = float(input())
        index += 1

    # Wyświetlenie podanych wartości.
    print('Oto podane wartości:')
    for value in sales:
        print(value)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

24. Total_function.py 

# Ten program używa funkcji do obliczenia
# sumy wartości elementów listy.

def main():
    # Utworzenie listy.
    numbers = [2, 4, 6, 8, 10]

    # Wyświetlenie sumy wszystkich elementów listy.
    print('Suma wartości elementów listy wynosi', get_total(numbers))

# Funkcja get_total() akceptuje argument
# w postaci listy i zwraca sumę wartości
# wszystkich jej elementów.
def get_total(value_list):
    # Utworzenie zmiennej przeznaczonej do użycia w charakterze akumulatora.
    total = 0

    # Obliczenie sumy wszystkich elementów listy.
    for num in value_list:
        total += num

    # Zwrot wartości zmiennej total.
    return total

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

25. Total_list.py 	

# Ten program oblicza sumę
# wartości wszystkich elementów listy.

def main():
    # Utworzenie listy.
    numbers = [2, 4, 6, 8, 10]

    # Utworzenie zmiennej przeznaczonej do użycia w charakterze akumulatora.
    total = 0

    # Obliczenie sumy wartości wszystkich elementów listy.
    for value in numbers:
        total += value

    # Wyświetlenie obliczonej sumy.
    print('Suma wartości wszystkich elementów listy wynosi', total)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

26. Write_list.py 	

# Ten program zapisuje listę ciągów tekstowych w pliku

def main():
    # Utworzenie listy ciągów tekstowych.
    cities = ['Nowy Jork', 'Boston', 'Atlanta', 'Dallas']

    # Otworzenie pliku do odczytu.
    outfile = open('cities.txt', 'w')

    # Zapisanie listy w pliku.
    for item in cities:
        outfile.write(item + '\n')

    # Zamknięcie pliku.
    outfile.close()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

27. Write_number_list.py 	

# Ten program zapisuje w pliku listę liczb.

def main():
    # Utworzenie listy liczb.
    numbers = [1, 2, 3, 4, 5, 6, 7]

    # Otworzenie pliku do odczytu.
    outfile = open('numberlist.txt', 'w')

    # Zapisanie listy w pliku.
    for item in numbers:
        outfile.write(str(item) + '\n')

    # Zamknięcie pliku.
    outfile.close()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

28. Write_lines.py

# Ten program używa metody writelines() do
# zapisania w pliku listy ciągów tekstowych.

def main():
    # Utworzenie listy ciągów tekstowych.
    cities = ['Nowy Jork', 'Boston', 'Atlanta', 'Dallas']

    # Otworzenie pliku do odczytu.
    outfile = open('cities.txt', 'w')

    # Zapisanie listy w pliku.
    outfile.writelines(cities)

    # Zamknięcie pliku.
    outfile.close()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------
