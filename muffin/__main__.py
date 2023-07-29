__version__ = '0.4.0'


import tkinter as tk

from components import setup
from layout import Layout
from utils import Binder

root = tk.Tk()
root.title("Muffin")
setup(root)

root.layout = Layout(root)
root.layout.pack(expand=1, fill=tk.BOTH)

Binder(root).bind_all()
root.layout.logger.info(f"Initialized Muffin {__version__}")
root.layout.notifications.info(f"Welcome to Muffin {__version__} 🧁")

root.mainloop()
