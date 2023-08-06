import os, sys
from tkextrafont import Font


def setup(path, root):
    resdir = os.path.join(getattr(sys, "_MEIPASS", os.path.dirname(path)), "assets")
    root.title("Muffin")
    root.iconbitmap(os.path.join(resdir, 'icon.ico'))
    Font(file=os.path.join(resdir, "FSEX302.ttf"), family="FixedSys")
