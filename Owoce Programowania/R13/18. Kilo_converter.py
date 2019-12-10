# Ten program odległość wyrażoną w kilometrach
# konwertuje na mile. Wynik zostanie wyświetlony
# w informacyjnym oknie dialogowym.

import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):

        # Utworzenie okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie dwóch kontenerów do grupowania widżetów.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Utworzenie widżetów w górnym kontenerze.
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text='Podaj odległość w kilometrach:')
        self.kilo_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        # Wywołanie metod pack() widżetów w górnym kontenerze.
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

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

        # Wyświetlenie wyniku w informacyjnym oknie dialogowym.
        tkinter.messagebox.showinfo('Wynik',
                                    str(kilo) +
                                    ' kilometrów to ' +
                                    str(miles) + ' mil.')

# Utworzenie egzemplarza klasy KiloConverterGUI.
kilo_conv = KiloConverterGUI()
