# Ten program tworzy obiekty
# klas Car, Truck i SUV.

import vehicles

def main():
    # Utworzenie obiektu Car przedstawiającego
    # używane czterodrzwiowe BMW z roku 2001
    # o przebiegu 70000 i cenie 15000.
    car = vehicles.Car('BMW', 2001, 70000, 15000.0, 4)

    # Utworzenie obiektu Truck przedstawiającego
    # używaną Toyotę o przebiegu 40000 w cenie
    # 12000 oraz z napędem na cztery koła.
    truck = vehicles.Truck('Toyota', 2002, 40000, 12000.0, '4WD')

    # Utworzenie obiektu SUV przedstawiającego
    # używane pięciomiejscowe Volvo z roku 2000
    # o przebiegu 30000 i cenie 18500.
    suv = vehicles.SUV('Volvo', 2000, 30000, 18500.0, 5)

    print('DOSTĘPNE SAMOCHODY UŻYWANE')
    print('==========================')

    # Wyświetlenie danych samochodu osobowego.
    print('W ofercie jest następujący samochód osobowy:')
    print('Marka:', car.get_make())
    print('Model:', car.get_model())
    print('Przebieg:', car.get_mileage())
    print('Cena:', car.get_price())
    print('Liczba drzwi:', car.get_doors())
    print()

    # Wyświetlenie danych samochodu terenowego.
    print('W ofercie jest następujący samochód terenowy:')
    print('Marka:', truck.get_make())
    print('Model:', truck.get_model())
    print('Przebieg:', truck.get_mileage())
    print('Cena:', truck.get_price())
    print('Drive type:', truck.get_drive_type())
    print()

    # Wyświetlenie danych samochodu typu SUV.
    print('W ofercie jest następujący samochód typu SUV:')
    print('Marka:', suv.get_make())
    print('Model:', suv.get_model())
    print('Przebieg:', suv.get_mileage())
    print('Cena:', suv.get_price())
    print('Passenger Capacity:', suv.get_pass_cap())

# Wywołanie funkcji main().
main()

