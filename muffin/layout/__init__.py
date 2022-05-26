import tkinter as tk

from components import Editor


class Layout(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.editor = Editor(self)
        self.editor.pack(expand=1, fill=tk.BOTH)
