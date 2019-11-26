# Pobranie od użytkownika całkowitej liczby sekund.
total_seconds = float(input('Podaj liczbę sekund: '))

# Obliczenie liczby godzin.
hours = total_seconds // 3600.

# Obliczenie liczby pozostałych minut.
minutes = (total_seconds // 60) % 60

# Obliczenie liczby pozostałych sekund.
seconds = total_seconds % 60

# Wyświetlenie wyniku.
print('Podana liczba sekund wyrażona w godzinach, minutach i sekundach:')
print('Godziny:', hours)
print('Minuty:', minutes)
print('Sekundy:', seconds)
