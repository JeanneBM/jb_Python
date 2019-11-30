
# Ten program wyświetla instrukcje krok po kroku
# demontażu suszarki na pranie Acme.
# Funkcja main() zawiera logikę główną programu.
def main():
    # Wyświetlenie komunikatu początkowego.
    startup_message()
    input('Naciśnij Enter, aby przejść do kroku 1.')
    # Wyświetlenie kroku 1.
    step1()
    input('Naciśnij Enter, aby przejść do kroku 2.')
    # Wyświetlenie kroku 2.
    step2()
    input('Naciśnij Enter, aby przejść do kroku 3.')
    # Wyświetlenie kroku 3.
    step3()
    input('Naciśnij Enter, aby przejść do kroku 4.')
    # Wyświetlenie kroku 4.
    step4()

# Funkcja startup_message() wyświetla na ekranie
# początkowy komunikat programu.
def startup_message():
    print('Ten program pokaże Ci,')
    print('jak zdemontować suszarkę na pranie ACME.')
    print('Proces składa się z czterech kroków.')
    print()

# Funkcja step1() wyświetla instrukcje
# dla kroku 1.
def step1():
    print('Krok 1. Odłącz suszarkę i')
    print('odsuń ją od ściany.')
    print()

# Funkcja step2() wyświetla instrukcje
# dla kroku 2.
def step2():
    print('Krok 2. Odkręć sześć śrub')
    print('z tyłu suszarki.')
    print()

# Funkcja step3() wyświetla instrukcje
# dla kroku 3.
def step3():
    print('Krok 3. Zdejmij tylny panel')
    print('suszarki.')
    print()

# Funkcja step4() wyświetla instrukcje
# dla kroku 4.
def step4():
    print('Krok 4. Pociągnij do góry')
    print('pokrywę suszarki.')

# Wywołanie funkcji main() i rozpoczęcie działania programu.
main()


