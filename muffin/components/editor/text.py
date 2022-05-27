import tkinter as tk

from .percolator import Percolator


class Text(tk.Text):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.percolator = Percolator(self)
    
    def write(self, text):
        self.insert('1.0', text)
    
    def clear(self):
        self.delete('1.0', tk.END)

    def readfile(self, path):
        self.clear()
        print(path)
        with open(path, 'r') as fp:
            self.write(fp.read())
