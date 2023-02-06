import tkinter as tk

from .section import Section
from components import Notifications


class Statusbar(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.config(bd=1, bg='white')

        self.left = Section(self, text=(" Python ", " UTF-8 ", " Ln y, Col x "))
        self.left.pack(side=tk.LEFT)

        self.notif = Section(self, text="🔔 ", sep=" ")
        self.notif.pack(side=tk.RIGHT)
        self.notifications = Notifications(self.notif)
        self.notif.bind("<Button-1>", self.notifications.showbtn)

        self.right = Section(self, text=(" branch ",), justify=tk.RIGHT)
        self.right.pack(side=tk.RIGHT)

        self.right.update(" Python ", " UTF-8 ", " Ln y, Col x ")
        self.left.update(" branch ")
