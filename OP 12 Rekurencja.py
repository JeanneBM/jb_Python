01. Endless_recursion.py 	

# Ten program zawiera funkcję rekurencyjną.

def main():
    message()

def message():
    print('To jest funkcja rekurencyjna.')
    message()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

02. Recursive1.py 	

# Ten program zawiera funkcję rekurencyjną.

def main():
    # Przekazanie funkcji message() argumentu
    # w postaci liczby całkowitej 5 powoduje,
    # że zostanie ona wywołana pięciokrotnie.
    message(5)

def message(times):
    if times > 0:
        print('To jest funkcja rekurencyjna.')
        message(times - 1)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

03. Recursive2.py 	

# Ten program używa rekurencji
# do obliczenia silni.

def main():
    # Pobranie liczby od użytkownika.
    number = int(input('Podaj nieujemną liczbę całkowitą: '))

    # Obliczenie silni podanej liczby.
    fact = factorial(number)

    # Wyświetlenie obliczonej silni.
    print('Silnia liczby', number, 'wynosi', fact)

# Funkcja factorial() używa rekurencji do obliczenia
# silni liczby przekazanej jej jako argument. Zakładamy,
# że argument jest liczbą nieujemną.
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

04. Recursive3.py 

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

----------------------------------------------------------------------------------------------------------------------------------------------

05. Gcd.py 	

# Ten program używa rekurencji do wyznaczenia
# największego wspólnego dzielnika dwóch liczb.

def main():
    # Pobranie dwóch liczb.
    num1 = int(input('Podaj pierwszą liczbę całkowitą: '))
    num2 = int(input('Podaj drugą liczbę całkowitą: '))

    # Wyświetlenie największego wspólnego dzielnika.
    print('Największy wspólny dzielnik tych')
    print('dwóch liczb wynosi', gcd(num1, num2))

# Funkcja gcd() zwraca największy wspólny
# dzielnik dwóch podanych liczb całkowitych.
def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(x, x % y)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

06. Fibbonacci.py 	

# Ten program używa rekurencji do
# wyświetlenia liczb ciągu Fibonacciego.

def main():
    print('10 pierwszych liczb')
    print('ciągu Fibonacciego to:')

    for number in range(1, 11):
        print(fib(number))

# Funkcja fib() zwraca n-tą liczbę
# ciągu Fibonacciego.
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

07. Towers_of_Hanoi.py

# Ten program symuluje grę „Wieże Hanoi”.

def main():
    # Zdefiniowanie pewnych wartości początkowych.
    num_discs = 3
    from_peg = 1
    to_peg = 3
    temp_peg = 2

    # Symulacja gry.
    move_discs(num_discs, from_peg, to_peg, temp_peg)
    print('Wszystkie krążki zostały przeniesione!')

# Funkcja moveDiscs() wyświetla ruch, który
# należy wykonać w grze „Wieże Hanoi”.
# Parametry funkcji są następujące:
#    num:        liczba krążków do przeniesienia,
#    from_peg:   słupek, z którego należy zdjąć krążek,
#    to_peg:     słupek, na którym należy umieścić krążek,
#    temp_peg:   słupek tymczasowy.
def move_discs(num, from_peg, to_peg, temp_peg):
    if num > 0:
        move_discs(num - 1, from_peg, temp_peg, to_peg)
        print('Przeniesienie krążka ze słupka', from_peg, '. na słupek', to_peg)
        move_discs(num - 1, temp_peg, to_peg, from_peg)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

