# Ta stała globalna przechowuje procent kwoty
# wynagrodzenia przekazywany na fundusz emerytalny.
CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input('Podaj kwotę wynagrodzenia: '))
    bonus = float(input('Podaj kwotę premii: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

# Funkcja show_pay_contrib() pobiera argument w postaci
# kwoty wynagrodzenia i wyświetla obliczoną wysokość składki
# naliczoną dla podanego wynagrodzenia.
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print('Wysokość składki naliczona dla wynagrodzenia wynosi: ',
          format(contrib, '.2f'),
          sep='')

# Funkcja show_bonus_contrib() pobiera argument w postaci
# kwoty premii i wyświetla obliczoną wysokość składki
# naliczoną dla podanej premii.
def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print('Wysokość składki naliczona dla premii wynosi ',
          format(contrib, '.2f'),
          sep='')

# Wywołanie funkcji main().
main()
