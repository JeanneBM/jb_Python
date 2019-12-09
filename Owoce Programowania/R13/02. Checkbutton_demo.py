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
