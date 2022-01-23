from tkinter import Button, Frame


class FuncButton(Button):
    config_data = {
        'height': 3,
        'width': 5,
        'relief': 'flat',
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.config_data)


class FuncButtonFrame(Frame):
    buttons = ['+', '-', 'x', '÷', '=', 'CLR']

    def build_buttons(self):
        y = 0
        for button in self.buttons:
            button = FuncButton(self, text=str(button))
            button.grid(row=y, column=0, padx=10)
            y += 1

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.build_buttons()
