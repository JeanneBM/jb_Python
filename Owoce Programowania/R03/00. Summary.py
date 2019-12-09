01. Auto_repair_payroll.py 
  
# Stałe nazwane przedstawiające zwykłą stawkę
# za godzinę i mnożnik za nadgodziny.
BASE_HOURS = 40  # Standardowa stawka godzinowa.
OT_MULTIPLIER = 1.5  # Mnożnik za nadgodziny.

# Pobranie liczby przeprowadzonych godzin i stawki godzinowej.
hours = float(input('Podaj liczbę przepracowanych godzin: '))
pay_rate = float(input('Podaj stawkę godzinową: '))

# Obliczenie i wyświetlenie wynagrodzenia.
if hours > BASE_HOURS:
    # Obliczenie wynagrodzenia wraz z nadgodzinami.
    # Najpierw należy pobrać liczbę nadgodzin.
    overtime_hours = hours - BASE_HOURS

    # Obliczenie wynagrodzenia za nadgodziny.
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER

    # Obliczenie całkowitego wynagrodzenia.
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
    # Obliczenie wynagrodzenia bez nadgodzin.
    gross_pay = hours * pay_rate

# Wyświetlenie obliczonego wynagrodzenia.
print('Wynagrodzenie wynosi', format(gross_pay, ',.2f'), sep='')

----------------------------------------------------------------------------------------------------------------------------------------------

02. Grader.py 	

# Ten program pobiera liczbę punktów ze sprawdzianu,
# a następnie wyświetla ocenę, którą zdobył uczeń.

# Stałe nazwane przedstawiające oceny za poszczególne liczby punktów.
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# Pobranie liczby punktów.
score = int(input('Podaj liczbę punktów ze sprawdzianu: '))

# Ustalenie oceny na podstawie pobranej liczby punktów.
if score >= A_SCORE:
    print('Twoja ocena to 5.')
else:
    if score >= B_SCORE:
        print('Twoja ocena to 4.')
    else:
        if score >= C_SCORE:
            print('Twoja ocena to 3.')
        else:
            if score >= D_SCORE:
                print('Twoja ocena to 2.')
            else:
                print('Twoja ocena to 1.')
                
----------------------------------------------------------------------------------------------------------------------------------------------

03. HIT_THE_TARGET.py 	

# Gra polegająca na trafieniu w cel.
import turtle

# Stałe nazwane.
SCREEN_WIDTH = 600     # Szerokość okna gry.
SCREEN_HEIGHT = 600    # Wysokość okna gry.
TARGET_LLEFT_X = 100   # Współrzędna X lewego dolnego wierzchołka celu.
TARGET_LLEFT_Y = 250   # Współrzędna Y lewego dolnego wierzchołka celu.
TARGET_WIDTH = 25      # Szerokość celu.
FORCE_FACTOR = 30      # Współczynnik siły.
PROJECTILE_SPEED = 1   # Szybkość animacji pocisku.
NORTH = 90             # Kąt określający kierunek północny.
SOUTH = 270            # Kąt określający kierunek południowy.
EAST = 0               # Kąt określający kierunek wschodni.
WEST = 180             # Kąt określający kierunek zachodni.

# Konfiguracja okna.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Narysowanie celu.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Umieszczenie żółwia na środku ekranu.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Pobranie od gracza wartości określających kąt i siłę.
angle = float(input("Podaj kąt pocisku: "))
force = float(input("Podaj siłę początkową (1−10): "))

# Obliczenie odległości.
distance = force * FORCE_FACTOR

# Określenie kierunku.
turtle.setheading(angle)

# Wystrzelenie pocisku.
turtle.pendown()
turtle.forward(distance)

# Czy cel został trafiony?
if (turtle.xcor() >= TARGET_LLEFT_X and
        turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
        turtle.ycor() >= TARGET_LLEFT_Y and
        turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print('Cel został trafiony!')
else:
    print('Cel nie został trafiony.')

----------------------------------------------------------------------------------------------------------------------------------------------

04. Loan_qualifier.py 	

# Ten program ustala, czy klient banku
# ma zdolność kredytową.

MIN_SALARY = 30000.0  # Wysokość minimalnego rocznego wynagrodzenia.
MIN_YEARS = 2  # Minimalna liczba lat pracy u aktualnego pracodawcy.

# Pobranie wynagrodzenia klienta.
salary = float(input('Podaj wysokość rocznego wynagrodzenia: '))

# Pobranie liczby lat pracy u aktualnego pracodawcy.
years_on_job = int(input('Podaj liczbę lat pracy' +
                         'u obecnego pracodawcy: '))

# Ustalenie, czy klient ma zdolność kredytową.
if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print('Masz zdolność kredytową.')
    else:
        print('Musisz być zatrudniony',
              'przez przynajmniej', MIN_YEARS,
              'lata.')
else:
    print('Musisz zarabiać przynajmniej ',
          format(MIN_SALARY, '.2f'),
          ' zł rocznie.', sep='')
          
----------------------------------------------------------------------------------------------------------------------------------------------

05. Loan_qualifier2.py 	

# Ten program ustala, czy klient banku
# ma zdolność kredytową.

MIN_SALARY = 30000.0  # Wysokość minimalnego rocznego wynagrodzenia.
MIN_YEARS = 2  # Minimalna liczba lat pracy u aktualnego pracodawcy.

# Pobranie wynagrodzenia klienta.
salary = float(input('Podaj wysokość rocznego wynagrodzenia: '))

# Pobranie liczby lat pracy u aktualnego pracodawcy.
years_on_job = int(input('Podaj liczbę lat pracy ' +
                         'u obecnego pracodawcy: '))

# Ustalenie, czy klient ma zdolność kredytową.
if salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
    print('Masz zdolność kredytową.')
else:
    print('Nie masz zdolności kredytowej.')
    
----------------------------------------------------------------------------------------------------------------------------------------------

06. Loan_qualifier3.py 	

# Ten program ustala, czy klient banku
# ma zdolność kredytową.

MIN_SALARY = 30000.0  # Wysokość minimalnego rocznego wynagrodzenia.
MIN_YEARS = 2  # Minimalna liczba lat pracy u aktualnego pracodawcy.

# Pobranie wynagrodzenia klienta.
salary = float(input('Podaj wysokość rocznego wynagrodzenia: '))

# Pobranie liczby lat pracy u aktualnego pracodawcy.
years_on_job = int(input('Podaj liczbę lat pracy ' +
                         'u obecnego pracodawcy: '))

# Ustalenie, czy klient ma zdolność kredytową.
if salary >= MIN_SALARY or years_on_job >= MIN_YEARS:
    print('Masz zdolność kredytową.')
else:
    print('Nie masz zdolności kredytowej.')
    
----------------------------------------------------------------------------------------------------------------------------------------------

07. Password.py 	

# Ten program porównuje dwa ciągi tekstowe.
# Pobranie hasła od użytkownika.
password = input('Podaj hasło: ')

# Ustalenie, czy użytkownik
# podał prawidłowe hasło.
if password == 'prospero':
    print('Hasło jest poprawne.')
else:
    print('Podane hasło jest niepoprawne.')
    
----------------------------------------------------------------------------------------------------------------------------------------------

08. SORT_NAMES.py 	

# Ten program porównuje ciągi tekstowe za pomocą operatora <.
# Pobranie dwóch ciągów tekstowych od użytkownika.
name1 = input('Podaj imię i nazwisko (nazwisko pierwsze): ')
name2 = input('Podaj kolejne imię i nazwisko (nazwisko pierwsze): ')

# Wyświetlenie danych w kolejności alfabetycznej.
print('Oto posortowana alfabetycznie lista osób.')

if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)
    
----------------------------------------------------------------------------------------------------------------------------------------------

09. Test_average.py

# Ten program pobiera wyniki trzech sprawdzianów
# i wyświetla ich średnią. Jeżeli średnia jest wyższa niż
# pewna wartość, wówczas program składa uczniowi gratulacje..

# HIGH_SCORE to stała nazwana przechowująca wartość
# po przekroczeniu której uczeń otrzymuje gratulacje.
HIGH_SCORE = 95

# Pobranie wyników z trzech testów.
test1 = int(input('Podaj wynik ze sprawdzanu nr 1: '))
test2 = int(input('Podaj wynik ze sprawdzanu nr 2: '))
test3 = int(input('Podaj wynik ze sprawdzanu nr 3: '))

# Obliczenie średniego wyniku.
average = (test1 + test2 + test3) / 3

# Wyświetlenie średniego wyniku.
print('Średni wynik wynosi', average)

# Jeżeli średnia jest powyżej wartości HIGH_SCORE,
# należe pogratulować uczniowi.
if average >= HIGH_SCORE:
    print('Gratulacje!')
    print('Świetny wynik!')
    
----------------------------------------------------------------------------------------------------------------------------------------------
