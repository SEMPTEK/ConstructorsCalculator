from tkinter import Button, Frame
import app


class NumButton(Button):
    config_data = {
        'height': 4,
        'width': 10,
        'relief': 'flat',
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.config_data)


class NumButtonFrame(Frame):
    frame_size = "500x200"
    buttons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '—', '.']
    x_grid_count = 3
    y_grid_count = 3

    def build_buttons(self):
        i = 0
        x = 0
        y = 0

        for button in self.buttons:
            if x >= self.x_grid_count:
                x = 0
                y += 1
            button_obj = NumButton(self, text=str(button), command=lambda: app.equation_display.append(button))
            button_obj.grid(row=y, column=x)
            i += 1
            x += 1

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.build_buttons()
