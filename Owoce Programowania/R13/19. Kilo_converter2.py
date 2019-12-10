# Ten odległość wyrażoną w kilometrach
# konwertuje na mile. Wynik zostanie
# wyświetlony w etykiecie okna głównego.

import tkinter

class KiloConverterGUI:
    def __init__(self):

        # Utworzenie okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie trzech kontenerów do grupowania widżetów.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Utworzenie widżetów w górnym kontenerze.
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text='Podaj odległość w kilometrach:')
        self.kilo_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        # Wywołanie metod pack() widżetów w górnym kontenerze.
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        # Utworzenie widżetów w środkowym kontenerze.
        self.descr_label = tkinter.Label(self.mid_frame,
                                         text='Po konwersji na mile:')

        # Konieczne jest powiązanie obiektu StringVar z etykietą
        # danych wyjściowych. Metoda set() obiektu będzie
        # użyta do przechowywania pustego ciągu tekstowego.
        self.value = tkinter.StringVar()

        # Utworzenie etykiety i powiązanie jej
        # z obiektem StringVar. Każda wartość
        # przechowywana w tym obiekcie zostanie
        # automatycznie wyświetlona w etykiecie.
        self.miles_label = tkinter.Label(self.mid_frame,
                                         textvariable=self.value)

        # Wywołanie metod pack() widżetów w środkowym kontenerze.
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

        # Utworzenie widżetów Button w dolnym kontenerze.
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Konwertuj',
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Zakończ',
                                          command=self.main_window.destroy)

        # Wywołanie metody pack() przycisków.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Wywołanie metody pack() kontenerów.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Wejście do pętli głównej tkinter.
        tkinter.mainloop()

    # Metoda convert() jest funkcją wywołania
    # zwrotnego przycisku Konwertuj.

    def convert(self):
        # Pobranie wartości wprowadzonej
        # przez użytkownika w widżecie kilo_entry.
        kilo = float(self.kilo_entry.get())

        # Konwersja kilometrów na mile.
        miles = kilo * 0.6214

        # Konwersja wartości miles na postać ciągu tekstowego
        # i umieszczenie jej w obiekcie StringVal. To spowoduje
        # automatyczne uaktualnienie widżetu miles_label.
        self.value.set(miles)

# Utworzenie egzemplarza klasy KiloConverterGUI.
kilo_conv = KiloConverterGUI()
