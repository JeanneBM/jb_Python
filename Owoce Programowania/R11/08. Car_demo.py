# Ten program pokazuje przykład użycia klasy Car.

import vehicles

def main():
    # Utworzenie obiektu na podstawie klasy Car.
    # Samochodem jest Audi z 2007 roku o przebiegu 12500
    # w cenie 21500. Ten samochód jest czterodrzwiowy.
    used_car = vehicles.Car('Audi', 2007, 12500, 21500.0, 4)

    # Wyświetlenie danych samochodu.
    print('Marka:', used_car.get_make())
    print('Model:', used_car.get_model())
    print('Przebieg:', used_car.get_mileage())
    print('Cena:', used_car.get_price())
    print('Liczba drzwi:', used_car.get_doors())

# Wywołanie funkcji main().
main()
