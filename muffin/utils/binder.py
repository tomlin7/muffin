from .events import Events


class Binder:
    def __init__(self, master):
        self.master = master
        self.events = Events(self.master)

    def bind_all(self):
        self.bind('<Control-o>', self.events.openfile)
        self.bind('<Control-s>', self.events.savefile)

    def bind(self, event, function):
        self.master.bind(event, function)
