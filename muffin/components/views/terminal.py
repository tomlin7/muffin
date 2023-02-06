import asyncio
import tkinter as tk

from .view import View


class Terminal(View):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.symbol = ">_"

        self.text = tk.Text(self, relief=tk.FLAT, font=("FixedSys", 15), fg="#4E4E4E")
        self.text.pack(expand=1, fill=tk.BOTH, side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(fill=tk.Y, side=tk.LEFT, padx=(1, 0))
        
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)
        
        self.text.tag_configure("prompt", foreground="#989898")
        self.text.tag_configure("return", foreground="#C9C9C9")
        self.text.tag_configure("stdfn", background="#515151", foreground="#C9C9C9")

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
        self.write((f'[{cmd!r} exited with {proc.returncode}]', "return"))
        if stdout:
            self.newline()
            self.write(('[stdout]', 'stdfn'), f' {stdout.decode().rstrip()}')
        if stderr:
            self.newline()
            self.write(('[stderr]', 'stdfn'), f' {stderr.decode().rstrip()}')
        
        self.newline()
        self.write(('⋅'*int(self.text.winfo_width()/3.05) + '\n', 'return'))
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
