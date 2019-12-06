# Ten program odczytuje wartości z pliku
# video_times.txt i oblicza ich sumę.

def main():
    # Otworzenie pliku video_times.txt do odczytu.
    video_file = open('video_times.txt', 'r')

    # Inicjalizacja akumulatora wraz z wartością 0.0.
    total = 0.0

    # Inicjalizacja zmiennej przeznaczonej do przechowywania liczby ujęć.
    count = 0

    print('Oto czasy trwania poszczególnych ujęć:')

    # Pobranie wartości z pliku i obliczenie ich sumy.
    for line in video_file:
        # Konwersja wiersza na postać wartości typu float.
        run_time = float(line)

        # Dodanie 1 do wartości zmiennej count.
        count += 1

        # Wyświetlenie czasu trwania ujęcia.
        print('Ujęcie nr ', count, ': ', run_time, sep='')

        # Dodanie czasu trwania do zmiennej total.
        total += run_time

    # Zamknięcie pliku.
    video_file.close()

    # Wyświetlenie całkowitego czasu trwania reklamy.
    print('Całkowity czas trwania reklamy wynosi', total, 'sekund.')

# Wywołanie funkcji main().
main()

