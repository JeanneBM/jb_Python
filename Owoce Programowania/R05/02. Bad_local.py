# Zdefiniowanie funkcji main().
def main():
    get_name()
    print('Witaj,', name)      # Ten wiersz powoduje błąd!

# Zdefiniowanie funkcji get_name().
def get_name():
    name = input('Podaj imię: ')

# Wywołanie funkcji main().
main()

