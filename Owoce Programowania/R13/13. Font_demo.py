# Ten program pokazuje przykład wyświetlenia tekstu w widżecie Canvas.
import tkinter
import tkinter.font

class MyGUI:
    def __init__(self):
        # Utworzenie okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie widżetu Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Utworzenie obiektu Font.
        myfont = tkinter.font.Font(family='Helvetica', size=18, weight='bold')

        # Wyświetlenie tekstu.
        self.canvas.create_text(100, 100, text='Witaj, świecie', font=myfont)

        # Wywołanie metody pack() widżetu Canvas.
        self.canvas.pack()

        # Wywołanie metody mainloop() modułu tkinter.
        tkinter.mainloop()

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()

