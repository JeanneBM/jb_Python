01. Apostrophe.py

print("Nie obawiaj się użycia znaku ' w tekście.")
print("Apostrof ' w tekście.")

------------------------------------------------------------------------------------------------------------------------------------------

02. Columns.py

# Ten program wyświetla poniższe liczby
# zmiennoprzecinkowe w kolumnie wyrównane
# według położenia przecinka dziesiętnego.
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

# Wyświetlenie w polu o szerokości siedmiu znaków
# wszystkich liczb wraz z dwoma cyframi po przecinku dziesiętnym.
print(format(num1, '7.2f'))
print(format(num2, '7.2f'))
print(format(num3, '7.2f'))
print(format(num4, '7.2f'))
print(format(num5, '7.2f'))
print(format(num6, '7.2f'))

------------------------------------------------------------------------------------------------------------------------------------------

03. Comment1.py
  
# Ten program wyświetla imię
# i nazwisko osoby oraz jej adres.
print('Jan Kowalski')
print('ul. Ogrodowa 123')
print('44-100 Gliwice')

------------------------------------------------------------------------------------------------------------------------------------------

04. Comment2.py
  
print('Jan Kowalski')       # Wyświetlenie imienia i nazwiska.
print('ul. Ogrodowa 123')   # Wyświetlenie adresu.
print('44-100 Gliwice')     # Wyświetlenie kodu pocztowego i miejscowości.

------------------------------------------------------------------------------------------------------------------------------------------

05. Display_quote.py

print('Twoje zadanie na jutro to przeczytanie "Hamleta".')

------------------------------------------------------------------------------------------------------------------------------------------

06. Dollar_display.py 

# Ten program pokazuje, jak liczba zmiennoprzecinkowa
# może zostać sformatowana jako wartość pieniężna.
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print('Opłata roczna wynosi',
      format(annual_pay, ',.2f'),
      'zł.', sep='')
      
------------------------------------------------------------------------------------------------------------------------------------------

07. Double_quotes.py

print("Jan Kowalski")
print("ul. Ogrodowa 123")
print("44-100 Gliwice")

------------------------------------------------------------------------------------------------------------------------------------------

08. Formatting.py 	

# Ten program pokazuje sposób wyświetlenia
# liczby zmiennoprzecinkowej wraz z formatowaniem.
amount_due = 5000.0
monthly_payment = amount_due / 12
print('Miesięczna rata wynosi', format(monthly_payment, '.2f'))

------------------------------------------------------------------------------------------------------------------------------------------

09. Future_value.py 

# Pobranie kwoty końcowej, która ma zostać zebrana na rachunku.
future_value = float(input('Podaj kwotę, jaką chcesz uzyskać na rachunku: '))

# Pobranie stopy rocznego oprocentowania rachunku.
rate = float(input('Podaj stopę oprocentowania rachunku: '))

# Pobranie liczby lat, przez które pieniądze mają być ulokowane na rachunku.
years = int(input('Przez ile lat chcesz trzymać pieniądze na rachunku? '))

# Obliczenie kwoty, którą trzeba przelać na rachunek.
present_value = future_value / (1.0 + rate)**years

# Wyświetlenie kwoty, którą trzeba przelać na rachunek.
print('Musisz przelać na rachunek', present_value, 'zł.')

------------------------------------------------------------------------------------------------------------------------------------------

10. Input.py 	

# Pobranie imienia, wieku i dochodu użytkownika.
name = input('Jak masz na imię? ')
age = int(input('Ile masz lat? '))
income = float(input('Ile zarabiasz? '))

# Wyświetlenie danych.
print('Oto wprowadzone przez Ciebie dane.')
print('Imię:', name)
print('Wiek:', age)
print('Dochód:', income)

------------------------------------------------------------------------------------------------------------------------------------------

11. No_formatting.py 	

# Ten program pokazuje sposób wyświetlenia
# liczby zmiennoprzecinkowej bez formatowania.
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print('Miesięczna rata wynosi', monthly_payment)

------------------------------------------------------------------------------------------------------------------------------------------

12. ORION.py 	

# Ten program wyświetla wybrane gwiazdy gwiazdozbioru Oriona,
# ich nazwy oraz łączące je linie.
import turtle

# Określenie wielkości okna.
turtle.setup(500, 600)

# Konfiguracja żółwia.
turtle.penup()
turtle.hideturtle()

# Utworzenie stałych nazwanych dla współrzędnych gwiazd.
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# Narysowanie gwiazd.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)      # Lewe kolano.
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)    # Prawe kolano.
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)      # Gwiazda po lewej stronie pasa.
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)  # Gwiazda pośrodku pasa.
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)    # Gwiazda po prawej stronie pasa.
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)              # Lewe kolano.
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)            # Prawe kolano.
turtle.dot()

# Wyświetlenie nazw gwiazd
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)      # Lewe kolano.
turtle.write('Betegeuse')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)    # Prawe kolano.
turtle.write('Meissa')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)      # Gwiazda po lewej stronie pasa.
turtle.write('Alnitak')
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)  # Gwiazda pośrodku pasa.
turtle.write('Alnilam')
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)    # Gwiazda po prawej stronie pasa.
turtle.write('Mintaka')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)              # Lewe kolano.
turtle.write('Saiph')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)            # Prawe kolano.
turtle.write('Rigel')

# Narysowanie linii od lewego ramienia do gwiazdy po lewej stronie pasa.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()

# Narysowanie linii od prawego ramienia do gwiazdy po prawej stronie pasa.
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

# Narysowanie linii między gwiazdami po lewej stronie i pośrodku pasa.
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.penup()

# Narysowanie linii między gwiazdami pośrodku i po prawej stronie pasa.
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

# Narysowanie linii od gwiazdy po lewej stronie pasa do lewego kolana.
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

# Narysowanie linii od gwiazdy po prawej stronie pasa do prawego kolana.
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)

# Pozostawienie otwartego okna. (To nie jest konieczne podczas użycia IDLE).
turtle.done()

------------------------------------------------------------------------------------------------------------------------------------------

13. Output.py 	

print('Jan Kowalski')
print('ul. Ogrodowa 123')
print('44-100 Gliwice')

------------------------------------------------------------------------------------------------------------------------------------------

14. Sale_price.py 	

# Ten program pobiera cenę detaliczną artykułu
# i oblicza cenę sprzedaży uwzględniającą 20% rabat.

# Pobranie ceny detalicznej artykułu.
original_price = float(input("Podaj cenę detaliczną artykułu: "))

# Obliczenie wysokości rabatu.
discount = original_price * 0.2

# Obliczenie ceny sprzedaży.
sale_price = original_price - discount

# Wyświetlenie ceny sprzedaży.
print('Cena sprzedaży wynosi', sale_price)

------------------------------------------------------------------------------------------------------------------------------------------

15. Simple_math.py 

# Przypisanie wartości zmiennej salary.
salary = 2500.0

# Przypisanie wartości zmiennej bonus.
bonus = 1200.0

# Obliczenie wynagrodzenia przez dodanie wartości zmiennych
# salary i bonus. Wynik zostaje przypisany zmiennej pay.
pay = salary + bonus

# Wyświetlenie wynagrodzenia.
print('Twoje wynagrodzenie wynosi', pay)

------------------------------------------------------------------------------------------------------------------------------------------

16. String_input.py 	

# Pobranie imienia użytkownika.
first_name = input('Podaj imię: ')

# Pobranie nazwiska użytkownika.
last_name = input('Podaj nazwisko: ')

# Wyświetlenie komunikatu powitania.
print('Witaj,', first_name, last_name)

------------------------------------------------------------------------------------------------------------------------------------------

17. String_Variable.py 	

# Utworzenie dwóch zmiennych przechowujących ciągi tekstowe.
first_name = 'Jan'
last_name = 'Kowalski'

# Wyświetlenie wartości obu zmiennych.
print(first_name, last_name)

------------------------------------------------------------------------------------------------------------------------------------------

18. Test_score_average.py 	

# Pobranie wyników trzech sprawdzanów i umieszczenie
# ich w zmiennych o nazwach test1, test2 i test3.
test1 = float(input('Podaj wynik z pierwszego sprawdzianu: '))
test2 = float(input('Podaj wynik z drugiego sprawdzianu: '))
test3 = float(input('Podaj wynik z trzeciego sprawdzianu: '))

# Obliczenie średniej trzech wyników i przypisanie
# wartości średniej do zmiennej average.
average = (test1 + test2 + test3) / 3.0

# Wyświetlenie wartości średniej.
print('Twój średni wynik wynosi', average)

------------------------------------------------------------------------------------------------------------------------------------------

19. Time_converter.py 	

# Pobranie od użytkownika całkowitej liczby sekund.
total_seconds = float(input('Podaj liczbę sekund: '))

# Obliczenie liczby godzin.
hours = total_seconds // 3600.

# Obliczenie liczby pozostałych minut.
minutes = (total_seconds // 60) % 60

# Obliczenie liczby pozostałych sekund.
seconds = total_seconds % 60

# Wyświetlenie wyniku.
print('Podana liczba sekund wyrażona w godzinach, minutach i sekundach:')
print('Godziny:', hours)
print('Minuty:', minutes)
print('Sekundy:', seconds)

------------------------------------------------------------------------------------------------------------------------------------------

20. Variable_demo.py 	

# Ten program pokazuje przykład zmiennej.
room = 503
print('Zatrzymam się w pokoju numer')
print(room)

------------------------------------------------------------------------------------------------------------------------------------------

21. Variable_demo2.py 	

# Utworzenie dwóch zmiennych: top_speed i distance.
top_speed = 160
distance = 300

# Wyświetlenie wartości przechowywanych przez te zmienne.
print('Szybkość maksymalna wynosi')
print(top_speed)
print('Pokonana odległość to')
print(distance)

------------------------------------------------------------------------------------------------------------------------------------------

22. Variable_demo3.py 	

# Ten program pokazuje przykład zmiennej.
room = 503
print('Zatrzymam się w pokoju numer', room)

------------------------------------------------------------------------------------------------------------------------------------------

23. Variable_demo4.py

# Ten program pokazuje ponowne przypisanie zmiennej.
# Wartość jest przypisywana zmiennej dollars.
dollars = 2.75
print('Mam na koncie', dollars, 'dolarów.')

# Ponowne przypisanie zmiennej, która
# teraz odwołuje się do innej wartości.
dollars = 99.95
print('A teraz mam na koncie', dollars, 'dolarów.')

------------------------------------------------------------------------------------------------------------------------------------------
