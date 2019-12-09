# Ten program pokazuje narysowanie dwóch owali w widżecie Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        # Utworzenie okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie widżetu Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Narysowanie dwóch owali.
        self.canvas.create_oval(20, 20, 70, 70)
        self.canvas.create_oval(100, 100, 180, 130)

        # Wywołanie metody pack() widżetu Canvas.
        self.canvas.pack()

        # Wywołanie metody mainloop() modułu tkinter.
        tkinter.mainloop()

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()
