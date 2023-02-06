import tkinter as tk

from .base import Base
from .statusbar import Statusbar


class Layout(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.config(bg="#a0a0a0")
        
        self.base = Base(self)
        self.base.pack(expand=1, fill=tk.BOTH)

        self.statusbar = Statusbar(self)
        self.statusbar.pack(fill=tk.X, pady=(1, 0))

        self.logger = self.base.panel.get_logger()
        self.terminal = self.base.panel.get_terminal()
        self.notifications = self.statusbar.notifications
