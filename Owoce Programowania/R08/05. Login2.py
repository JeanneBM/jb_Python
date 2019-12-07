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
