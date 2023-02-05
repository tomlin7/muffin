import tkinter as tk


class View(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.config(bd=0, bg='#a0a0a0')
