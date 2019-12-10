# Ten program tworzy etykiety w dwóch oddzielnych kontenerach.

import tkinter

class MyGUI:
    def __init__(self):
        # Utworzenie widżetu okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie dwóch kontenerów w oknie,
        # pierwszy na górze, a drugi pod nim.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Utworzenie trzech widżetów Label
        # w górnym kontenerze.
        self.label1 = tkinter.Label(self.top_frame,
                                    text='Winken')
        self.label2 = tkinter.Label(self.top_frame,
                                    text='Blinken')
        self.label3 = tkinter.Label(self.top_frame,
                                    text='Nod')

        # Ułożenie etykiet w górnym kontenerze.
        # Za pomocą argumentu side='top' zostały
        # rozmieszczone pionowo jeden po drugim.
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        # Utworzenie trzech widżetów Label
        # w dolnym kontenerze.
        self.label4 = tkinter.Label(self.bottom_frame,
                                    text='Winken')
        self.label5 = tkinter.Label(self.bottom_frame,
                                    text='Blinken')
        self.label6 = tkinter.Label(self.bottom_frame,
                                    text='Nod')

        # Ułożenie etykiet w dolnym kontenerze.
        # Za pomocą argumentu side='left' zostały
        # rozmieszczone poziomo jeden po drugim..
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        # Tak, w kontenerze również konieczne jest wywołanie metody pack()!
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Wejście do pętli głównej tkinter.
        tkinter.mainloop()

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()
