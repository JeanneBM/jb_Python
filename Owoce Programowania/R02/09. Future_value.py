# Pobranie kwoty końcowej, która ma zostać zebrana na rachunku.
future_value = float(input('Podaj kwotę, jaką chcesz uzyskać na rachunku: '))

# Pobranie stopy rocznego oprocentowania rachunku.
rate = float(input('Podaj stopę oprocentowania rachunku: '))

# Pobranie liczby lat, przez które pieniądze mają być ulokowane na rachunku.
years = int(input('Przez ile lat chcesz trzymać pieniądze na rachunku? '))

# Obliczenie kwoty, którą trzeba przelać na rachunek.
present_value = future_value / (1.0 + rate)**years

# Wyświetlenie kwoty, którą trzeba przelać na rachunek.
print('Musisz przelać na rachunek', present_value, 'zł.')
