import tkinter as tk
from tkinter import ttk

from .item import StatusbarItem


class Statusbar(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.config(bd=1, bg='white', relief=tk.SUNKEN)

        for i in ("Python", "UTF-8", "Ln y, Col x"):
            self.add_item(i, tk.RIGHT)

        for i in ("branch",):
            self.add_item(i, tk.LEFT)

    def add_item(self, name, side):
        item = StatusbarItem(self, name=name)
        item.pack(fill=tk.Y, side=side, padx=2)
        self.add_separator(side)

    def add_separator(self, side):
        sep = ttk.Separator(self, orient=tk.VERTICAL)
        sep.pack(side=side, fill=tk.Y, pady=1)
