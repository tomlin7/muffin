from .events import Events


class Binder:
    def __init__(self, master):
        self.master = master
        self.events = Events(self.master)

    def bind_all(self):
        self.bind('<Control-o>', self.events.open)

    def bind(self, event, function):
        self.master.bind(event, function)
