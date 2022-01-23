from tkinter import Label, Frame
import app


class DisplayText(Label):
    font = ("Helvetica", 20)
    test_text = "1000123"

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        label = Label(self, text=self.test_text)
        app.display_label = label


class EquationDisplay(Label):
    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)


class AnswerDisplay(Label):
    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)


class DisplayFrame(Frame):
    config_data = {
        'background': '#002d04',
        'height': 75,
    }
    display_label = DisplayText
    equation_display = EquationDisplay

    def add_sub_frames(self):
        self.display_label = self.display_label(self)
        self.equation_display = self.equation_display(self)

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.config_data)
        self.add_sub_frames()
