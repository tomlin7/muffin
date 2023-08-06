__version__ = '0.22.0'


import sys
import tkinter as tk

from muffin.components import setup
from muffin.layout import Layout
from muffin.utils import Binder

root = tk.Tk()
setup(sys.argv[0], root)

root.layout = Layout(root)
root.layout.pack(expand=1, fill=tk.BOTH)

Binder(root).bind_all()
root.layout.logger.info(f"Initialized Muffin {__version__}")
root.layout.notifications.info(f"Welcome to Muffin {__version__} 🧁")

root.mainloop()
