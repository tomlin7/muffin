import tkinter as tk


class StatusbarItem(tk.Frame):
    def __init__(self, master, name, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.name = name

        self.label = tk.Label(self, text=name, bg='white', padx=2)
        self.label.pack(fill=tk.BOTH)
