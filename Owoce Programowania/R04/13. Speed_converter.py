# Ten program konwertuje szybkości w km/h
# (od 60 do 130 w krokach co 10)
# na wyrażone w milach na godzinę.

START_SPEED = 60            # Pierwsza wartość na liście.
END_SPEED = 131             # Górna granica listy.
INCREMENT = 10              # Wielkość kroku.
CONVERSION_FACTOR = 0.6214  # Współczynnik konwersji.

# Wyświetlenie nagłówków tabeli.
print('KPH\tMPH')
print('--------------')

# Wyświetlenie wyniku.
for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(kph, '\t', format(mph, '.1f'))

