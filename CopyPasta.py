import tkinter as tk
from tkinter import filedialog
import os
import shutil

BUTTONCOLOR = "#b3b3b3"
GREEN = "#B0FF92"
DEFUALT = '#%02x%02x%02x' % (240, 240, 237)

class CopyPasta:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x200")
        self.window.resizable(0, 0)
        self.window.title("CopyPasta")
        self.window.wm_attributes('-toolwindow', 'True')
        self.window.configure(bg=DEFUALT)

        self.FileButton()
        self.FolderButton()
        self.StartButton()
        self.folderlist = os.listdir()

        self.FILE = ""
        self.FOLDER = ""

    def FileButton(self):
        button = tk.Button(width = 20, text="File to Copy", command=lambda: self.FindFile(),relief="flat", bg=BUTTONCOLOR)
        button.pack(pady=20)

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
        for root, subdirectories, files in os.walk(self.FOLDER):
            for subdirectorie in subdirectories:
                print(os.path.join(root, subdirectorie))
                shutil.copy(str(self.FILE), str(os.path.join(root, subdirectorie)))
        self.window.configure(bg=GREEN)



    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = CopyPasta()
    app.run()