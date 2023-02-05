import asyncio
import tkinter as tk

from .view import View


class Terminal(View):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.text = tk.Text(self, relief=tk.FLAT)
        self.text.pack(expand=1, fill=tk.BOTH, side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(fill=tk.Y, side=tk.LEFT, padx=(1, 0))
        
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)

        self.text.tag_config('normal', font=('Courier New', 10))
        self.text.tag_config('bold', font=('Courier New', 10, 'bold'))

        self.text.tag_config('prompt', foreground='grey')
        asyncio.run(self.show_prompt())

        self.text.bind('<Return>', self.enter)
    
    def get_command(self):
        return self.text.get(self.line_start, tk.END).rstrip()
    
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

        self.newline()
        self.write(f'[{cmd!r} exited with {proc.returncode}]')
        if stdout:
            self.newline()
            self.write(('[stdout] ', 'bold'), f'{stdout.decode().rstrip()}')
        if stderr:
            self.newline()
            self.write(('[stderr] ', 'bold'), f'{stderr.decode().rstrip()}')
        
        self.newline()
        await self.show_prompt()
    
    async def show_prompt(self):
        proc = await asyncio.create_subprocess_shell(
            'cd', stdout=asyncio.subprocess.PIPE)

        stdout, _ = await proc.communicate()
        if stdout:
            self.write((f'{stdout.decode().rstrip()}>', 'prompt'))

        self.refresh_linestart()
    
    def refresh_linestart(self):
        self.line_start = self.text.index(tk.INSERT)
        self.text.see(self.line_start)
    
    def newline(self):
        self.write('\n')

    def write(self, *args):
        for i in args:
            if isinstance(i, tuple):
                self.text.insert(tk.END, i[0], i[1])
            else:
                self.text.insert(tk.END, i)
