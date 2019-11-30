# Ten program używa pętli do wyświetlenia
# tabeli zawierającej liczby od 1 do 10
# i ich kwadraty.

# Wyświetlenie nagłówków tabeli.
print('Liczba\tKwadrat')
print('--------------')

# Wyświetlenie liczb od 1 do 10
# i ich kwadratów.
for number in range(1, 11):
    square = number**2
    print(number, '\t', square)

