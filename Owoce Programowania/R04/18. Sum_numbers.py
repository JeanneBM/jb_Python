# Ten program oblicza sumę serii
# liczb podanych przez użytkownika.

MAX = 5  # Wartość maksymalna.

# Inicjalizacja zmiennej akumulatora.
total = 0.0

# Wyjaśnienie sposobu działania programu..
print('Ten program oblicza sumę')
print(MAX, 'podanych liczb.')

# Pobieranie liczb i ich sumowanie.
for counter in range(MAX):
    number = int(input('Podaj liczbę: '))
    total = total + number

# Wyświetlenie sumy bieżącej.
print('Suma wynosi', total)


