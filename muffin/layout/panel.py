import tkinter as tk

from components.views import Terminal

class Panel(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.pack_propagate(False)

        self.terminal = Terminal(self)
        self.terminal.pack(expand=1, fill=tk.BOTH)
