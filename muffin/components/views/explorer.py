import os
import tkinter as tk
from tkinter import ttk

from .view import View
from ..utils import DirectoryTreeWatcher


class Explorer(View):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.tree = ttk.Treeview(self)
        self.tree.config(show="tree")
        self.tree.pack(fill=tk.BOTH, side=tk.LEFT)

        style = ttk.Style()
        style.layout("Treeview", [
            ('Treeview.treearea', {'sticky': 'nswe'})
        ])

        self.watcher = DirectoryTreeWatcher(self.tree)

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(fill=tk.Y, side=tk.LEFT, padx=(1, 0))
