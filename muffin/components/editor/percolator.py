from idlelib.percolator import Percolator as _Percolator
from idlelib.colorizer import ColorDelegator


class Percolator(_Percolator):
    def __init__(self, text, *args, **kwargs):
        super().__init__(text, *args, **kwargs)

        self.colordelegator = ColorDelegator()
        self.insertfilter(self.colordelegator)

        self.redir.unregister("insert")
        self.redir.unregister("delete")

        self.redir.register("insert", self.insert)
        self.redir.register("delete", self.delete)

    def insert(self, index, chars, tags=None):
        self.top.insert(index, chars, tags)
        self.text.event_generate("<<Change>>")

    def delete(self, index1, index2=None):
        self.top.delete(index1, index2)
        self.text.event_generate("<<Change>>")
