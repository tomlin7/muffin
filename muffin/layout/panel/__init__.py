import tkinter as tk

from muffin.components.views import *

from .tabs import Tabs


class Panel(tk.Frame):
    """
    Panel can hold views.

    +---------------------------------+
    | Logs | Terminal |               |
    +---------------------------------+
    | \    \    \    \    \    \    \ |
    |  \    \    \    \    \    \    \|
    |   \    \    \    \    \    \    |
    |    \    \    \    \    \    \   |
    |\    \    \    \    \    \    \  |
    +---------------------------------+
    """
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.pack_propagate(False)
        self.config(bg='#a0a0a0')

        self.tabs = Tabs(self)
        self.tabs.pack(expand=1, fill=tk.BOTH, pady=(0, 1))

        self.active_view = None
        self.views = []

        self.default_views = [Logs(self), Terminal(self)]
        self.add_views(self.default_views)
        if self.default_views:
            self.tabs.set_active_tab(self.views[1])

    def add_views(self, views):
        "Append views to list. Create tabs for them."
        for view in views:
            self.add_view(view)
    
    def add_view(self, view):
        "Appends a view to list. Create a tab."
        self.views.append(view)
        self.tabs.add_tab(view)
        self.set_active_view(view)
        
    def delete_all_views(self):
        "Permanently delete all views."
        for view in self.views:
            view.destroy()

        self.views.clear()
    
    def delete_view(self, view):
        "Permanently delete a view."
        view.destroy()
        self.views.remove(view)
    
    def set_active_view(self, view):
        "Set active view and active tab."
        self.active_view = view
        for _view in self.views:
            _view.pack_forget()
        view.pack(fill=tk.BOTH)
    
    def get_logger(self):
        return self.default_views[0]
    
    def get_terminal(self):
        return self.default_views[1]
