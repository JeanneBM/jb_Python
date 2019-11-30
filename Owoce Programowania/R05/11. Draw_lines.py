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


