import asyncio
import tkinter as tk

from .view import View


class Terminal(View):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.text = tk.Text(self)
        self.text.pack(expand=1, fill=tk.BOTH, side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(fill=tk.Y, side=tk.LEFT)
        
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)

        self.line_start = '1.0'
        
        self.text.bind("<Return>", self.enter)
    
    def get_command(self):
        return self.text.get(self.line_start, tk.END)
    
    def enter(self, *_):
        asyncio.run(self.run(self.get_command()))

    async def run(self, cmd):
        proc = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)

        stdout, stderr = await proc.communicate()

        # self.write(f'[{cmd!r} exited with {proc.returncode}]')
        if stdout:
            self.write(f'[stdout]\n{stdout.decode()}')
        if stderr:
            self.write(f'[stderr]\n{stderr.decode()}')
        
        self.line_start = self.index(tk.END)
    
    def write(self, text):
        self.text.insert(tk.END, text)
