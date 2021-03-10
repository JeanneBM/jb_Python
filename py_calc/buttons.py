
# Install the State Tool
# Windows: 
# IEX(New-Object Net.WebClient).downloadString('https://platform.activestate.com/dl/cli/install.ps1')
# state activate --default ActiveState/ActivePython-3.8

# Linux, Mac : 
# sh <(curl -q https://platform.activestate.com/dl/cli/install.sh)
# state activate --default ActiveState/ActivePython-3.8 

from tkinter import *


def PyCalculator(source, side):
    window = Frame(source, borderwidth=1000, bd=10, bg="DarkOrchid1")
    window.pack(side=side, expand=YES, fill=BOTH)
    return window


def button(source, side, text, command=None):
    window = Button(source, text=text, command=command)
    window.pack(side=side, expand=YES, fill=BOTH)
    return window


class Application(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 16')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('PyCalculator')

        output = StringVar()
        Entry(self, relief=RIDGE, textvariable=output,
              justify='right'
              , bd=30, bg="OliveDrab1").pack(side=TOP,
                                              expand=YES, fill=BOTH)

        for clearButton in (["Clear"]):
            cleaning = PyCalculator(self, TOP)
            for ichar in clearButton:
                button(cleaning, LEFT, ichar, lambda
                    window=output, q=ichar: window.set(''))

        for buttonsTable in ("123-", "456*","789/", "0.+"):
            operation = PyCalculator(self, TOP)
            for choice in buttonsTable:
                button(operation, LEFT, choice, lambda
                    window=output, q=choice: window
                       .set(window.get() + q))

        resultButton = PyCalculator(self, TOP)
        for choice in "=":
            if choice == '=':
                score = button(resultButton, LEFT, choice)
                score.bind('<ButtonRelease-1>', lambda e, s=self,
                                                            window=output: s.machine(window), '+')


            else:
                score = button(resultButton, LEFT, choice,
                                    lambda window=output, s=' %s ' % choice: window.set
                                    (window.get() + s))

    def machine(self, output):
        try:
            output.set(eval(output.get()))
        except:
            output.set("ERROR")


if __name__ == '__main__':
    Application().mainloop()
