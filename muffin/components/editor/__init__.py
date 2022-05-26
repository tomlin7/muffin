import tkinter as tk

from .text import Text
from .linenumbers import Linenumbers


class Editor(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.linenumbers = Linenumbers(self)
        self.linenumbers.config(yscrollcommand=self.scroll)
        self.linenumbers.pack(fill=tk.Y, side=tk.LEFT)

        self.text = Text(self)
        self.text.config(yscrollcommand=self.scroll)
        self.text.pack(expand=1, fill=tk.BOTH, side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(fill=tk.Y, side=tk.LEFT)
        self.scrollbar.config(command=self._scrollbar)

        self.linenumbers.attach(self.text)
        self.text.bind("<<Change>>", self.update)
    
    def update(self, *_):
        self.linenumbers.redraw()
    
    def _scrollbar(self, *args):
        self.text.yview(*args)
        self.linenumbers.yview(*args)

    def scroll(self, *args):
        self.scrollbar.set(*args)
        self._scrollbar('moveto', args[0])
