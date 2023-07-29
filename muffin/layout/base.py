import tkinter as tk

from .content import Content
from .panel import Panel


class Base(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.content = Content(self)
        self.content.pack(expand=1, fill=tk.BOTH)

        self.panel = Panel(self)
        self.panel.config(height=250)
        self.panel.pack(fill=tk.BOTH)
