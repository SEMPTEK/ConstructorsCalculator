from tkinter import Tk
from numpad import NumButtonFrame
from display import DisplayFrame
from funcpad import FuncButtonFrame
import app


class Root(Tk):
    title_text = app.name
    config_data = {
        'background': "white",
    }
    display = DisplayFrame
    num_pad = NumButtonFrame
    func_pad = FuncButtonFrame

    def build_frames(self):
        self.display = self.display(self)
        self.display.grid(row=0, column=0, columnspan=5, sticky='nsew')
        self.num_pad = self.num_pad(self)
        self.num_pad.grid(row=1, column=0, columnspan=3, sticky='nsew')
        self.func_pad = self.func_pad(self)
        self.func_pad.grid(row=1, column=4)

    def set_binds(self):
        self.bind("<KeyPress>", lambda value: self.display.append(value))

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.config_data)
        self.title(self.title_text)
        self.resizable(False, False)
        self.build_frames()
        self.mainloop()


if __name__ == "__main__":
    Root()
