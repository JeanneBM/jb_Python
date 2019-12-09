# Ten program używa rekurencji do
# wyświetlenia liczb ciągu Fibonacciego.

def main():
    print('10 pierwszych liczb')
    print('ciągu Fibonacciego to:')

    for number in range(1, 11):
        print(fib(number))

# Funkcja fib() zwraca n-tą liczbę
# ciągu Fibonacciego.
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Wywołanie funkcji main().
main()
