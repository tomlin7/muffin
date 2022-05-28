import tkinter as tk

from layout import Layout
from utils import Binder

root = tk.Tk()
root.title("Muffin")

root.layout = Layout(root)
root.layout.pack(expand=1, fill=tk.BOTH)

Binder(root).bind_all()
root.mainloop()
