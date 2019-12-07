# Ten program pokazuje przykład użycia wielu metod ciągu tekstowego.

def main():
    # Pobranie ciągu tekstowego od użytkownika.
    user_string = input('Podaj ciąg tekstowy: ')

    print('Oto kilka informacji o podanym ciągu tekstowym:')

    # Sprawdzenie ciągu tekstowego.
    if user_string.isalnum():
        print('Ciąg tekstowy jest alfanumeryczny.')
    if user_string.isdigit():
        print('Ciąg tekstowy zawiera jedynie cyfry.')
    if user_string.isalpha():
        print('Ciąg tekstowy zawiera jedynie znaki alfabetu.')
    if user_string.isspace():
        print('Ciąg tekstowy zawiera jedynie białe znaki.')
    if user_string.islower():
        print('Ciąg tekstowy zawiera jedynie małe litery.')
    if user_string.isupper():
        print('Ciąg tekstowy zawiera jedynie duże litery.')

# Wywołanie metody main().
main()
