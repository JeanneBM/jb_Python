# Ten program zawiera funkcję rekurencyjną.

def main():
    # Przekazanie funkcji message() argumentu
    # w postaci liczby całkowitej 5 powoduje,
    # że zostanie ona wywołana pięciokrotnie.
    message(5)

def message(times):
    if times > 0:
        print('To jest funkcja rekurencyjna.')
        message(times - 1)

# Wywołanie funkcji main().
main()
