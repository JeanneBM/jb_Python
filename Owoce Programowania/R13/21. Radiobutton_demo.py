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
