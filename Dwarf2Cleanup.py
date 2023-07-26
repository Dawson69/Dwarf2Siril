
import os
import tkinter.filedialog as tk

def doesProcessDirExist(path):
    if os.path.isdir(path+'/process'):
       return True
    else:
        return False

def removeProcessDir(path):
    processpath = path + "/Process"
    files = os.listdir(processpath)
    for f in files:
        os.remove(processpath+'/'+f)
    os.rmdir(path+"/Process")


def iterateDirectories(path):
    dirlist = os.listdir(path)
    for dir in dirlist:
        if os.path.isdir(path + '/' + dir):
            if doesProcessDirExist(path+'/'+dir):
                print('remove process dir '+path+'/'+dir)
                removeProcessDir(path+'/'+dir)
            else:
                iterateDirectories(path+'/'+dir)



filepath = tk.askdirectory(initialdir="D:\\Astronomy")
files = os.listdir(filepath)

for f in files:
    if os.path.isdir(filepath + '/' + f):
        if doesProcessDirExist(filepath +'/' + f):
            print('remove directory '+filepath +'/' + f)
            removeProcessDir(filepath+'/'+dir)
        else:
            iterateDirectories(filepath +'/' + f)

if not doesProcessDirExist(filepath):
    print("directory does not exist")
else:
    print('remove directory')
    removeProcessDir(filepath)
