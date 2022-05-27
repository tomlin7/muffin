import asyncio
import tkinter as tk
from tkinter import font

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

        self.boldfont = font.nametofont('TkDefaultFont')
        self.boldfont.configure(weight='bold')
        self.text.tag_config('bold', font=self.boldfont)

        self.refresh_linestart()
        self.text.tag_config('prompt', foreground='grey')
        asyncio.run(self.show_prompt())

        self.text.bind('<Return>', self.enter)
    
    def get_command(self):
        return self.text.get(self.line_start, tk.END)
    
    def enter(self, *_):
        self.run(self.get_command())
        return "break"
        
    def run(self, cmd):
        asyncio.run(self.run_command(cmd))

    async def run_command(self, cmd):
        proc = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)

        stdout, stderr = await proc.communicate()

        self.write(f'\n[{cmd!r} exited with {proc.returncode}]\n')
        if stdout:
            self.write(('[stdout]', 'bold'), f'\n{stdout.decode().rstrip()}\n')
        if stderr:
            self.write(('[stderr]', 'bold'), f'\n{stderr.decode().rstrip()}\n')
        
        await self.show_prompt()
    
    async def show_prompt(self):
        proc = await asyncio.create_subprocess_shell(
            'cd', stdout=asyncio.subprocess.PIPE)

        stdout, _ = await proc.communicate()
        if stdout:
            self.write((f'{stdout.decode().rstrip()}>', 'prompt'))

        self.refresh_linestart()
    
    def refresh_linestart(self):
        self.line_start = self.text.index(tk.END)
        self.text.see(self.line_start)

    def write(self, *args):
        for i in args:
            if isinstance(i, tuple):
                self.text.insert(tk.END, i[0], i[1])
            else:
                self.text.insert(tk.END, i)
