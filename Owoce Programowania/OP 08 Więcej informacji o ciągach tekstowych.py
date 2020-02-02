01. Concatenate.py 	

# Ten program pokazuje konkatenację ciągów tekstowych.

def main():
    name = 'Karina'
    print('Imię to', name)
    name = name + ' Malinowska'
    print('Teraz imię i nazwisko to', name)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

02. Count_Ts.py 	

# Ten program zlicza ilość wystąpień
# litery T (zarówno małej, jak i dużej)
# w podanym ciągu tekstowym.

def main():
    # Utworzenie zmiennej do obsługi licznika pętli.
    # Ta zmienna musi mieć wartość początkową 0.
    count = 0

    # Pobranie ciągu tekstowego od użytkownika.
    my_string = input('Podaj dowolne zdanie: ')

    # Zliczenie wystąpień litery T.
    for ch in my_string:
        if ch == 'T' or ch == 't':
            count += 1

    # Wyświetlenie wyniku.
    print('Litera T wystąpiła', count, 'razy.')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

03. Generate_login.py 	

# Ten program pobiera imię, nazwisko i numer
# identyfikacyjny studenta. Następnie te dane są
# używane do wygenerowania nazwy użytkownika.

import login

def main():
    # Pobranie imienia, nazwiska i numeru identyfikacyjnego studenta.
    first = input('Podaj imię: ')
    last = input('Podaj nazwisko: ')
    idnumber = input('Podaj numer identyfikacyjny: ')

    # Wyświetlenie wygenerowanej nazwy użytkownika.
    print('Twoja nazwa użytkownika to:')
    print(login.get_login_name(first, last, idnumber))

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

04. Login1.py 	

# Funkcja get_login_name() akceptuje argumenty w postaci
# imienia, nazwiska i numeru identyfikacyjnego. Jej wartością
# zwrotną jest wygenerowana nazwa użytkownika.

def get_login_name(first, last, idnumber):
    # Pobranie trzech pierwszych liter imienia.
    # Jeżeli imię jest krótsze niż trzy znaki,
    # wycinek zwróci je w całości.
    set1 = first[0:3]

    # Pobranie trzech pierwszych liter nazwiska.
    # Jeżeli nazwisko jest krótsze niż trzy znaki,
    # wycinek zwróci je w całości.
    set2 = last[0:3]

    # Pobranie trzech ostatnich znaków numeru identyfikacyjnego.
    # Jeżeli numer identyfikacyjny jest krótszy niż trzy znaki,
    # wycinek zwróci go w całości.
    set3 = idnumber[-3:]

    # Połączenie ze sobą zbiorów znaków.
    login_name = set1 + set2 + set3

    # Zwrot nazwy użytkownika.
    return login_name
  
----------------------------------------------------------------------------------------------------------------------------------------------

05. Login2.py 	

# Funkcja get_login_name() akceptuje argumenty w postaci
# imienia, nazwiska i numeru identyfikacyjnego. Jej wartością
# zwrotną jest wygenerowana nazwa użytkownika.

def get_login_name(first, last, idnumber):
    # Pobranie trzech pierwszych liter imienia.
    # Jeżeli imię jest krótsze niż trzy znaki,
    # wycinek zwróci je w całości.
    set1 = first[0:3]

    # Pobranie trzech pierwszych liter nazwiska.
    # Jeżeli nazwisko jest krótsze niż trzy znaki,
    # wycinek zwróci je w całości.
    set2 = last[0:3]

    # Pobranie trzech ostatnich znaków numeru identyfikacyjnego.
    # Jeżeli numer identyfikacyjny jest krótszy niż trzy znaki,
    # wycinek zwróci go w całości.
    set3 = idnumber[-3:]

    # Połączenie ze sobą zbiorów znaków.
    login_name = set1 + set2 + set3

    # Zwrot nazwy użytkownika.
    return login_name

# Funkcja valid_password() akceptuje argument
# w postaci hasła i zwraca wartość True lub False,
# wskazując, czy hasło jest prawidłowe. Aby było
# prawidłowe, musi mieć przynajmniej 7 znaków
# oraz co najmniej po jednej dużej i małej literze,
# a także powinno zawierać cyfrę.

def valid_password(password):
    # Przypisanie wartości False zmiennym boolowskim.
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Rozpoczęcie weryfikacji hasła. Na początku
    # sprawdzana jest jego długość.
    if len(password) >= 7:
        correct_length = True

        # Trzeba sprawdzić każdy znak
        # i przypisać odpowiednią wartość
        # po znalezieniu wymaganego znaku.
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True

    # Ustalenie, czy wszystkie wymagania zostały spełnione.
    # Jeżeli tak, zmienna is_valid będzie miała wartość True.
    # W przeciwnym razie wartością zmiennej is_valid jest False.
    if correct_length and has_uppercase and \
            has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False

    # Zwrot zmiennej is_valid.
    return is_valid
  
----------------------------------------------------------------------------------------------------------------------------------------------

06. Repetition_operator.py 

# Ten program pokazuje przykład użycia operatora powtarzania.

def main():
    # Wyświetlenie dziewięciu wierszy, z których każdy jest coraz dłuższy.
    for count in range(1, 10):
        print('Z' * count)

    # Wyświetlenie dziewięciu wierszy, z których każdy jest coraz krótszy.
    for count in range(8, 0, -1):
        print('Z' * count)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

07. Split_date.py 	

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

----------------------------------------------------------------------------------------------------------------------------------------------

08. String_split.py 	

# Ten program pokazuje przykład użycia metody split().

def main():
    # Utworzenie ciągu tekstowego wraz z wieloma słowami.
    my_string = 'jeden dwa trzy cztery'

    # Podział ciągu tekstowego.
    word_list = my_string.split()

    # Wyświetlenie listy słów.
    print(word_list)

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

09. String_test.py 	

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

----------------------------------------------------------------------------------------------------------------------------------------------

10. Validate_password.py

# Ten program pobiera od użytkownika
# hasło i sprawdza je.

import login

def main():
    # Pobranie hasła od użytkownika.
    password = input('Podaj hasło: ')

    # Validate the password.
    while not login.valid_password(password):
        print('Hasło jest nieprawidłowe.')
        password = input('Podaj hasło: ')

    print('Hasło jest prawidłowe.')

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------
