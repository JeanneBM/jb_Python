# Ten program ustala, czy klient banku
# ma zdolność kredytową.

MIN_SALARY = 30000.0  # Wysokość minimalnego rocznego wynagrodzenia.
MIN_YEARS = 2  # Minimalna liczba lat pracy u aktualnego pracodawcy.

# Pobranie wynagrodzenia klienta.
salary = float(input('Podaj wysokość rocznego wynagrodzenia: '))

# Pobranie liczby lat pracy u aktualnego pracodawcy.
years_on_job = int(input('Podaj liczbę lat pracy ' +
                         'u obecnego pracodawcy: '))

# Ustalenie, czy klient ma zdolność kredytową.
if salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
    print('Masz zdolność kredytową.')
else:
    print('Nie masz zdolności kredytowej.')
