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


