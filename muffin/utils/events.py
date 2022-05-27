class Events:
    def __init__(self, master):
        self.master = master
        self.editor = self.master.layout.base.editor

    def openfile(self, *_):
        self.editor.openfile()
