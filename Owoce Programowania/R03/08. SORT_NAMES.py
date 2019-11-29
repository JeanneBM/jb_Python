# Ten program porównuje ciągi tekstowe za pomocą operatora <.
# Pobranie dwóch ciągów tekstowych od użytkownika.
name1 = input('Podaj imię i nazwisko (nazwisko pierwsze): ')
name2 = input('Podaj kolejne imię i nazwisko (nazwisko pierwsze): ')

# Wyświetlenie danych w kolejności alfabetycznej.
print('Oto posortowana alfabetycznie lista osób.')

if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)
