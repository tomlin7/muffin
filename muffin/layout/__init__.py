import tkinter as tk

from .base import Base
from components import Statusbar


class Layout(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.base = Base(self)
        self.base.pack(expand=1, fill=tk.BOTH)

        self.statusbar = Statusbar(self)
        self.statusbar.pack(fill=tk.X)
