# Ten program pokazuje przykłady użycia metody create_arc() w widżecie Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        self.__CANVAS_WIDTH = 320   # Długość widżetu Canvas.
        self.__CANVAS_HEIGHT = 240  # Wysokość widżetu Canvas.
        self.__X1 = 60              # Współrzędna X lewego górnego wierzchołka prostokąta.
        self.__Y1 = 20              # Współrzędna Y lewego górnego wierzchołka prostokąta.
        self.__X2 = 260             # Współrzędna X prawego dolnego wierzchołka prostokąta
        self.__Y2 = 220             # Współrzędna Y prawego dolnego wierzchołka prostokąta
        self.__PIE1_START = 0      # Kąt początkowy dla kształtu nr 1.
        self.__PIE1_WIDTH = 45     # Kąt obrotu dla kształtu nr 1.
        self.__PIE2_START = 45     # Kąt początkowy dla kształtu nr 2.
        self.__PIE2_WIDTH = 90     # Kąt obrotu dla kształtu nr 2.
        self.__PIE3_START = 135    # Kąt początkowy dla kształtu nr 3.
        self.__PIE3_WIDTH = 120    # Kąt obrotu dla kształtu nr 3.
        self.__PIE4_START = 255    # Kąt początkowy dla kształtu nr 4.
        self.__PIE4_WIDTH = 105    # Kąt obrotu dla kształtu nr 4.

        # Utworzenie okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie widżetu Canvas.
        self.canvas = tkinter.Canvas(self.main_window,
                                     width=self.__CANVAS_WIDTH,
                                     height=self.__CANVAS_HEIGHT)

        # Narysowanie kształtu nr 1.
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, self.__Y2,
                               start=self.__PIE1_START,
                               extent=self.__PIE1_WIDTH,
                               fill='red')

        # Narysowanie kształtu nr 2.
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, self.__Y2,
                               start=self.__PIE2_START,
                               extent=self.__PIE2_WIDTH,
                               fill='green')

        # Narysowanie kształtu nr 3.
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, self.__Y2,
                               start=self.__PIE3_START,
                               extent=self.__PIE3_WIDTH,
                               fill='black')

        # Narysowanie kształtu nr 4.
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, self.__Y2,
                               start=self.__PIE4_START,
                               extent=self.__PIE4_WIDTH,
                               fill='yellow')

        # Wywołanie metody pack() widżetu Canvas.
        self.canvas.pack()

        # Wywołanie metody mainloop() modułu tkinter.
        tkinter.mainloop()

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()
