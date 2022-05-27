from idlelib.colorizer import ColorDelegator as _ColorDelegator


class ColorDelegator(_ColorDelegator):
    def __init__(self):
        super().__init__()

    def LoadTagDefs(self):
        "Create dictionary of tag names to text colors."
        self.tagdefs = {
            "COMMENT":  {"foreground": '#008000', "background": None},
            "KEYWORD":  {"foreground": '#c000db', "background": None},
            "BUILTIN":  {"foreground": '#267f99', "background": None},
            "STRING":  {"foreground": '#a31515', "background": None},
            "DEFINITION":  {"foreground": '#795e26', "background": None},
            "SYNC": {'background': None, 'foreground': '#0000ff'},
            "TODO": {'background': None, 'foreground': '#0000ff'},
            "ERROR":  {"foreground": '#e44a4a', "background": None},
            "hit":  {"foreground": '#e51400', "background": None},
            }
