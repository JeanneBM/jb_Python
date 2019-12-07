# Ten program pokazuje różne operacje przeprowadzane na zbiorach.
baseball = set(['Justyna', 'Celina', 'Ada', 'Alicja'])
basketball = set(['Ewa', 'Celina', 'Alicja', 'Sara'])

# Wyświetlenie elementów zbioru baseball.
print('Oto osoby grające w drużynie bejsbolowej:')
for name in baseball:
    print(name)

# Wyświetlenie elementów zbioru basketball.
print()
print('Oto osoby grające w drużynie koszykówki:')
for name in basketball:
    print(name)

# Część wspólna zbiorów.
print()
print('Oto osoby grające w obu drużynach:')
for name in baseball.intersection(basketball):
    print(name)

# Unia zbiorów.
print()
print('Oto osoby grające w jednej z drużyn:')
for name in baseball.union(basketball):
    print(name)

# Różnica między zbiorami baseball i basketball.
print()
print('Oto osoby grające w drużynie bejsbolowej, ale nie w drużynie koszykówki:')
for name in baseball.difference(basketball):
    print(name)

# Różnica między zbiorami basketball i baseball.
print()
print('Oto osoby grające w drużynie koszykówki, ale nie w drużynie bejsbolowej:')
for name in basketball.difference(baseball):
    print(name)

# Różnica symetryczna.
print()
print('Oto osoby grające w jednej drużynie, ale nie w obu:')
for name in baseball.symmetric_difference(basketball):
    print(name)
