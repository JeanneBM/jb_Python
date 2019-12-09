01. COMMISSION.py 

# Ten program oblicza wysokość premii ze sprzedaży.

# Utworzenie zmiennej kontrolującej działanie pętli.
keep_going = 't'

# Obliczenie serii premii.
while keep_going == 't':
    # Pobranie wielkości sprzedaży i premii.
    sales = float(input('Podaj wielkość sprzedaży: '))
    comm_rate = float(input('Podaj wysokość premii: '))

    # Obliczenie premii.
    commission = sales * comm_rate

    # Wyświetlenie premii.
    print('Premia wynosi ',
          format(commission, '.2f'), ' zł.', sep='')

    # Czy użytkownik chce obliczyć kolejną premię?
    keep_going = input('Czy chcesz obliczyć kolejną ' +
                       'premię? (Jeśli tak, wpisz t): ')

--------------------------------------------------------------------------------------------------------------------------------------------

02. CONCENTRIC_CIRCLES.py 	

# Ten program rysuje zagnieżdżone okręgi.
import turtle

# Stałe nazwane.
NUM_CIRCLES = 20
STARTING_RADIUS = 20
OFFSET = 10
ANIMATION_SPEED = 0

# Konfiguracja żółwia.
turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

# Określenie promienia pierwszego okręgu.
radius = STARTING_RADIUS

# Narysowanie okręgów.
for count in range(NUM_CIRCLES):
    # Narysowanie okręgu.
    turtle.circle(radius)

    # Pobranie współrzędnych następnego okręgu.
    x = turtle.xcor()
    y = turtle.ycor() - OFFSET

    # Określenie promienia następnego okręgu.
    radius = radius + OFFSET

    # Umieszczenie żółwia w położeniu do narysowania następnego okręgu.
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

--------------------------------------------------------------------------------------------------------------------------------------------

03. Gross_pay.py 	

# Ten program oblicza i wyświetla wynagrodzenie.
# Pobranie liczby przepracowanych godzin.
hours = int(input('Podaj liczbę godzin przepracowanych w tym tygodniu: '))

# Pobranie stawki godzinowej.
pay_rate = float(input('Podaj stawkę godzinową: '))

# Obliczenie wynagrodzenia.
gross_pay = hours * pay_rate

# Wyświetlenie wynagrodzenia.
print('Wynagrodzenie wynosi ', format(gross_pay, '.2f'), ' zł')

--------------------------------------------------------------------------------------------------------------------------------------------

04. Infinite.py 	

# Ten program przedstawia przykład pętli działającej w nieskończoność.
# Utworzenie zmiennej kontrolującej działanie pętli.
keep_going = 't'

# Uwaga! Pętla działająca w nieskończoność!
while keep_going == 't':
    # Pobranie wielkości sprzedaży i premii.
    sales = float(input('Podaj wielkość sprzedaży: '))
    comm_rate = float(input('Podaj wysokość premii: '))

    # Obliczenie premii.
    commission = sales * comm_rate

    # Wyświetlenie premii.
    print('Premia wynosi ',
          format(commission, '.2f'), ' zł.', sep='')

--------------------------------------------------------------------------------------------------------------------------------------------

05. Property_tax.py 	

# Ten program wyświetla wysokość podatku od nieruchomości.

TAX_FACTOR = 0.0065  # Wysokość stawki podatku.

# Pobranie pierwszego numeru działki.
print('Podaj numer działki')
print('lub 0, aby zakończyć.')
lot = int(input('Numer działki: '))

# Kontynuacja przetwarzania dopóki, dopóty
# użytkownik nie wpisze 0.
while lot != 0:
    # Pobranie wartości nieruchomości.
    value = float(input('Podaj wartość nieruchomości: '))

    # Obliczenie wysokości podatku.
    tax = value * TAX_FACTOR

    # Wyświetlenie wysokości podatku.
    print('Wysokość podatku: ', format(tax, ',.2f'), ' zł.', sep='')

    # Pobranie następnego numeru działki.
    print('Podaj następny numer działki lub')
    print('0, aby zakończyć.')
    lot = int(input('Numer działki: '))
	
--------------------------------------------------------------------------------------------------------------------------------------------

06. Rectangular_pattern.py 	

# Ten program wyświetla prostokątny
# kształt zbudowany z gwiazdek.
rows = int(input('Podaj liczbę wierszy: '))
cols = int(input('Podaj licz# Ten program wyświetla prostokątny
# kształt zbudowany z gwiazdek.
rows = int(input('Podaj liczbę wierszy: '))
cols = int(input('Podaj liczbę kolumn: '))

for r in range(rows):
    for c in range(cols):
        print('*', end='')
    print()
bę kolumn: '))

for r in range(rows):
    for c in range(cols):
        print('*', end='')
    print()
    
--------------------------------------------------------------------------------------------------------------------------------------------

07. Retail_no_validation.py 	

# Ten program oblicza cenę detaliczną produktu.

MARK_UP = 2.5  # Procentowa wysokość marży.
another = 't'  # Zmienna kontrolująca działanie pętli.

# Przetworzenie jednego lub większej liczby produktów.
while another == 't' or another == 'T':
    # Pobranie kosztu całkowitego produktu.
    wholesale = float(input("Podaj cenę hurtową " +
                            "produktu: "))

    # Obliczenie ceny detalicznej.
    retail = wholesale * MARK_UP

    # Wyświetlenie ceny detalicznej.
    print('Cena detaliczna: ', format(retail, '.2f'), ' zł.', sep='')

    # Czy powtórzyć operację?
    another = input('Czy chcesz obliczyć cenę innego produktu? ' +
                    '(Jeśli tak, wpisz t): ')

--------------------------------------------------------------------------------------------------------------------------------------------

08. Retail_with_validation.py 	

# Ten program oblicza cenę detaliczną produktu.

MARK_UP = 2.5  # Procentowa wysokość marży.
another = 't'  # Zmienna kontrolująca działanie pętli.

# Przetworzenie jednego lub większej liczby produktów.
while another == 't' or another == 'T':
    # Pobranie kosztu całkowitego produktu.
    wholesale = float(input("Podaj cenę hurtową " +
                            "produktu: "))

    # Weryfikacja podanego kosztu produktu.
    while wholesale < 0:
        print('BŁĄD: Koszt produktu nie może być ujemny.')
        wholesale = float(input('Podaj poprawną' +
                                'cenę produktu: '))

    # Obliczenie ceny detalicznej.
    retail = wholesale * MARK_UP

    # Wyświetlenie ceny detalicznej.
    print('Cena detaliczna: ', format(retail, '.2f'), ' zł.', sep='')

    # Czy powtórzyć operację?
    another = input('Czy chcesz obliczyć cenę innego produktu? ' +
                    '(Jeśli tak, wpisz t): ')

--------------------------------------------------------------------------------------------------------------------------------------------

09. Simple_loop1.py 	

# Ten program przedstawia prostą pętlę for,
# która wykorzystuje listę liczb.

print('Teraz będą wyświetlone liczby od 1 do 5.')
for num in [1, 2, 3, 4, 5]:
    print(num)

--------------------------------------------------------------------------------------------------------------------------------------------

10. Simple_loop2.py 	
		 
# Ten program również przedstawia prostą pętlę for,
# która wykorzystuje listę liczb.

print('Teraz będą wyświetlone liczby nieparzyste od 1 do 9.')
for num in [1, 3, 5, 7, 9]:
    print(num)
		 
--------------------------------------------------------------------------------------------------------------------------------------------

11. Simple_loop3.py 	

# Ten program również przedstawia prostą pętlę for,
# która wykorzystuje listę ciągów tekstowych.

for name in ['Winken', 'Blinken', 'Nod']:
    print(name)
		 
--------------------------------------------------------------------------------------------------------------------------------------------

12. Simple_loop4.py 	
		 
# Ten program pokazuje przykład użycia
# funkcji range() w pętli for.

# Pięciokrotne wyświetlenie komunikatu.
for x in range(5):
    print('Witaj, świecie!')

--------------------------------------------------------------------------------------------------------------------------------------------

13. Speed_converter.py 	
		 
# Ten program konwertuje szybkości w km/h
# (od 60 do 130 w krokach co 10)
# na wyrażone w milach na godzinę.

START_SPEED = 60            # Pierwsza wartość na liście.
END_SPEED = 131             # Górna granica listy.
INCREMENT = 10              # Wielkość kroku.
CONVERSION_FACTOR = 0.6214  # Współczynnik konwersji.

# Wyświetlenie nagłówków tabeli.
print('KPH\tMPH')
print('--------------')

# Wyświetlenie wyniku.
for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(kph, '\t', format(mph, '.1f'))

--------------------------------------------------------------------------------------------------------------------------------------------

14. Spiral_circles.py 	
		 
# Ten program rysuje wzór składający się z powtarzających się okręgów.
import turtle

# Stałe nazwane.
NUM_CIRCLES = 36     # Liczba okręgów do narysowania.
RADIUS = 100         # Promień każdego okręgu.
ANGLE = 10           # Kąt obrotu okręgu.
ANIMATION_SPEED = 0  # Szybkość animacji.

# Określenie szybkości animacji.
turtle.speed(ANIMATION_SPEED)

# Narysowanie 36 okręgów, w trakcie każdej
# żółw będzie obrócony o 10 stopni.
for x in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)

--------------------------------------------------------------------------------------------------------------------------------------------

15. Spiral_lines.py 	
		 
# Ten program rysuje wzór za pomocą powtarzających się linii prostych.
import turtle

# Stałe nazwane.
START_X = -200       # Współrzędna X punktu początkowego.
START_Y = 0          # Współrzędna Y punktu początkowego.
NUM_LINES = 36       # Liczba linii do narysowania.
LINE_LENGTH = 400    # Długość każdej linii.
ANGLE = 170          # Kąt obrotu linii.
ANIMATION_SPEED = 0  # Szybkość animacji.

# Umieszczenie żółwia w położeniu początkowym.
turtle.hideturtle()
turtle.penup()
turtle.goto(START_X, START_Y)
turtle.pendown()

# Określenie szybkości animacji.
turtle.speed(ANIMATION_SPEED)

# Narysowanie 36 linii, w trakcie każdej
# żółw będzie obrócony o 170 stopni.
for x in range(NUM_LINES):
    turtle.forward(LINE_LENGTH)
    turtle.left(ANGLE)

--------------------------------------------------------------------------------------------------------------------------------------------

16. Squares.py 	
		 
# Ten program używa pętli do wyświetlenia
# tabeli zawierającej liczby od 1 do 10
# i ich kwadraty.

# Wyświetlenie nagłówków tabeli.
print('Liczba\tKwadrat')
print('--------------')

# Wyświetlenie liczb od 1 do 10
# i ich kwadratów.
for number in range(1, 11):
    square = number**2
    print(number, '\t', square)
		 
--------------------------------------------------------------------------------------------------------------------------------------------

17. Stair_step_pattern.py 	
		 
# Ten program wyświetla kształt przypominający schody.
NUM_STEPS = 6

for r in range(NUM_STEPS):
    for c in range(r):
        print(' ', end='')
    print('#')
		 
--------------------------------------------------------------------------------------------------------------------------------------------

18. Sum_numbers.py 	
		 
# Ten program oblicza sumę serii
# liczb podanych przez użytkownika.

MAX = 5  # Wartość maksymalna.

# Inicjalizacja zmiennej akumulatora.
total = 0.0

# Wyjaśnienie sposobu działania programu..
print('Ten program oblicza sumę')
print(MAX, 'podanych liczb.')

# Pobieranie liczb i ich sumowanie.
for counter in range(MAX):
    number = int(input('Podaj liczbę: '))
    total = total + number

# Wyświetlenie sumy bieżącej.
print('Suma wynosi', total)

--------------------------------------------------------------------------------------------------------------------------------------------

19. Temperature.py 	

# Ten program pomaga pracownikowi w procesie
# sprawdzania temperatury substancji.

# Stała nazwana przedstawiająca
# temperaturę maksymalną.
MAX_TEMP = 102.5

# Pobranie temperatury substancji.
temperature = float(input("Podaj w Celsjuszach temperaturę substancji: "))

# Dopóki to konieczne, trzeba nakazać
# użytkownikowi dostosowanie termostatu.
while temperature > MAX_TEMP:
    print('Temperatura jest zbyt wysoka.')
    print('Wyłącz termostat i odczekaj')
    print('5 minut. Następnie ponownie sprawdź')
    print('temperaturę i wpisz ją tutaj.')
    temperature = float(input('Ponownie podaj w Celsjuszach temperaturę substancji: '))

# Przypomnienie użytkownikowi o konieczności
# ponownego sprawdzenia temperatury w ciągu 15 minut.
print('Temperatura jest do zaakceptowania.')
print('Sprawdź ją ponownie w ciągu 15 minut.')

--------------------------------------------------------------------------------------------------------------------------------------------

20. Test_score_averages.py 	
		 
# Ten program oblicza średni wynik z kilku sprawdzianów. Prosi użytkownika
# o podanie liczby uczniów i sprawdzianów.

# Pobranie liczby uczniów.
num_students = int(input('Podaj liczbę uczniów: '))

# Pobranie liczby sprawdzianów.
num_test_scores = int(input('Podaj liczbę sprawdzianów: '))

# Obliczenie średniego wyniku ze sprawdzianów uczniów.
for student in range(num_students):
    # Inicjalizacja akumulatora wyników sprawdzianów.
    total = 0.0
    # Pobranie wyników sprawdzianów danego ucznia.
    print('Uczeń numer', student + 1)
    print('–––––––––––––––––')
    for test_num in range(num_test_scores):
        print('Podaj wynik ze sprawdzianu numer', test_num + 1, end='')
        score = float(input(': '))
        # Dodanie wyniku do akumulatora.
        total += score

    # Obliczenie średniego wyniku ze sprawdzianów danego ucznia.
    average = total / num_test_scores

    # Wyświetlenie obliczonej wartości.
    print('Średni wynik ucznia', student + 1,
          'to', average)
    print()

--------------------------------------------------------------------------------------------------------------------------------------------

21. Triangle_pattern.py 	
		 
# Ten program wyświetla kształt przypominający trójkąt.
BASE_SIZE = 8

for r in range(BASE_SIZE):
    for c in range(r + 1):
        print('*', end='')
    print()
 
--------------------------------------------------------------------------------------------------------------------------------------------

22. User_squares1.py 	
		 
# Ten program używa pętli do wyświetlenia
# tabeli liczb i ich kwadratów.

# Pobranie wartości maksymalnej sekwencji liczb.
print('Ten program wyświetla listę liczb')
print('(począwszy od 1) i ich kwadraty.')
end = int(input('Podaj wartość maksymalną: '))

# Wyświetlenie nagłówków tabeli.
print()
print('Liczba\tKwadrat')
print('--------------')

# Wyświetlenie liczb i ich kwadratów.
for number in range(1, end + 1):
    square = number**2
    print(number, '\t', square)

--------------------------------------------------------------------------------------------------------------------------------------------

23. User_squares2.py
		 
# Ten program używa pętli do wyświetlenia
# tabeli liczb i ich kwadratów.

# Pobranie wartości początkowej sekwencji liczb.
print('Ten program wyświetla listę liczb')
print('i ich kwadraty.')
start = int(input('Podaj wartość początkową: '))

# Pobranie wartości maksymalnej sekwencji liczb.
end = int(input('Podaj wartość maksymalną: '))

# Wyświetlenie nagłówków tabeli.
print()
print('Liczba\tKwadrat')
print('--------------')

# Wyświetlenie liczb i ich kwadratów.
for number in range(start, end + 1):
    square = number**2
    print(number, '\t', square)

--------------------------------------------------------------------------------------------------------------------------------------------
