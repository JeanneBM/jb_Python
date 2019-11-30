# Ten program pomaga pracownikowi w procesie
# sprawdzania temperatury substancji.

# Stała nazwana przedstawiająca
# temperaturę maksymalną.
MAX_TEMP = 102.5

# Pobranie temperatury substancji.
temperature = float(input("Podaj w Celsjuszach temperaturę substancji: "))

# Dopóki to konieczne, trzeba nakazać
# użytkownikowi dostosowanie termostatu.
while temperature > MAX_TEMP:
    print('Temperatura jest zbyt wysoka.')
    print('Wyłącz termostat i odczekaj')
    print('5 minut. Następnie ponownie sprawdź')
    print('temperaturę i wpisz ją tutaj.')
    temperature = float(input('Ponownie podaj w Celsjuszach temperaturę substancji: '))

# Przypomnienie użytkownikowi o konieczności
# ponownego sprawdzenia temperatury w ciągu 15 minut.
print('Temperatura jest do zaakceptowania.')
print('Sprawdź ją ponownie w ciągu 15 minut.')

