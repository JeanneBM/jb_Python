# Ten program pokazuje przykład użycia widżetu Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        # Utworzenie okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie widżetu Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Narysowanie dwóch linii.
        self.canvas.create_line(0, 0, 199, 199)
        self.canvas.create_line(199, 0, 0, 199)

        # Wywołanie metody pack() widżetu Canvas.
        self.canvas.pack()

        # Wywołanie metody mainloop() modułu tkinter.
        tkinter.mainloop()

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()
