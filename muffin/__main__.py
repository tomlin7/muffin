import tkinter as tk

from layout import Layout

root = tk.Tk()

layout = Layout(root)
layout.pack(expand=1, fill=tk.BOTH)

root.mainloop()
