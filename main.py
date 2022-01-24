from tkinter import Tk
from display import EquationDisplay
from numpad import NumButtonFrame
from funcpad import FuncButtonFrame
from calculate import Calculator
import app


class Root(Tk):
    title_text = app.name
    config_data = {
        'background': "white",
    }
    display = EquationDisplay
    num_pad = NumButtonFrame
    func_pad = FuncButtonFrame

    def build_frames(self):
        self.display = self.display(self)
        app.equation_display = self.display
        self.display.grid(row=0, column=0, columnspan=5, sticky='nsew')
        self.num_pad = self.num_pad(self)
        self.num_pad.grid(row=1, column=0, columnspan=3, sticky='nsew')
        self.func_pad = self.func_pad(self)
        self.func_pad.grid(row=1, column=4)

    def set_binds(self):
        self.bind("<KeyPress>", lambda event: self.display.append(event.char))
        self.bind("<Escape>", lambda _: self.display.clear())
        self.bind("<BackSpace>", lambda _: self.display.backspace())
        self.bind("<Control-minus>", lambda _: self.display.append(" — "))
        self.bind("-", lambda _: self.display.append("-"))
        self.bind("+", lambda _: self.display.append(" "))
        self.bind("<Return>", lambda _: Calculator(self.display.equation_text))
        self.bind("*", lambda _: Calculator(self.display.append(" x ")))
        self.bind("<Control-+>", lambda _: self.display.append(" + "))
        self.bind("<Control-/>", lambda _: self.display.append(" ÷ "))

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.config_data)
        self.title(self.title_text)
        self.resizable(False, False)
        self.build_frames()
        self.set_binds()
        self.mainloop()


if __name__ == "__main__":
    Root()
