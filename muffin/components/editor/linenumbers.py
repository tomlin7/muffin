import tkinter as tk


class Linenumbers(tk.Text):
    def __init__(self, master, textw=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.text = textw
        
        self.config(width=5, relief=tk.FLAT)

    def attach(self, text):
        self.text = text
        self.text.focus()
        self.redraw()
    
    def redraw(self):
        self.config(state=tk.NORMAL)
        self.delete("1.0", tk.END)
        lines = int(self.text.index(tk.END).split(".")[0])
        for i in range(1, lines):
            self.insert(f"{i}.0", f"{i}\n")
        
        self.see(self.text.index(tk.INSERT))
        self.config(state=tk.DISABLED)
