import tkinter as tk

from muffin.components import Editor

from .sidebar import Sidebar


class Content(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.config(bg='#a0a0a0')

        self.panel = Sidebar(self)
        self.panel.config(width=200)
        self.panel.pack(fill=tk.BOTH, side=tk.LEFT, pady=1)

        self.editor = Editor(self)
        self.editor.pack(expand=1, fill=tk.BOTH)

