# Ten program używa argumentu side='left' metody
# pack(), aby zmienić układ ułożenia etykiet.

import tkinter

class MyGUI:
    def __init__(self):
        # Utworzenie widżetu okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie dwóch widżetów Label.
        self.label1 = tkinter.Label(self.main_window,
                                    text='Witaj, świecie!')
        self.label2 = tkinter.Label(self.main_window,
                                    text='To jest program wraz z GUI.')

        # Wywołanie metody pack() w obu widżetach Label.
        self.label1.pack(side='left')
        self.label2.pack(side='left')

        # Wejście do pętli głównej tkinter.
        tkinter.mainloop()

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()
