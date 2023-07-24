
import os
import tkinter.filedialog as tk

filepath = tk.askdirectory(initialdir="D:\\Astronomy")

path = filepath+"/Process"

if not os.path.isdir(path):
    print("directory does not exist")
else:
    files = os.listdir(path)
    for f in files:
        os.remove(path+'/'+f)

    os.rmdir(filepath+"/Process")
