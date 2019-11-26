# Ten program pobiera liczbę punktów ze sprawdzianu,
# a następnie wyświetla ocenę, którą zdobył uczeń.

# Stałe nazwane przedstawiające oceny za poszczególne liczby punktów.
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# Pobranie liczby punktów.
score = int(input('Podaj liczbę punktów ze sprawdzianu: '))

# Ustalenie oceny na podstawie pobranej liczby punktów.
if score >= A_SCORE:
    print('Twoja ocena to 5.')
else:
    if score >= B_SCORE:
        print('Twoja ocena to 4.')
    else:
        if score >= C_SCORE:
            print('Twoja ocena to 3.')
        else:
            if score >= D_SCORE:
                print('Twoja ocena to 2.')
            else:
                print('Twoja ocena to 1.')
