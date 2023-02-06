import tkinter as tk


class Linenumbers(tk.Canvas):
    def __init__(self, master, text=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.text = text

        self.font = ("FixedSys", 16)
        self.config(width=50, relief=tk.FLAT, bg="#ffffff", bd=0, highlightthickness=0)

    def attach(self, text):
        self.text = text
    
    def redraw(self, *_):
        self.delete(tk.ALL)
        i = self.text.index("@0,0")
        while True :
            dline = self.text.dlineinfo(i)
            if dline is None: 
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            text = linenum
            if not int(linenum)%100:
                text = '--' + linenum
            self.create_text(40, y, anchor=tk.NE, text=text, font=self.font, fill="#515151", activefill="#949494")
            i = self.text.index("%s+1line" % i)
