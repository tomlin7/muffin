import tkinter as tk
from tkinter import ttk

from .section import Section


class Statusbar(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.config(bd=1, bg='white')

        self.left = Section(self, text=(" Python ", " UTF-8 ", " Ln y, Col x "))
        self.left.config(relief=tk.FLAT, height=1, padx=5)
        self.left.pack(side=tk.LEFT)

        self.right = Section(self, text=(" branch ",), justify=tk.RIGHT)
        self.right.config(relief=tk.FLAT, height=1, padx=5)
        self.right.pack(side=tk.RIGHT)

        self.right.update(" Python ", " UTF-8 ", " Ln y, Col x ")
        self.left.update(" branch ")
