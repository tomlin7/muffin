import tkinter as tk

from .linenumbers import Linenumbers
from .text import Text


class Editor(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.config(bg='#a0a0a0', bd=1)

        self.text = Text(self)
        self.linenumbers = Linenumbers(self, self.text)

        self.linenumbers.pack(fill=tk.Y, side=tk.LEFT)
        self.text.pack(expand=1, fill=tk.BOTH, side=tk.LEFT, padx=(1, 0))

        self.scrollbar = tk.Scrollbar(self, command=self._scrollbar)
        self.scrollbar.pack(fill=tk.Y, side=tk.LEFT, padx=(1, 0))
        self.text.config(yscrollcommand=self.scrollbar.set)

        self.text.bind("<<Change>>", self._update)
    
    def _update(self, *_):
        self.text.highlight()
        self.linenumbers.redraw()
    
    def _scrollbar(self, *args):
        self.text.yview(*args)
        self.linenumbers.yview(*args)

    def scroll(self, *args):
        self.scrollbar.set(*args)
        self._scrollbar('moveto', args[0])

    def openfile(self, path):
        self.text.readfile(path)

    def savefile(self, path):
        self.text.readfile(path)
