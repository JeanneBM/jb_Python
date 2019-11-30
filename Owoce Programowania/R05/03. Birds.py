# Ten program pokazuje, że dwie funkcje mogą
# mieć zmienne lokalne o tej samej nazwie.

def main():
    # Wywołanie funkcji texas().
    texas()
    # Wywołanie funkcji california()
    california()

# Definicja funkcji texas(). Tworzy ona
# zmienną lokalną o nazwie birds.
def texas():
    birds = 5000
    print('Teksas ma', birds, 'gatunków ptaków.')

# Definicja funkcji california(). Ona również
# tworzy zmienną lokalną o nazwie birds.
def california():
    birds = 8000
    print('Kalifornia ma', birds, 'gatunków ptaków.')

# Wywołanie funkcji main().
main()


