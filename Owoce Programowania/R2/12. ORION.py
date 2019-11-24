# Ten program wyświetla wybrane gwiazdy gwiazdozbioru Oriona,
# ich nazwy oraz łączące je linie.
import turtle

# Określenie wielkości okna.
turtle.setup(500, 600)

# Konfiguracja żółwia.
turtle.penup()
turtle.hideturtle()

# Utworzenie stałych nazwanych dla współrzędnych gwiazd.
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# Narysowanie gwiazd.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)      # Lewe kolano.
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)    # Prawe kolano.
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)      # Gwiazda po lewej stronie pasa.
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)  # Gwiazda pośrodku pasa.
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)    # Gwiazda po prawej stronie pasa.
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)              # Lewe kolano.
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)            # Prawe kolano.
turtle.dot()

# Wyświetlenie nazw gwiazd
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)      # Lewe kolano.
turtle.write('Betegeuse')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)    # Prawe kolano.
turtle.write('Meissa')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)      # Gwiazda po lewej stronie pasa.
turtle.write('Alnitak')
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)  # Gwiazda pośrodku pasa.
turtle.write('Alnilam')
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)    # Gwiazda po prawej stronie pasa.
turtle.write('Mintaka')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)              # Lewe kolano.
turtle.write('Saiph')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)            # Prawe kolano.
turtle.write('Rigel')

# Narysowanie linii od lewego ramienia do gwiazdy po lewej stronie pasa.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()

# Narysowanie linii od prawego ramienia do gwiazdy po prawej stronie pasa.
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

# Narysowanie linii między gwiazdami po lewej stronie i pośrodku pasa.
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.penup()

# Narysowanie linii między gwiazdami pośrodku i po prawej stronie pasa.
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

# Narysowanie linii od gwiazdy po lewej stronie pasa do lewego kolana.
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

# Narysowanie linii od gwiazdy po prawej stronie pasa do prawego kolana.
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)

# Pozostawienie otwartego okna. (To nie jest konieczne podczas użycia IDLE).
turtle.done()
