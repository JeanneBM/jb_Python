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
