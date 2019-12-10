# Ten program wyświetla etykietę wraz z tekstem.

import tkinter

class MyGUI:
    def __init__(self):
        # Utworzenie widżetu okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie widżetu Label zawierającego
        # komunikat 'Witaj, świecie!'
        self.label = tkinter.Label(self.main_window,
                                   text='Witaj, świecie!')

        # Wywołanie metody pack() widżetu Label.
        self.label.pack()

        # Wejście do pętli głównej tkinter.
        tkinter.mainloop()

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()
