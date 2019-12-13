01. Acme_dryer.py

# Ten program wyświetla instrukcje krok po kroku
# demontażu suszarki na pranie Acme.
# Funkcja main() zawiera logikę główną programu.
def main():
    # Wyświetlenie komunikatu początkowego.
    startup_message()
    input('Naciśnij Enter, aby przejść do kroku 1.')
    # Wyświetlenie kroku 1.
    step1()
    input('Naciśnij Enter, aby przejść do kroku 2.')
    # Wyświetlenie kroku 2.
    step2()
    input('Naciśnij Enter, aby przejść do kroku 3.')
    # Wyświetlenie kroku 3.
    step3()
    input('Naciśnij Enter, aby przejść do kroku 4.')
    # Wyświetlenie kroku 4.
    step4()

# Funkcja startup_message() wyświetla na ekranie
# początkowy komunikat programu.
def startup_message():
    print('Ten program pokaże Ci,')
    print('jak zdemontować suszarkę na pranie ACME.')
    print('Proces składa się z czterech kroków.')
    print()

# Funkcja step1() wyświetla instrukcje
# dla kroku 1.
def step1():
    print('Krok 1. Odłącz suszarkę i')
    print('odsuń ją od ściany.')
    print()

# Funkcja step2() wyświetla instrukcje
# dla kroku 2.
def step2():
    print('Krok 2. Odkręć sześć śrub')
    print('z tyłu suszarki.')
    print()

# Funkcja step3() wyświetla instrukcje
# dla kroku 3.
def step3():
    print('Krok 3. Zdejmij tylny panel')
    print('suszarki.')
    print()

# Funkcja step4() wyświetla instrukcje
# dla kroku 4.
def step4():
    print('Krok 4. Pociągnij do góry')
    print('pokrywę suszarki.')

# Wywołanie funkcji main() i rozpoczęcie działania programu.
main()

----------------------------------------------------------------------------------------------------------------------------------------------
 
02. Bad_local.py 	
# Zdefiniowanie funkcji main().
def main():
    get_name()
    print('Witaj,', name)      # Ten wiersz powoduje błąd!

# Zdefiniowanie funkcji get_name().
def get_name():
    name = input('Podaj imię: ')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------
  
03. Birds.py 	

# Ten program pokazuje, że dwie funkcje mogą
# mieć zmienne lokalne o tej samej nazwie.

def main():
    # Wywołanie funkcji texas().
    texas()
    # Wywołanie funkcji california()
    california()

# Definicja funkcji texas(). Tworzy ona
# zmienną lokalną o nazwie birds.
def texas():
    birds = 5000
    print('Teksas ma', birds, 'gatunków ptaków.')

# Definicja funkcji california(). Ona również
# tworzy zmienną lokalną o nazwie birds.
def california():
    birds = 8000
    print('Kalifornia ma', birds, 'gatunków ptaków.')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

04. Change_me.py 	

# Te program pokazuje, co się stanie
# po zmianie wartości parametru.

def main():
    value = 99
    print('Wartość wynosi', value)
    change_me(value)
    print('Wartość w funkcji main() wynosi', value)

def change_me(arg):
    print('W tym miejscu wartość zostaje zmieniona')
    arg = 0
    print('Teraz wartość wynosi', arg)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

05. Circle.py 	

# Moduł circle zawiera funkcje przeprowadzające
# obliczenia związane z okręgiem.
import math

# Funkcja area() akceptuje argument w postaci
# promienia okręgu i zwraca pole powierzchni.
def area(radius):
    return math.pi * radius**2

# Funkcja circumference() akceptuje argument w postaci
# promienia okręgu i zwraca obwód okręgu.
def circumference(radius):
    return 2 * math.pi * radius

----------------------------------------------------------------------------------------------------------------------------------------------

06. Coin_toss.py 	

# Ten program symuluje 10 rzutów monetą.
import random

# Definicje stałych.
HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        # Symulacja rzutu monetą.
        if random.randint(HEADS, TAILS) == HEADS:
            print('orzeł')
        else:
            print('reszka')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

07. Commission_rate.py 

# Ten program oblicza wynagrodzenie
# pracownika firmy Make Your Own Music.
def main():
    # Pobranie wartości sprzedaży.
    sales = get_sales()

    # Pobranie wartości zaliczki wypłaconej pracownikowi.
    advanced_pay = get_advanced_pay()

    # Ustalenie procentowej wysokości prowizji.
    comm_rate = determine_comm_rate(sales)

    # Obliczenie należnego wynagrodzenia.
    pay = sales * comm_rate - advanced_pay

    # Wyświetlenie obliczonego wynagrodzenia.
    print('Wynagrodzenie wynosi ', format(pay, '.2f'), ' zł.', sep='')

    # Ustalenie, czy kwota do wypłaty jest ujemna.
    if pay < 0:
        print('Pracownik musi zwrócić')
        print('pieniądze firmie.')

# Funkcja get_sales() pobiera od użytkownika wysokość
# miesięcznej sprzedaży i zwraca tę wartość.
def get_sales():
    # Pobranie wartości miesięcznej sprzedaży.
    monthly_sales = float(input('Podaj wartość miesięcznej sprzedaży: '))

    # Zwrot podanej wartości.
    return monthly_sales

# Funkcja get_advanced_pay() pobiera wartość
# zaliczki wypłaconej danemu pracownikowi
# i zwraca ją.
def get_advanced_pay():
    # Pobranie wartości wypłaconej zaliczki.
    print('Podaj wartość wypłaconej zaliczki lub 0,')
    print('jeżeli zaliczka nie została wypłacona.')
    advanced = float(input('Wypłacona zaliczka: '))

    # Return the amount entered.
    return advanced

# Funkcja determine_comm_rate() przyjmuje
# argument w postaci wartości sprzedaży
# i zwraca procentową wysokość prowizji.
def determine_comm_rate(sales):
    # Ustalenie procentowej wysokości prowizji.
    if sales < 10000.00:
        rate = 0.10
    elif sales >= 10000 and sales <= 14999.99:
        rate = 0.12
    elif sales >= 15000 and sales <= 17999.99:
        rate = 0.14
    elif sales >= 18000 and sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18

    # Zwrot procentowej wysokości prowizji.
    return rate

----------------------------------------------------------------------------------------------------------------------------------------------

08. Cups_to_ounces.py 

# Ten program konwertuje liczbę szklanek na uncje.

def main():
    # Wyświetlenie komunikatu informującego, do czego służy program.
    intro()
    # Pobranie liczby szklanek.
    cups_needed = int(input('Podaj liczbę szklanek: '))
    # Konwersja liczby szklanek na uncje.
    cups_to_ounces(cups_needed)

# Funkcja intro() wyświetla komunikat informujący, do czego służy program.
def intro():
    print('Ten program konwertuje liczbę')
    print('szklanek na uncje. W programie')
    print('użyłem następującego wzoru:')
    print(' 1 szklanka = 8 uncji.')
    print()

# Funkcja cups_to_ounces() pobiera liczbę szklanek,
# a następnie wyświetla odpowiadającą im liczbę uncji.
def cups_to_ounces(cups):
    ounces = cups * 8
    print('To odpowiada następującej liczbie uncji:', ounces, '.')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

09. Dice.py 	

# Ten program symuluje rzut kośćmi.
import random

# Stałe określające minimalną i maksymalną liczbę losową.
MIN = 1
MAX = 6

def main():
    # Utworzenie zmiennej kontrolującej działanie pętli.
    again = 't'

    # Symulacja rzutu kośćmi.
    while again == 't' or again == 'T':
        print('Rzucam kośćmi . . .')
        print('Oto wynik:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        # Czy chcesz rzucić jeszcze raz?
        again = input('Czy chcesz rzucić jeszcze raz (t = tak): ')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

10. Draw_circles.py 	

import turtle

def main():
    turtle.hideturtle()
    circle(0, 0, 100, 'red')
    circle(-150, -75, 50, 'blue')
    circle(-200, 150, 75, 'green')

# Funkcja circle() rysuje okrąg. Parametry x i y
# to współrzędne środka okręgu. Parametr radius
# to promień okręgu. Z kolei parametr color
# to ciąg tekstowy określający kolor wypełnienia okręgu.

def circle(x, y, radius, color):
    turtle.penup()              # Podniesienie pióra.
    turtle.goto(x, y - radius)  # Umieszczenie żółwia w odpowiednim położeniu.
    turtle.fillcolor(color)     # Określenie koloru wypełnienia.
    turtle.pendown()            # Opuszczenie pióra.
    turtle.begin_fill()         # Rozpoczęcie wypełniania kolorem.
    turtle.circle(radius)       # Narysowanie okręgu
    turtle.end_fill()           # Zakończenie wypełniania kolorem.

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

11. Draw_lines.py 	

import turtle

# Stałe nazwane dla wierzchołków trójkąta.
TOP_X = 0
TOP_Y = 100
BASE_LEFT_X = -100
BASE_LEFT_Y = -100
BASE_RIGHT_X = 100
BASE_RIGHT_Y = -100

def main():
    turtle.hideturtle()
    line(TOP_X, TOP_Y, BASE_LEFT_X, BASE_LEFT_Y, 'red')
    line(TOP_X, TOP_Y, BASE_RIGHT_X, BASE_RIGHT_Y, 'blue')
    line(BASE_LEFT_X, BASE_LEFT_Y, BASE_RIGHT_X, BASE_RIGHT_Y, 'green')

# Funkcja line() rysuje linię z punktu o współrzędnych (startX, startY)
# do punktu o współrzędnych (endX, endY). Parametr color określa jej kolor.

def line(startX, startY, endX, endY, color):
    turtle.penup()               # Podniesienie pióra.
    turtle.goto(startX, startY)  # Przejście do punktu początkowego.
    turtle.pendown()             # Opuszczenie pióra.
    turtle.pencolor(color)       # Określenie koloru pióra.
    turtle.goto(endX, endY)      # Narysowanie linii.

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

12. Draw_squares.py 	

import turtle

def main():
    turtle.hideturtle()
    square(100, 0, 50, 'red')
    square(-150, -100, 200, 'blue')
    square(-200, 150, 75, 'green')

# Funkcja square() rysuje kwadrat. Parametry x i y
# to współrzędne lewego dolnego wierzchołka. Parametr width
# określa długość boku kwadratu. Z kolei parametr color
# to ciąg tekstowy określający kolor wypełnienia kwadratu.

def square(x, y, width, color):
    turtle.penup()             # Podniesienie pióra.
    turtle.goto(x, y)          # Przejście do wskazanego położenia.
    turtle.fillcolor(color)    # Określenie koloru wypełnienia.
    turtle.pendown()           # Opuszczenie pióra.
    turtle.begin_fill()        # Rozpoczęcie wypełniania kolorem.
    for count in range(4):     # Narysowanie kwadratu.
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()          # Zakończenie wypełniania kolorem.

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

13. Function_demo.py 	

# Ten program pokazuje przykład funkcji.
# Najpierw należy zdefiniować funkcję o nazwie message().
def message():
    print('Jestem Artur,')
    print('król Brytyjczyków.')

# Wywołanie funkcji message().
message()

----------------------------------------------------------------------------------------------------------------------------------------------

14. Geometry.py 	

# Ten program pozwala użytkownikowi na wybór
# z menu różnych funkcji geometrycznych. Na
# początku importuje moduły circle i rectangle.
import circle
import rectangle

# Stałe przeznaczone do obsługi menu.
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

# Funkcja main().
def main():
    # Zmienna choice kontroluje działanie pętli
    # i przechowuje wybór dokonany przez użytkownika.
    choice = 0

    while choice != QUIT_CHOICE:
        # Wyświetlenie menu.
        display_menu()

        # Pobranie wyboru dokonanego przez użytkownika.
        choice = int(input('Wybierz opcję: '))

        # Wykonanie wybranej akcji.
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Podaj promień okręgu: "))
            print('Pole powierzchni wynosi', circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("Podaj promień okręgu: "))
            print('Obwód wynosi',
                  circle.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Podaj długość prostokąta: "))
            length = float(input("Podaj szerokość prostokąta: "))
            print('Pole powierzchni wynosi', rectangle.area(width, length))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Podaj długość prostokąta: "))
            length = float(input("Podaj szerokość prostokąta: "))
            print('Obwód wynosi',
                  rectangle.perimeter(width, length))
        elif choice == QUIT_CHOICE:
            print('Zakończenie działania programu...')
        else:
            print('Błąd: nieprawidłowa opcja.')

# Funkcja display_menu() wyświetla menu.
def display_menu():
    print(' MENU')
    print('1) Pole powierzchni okręgu')
    print('2) Obwód okręgu')
    print('3) Pole powierzchni prostokąta')
    print('4) Obwód prostokąta')
    print('5) Koniec')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

15. Global1.py 	

# Utworzenie zmiennej globalnej.
my_value = 10

# Funkcja show_value() wyświetla
# wartość zmiennej globalnej.
def show_value():
    print(my_value)

# Wywołanie funkcji show_value().
show_value()

----------------------------------------------------------------------------------------------------------------------------------------------
16. Global2.py 	
----------------------------------------------------------------------------------------------------------------------------------------------
17. Graphics_mod_demo.py 	
----------------------------------------------------------------------------------------------------------------------------------------------
18. Hypotenuse.py 	
----------------------------------------------------------------------------------------------------------------------------------------------
19. Keyword_args.py 
----------------------------------------------------------------------------------------------------------------------------------------------
20. Keyword_string_args.py 	
----------------------------------------------------------------------------------------------------------------------------------------------
21. Multiple_args.py 	
----------------------------------------------------------------------------------------------------------------------------------------------
22. My_graphics.py 	
----------------------------------------------------------------------------------------------------------------------------------------------
23. Pass_arg.py 	
----------------------------------------------------------------------------------------------------------------------------------------------
24. Random_numbers.py 	
----------------------------------------------------------------------------------------------------------------------------------------------
25. Random_numbers2.py 
----------------------------------------------------------------------------------------------------------------------------------------------
26. Random_numbers3.py 	
----------------------------------------------------------------------------------------------------------------------------------------------
27. Rectangle.py 	
----------------------------------------------------------------------------------------------------------------------------------------------
28. Retirement.py 	
----------------------------------------------------------------------------------------------------------------------------------------------
29. Sale_price.py 	
----------------------------------------------------------------------------------------------------------------------------------------------
30. Square_root.py 	
----------------------------------------------------------------------------------------------------------------------------------------------
31. String_args.py 	
----------------------------------------------------------------------------------------------------------------------------------------------
32. Total_ages.py 	
----------------------------------------------------------------------------------------------------------------------------------------------
33. Two_functions.py
----------------------------------------------------------------------------------------------------------------------------------------------
