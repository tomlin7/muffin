from tkinter import font


class Fonts:
    def __init__(self, master):
        self.master = master

        self.boldfont = font.nametofont('TkDefaultFont')
        self.boldfont.configure(weight='bold')

        self.normalfont = font.nametofont('TkDefaultFont')
        self.normalfont.configure(weight='normal')

    @property
    def bold(self):
        return self.boldfont
    
    @property
    def normal(self):
        return self.boldfont
    
