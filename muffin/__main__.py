__version__ = '0.3.0'


import tkinter as tk

from layout import Layout
from utils import Binder
from components import setup

root = tk.Tk()
root.title("Muffin")
setup(root)

root.layout = Layout(root)
root.layout.pack(expand=1, fill=tk.BOTH)

Binder(root).bind_all()
root.layout.logger.info(f"Initialized muffin {__version__}")
root.layout.logger.warning(f"you good?")
root.layout.logger.error(f"no")

root.mainloop()
