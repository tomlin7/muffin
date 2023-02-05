import tkinter as tk

class VerticalButton(tk.Canvas):
    def __init__(self, master, text, angle=90, *args, **kwargs):
        tk.Canvas.__init__(self, master, *args, **kwargs)
        self.text = text
        self.config(bg='white', width=30, height=len(text)*10, highlightthickness=0)

        self.text_id = self.create_text(15, len(text)*5, text=text, 
            anchor="center", angle=angle, font=('Courier New', 9))
        
        self.bind("<Enter>", self.hoverin)
        self.bind("<Leave>", self.hoverout)
    
    def hoverin(self, *_):
        self.config(bg='#f0f0f0')

    def hoverout(self, *_):
        self.config(bg='white')