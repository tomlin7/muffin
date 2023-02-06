import tkinter as tk

class Notifications(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.attributes("-toolwindow", True)
        self.overrideredirect(True)

        self.configure(bg="#a0a0a0")
        self.offset = 10
        self.minsize(width=400, height=1)

        self.icon = tk.Label(self, text="⚠", font=("FixedSys", 16), anchor=tk.W, padx=2)
        self.icon.pack(padx=(1,0), pady=1, side=tk.LEFT, fill=tk.BOTH)

        self.label = tk.Label(self, text="NO NEW NOTIFICATIONS", font=("FixedSys", 16), anchor=tk.W, padx=5)
        self.label.pack(pady=1, padx=1, side=tk.LEFT, expand=1, fill=tk.BOTH)

        close_button = tk.Menubutton(self, text="▼", activebackground="#949494", width=2)
        close_button.pack(side=tk.RIGHT, padx=(0,1), pady=1, fill=tk.BOTH)
        close_button.bind('<Button-1>', self.hide)

        self.bind("<Configure>", self._follow_root)
        self.bind("<Map>", self._follow_root)
        self.withdraw()
    
    def info(self, text):
        self.icon.configure(text="✈")
        self.label.configure(text=text)
        self.showbtn()
    
    def warning(self, text):
        self.icon.configure(text="☁")
        self.label.configure(text=text)
        self.showbtn()

    def error(self, text):
        self.icon.configure(text="❄")
        self.label.configure(text=text)
        self.showbtn()
    
    def showbtn(self, *_):
        self.wm_deiconify()
        self.after(10000, self.hide)
    
    def hide(self, *_):
        self.withdraw()
    
    def clear(self, *_):
        self.label.configure(text="NO NEW NOTIFICATIONS")

    def _follow_root(self, event):
        x = self.master.winfo_rootx()- self.winfo_width() + self.offset 
        y = self.master.winfo_rooty() - self.winfo_height() - self.offset 
        self.geometry(f"+{x}+{y}")
