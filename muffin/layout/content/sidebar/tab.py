import tkinter as tk


class Tab(tk.Menubutton):
    def __init__(self, master, manager, view, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.manager = manager
        self.view = view
        self.selected = True
        
        self.config(
            text=f"{view.symbol}", 
            font=('Courier New', 10),
            bg='white')

        self.bind('<Button-1>', self.select)

    def deselect(self, *_):
        if self.selected:
            self.selected = False
            self.config(bg="#ececec", activebackground="#f0f0f0")
        
    def select(self, *_):
        if not self.selected:
            self.selected = True
            self.config(bg="white", activebackground="white")
        self.manager.set_active_tab(self.view)