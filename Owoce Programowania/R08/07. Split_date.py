# Ten program wywołuje metodę split()
# wraz z separatorem w postaci znaku '/'.

def main():
    # Utworzenie ciągu tekstowego zawierającego datę.
    date_string = '26/11/2018'

    # Podział ciągu tekstowego.
    date_list = date_string.split('/')

    # Wyświetlenie poszczególnych elementów daty.
    print('dzień:', date_list[0])
    print('miesiąc:', date_list[1])
    print('rok:', date_list[2])

# Wywołanie funkcji main().
main()
