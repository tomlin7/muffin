import tkinter as tk

class FloatingNotification(tk.Toplevel):
    def __init__(self, master, text):
        super().__init__(master)
        self.attributes("-toolwindow", True)
        self.overrideredirect(True)
        self.configure(background='white')

        label = tk.Label(self, text=text, background='white')
        label.pack(pady=10, padx=10)

        close_button = tk.Button(self, text="X", command=self.destroy)
        close_button.pack(side='right', padx=10)

        self.bind("<Configure>", self._follow_root)
        self.bind("<Map>", self._follow_root)

    def _follow_root(self, event):
        x = self.master.winfo_rootx()
        y = self.master.winfo_rooty() + self.master.winfo_height() - self.winfo_height()
        self.geometry(f"+{x}+{y}")

root = tk.Tk()
root.geometry("200x200")

def show_notification():
    notification = FloatingNotification(root, "This is a floating notification")

button = tk.Button(root, text="Show notification", command=show_notification)
button.pack()

root.mainloop()
