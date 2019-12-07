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
