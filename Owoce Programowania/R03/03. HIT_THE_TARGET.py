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
