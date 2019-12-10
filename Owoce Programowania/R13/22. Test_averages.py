# Ten program używa GUI do pobrania wyników
# z trzech sprawdzianów i wyświetlenia ich średniej.

import tkinter

class TestAvg:
    def __init__(self):
        # Utworzenie okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie pięciu kontenerów.
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Utworzenie widżetów dla kontenera sprawdzianu nr 1. i wywołanie ich metod pack().
        self.test1_label = tkinter.Label(self.test1_frame,
                                         text='Podaj wynik ze sprawdzianu nr 1:')
        self.test1_entry = tkinter.Entry(self.test1_frame,
                                         width=10)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')

        # Utworzenie widżetów dla kontenera sprawdzianu nr 2. i wywołanie ich metod pack().
        self.test2_label = tkinter.Label(self.test2_frame,
                                         text='Podaj wynik ze sprawdzianu nr 2:')
        self.test2_entry = tkinter.Entry(self.test2_frame,
                                         width=10)
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')

        # Utworzenie widżetów dla kontenera sprawdzianu nr 3. i wywołanie ich metod pack().
        self.test3_label = tkinter.Label(self.test3_frame,
                                         text='Podaj wynik ze sprawdzianu nr 3:')
        self.test3_entry = tkinter.Entry(self.test3_frame,
                                         width=10)
        self.test3_label.pack(side='left')
        self.test3_entry.pack(side='left')

        # Utworzenie widżetów dla kontenera wyświetlającego średnią. i wywołanie ich metod pack().
        self.result_label = tkinter.Label(self.avg_frame,
                                          text='Średnia:')
        self.avg = tkinter.StringVar()  # Aby uaktualnić widżet avg_label.
        self.avg_label = tkinter.Label(self.avg_frame,
                                       textvariable=self.avg)
        self.result_label.pack(side='left')
        self.avg_label.pack(side='left')

        # Utworzenie widżetów dla kontenera przycisków i wywołanie ich metod pack().
        self.calc_button = tkinter.Button(self.button_frame,
                                          text='Średnia',
                                          command=self.calc_avg)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Zakończ',
                                          command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Wywołanie metody pack() kontenerów.
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        # Wywołanie metody mainloop() modułu tkinter.
        tkinter.mainloop()

    # Metoda calc_avg() jest funkcją wywołania
    # zwrotnego dla widżetu calc_button.

    def calc_avg(self):
        # Pobranie wyników ze trzech sprawdzianów
        # i umieszczenie ich w zmiennych.
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())

        # Obliczenie średniego wyniku.
        self.average = (self.test1 + self.test2 +
                        self.test3) / 3.0

        # Uaktualnienie widżetu avg_label przez umieszczenie
        # wartości zmiennej self.average w obiekcie StringVar
        # wskazywanym przez avg.
        self.avg.set(self.average)

# Utworzenie egzemplarza klasy TestAvg.
test_avg = TestAvg()
