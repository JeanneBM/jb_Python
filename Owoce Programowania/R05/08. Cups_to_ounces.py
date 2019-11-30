# Ten program konwertuje liczbę szklanek na uncje.

def main():
    # Wyświetlenie komunikatu informującego, do czego służy program.
    intro()
    # Pobranie liczby szklanek.
    cups_needed = int(input('Podaj liczbę szklanek: '))
    # Konwersja liczby szklanek na uncje.
    cups_to_ounces(cups_needed)

# Funkcja intro() wyświetla komunikat informujący, do czego służy program.
def intro():
    print('Ten program konwertuje liczbę')
    print('szklanek na uncje. W programie')
    print('użyłem następującego wzoru:')
    print(' 1 szklanka = 8 uncji.')
    print()

# Funkcja cups_to_ounces() pobiera liczbę szklanek,
# a następnie wyświetla odpowiadającą im liczbę uncji.
def cups_to_ounces(cups):
    ounces = cups * 8
    print('To odpowiada następującej liczbie uncji:', ounces, '.')

# Wywołanie funkcji main().
main()


