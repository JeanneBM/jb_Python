01. Button_demo.py 	

# Ten program pokazuje widżet Button.
# Po jego kliknięciu przez użytkownika,
# zostanie wyświetlone informacyjne okno dialogowe.

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Utworzenie widżetu okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie widżetu Button. Tekst 'Kliknij mnie!'
        # powinien zostać wyświetlony na przycisku. Metoda
        # do_something() będzie wywołana, gdy użytkownik
        # kliknie ten widżet.
        self.my_button = tkinter.Button(self.main_window,
                                        text='Kliknij mnie!',
                                        command=self.do_something)

        # Wywołanie metody pack() widżetu.
        self.my_button.pack()

        # Wejście do pętli głównej tkinter.
        tkinter.mainloop()

    # Metoda do_something() to funkcja wywołania
    # zwrotnego dla widżetu Button.

    def do_something(self):
        # Wyświetlenie informacyjnego okna dialogowego.
        tkinter.messagebox.showinfo('Odpowiedź',
                                    'Dziękujemy za kliknięcie przycisku.')

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()

----------------------------------------------------------------------------------------------------------------------------------------------

02. Checkbutton_demo.py 	

# Ten program pokazuje grupę widżetów Checkbutton.
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Utworzenie okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie dwóch kontenerów. Jeden dla widżetów Checkbutton,
        # natomiast drugi dla zwykłych widżetów Button.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Utworzenie obiektu IntVar przeznaczonego
        # do użycia wraz z widżetami Checkbuttons.
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        # Przypisanie obiektom IntVar wartości 0.
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        # Utworzenie widżetów Checkbutton w kontenerze top_frame.
        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                       text='Opcja 1',
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text='Opcja 2',
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                       text='Opcja 3',
                                       variable=self.cb_var3)

        # Wywołanie metody pack() widżetów Checkbutton.
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        # Utworzenie przycisków OK i Zakończ.
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='OK',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Zakończ',
                                          command=self.main_window.destroy)

        # Wywołanie metody pack() widżetów Button.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Wywołanie metody pack() kontenerów.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Wywołanie metody mainloop() modułu tkinter.
        tkinter.mainloop()

    # Metoda show_choice() jest funkcją
    # wywołania zwrotnego dla przycisku OK.

    def show_choice(self):
        # Utworzenie ciągu tekstowego zawierającego komunikat.
        self.message = 'Wybrane opcje:\n'

        # Ustalenie zaznaczonego pola wyboru i odpowiednie
        # przygotowanie ciągu tekstowego komunikatu.
        if self.cb_var1.get() == 1:
            self.message = self.message + '1\n'
        if self.cb_var2.get() == 1:
            self.message = self.message + '2\n'
        if self.cb_var3.get() == 1:
            self.message = self.message + '3\n'

        # Wyświetlenie komunikatu w informacyjnym oknie dialogowym.
        tkinter.messagebox.showinfo('Wybór', self.message)

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()

----------------------------------------------------------------------------------------------------------------------------------------------

03. Draw_arc.py 	

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

----------------------------------------------------------------------------------------------------------------------------------------------

04. Draw_line.py 	

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

----------------------------------------------------------------------------------------------------------------------------------------------

05. Draw_multilines.py 	

# Ten program łączy linią wiele punktów.
import tkinter

class MyGUI:
    def __init__(self):
        # Utworzenie okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie widżetu Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Narysowanie linii łączącej wiele punktów.
        self.canvas.create_line(10, 10, 189, 10, 100, 189, 10, 10)

        # Wywołanie metody pack() widżetu Canvas.
        self.canvas.pack()

        # Wywołanie metody mainloop() modułu tkinter.
        tkinter.mainloop()

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()

----------------------------------------------------------------------------------------------------------------------------------------------

06. Draw_ovals.py 	

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

----------------------------------------------------------------------------------------------------------------------------------------------

07. Draw_piechart.py 	

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

----------------------------------------------------------------------------------------------------------------------------------------------

08. Draw_polygon.py 

# Ten program pokazuje przykład narysowania wielokąta w widżecie Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        # Utworzenie okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie widżetu Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=160, height=160)

        # Narysowanie wielokąta.
        self.canvas.create_polygon(60, 20, 100, 20, 140, 60, 140, 100,
                                   100, 140, 60, 140, 20, 100, 20, 60)

        # Wywołanie metody pack() widżetu Canvas.
        self.canvas.pack()

        # Wywołanie metody mainloop() modułu tkinter.
        tkinter.mainloop()

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()

----------------------------------------------------------------------------------------------------------------------------------------------

09. Draw_square.py 

# Ten program rysuje prostokąt w widżecie Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        # Utworzenie okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie widżetu Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Narysowanie prostokąta.
        self.canvas.create_rectangle(20, 20, 180, 180)

        # Wywołanie metody pack() widżetu Canvas.
        self.canvas.pack()

        # Wywołanie metody mainloop() modułu tkinter.
        tkinter.mainloop()

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()

----------------------------------------------------------------------------------------------------------------------------------------------

10. Draw_text.py 

# Ten program pokazuje przykład wyświetlenia tekstu w widżecie Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        # Utworzenie okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie widżetu Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Wyświetlenie tekstu na środku okna.
        self.canvas.create_text(100, 100, text='Witaj, świecie!')

        # Wywołanie metody pack() widżetu Canvas.
        self.canvas.pack()

        # Wywołanie metody mainloop() modułu tkinter.
        tkinter.mainloop()

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()

----------------------------------------------------------------------------------------------------------------------------------------------

11. Empty_window.py 	

# Ten program wyświetla puste okno.

import tkinter

def main():
    # Utworzenie widżetu okna głównego.
    main_window = tkinter.Tk()

    # Wejście do pętli głównej tkinter.
    tkinter.mainloop()

# Wywołanie funkcji main().
main()

----------------------------------------------------------------------------------------------------------------------------------------------

12. Empty_window2.py 

# Ten program wyświetla puste okno.

import tkinter

class MyGUI:
    def __init__(self):
        # Utworzenie widżetu okna głównego.
        self.main_window = tkinter.Tk()

        # Wejście do pętli głównej tkinter.
        tkinter.mainloop()

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()

----------------------------------------------------------------------------------------------------------------------------------------------

13. Font_demo.py 	

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

----------------------------------------------------------------------------------------------------------------------------------------------

14. Frame_demo.py 	

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

----------------------------------------------------------------------------------------------------------------------------------------------

15. Hello_world.py 

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

----------------------------------------------------------------------------------------------------------------------------------------------

16. Hello_world2.py 	

# Ten program wyświetla dwie etykiety wraz z tekstem.

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
        self.label1.pack()
        self.label2.pack()

        # Wejście do pętli głównej tkinter.
        tkinter.mainloop()

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()

----------------------------------------------------------------------------------------------------------------------------------------------

17. Hello_world3.py 

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

----------------------------------------------------------------------------------------------------------------------------------------------

18. Kilo_converter.py 	

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

----------------------------------------------------------------------------------------------------------------------------------------------

19. Kilo_converter2.py 	

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

----------------------------------------------------------------------------------------------------------------------------------------------

20. Quit_button.py 

# Ten program ma przycisk kończący działanie aplikacji.
# Po kliknięciu ten przycisk wywołuje metodę destroy() klasy Tk.

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Utworzenie widżetu okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie widżetu Button. Tekst 'Kliknij mnie!'
        # powinien zostać wyświetlony na przycisku. Metoda
        # do_something() będzie wywołana, gdy użytkownik
        # kliknie ten widżet.
        self.my_button = tkinter.Button(self.main_window,
                                        text='Kliknij mnie!',
                                        command=self.do_something)

        # Utworzenie przycisku zamykającego program. Po jego kliknięciu
        # nastąpi wywołanie metody destroy() widżetu głównego.
        # (Zmienna main_window odwołuje się do widżetu głównego,
        # więc funkcją wywołania zwrotnego jest self.main_window.destroy()).
        self.quit_button = tkinter.Button(self.main_window,
                                          text='Zakończ',
                                          command=self.main_window.destroy)

        # Wywołanie metody pack() widżetu.
        self.my_button.pack()
        self.quit_button.pack()

        # Wejście do pętli głównej tkinter.
        tkinter.mainloop()

    # Metoda do_something() to funkcja wywołania
    # zwrotnego dla widżetu Button.

    def do_something(self):
        # Wyświetlenie informacyjnego okna dialogowego.
        tkinter.messagebox.showinfo('Odpowiedź',
                                    'Dziękujemy za kliknięcie przycisku.')

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()

----------------------------------------------------------------------------------------------------------------------------------------------

21. Radiobutton_demo.py 	

# Ten program pokazuje użycie grupy widżetów Radiobutton.
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Utworzenie okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie dwóch kontenerów. Jeden dla widżetów Radiobutton,
        # natomiast drugi dla zwykłych widżetów Button.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Utworzenie obiektu IntVar przeznaczonego
        # do użycia wraz z widżetami Radiobutton.
        self.radio_var = tkinter.IntVar()

        # Przypisanie obiektowi IntVar wartości 1.
        self.radio_var.set(1)

        # Utworzenie widżetów Radiobutton w kontenerze top_frame.
        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Opcja 1',
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Opcja 2',
                                       variable=self.radio_var,
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Opcja 3',
                                       variable=self.radio_var,
                                       value=3)

        # Wywołanie metody pack() widżetów Radiobutton.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Utworzenie przycisków OK i Zakończ.
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='OK',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Zakończ',
                                          command=self.main_window.destroy)

        # Wywołanie metody pack() widżetów Button.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Wywołanie metody pack() kontenerów.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Wywołanie metody mainloop() modułu tkinter.
        tkinter.mainloop()

    # Metoda show_choice() jest funkcją
    # wywołania zwrotnego dla przycisku OK.
    def show_choice(self):
        tkinter.messagebox.showinfo('Wybór', 'Wybrałeś opcję ' +
                                    str(self.radio_var.get()))

# Utworzenie egzemplarza klasy MyGUI.
my_gui = MyGUI()

----------------------------------------------------------------------------------------------------------------------------------------------

22. Test_averages.py

# Ten program używa GUI do pobrania wyników
# z trzech sprawdzianów i wyświetlenia ich średniej.

import tkinter

class TestAvg:
    def __init__(self):
        # Utworzenie okna głównego.
        self.main_window = tkinter.Tk()

        # Utworzenie pięciu kontenerów.
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Utworzenie widżetów dla kontenera sprawdzianu nr 1. i wywołanie ich metod pack().
        self.test1_label = tkinter.Label(self.test1_frame,
                                         text='Podaj wynik ze sprawdzianu nr 1:')
        self.test1_entry = tkinter.Entry(self.test1_frame,
                                         width=10)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')

        # Utworzenie widżetów dla kontenera sprawdzianu nr 2. i wywołanie ich metod pack().
        self.test2_label = tkinter.Label(self.test2_frame,
                                         text='Podaj wynik ze sprawdzianu nr 2:')
        self.test2_entry = tkinter.Entry(self.test2_frame,
                                         width=10)
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')

        # Utworzenie widżetów dla kontenera sprawdzianu nr 3. i wywołanie ich metod pack().
        self.test3_label = tkinter.Label(self.test3_frame,
                                         text='Podaj wynik ze sprawdzianu nr 3:')
        self.test3_entry = tkinter.Entry(self.test3_frame,
                                         width=10)
        self.test3_label.pack(side='left')
        self.test3_entry.pack(side='left')

        # Utworzenie widżetów dla kontenera wyświetlającego średnią. i wywołanie ich metod pack().
        self.result_label = tkinter.Label(self.avg_frame,
                                          text='Średnia:')
        self.avg = tkinter.StringVar()  # Aby uaktualnić widżet avg_label.
        self.avg_label = tkinter.Label(self.avg_frame,
                                       textvariable=self.avg)
        self.result_label.pack(side='left')
        self.avg_label.pack(side='left')

        # Utworzenie widżetów dla kontenera przycisków i wywołanie ich metod pack().
        self.calc_button = tkinter.Button(self.button_frame,
                                          text='Średnia',
                                          command=self.calc_avg)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Zakończ',
                                          command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Wywołanie metody pack() kontenerów.
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        # Wywołanie metody mainloop() modułu tkinter.
        tkinter.mainloop()

    # Metoda calc_avg() jest funkcją wywołania
    # zwrotnego dla widżetu calc_button.

    def calc_avg(self):
        # Pobranie wyników ze trzech sprawdzianów
        # i umieszczenie ich w zmiennych.
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())

        # Obliczenie średniego wyniku.
        self.average = (self.test1 + self.test2 +
                        self.test3) / 3.0

        # Uaktualnienie widżetu avg_label przez umieszczenie
        # wartości zmiennej self.average w obiekcie StringVar
        # wskazywanym przez avg.
        self.avg.set(self.average)

# Utworzenie egzemplarza klasy TestAvg.
test_avg = TestAvg()

----------------------------------------------------------------------------------------------------------------------------------------------

