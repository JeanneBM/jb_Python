# Funkcje grafiki żółwia.
import turtle

# Funkcja square() rysuje kwadrat. Parametry x i y
# to współrzędne lewego dolnego wierzchołka. Parametr width
# określa długość boku kwadratu. Z kolei parametr color
# to ciąg tekstowy określający kolor wypełnienia kwadratu.

def square(x, y, width, color):
    turtle.penup()           # Podniesienie pióra.
    turtle.goto(x, y)        # Umieszczenie żółwia w odpowiednim położeniu.
    turtle.fillcolor(color)  # Określenie koloru wypełnienia.
    turtle.pendown()         # Opuszczenie pióra.
    turtle.begin_fill()      # Rozpoczęcie wypełniania kolorem.
    for count in range(4):   # Narysowanie kwadratu.
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()        # Zakończenie wypełniania kolorem.

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
    turtle.circle(radius)       # Narysowanie okręgu.
    turtle.end_fill()           # Zakończenie wypełniania kolorem.

# Funkcja line() rysuje linię z punktu o współrzędnych (startX, startY)
# do punktu o współrzędnych (endX, endY). Parametr color określa jej kolor.

def line(startX, startY, endX, endY, color):
    turtle.penup()               # Podniesienie pióra.
    turtle.goto(startX, startY)  # Przejście do punktu początkowego.
    turtle.pendown()             # Opuszczenie pióra.
    turtle.pencolor(color)       # Określenie koloru pióra.
    turtle.goto(endX, endY)      # Narysowanie kwadratu.

