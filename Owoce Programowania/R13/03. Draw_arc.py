# Ten program pokazuje przykład narysowania wycinka koła w widżetcie Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        # Utworzenie okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie widżetu Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Narysowanie wycinka koła.
        self.canvas.create_arc(10, 10, 190, 190, start=45, extent=30)

        # Wywołanie metody pack() widżetu Canvas.
        self.canvas.pack()

        # Wywołanie metody mainloop() modułu tkinter.
        tkinter.mainloop()

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()
