import tkinter.filedialog as fd


class Events:
    def __init__(self, master):
        self.master = master
        self.editor = self.master.layout.base.editor

    def openfile(self, *_):
        path = fd.askopenfilename()
        if path:
            self.editor.openfile(path)
