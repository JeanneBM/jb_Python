# Ten program oblicza cenę
# promocyjną produktu.

# DISCOUNT_PERCENTAGE to stała globalna
# określająca procentową wielkość rabatu.
DISCOUNT_PERCENTAGE = 0.20

# Funkcja main().
def main():
    # Pobranie ceny detalicznej produktu.
    reg_price = get_regular_price()

    # Obliczenie ceny promocyjnej.
    sale_price = reg_price - discount(reg_price)

    # Wyświetlenie ceny promocyjnej.
    print('Cena promocyjna wynosi ', format(sale_price, '.2f'), ' zł.', sep='')

# Funkcja get_regular_price() prosi
# użytkownika o podanie ceny detalicznej
# produktu i zwraca tę wartość.
def get_regular_price():
    price = float(input("Podaj cenę detaliczną produktu: "))
    return price

# Funkcja discount() akceptuje argument w postaci
# ceny produktu i zwraca wysokość rabatu obliczoną
# na podstawie wartości DISCOUNT_PERCENTAGE.
def discount(price):
    return price * DISCOUNT_PERCENTAGE

# Wywołanie funkcji main().
main()
