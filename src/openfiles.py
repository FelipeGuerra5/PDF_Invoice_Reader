import tkinter as tk
from tkinter import filedialog

def openFiles():    
    root = tk.Tk()
    root.withdraw()

    files = filedialog.askopenfilenames()

    return files

if __name__ == "__main__":
    print('openfiles')
