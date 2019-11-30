# Ten program wyświetla pięć liczb losowych
# z przedziału od 1 do 100.
import random

def main():
    for count in range(5):
        print(random.randint(1, 100))

# Wywołanie funkcji main().
main()


