# Ten program pobiera cenę detaliczną artykułu
# i oblicza cenę sprzedaży uwzględniającą 20% rabat.

# Pobranie ceny detalicznej artykułu.
original_price = float(input("Podaj cenę detaliczną artykułu: "))

# Obliczenie wysokości rabatu.
discount = original_price * 0.2

# Obliczenie ceny sprzedaży.
sale_price = original_price - discount

# Wyświetlenie ceny sprzedaży.
print('Cena sprzedaży wynosi', sale_price)
