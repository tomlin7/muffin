import tkinter as tk
from components import Editor

from .panel import Panel


class Base(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.editor = Editor(self)
        self.editor.pack(expand=1, fill=tk.BOTH)

        self.panel = Panel(self)
        self.panel.config(height=250)
        self.panel.pack(fill=tk.BOTH)
