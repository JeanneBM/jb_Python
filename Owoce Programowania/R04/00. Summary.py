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

--------------------------------------------------------------------------------------------------------------------------------------------

12. Simple_loop4.py 	

--------------------------------------------------------------------------------------------------------------------------------------------

13. Speed_converter.py 	

--------------------------------------------------------------------------------------------------------------------------------------------

14. Spiral_circles.py 	

--------------------------------------------------------------------------------------------------------------------------------------------

15. Spiral_lines.py 	

--------------------------------------------------------------------------------------------------------------------------------------------

16. Squares.py 	

--------------------------------------------------------------------------------------------------------------------------------------------

17. Stair_step_pattern.py 	

--------------------------------------------------------------------------------------------------------------------------------------------

18. Sum_numbers.py 	

--------------------------------------------------------------------------------------------------------------------------------------------

19. Temperature.py 	

--------------------------------------------------------------------------------------------------------------------------------------------

20. Test_score_averages.py 	

--------------------------------------------------------------------------------------------------------------------------------------------

21. Triangle_pattern.py 	

--------------------------------------------------------------------------------------------------------------------------------------------

22. User_squares1.py 	

--------------------------------------------------------------------------------------------------------------------------------------------

23. User_squares2.py

--------------------------------------------------------------------------------------------------------------------------------------------
