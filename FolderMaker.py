import tkinter as tk
from tkinter import filedialog
import os
import shutil

BUTTONCOLOR = "#b3b3b3"
GREEN = "#B0FF92"
DEFUALT = '#%02x%02x%02x' % (240, 240, 237)

class FolderMaker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x200")
        self.window.resizable(0, 0)
        self.window.title("Folder Maker")
        self.window.wm_attributes('-toolwindow', 'True')
        self.window.configure(bg=DEFUALT)

        self.entryName = self.NameInput()
        self.FolderButton()
        self.StartButton()
        self.folderlist = os.listdir()

        self.FILE = ""
        self.FOLDER = ""

    def NameInput(self):
        entry = tk.Entry(width = 20,relief="flat", bg=BUTTONCOLOR)
        entry.insert(0, "Folder Name")
        entry.pack(pady=20)
        return entry

    def FolderButton(self):
        button = tk.Button(width = 20, text="Master Folder", command=lambda: self.FindFolder(),relief="flat", bg=BUTTONCOLOR)
        button.pack(pady=20)

    def StartButton(self):
        button = tk.Button(width = 20, text="Start", command=lambda: self.CopyFileToFolders(), relief="flat", bg=BUTTONCOLOR)
        button.pack(pady=20)

    def FindFile(self):
        self.window.configure(bg=DEFUALT)
        self.FILE = filedialog.askopenfilename()

    def FindFolder(self):
        self.window.configure(bg=DEFUALT)
        self.FOLDER = filedialog.askdirectory()

    def CopyFileToFolders(self):
        self.window.configure(bg=DEFUALT)
        name = self.entryName.get()
        count = 0
        for root, subdirectories, files in os.walk(self.FOLDER):
            print("run")
            for subdirectorie in subdirectories:
                path = (root + "/" + subdirectorie + "/" + name)
                if not os.path.exists(path):
                    os.makedirs(path)
            count += 1
            if count == 1:
                break
        self.window.configure(bg=GREEN)



    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = FolderMaker()
    app.run()