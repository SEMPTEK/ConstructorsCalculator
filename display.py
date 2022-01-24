from tkinter import Label


class EquationDisplay(Label):
    equation_text = ""
    config_data = {
        'background': '#002d04',
        'height': 3,
        'font': ('Arial', 18),
        'fg': 'white',
    }

    def append(self, value):
        value = str(value)
        self.equation_text += value
        self.update_text()

    def update_text(self):
        self.configure(text=str(self.equation_text))

    def clear(self):
        self.equation_text = ""
        self.update_text()

    def backspace(self):
        if self.equation_text == "":
            return
        self.equation_text = self.equation_text[0:-1]
        self.update_text()

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.config_data)
