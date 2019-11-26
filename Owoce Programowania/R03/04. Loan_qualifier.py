# Ten program ustala, czy klient banku
# ma zdolność kredytową.

MIN_SALARY = 30000.0  # Wysokość minimalnego rocznego wynagrodzenia.
MIN_YEARS = 2  # Minimalna liczba lat pracy u aktualnego pracodawcy.

# Pobranie wynagrodzenia klienta.
salary = float(input('Podaj wysokość rocznego wynagrodzenia: '))

# Pobranie liczby lat pracy u aktualnego pracodawcy.
years_on_job = int(input('Podaj liczbę lat pracy' +
                         'u obecnego pracodawcy: '))

# Ustalenie, czy klient ma zdolność kredytową.
if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print('Masz zdolność kredytową.')
    else:
        print('Musisz być zatrudniony',
              'przez przynajmniej', MIN_YEARS,
              'lata.')
else:
    print('Musisz zarabiać przynajmniej ',
          format(MIN_SALARY, '.2f'),
          ' zł rocznie.', sep='')
