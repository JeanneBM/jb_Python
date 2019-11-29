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
