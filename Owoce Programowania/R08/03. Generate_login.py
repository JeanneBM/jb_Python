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
