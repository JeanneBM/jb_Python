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
