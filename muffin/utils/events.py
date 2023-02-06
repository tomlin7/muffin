import tkinter.filedialog as fd


class Events:
    def __init__(self, master):
        self.master = master
        self.editor = self.master.layout.base.content.editor

    def openfile(self, *_):
        path = fd.askopenfilename()
        if path:
            self.editor.openfile(path)
    
    # TODO open directory
    
    def savefile(self, *_):
        self.editor.savefile()
    
    def savefileas(self, *_):
        path = fd.asksaveasfilename()
        if path:
            self.editor.savefile(path=path)
