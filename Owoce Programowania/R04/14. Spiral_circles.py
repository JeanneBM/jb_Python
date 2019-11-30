# Ten program rysuje wzór składający się z powtarzających się okręgów.
import turtle

# Stałe nazwane.
NUM_CIRCLES = 36     # Liczba okręgów do narysowania.
RADIUS = 100         # Promień każdego okręgu.
ANGLE = 10           # Kąt obrotu okręgu.
ANIMATION_SPEED = 0  # Szybkość animacji.

# Określenie szybkości animacji.
turtle.speed(ANIMATION_SPEED)

# Narysowanie 36 okręgów, w trakcie każdej
# żółw będzie obrócony o 10 stopni.
for x in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)


