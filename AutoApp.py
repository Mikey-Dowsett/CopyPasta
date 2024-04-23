import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import shutil

BUTTONCOLOR = "#b3b3b3"
GREEN = "#B0FF92"
DEFUALT = '#%02x%02x%02x' % (240, 240, 237)

#Class for file copier
class File():
    def __init__(self, frame):
        self.fileButton = self.FileButton(frame)
        self.folderButton = self.FolderButton(frame)
        self.startButton = self.StartButton(frame)
        self.folderlist = os.listdir()

        self.FILE = ""
        self.FOLDER = ""

    def FileButton(self, frame):
        button = tk.Button(frame, width = 20, text="File to Copy", command=lambda: self.FindFile(frame),relief="flat", bg=BUTTONCOLOR)
        button.pack(pady=20)

    def FolderButton(self, frame):
        button = tk.Button(frame, width = 20, text="Master Folder", command=lambda: self.FindFolder(frame),relief="flat", bg=BUTTONCOLOR)
        button.pack(pady=20)

    def StartButton(self, frame):
        button = tk.Button(frame, width = 20, text="Start", command=lambda: self.CopyFileToFolders(frame), relief="flat", bg=BUTTONCOLOR)
        button.pack(pady=20)

    def FindFile(self, frame):
        frame.configure(bg=DEFUALT)
        self.FILE = filedialog.askopenfilename()

    def FindFolder(self,frame):
        frame.configure(bg=DEFUALT)
        self.FOLDER = filedialog.askdirectory()

    def CopyFileToFolders(self, frame):
        frame.configure(bg=DEFUALT)
        for root, subdirectories, files in os.walk(self.FOLDER):
            for subdirectorie in subdirectories:
                print(os.path.join(root, subdirectorie))
                shutil.copy(str(self.FILE), str(os.path.join(root, subdirectorie)))
        frame.configure(bg=GREEN)

#Class for the folder Generator
class FolderMaker():
    def __init__(self, frame):
        self.entryName = self.NameInput(frame)
        self.FolderButton(frame)
        self.StartButton(frame)
        self.folderlist = os.listdir()

        self.FILE = ""
        self.FOLDER = ""

    def NameInput(self, frame):
        entry = tk.Entry(frame, width = 20,relief="flat", bg=BUTTONCOLOR)
        entry.insert(0, "Folder Name")
        entry.pack(pady=20)
        return entry

    def FolderButton(self, frame):
        button = tk.Button(frame, width = 20, text="Master Folder", command=lambda: self.FindFolder(frame),relief="flat", bg=BUTTONCOLOR)
        button.pack(pady=20)

    def StartButton(self, frame):
        button = tk.Button(frame, width = 20, text="Start", command=lambda: self.CopyFileToFolders(frame), relief="flat", bg=BUTTONCOLOR)
        button.pack(pady=20)

    def FindFile(self, frame):
        frame.configure(bg=DEFUALT)
        self.FILE = filedialog.askopenfilename()

    def FindFolder(self, frame):
        frame.configure(bg=DEFUALT)
        self.FOLDER = filedialog.askdirectory()

    def CopyFileToFolders(self, frame):
        frame.configure(bg=DEFUALT)
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
        frame.configure(bg=GREEN)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        style = ttk.Style()
        style.map('TNotebook.Tab', background=[("selected", GREEN), ('active', DEFUALT)])
        
        noteBook = ttk.Notebook(self)
        noteBook.pack(pady=0, expand=False, fill="both")

        fileFrame = tk.Frame(noteBook, width=400, height=280)
        folderFrame = tk.Frame(noteBook, width=400, height=280)

        File(fileFrame)
        FolderMaker(folderFrame)
        fileFrame.pack(fill="both", expand=True)
        folderFrame.pack(fill="both", expand=True)

        noteBook.add(fileFrame, text="File Copier")
        noteBook.add(folderFrame, text="Folder Maker")

if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("400x240")
    window.resizable(0, 0)
    window.title("AutoApp")
    window.wm_attributes('-toolwindow', 'True')
    window.configure(bg=DEFUALT)
    main = MainView(window)
    main.pack(side="top", fill="both", expand=True)
    window.mainloop()