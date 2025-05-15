# graphics.py

import tkinter as tk

class Canvas:
    def __init__(self, width, height):
        self._tk = tk.Tk()
        self._tk.title("Canvas")
        self._canvas = tk.Canvas(self._tk, width=width, height=height)
        self._canvas.pack()
        self._canvas.bind('<Motion>', self._on_mouse_move)
        self._canvas.bind('<Button-1>', self._on_click)
        self._mouse_x = 0
        self._mouse_y = 0
        self._click_x = None
        self._click_y = None
        self._tk.update()

    def _on_mouse_move(self, event):
        self._mouse_x = event.x
        self._mouse_y = event.y

    def _on_click(self, event):
        self._click_x = event.x
        self._click_y = event.y

    def get_mouse_x(self):
        self._tk.update()
        return self._mouse_x

    def get_mouse_y(self):
        self._tk.update()
        return self._mouse_y

    def get_last_click(self):
        while self._click_x is None or self._click_y is None:
            self._tk.update()
        click = (self._click_x, self._click_y)
        self._click_x = None
        self._click_y = None
        return click

    def wait_for_click(self):
        self.get_last_click()

    def create_rectangle(self, x1, y1, x2, y2, color='black'):
        rect = self._canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='')
        self._tk.update()
        return rect

    def set_color(self, shape, color):
        self._canvas.itemconfig(shape, fill=color)
        self._tk.update()

    def moveto(self, shape, x, y):
        coords = self._canvas.coords(shape)
        current_x = coords[0]
        current_y = coords[1]
        dx = x - current_x
        dy = y - current_y
        self._canvas.move(shape, dx, dy)
        self._tk.update()

    def find_overlapping(self, x1, y1, x2, y2):
        return self._canvas.find_overlapping(x1, y1, x2, y2)
