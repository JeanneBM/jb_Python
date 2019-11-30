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


