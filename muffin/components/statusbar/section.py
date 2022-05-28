import tkinter as tk


class Section(tk.Text):
    def __init__(self, master, text=None, justify=tk.LEFT, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.text = text
        self.justify = justify
        self.config(relief=tk.FLAT)
        
        self.tag_config('justify', justify=justify)
        if text:
            self.update(*text)
    
    def update(self, *args):
        self.text = "|".join(args)

        self.config(state=tk.NORMAL)
        self.delete('1.0', tk.END)
        self.insert('1.0', self.text, 'justify')

        self.config(width=len(self.text), state=tk.DISABLED)
    
    def refresh_geometry(self):
        self.config(width=len(self.text))
