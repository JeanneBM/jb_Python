01. Add_coffee_record.py

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

----------------------------------------------------------------------------------------------------------------------------------------------

02. Delete_coffee_record.py
  
# Ten program pozwala użytkownikowi
# na usunięcie rekordu w pliku coffee.txt.

import os  # To polecenie jest niezbędne do wywołania funkcji remove() i rename().

def main():
    # Utworzenie zmiennej boolowskiej do użycia jako flagi.
    found = False

    # Pobranie kawy przeznaczonej do usunięcia.
    search = input('Podaj nazwę kawy, którą chcesz usunąć: ')

    # Otworzenie pierwotnego pliku coffee.txt.
    coffee_file = open('coffee.txt', 'r')

    # Otworzenie pliku tymczasowego.
    temp_file = open('temp.txt', 'w')

    # Odczytanie pola opisu pierwszego rekordu.
    descr = coffee_file.readline()

    # Odczytanie pozostałej części pliku.
    while descr != '':
        # Odczytanie pola ilości.
        qty = float(coffee_file.readline())

        # Usunięcie sekwencji \n z opisu.
        descr = descr.rstrip('\n')

        # Jeżeli to nie jest rekord przeznaczony do usunięcia,
        # zapisz go w pliku tymczasowym.
        if descr != search:
            # Zapisanie rekordu w pliku tymczasowym.
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')
        else:
            # Przypisanie wartości True zmiennej found.
            found = True

        # Odczytanie pola opisu następnego rekordu.
        descr = coffee_file.readline()

    # Zamknięcie plików pierwotnego i tymczasowego.
    coffee_file.close()
    temp_file.close()

    # Usunięcie pierwotnego pliku coffee.txt.
    os.remove('coffee.txt')

    # Zmiana nazwy pliku tymczasowego.
    os.rename('temp.txt', 'coffee.txt')

    # Jeżeli szukana wartość nie została znaleziona
    # w pliku, należy wyświetlić odpowiedni komunikat.
    if found:
        print('Plik został uaktualniony.')
    else:
        print('Szukana kawa nie została znaleziona w pliku.')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

03. Display_file.py 	

# Ten program wyświetla
# zawartość pliku.

def main():
    # Pobranie nazwy pliku.
    filename = input('Podaj nazwę pliku: ')

    # Otworzenie pliku.
    infile = open(filename, 'r')

    # Odczytanie zawartości pliku.
    contents = infile.read()

    # Wyświetlenie zawartości pliku.
    print(contents)

    # Zamknięcie pliku.
    infile.close()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

04. Display_file2.py 	

# Ten program wyświetla
# zawartość pliku.

def main():
    # Pobranie nazwy pliku.
    filename = input('Podaj nazwę pliku: ')

    try:
        # Otworzenie pliku.
        infile = open(filename, 'r')

        # Odczytanie zawartości pliku.
        contents = infile.read()

        # Wyświetlenie zawartości pliku.
        print(contents)

        # Zamknięcie pliku.
        infile.close()
    except IOError:
        print('Wystąpił błąd podczas próby odczytania')
        print('pliku o nazwie', filename)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

05. Division1.py 

# Ten program dzieli jedną liczbę przez drugą.

def main():
    # Pobranie dwóch liczb.
    num1 = int(input('Podaj liczbę: '))
    num2 = int(input('Podaj następną liczbę: '))

    # Podzielenie liczby num1 przez num2 i wyświetlenie wyniku.
    result = num1 / num2
    print(num1, 'dzielone przez', num2, 'daje', result)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

06. Division2.py 	

# Ten program dzieli jedną liczbę przez drugą.

def main():
    # Pobranie dwóch liczb.
    num1 = int(input('Podaj liczbę : '))
    num2 = int(input('Podaj następną liczbę: '))

    # Jeżeli wartość num2 jest inna niż 0, następuje
    # podzielenie num1 przez num2 i wyświetlenie wyniku.
    if num2 != 0:
        result = num1 / num2
        print(num1, 'dzielone przez', num2, 'daje', result)
    else:
        print('Nie można dzielić przez zero.')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

07. File_read.py 	

# Ten program odczytuje i wyświetla
# zawartość pliku philosophers.txt.
def main():
    # Otworzenie pliku o nazwie philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Odczytanie zawartości pliku.
    file_contents = infile.read()

    # Zamknięcie pliku.
    infile.close()

    # Wyświetlenie danych
    # wczytanych do pamięci.
    print(file_contents)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

08. File_write.py 	

# Ten program zapisuje w pliku
# trzy wiersze danych.
def main():
    # Otworzenie pliku o nazwie philosophers.txt.
    outfile = open('philosophers.txt', 'w')

    # Zapisanie w pliku informacji
    # o trzech sławnych filozofach.
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # Zamknięcie pliku.
    outfile.close()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

09. Gross_pay.py 	

# Ten program oblicza wynagrodzenie pracownika.

def main():
    # Pobranie liczby przepracowanych godzin.
    hours = int(input('Podaj liczbę przepracowanych godzin: '))

    # Pobranie stawki godzinowej.
    pay_rate = float(input('Podaj stawkę godzinową: '))

    # Obliczenie należnego wynagrodzenia.
    gross_pay = hours * pay_rate

    # Wyświetlenie obliczonego wynagrodzenia.
    print('Wynagrodzenie wynosi ', format(gross_pay, '.2f'), ' zł', sep='')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

10. Gross_pay2.py 	

# Ten program oblicza wynagrodzenie pracownika.

def main():
    try:
        # Pobranie liczby przepracowanych godzin.
        hours = int(input('Podaj liczbę przepracowanych godzin: '))

        # Pobranie stawki godzinowej.
        pay_rate = float(input('Podaj stawkę godzinową: '))

        # Obliczenie należnego wynagrodzenia.
        gross_pay = hours * pay_rate

        # Wyświetlenie obliczonego wynagrodzenia.
        print('Wynagrodzenie wynosi ', format(gross_pay, '.2f'), ' zł', sep='')
    except ValueError:
        print('BŁĄD: Liczba przepracowanych godzin i stawka godzinowa')
        print('muszą być wartościami liczbowymi.')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

11. Gross_pay3.py 	

# Ten program oblicza wynagrodzenie pracownika.

def main():
    try:
        # Pobranie liczby przepracowanych godzin.
        hours = int(input('Podaj liczbę przepracowanych godzin: '))

        # Pobranie stawki godzinowej.
        pay_rate = float(input('Podaj stawkę godzinową: '))

        # Obliczenie należnego wynagrodzenia.
        gross_pay = hours * pay_rate

        # Wyświetlenie obliczonego wynagrodzenia.
        print('Wynagrodzenie wynosi ', format(gross_pay, '.2f'), ' zł', sep='')
    except ValueError as err:
        print(err)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

12. Line_read.py 

# Ten program odczytuje zawartość pliku
# philosophers.txt wiersz po wierszu.
def main():
    # Otworzenie pliku o nazwie philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Odczyt trzech wierszy z pliku.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Zamknięcie pliku.
    infile.close()

    # Wyświetlenie danych
    # wczytanych do pamięci.
    print(line1)
    print(line2)
    print(line3)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

13. Modify_coffee_records.py 	

# Ten program pozwala użytkownikowi na zmodyfikowanie
# wartości pola Ilość w rekordzie w pliku coffee.txt.

import os  # To polecenie jest niezbędne do wywołania funkcji remove() i rename().

def main():
    # Utworzenie zmiennej boolowskiej do użycia jako flagi.
    found = False

    # Pobranie szukanej wartości i nowej wartości pola Ilość.
    search = input('Podaj nazwę kawy, której szukasz: ')
    new_qty = int(input('Podaj nową wartość pola Ilość: '))

    # Otworzenie pierwotnego pliku coffee.txt.
    coffee_file = open('coffee.txt', 'r')

    # Otworzenie pliku tymczasowego.
    temp_file = open('temp.txt', 'w')

    # Odczytanie pola opisu pierwszego rekordu.
    descr = coffee_file.readline()

    # Odczytanie pozostałej części pliku.
    while descr != '':
        # Odczytanie pola ilości.
        qty = float(coffee_file.readline())

        # Usunięcie sekwencji \n z opisu.
        descr = descr.rstrip('\n')

        # Zapisanie w pliku tymczasowym,
        # tego rekordu lub nowego, jeśli dany
        # rekord ma zostać zmodyfikowany.
        if descr == search:
            # Zapisanie zmodyfikowanego rekordu w pliku tymczasowym.
            temp_file.write(descr + '\n')
            temp_file.write(str(new_qty) + '\n')

            # Przypisanie wartości True zmiennej found.
            found = True
        else:
            # Zapisanie pierwotnego rekordu w pliku tymczasowym.
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')

        # Odczytanie pola opisu następnego rekordu.
        descr = coffee_file.readline()

    # Zamknięcie plików pierwotnego i tymczasowego.
    coffee_file.close()
    temp_file.close()

    # Usunięcie pierwotnego pliku coffee.txt.
    os.remove('coffee.txt')

    # Zmiana nazwy pliku tymczasowego.
    os.rename('temp.txt', 'coffee.txt')

    # Jeżeli szukana wartość nie została znaleziona
    # w pliku, należy wyświetlić odpowiedni komunikat.
    if found:
        print('Plik został uaktualniony.')
    else:
        print('Szukana kawa nie została znaleziona w pliku.')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

14. Read_emp_records.py 	

# Ten program wyświetla rekordy
# zapisane w pliku employees.txt.

def main():
    # Otworzenie pliku employees.txt.
    emp_file = open('employees.txt', 'r')

    # Odczyt z pliku pierwszego wiersza, którym
    # jest pole imienia i nazwiska w pierwszym rekordzie.
    name = emp_file.readline()

    # Jeżeli pole zostało odczytane, należy kontynuować przetwarzanie.
    while name != '':
        # Odczytanie pola numeru identyfikacyjnego.
        id_num = emp_file.readline()

        # Odczytanie pola działu, w którym jest zatrudniony pracownik.
        dept = emp_file.readline()

        # Pozbycie się z pól znaków nowego wiersza.
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        # Wyświetlenie rekordu.
        print('Imię i nazwisko:', name)
        print('ID:', id_num)
        print('Dział:', dept)
        print()

        # Odczytanie pola imienia i nazwiska następnego rekordu.
        name = emp_file.readline()

    # Zamknięcie pliku.
    emp_file.close()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

15. Read_numbers.py 	

# Ten program pokazuje, jak liczby odczytane z pliku muszą
# zostać skonwertowane z ciągu tekstowego, zanim będą
# mogły być użyte w operacjach matematycznych.

def main():
    # Otworzenie pliku do odczytu.
    infile = open('numbers.txt', 'r')

    # Odczytanie trzech liczb z pliku.
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    # Zamknięcie pliku.
    infile.close()

    # Dodanie trzech odczytanych liczb.
    total = num1 + num2 + num3

    # Wyświetlenie liczb i ich sumy.
    print('Odczytane liczby to:', num1, num2, num3)
    print('Suma liczb wynosi:', total)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

16. Read_running_times.py 

# Ten program odczytuje wartości z pliku
# video_times.txt i oblicza ich sumę.

def main():
    # Otworzenie pliku video_times.txt do odczytu.
    video_file = open('video_times.txt', 'r')

    # Inicjalizacja akumulatora wraz z wartością 0.0.
    total = 0.0

    # Inicjalizacja zmiennej przeznaczonej do przechowywania liczby ujęć.
    count = 0

    print('Oto czasy trwania poszczególnych ujęć:')

    # Pobranie wartości z pliku i obliczenie ich sumy.
    for line in video_file:
        # Konwersja wiersza na postać wartości typu float.
        run_time = float(line)

        # Dodanie 1 do wartości zmiennej count.
        count += 1

        # Wyświetlenie czasu trwania ujęcia.
        print('Ujęcie nr ', count, ': ', run_time, sep='')

        # Dodanie czasu trwania do zmiennej total.
        total += run_time

    # Zamknięcie pliku.
    video_file.close()

    # Wyświetlenie całkowitego czasu trwania reklamy.
    print('Całkowity czas trwania reklamy wynosi', total, 'sekund.')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

17. Read_sales.py 

# Ten program odczytuje wszystkie
# wartości zapisane w pliku sales.txt.

def main():
    # Otworzenie pliku sales.txt do odczytu.
    sales_file = open('sales.txt', 'r')

    # Odczytanie pierwszego wiersza z pliku, ale jeszcze
    # nie będzie skonwertowany na liczbę. Wciąż trzeba
    # sprawdzić, czy wartość to pusty ciąg tekstowy.
    line = sales_file.readline()

    # Jeżeli metoda readline() nie zwróciła pustego ciągu
    # tekstowego, można kontynuować przetwarzanie danych.
    while line != '':
        # Konwersja wiersza na postać wartości typu float.
        amount = float(line)

        # Sformatowanie i wyświetlenie wartości liczbowej.
        print(format(amount, '.2f'))

        # Odczytanie następnego wiersza z pliku.
        line = sales_file.readline()

    # Zamknięcie pliku.
    sales_file.close()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

18. Read_sales2.py 	

# Ten program używa pętli for do odczytania
# wszystkich wartości zapisanych w pliku sales.txt.

def main():
    # Otworzenie pliku sales.txt do odczytu.
    sales_file = open('sales.txt', 'r')

    # Odczytanie wszystkich wierszy z pliku.
    for line in sales_file:
        # Konwersja wiersza na postać wartości typu float.
        amount = float(line)
        # Sformatowanie i wyświetlenie wartości liczbowej.
        print(format(amount, '.2f'))

    # Zamknięcie pliku.
    sales_file.close()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

19. Sales_report.py 	

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

----------------------------------------------------------------------------------------------------------------------------------------------

20. Sales_report2.py 	

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
    except:
        print('Wystąpił błąd.')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

21. Sales_report3.py 	

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
    except Exception as err:
        print(err)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

22. Sales_report4.py

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
    except Exception as err:
        print(err)
    else:
        # Wyświetlenie obliczonej sumy.
        print(format(total, '.2f'))

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

23. Save_emp_records.py 	

# Ten program pobiera od użytkownika dane pracownika,
# a następnie zapisuje rekordy w pliku employee.txt.

def main():
    # Pobranie liczby rekordów, które mają być utworzone.
    num_emps = int(input('Podaj liczbę rekordów, ' +
                         'które mają zostać utworzone: '))

    # Otworzenie pliku do zapisu.
    emp_file = open('employees.txt', 'w')

    # Pobranie danych o poszczególnych
    # pracownikach i zapisanie ich w pliku.
    for count in range(1, num_emps + 1):
        # Pobranie danych o pracowniku.
        print('Podaj dane o pracowniku nr ', count, sep='')
        name = input('Imię i nazwisko:')
        id_num = input('Numer identyfikacyjny: ')
        dept = input('Dział: ')

        # Zapisanie danych jako rekordu w pliku.
        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

        # Wyświetlenie pustego wiersza.
        print()

    # Zamknięcie pliku.
    emp_file.close()
    print('Rekordy pracowników zostały zapisane w pliku employees.txt.')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

24. Search_coffee_records.py 

# Ten program pozwala użytkownikowi na
# wyszukiwanie w pliku coffee.txt rekordów
# dopasowanych do opisu.

def main():
    # Utworzenie zmiennej boolowskiej do użycia jako flagi.
    found = False

    # Pobranie szukanej wartości.
    search = input('Podaj nazwę kawy, której szukasz: ')

    # Otworzenie pliku coffee.txt.
    coffee_file = open('coffee.txt', 'r')

    # Odczytanie pola opisu pierwszego rekordu.
    descr = coffee_file.readline()

    # Odczytanie pozostałej części pliku.
    while descr != '':
        # Odczytanie pola ilości.
        qty = float(coffee_file.readline())

        # Usunięcie sekwencji \n z opisu.
        descr = descr.rstrip('\n')

        # Ustalenie, czy rekord został dopasowany
        # do szukanej wartości.
        if descr == search:
            # Wyświetlenie rekordu.
            print('Opis:', descr)
            print('Ilość:', qty)
            print()
            # Przypisanie wartości True zmiennej found.
            found = True

        # Odczytanie pola opisu następnego rekordu.
        descr = coffee_file.readline()

    # Zamknięcie pliku.
    coffee_file.close()

    # Jeżeli szukana wartość nie została znaleziona
    # w pliku, należy wyświetlić odpowiedni komunikat.
    if not found:
        print('Szukana kawa nie została znaleziona w pliku.')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

25. Show_coffee_record.py 	

# Ten program wyświetla rekordy
# zapisane w pliku coffee.txt.

def main():
    # Otworzenie pliku coffee.txt.
    coffee_file = open('coffee.txt', 'r')

    # Odczytanie pola opisu pierwszego rekordu.
    descr = coffee_file.readline()

    # Odczytanie pozostałej części pliku.
    while descr != '':
        # Odczytanie pola ilości.
        qty = float(coffee_file.readline())

        # Usunięcie sekwencji \n z opisu.
        descr = descr.rstrip('\n')

        # Wyświetlenie rekordu.
        print('Opis:', descr)
        print('Ilość:', qty)

        # Odczytanie pola opisu następnego rekordu.
        descr = coffee_file.readline()

    # Zamknięcie pliku.
    coffee_file.close()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

26. Strip_newline.py 

# Ten program odczytuje zawartość pliku
# philosophers.txt wiersz po wierszu.
def main():
    # Otworzenie pliku o nazwie philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Odczyt trzech wierszy z pliku.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Usunięcie sekwencji \n z każdego ciągu tekstowego.
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    # Zamknięcie pliku.
    infile.close()

    # Wyświetlenie danych
    # wczytanych do pamięci.
    print(line1)
    print(line2)
    print(line3)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

27. Write_names.py 

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

----------------------------------------------------------------------------------------------------------------------------------------------

28. Write_numbers.py 	

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

----------------------------------------------------------------------------------------------------------------------------------------------

29. Write_sales.py

# Ten program prosi użytkownika o podanie wartości sprzedaży,
# a następnie zapisuje te informacje w pliku sales.txt.

def main():
    # Pobranie liczby dni.
    num_days = int(input('Z ilu dni chcesz ' +
                         'podać dane? '))

    # Otworzenie nowego pliku o nazwie sales.txt.
    sales_file = open('sales.txt', 'w')

    # Pobranie wartości sprzedaży dla poszczególnych dni
    # i zapisanie tych danych w pliku.
    for count in range(1, num_days + 1):
        # Pobranie wartości sprzedaży dla danego dnia.
        sales = float(input('Podaj wartość sprzedaży w dniu nr ' +
                            str(count) + ': '))

        # Zapisanie informacji w pliku.
        sales_file.write(str(sales) + '\n')

    # Zamknięcie pliku.
    sales_file.close()
    print('Dane zostały zapisane w pliku sales.txt.')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------
