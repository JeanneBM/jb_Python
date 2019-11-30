# Ten program oblicza wynagrodzenie
# pracownika firmy Make Your Own Music.
def main():
    # Pobranie wartości sprzedaży.
    sales = get_sales()

    # Pobranie wartości zaliczki wypłaconej pracownikowi.
    advanced_pay = get_advanced_pay()

    # Ustalenie procentowej wysokości prowizji.
    comm_rate = determine_comm_rate(sales)

    # Obliczenie należnego wynagrodzenia.
    pay = sales * comm_rate - advanced_pay

    # Wyświetlenie obliczonego wynagrodzenia.
    print('Wynagrodzenie wynosi ', format(pay, '.2f'), ' zł.', sep='')

    # Ustalenie, czy kwota do wypłaty jest ujemna.
    if pay < 0:
        print('Pracownik musi zwrócić')
        print('pieniądze firmie.')

# Funkcja get_sales() pobiera od użytkownika wysokość
# miesięcznej sprzedaży i zwraca tę wartość.
def get_sales():
    # Pobranie wartości miesięcznej sprzedaży.
    monthly_sales = float(input('Podaj wartość miesięcznej sprzedaży: '))

    # Zwrot podanej wartości.
    return monthly_sales

# Funkcja get_advanced_pay() pobiera wartość
# zaliczki wypłaconej danemu pracownikowi
# i zwraca ją.
def get_advanced_pay():
    # Pobranie wartości wypłaconej zaliczki.
    print('Podaj wartość wypłaconej zaliczki lub 0,')
    print('jeżeli zaliczka nie została wypłacona.')
    advanced = float(input('Wypłacona zaliczka: '))

    # Return the amount entered.
    return advanced

# Funkcja determine_comm_rate() przyjmuje
# argument w postaci wartości sprzedaży
# i zwraca procentową wysokość prowizji.
def determine_comm_rate(sales):
    # Ustalenie procentowej wysokości prowizji.
    if sales < 10000.00:
        rate = 0.10
    elif sales >= 10000 and sales <= 14999.99:
        rate = 0.12
    elif sales >= 15000 and sales <= 17999.99:
        rate = 0.14
    elif sales >= 18000 and sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18

    # Zwrot procentowej wysokości prowizji.
    return rate


