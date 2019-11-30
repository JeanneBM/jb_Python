# Ten program wyświetla pięć liczb losowych
# z przedziału od 1 do 100.
import random

def main():
    for count in range(5):
        # Wygenerowanie liczby losowej.
        number = random.randint(1, 100)
        # Wyświetlenie wygenerowanej liczby.
        print(number)

# Wywołanie funkcji main().
main()


