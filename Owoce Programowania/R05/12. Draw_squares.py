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


