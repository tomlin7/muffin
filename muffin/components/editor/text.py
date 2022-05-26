import tkinter as tk

from .percolator import Percolator


class Text(tk.Text):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.percolator = Percolator(self)
