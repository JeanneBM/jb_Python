# Te program pokazuje, co się stanie
# po zmianie wartości parametru.

def main():
    value = 99
    print('Wartość wynosi', value)
    change_me(value)
    print('Wartość w funkcji main() wynosi', value)

def change_me(arg):
    print('W tym miejscu wartość zostaje zmieniona')
    arg = 0
    print('Teraz wartość wynosi', arg)

# Wywołanie funkcji main().
main()


