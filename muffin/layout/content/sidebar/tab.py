import tkinter as tk


class Tab(tk.Menubutton):
    def __init__(self, master, view, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.view = view
        self.selected = True
        
        self.config(
            text=view.__class__.__name__, 
            font=('Courier New', 10),
            bg='white')

        self.bind('<Button-1>', self.select)

    def deselect(self, *_):
        if self.selected:
            self.selected = False
            self.config(bg="#ececec")
        
    def select(self, *_):
        if not self.selected:
            self.selected = True
            self.config(bg="white")
        self.master.set_active_tab(self.view)