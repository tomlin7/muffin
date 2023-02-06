import io, tokenize
import tkinter as tk


class Text(tk.Text):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.pack_propagate()
        self.config(relief=tk.FLAT, wrap=tk.WORD)

        self.tag_configure("keyword", foreground="#989898")
        self.tag_configure("def", foreground="#636363")
        self.tag_configure("builtin", foreground="#949494")
        self.tag_configure("string", foreground="#4E4E4E")
        self.tag_configure("comment", foreground="#C9C9C9")
        self.tag_configure("TODO", background="#515151", foreground="#C9C9C9")

        self.configure(font=("FixedSys", 16))

        self.focus_set()
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)
    
    def _proxy(self, *args):
        if args[0] == 'get' and (args[1] == tk.SEL_FIRST and args[2] == tk.SEL_LAST) and not self.tag_ranges(tk.SEL): 
            return
        if args[0] == 'delete' and (args[1] == tk.SEL_FIRST and args[2] == tk.SEL_LAST) and not self.tag_ranges(tk.SEL): 
            return

        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

        if (args[0] in ("insert", "replace", "delete") or 
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")
            
        return result

    def write(self, text):
        self.insert('1.0', text)
    
    def clear(self):
        self.delete('1.0', tk.END)

    def readfile(self, path):
        self.clear()
        with open(path, 'r') as fp:
            self.write(fp.read())

    def highlight(self, *_):
        io_text = io.StringIO(self.get("1.0", "end"))
        for token_type, token, start, end, _ in tokenize.generate_tokens(io_text.readline):
            s = f"{start[0]}.{start[1]}"
            e = f"{end[0]}.{end[1]}"
            if token in [
                'import', 'if', 'else', 'elif', 'for', 'while', 
                'try', 'except', 'as', 'any','is', 'not', 'with'
            ]:
                self.tag_add("keyword", s, e)
            elif token in [
                'def', 'class', 'int', 'float', 'char', 'str',
                'True', 'False', 'None', 'object', 'bool',
            ]:
                self.tag_add("def", s, e)
            elif token in [
                "abs","all","any","ascii","bytearray","callable",
                "classmethod","complex","delattr","dir","divmod",
                "enumerate","exec","filter","format","frozenset",
                "globals","hasattr","help","hex","id","input", "eval",
                "isinstance","issubclass","len","list","locals",
                "max","memoryview","next","open","ord","pow","print",
                "property","repr","reversed","setattr","sorted",
                "staticmethod","sum","super","tuple","type","vars","zip"
            ]:
                self.tag_add("builtin", s, e)
            elif token_type == tokenize.STRING:
                self.tag_add("string", s, e)
            elif token_type == tokenize.COMMENT:
                self.tag_add("comment", s, e)
            elif token == "TODO":
                self.tag_add("TODO", s, e)
