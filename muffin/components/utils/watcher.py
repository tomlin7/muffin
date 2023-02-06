import asyncio
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def contains(string, arr):
    for i in arr:
        if i in string:
            return True
    return False

def hasext(string, arr):
    for i in arr:
        if string.endswith(i):
            return True
    return False

class DirectoryTreeWatcher(FileSystemEventHandler):
    def __init__(self, tree):
        self.tree = tree

        self.nodes = {}
        
        self.observer = Observer()
        self.observer.schedule(self, ".", recursive=True)
        self.observer.start()

        self.ignore_dirs = [".git", "__pycache__"]
        self.ignore_exts = [".pyc"]
        self.update_tree()

    def on_created(self, event):
        self.update_tree()

    def on_deleted(self, event):
        self.update_tree()

    def on_modified(self, event):
        self.update_tree()
    
    async def async_scandir(self, path):
        entries = []
        for entry in os.scandir(path):
            entries.append((entry.name, entry.path))
        return entries

    async def async_update_tree(self, parent="", entries=[(p, os.path.abspath(p)) for p in os.listdir(os.curdir)]):
        entries.sort(key=lambda x: (not os.path.isdir(x[1]), x[0]))
        for name, path in entries:
            if os.path.isdir(path):
                if name in self.ignore_dirs:
                    continue
                if path in self.nodes.keys():    
                    continue
                item = self.tree.insert(parent, "end", text=name, open=False)
                self.nodes[path] = item
                await self.async_update_tree(item, await self.async_scandir(path))
            else:
                if name.split(".")[-1] in self.ignore_exts:
                    continue
                if path in self.nodes.keys():    
                    continue
                item = self.tree.insert(parent, "end", text=name)
                self.nodes[path] = item

    def update_tree(self):
        #self.tree.delete(*self.tree.get_children())
        asyncio.run(self.async_update_tree())
        for path, item in list(self.nodes.items()):
            if not os.path.exists(path):
                self.tree.delete(item)
                self.nodes.pop(path)

            