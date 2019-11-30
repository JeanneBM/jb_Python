# Ten program używa pętli do wyświetlenia
# tabeli liczb i ich kwadratów.

# Pobranie wartości początkowej sekwencji liczb.
print('Ten program wyświetla listę liczb')
print('i ich kwadraty.')
start = int(input('Podaj wartość początkową: '))

# Pobranie wartości maksymalnej sekwencji liczb.
end = int(input('Podaj wartość maksymalną: '))

# Wyświetlenie nagłówków tabeli.
print()
print('Liczba\tKwadrat')
print('--------------')

# Wyświetlenie liczb i ich kwadratów.
for number in range(start, end + 1):
    square = number**2
    print(number, '\t', square)


