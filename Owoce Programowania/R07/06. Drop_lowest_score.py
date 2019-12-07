# Ten program pobiera serię wyników ze sprawdzianów,
# a następnie oblicza średnią po wcześniejszym odrzuceniu
# najniższego wyniku.

def main():
    # Pobranie od użytkownika wyników sprawdzianów.
    scores = get_scores()

    # Obliczenie sumy wszystkich wyników.
    total = get_total(scores)

    # Pobranie najniższego wyniku ze sprawdzianu.
    lowest = min(scores)

    # Odjęcie od obliczonej sumy najniższego wyniku ze sprawdzianu.
    total -= lowest

    # Obliczenie średniej. Zwróć uwagę na podzielenie
    # sumy przez liczbę o jeden mniejszą od liczby wyników,
    # ponieważ został odrzucony najniższy.
    average = total / (len(scores) - 1)

    # Wyświetlenie obliczonej średniej.
    print('Po odrzuceniu najniższego wyniku',
          'średnia wynosi:', average)

# Funkcja get_scores() pobiera od użytkownika serię
# wyników ze sprawdzianów i umieszcza je na liście.
# Wartością zwrotną funkcji jest odwołanie do listy.
def get_scores():
    # Utworzenie pustej listy.
    test_scores = []

    # Utworzenie zmiennej kontrolującej działanie pętli.
    again = 't'

    # Pobranie od użytkownika wyników ze
    # sprawdzianów i umieszczenie ich na liście.
    while again == 't':
        # Pobranie wyniku ze sprawdzianu i umieszczenie go na liście.
        value = float(input('Podaj wynik ze sprawdzianu: '))
        test_scores.append(value)

        # Czy będzie podany kolejny wynik?
        print('Czy chcesz podać kolejny wynik?')
        again = input('Jeśli tak, wpisz t, w przeciwnym razie wpisz inny znak: ')
        print()

    # Zwrot listy.
    return test_scores

# Funkcja get_total() akceptuje argument
# w postaci listy i zwraca wartość całkowitą
# elementów znajdujących się na liście.
def get_total(value_list):
    # Utworzenie zmiennej przeznaczonej do użycia w charakterze akumulatora.
    total = 0.0

    # Obliczenie sumy wszystkich elementów listy.
    for num in value_list:
        total += num

    # Zwrot wartości zmiennej total.
    return total

# Wywołanie funkcji main().
main()
