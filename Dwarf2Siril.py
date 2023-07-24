
import os
import tkinter.filedialog as tk
import json
import re
filepath = tk.askdirectory(initialdir="D:\\Astronomy\\test")

tmp = re.split('_' , filepath)
filedate = tmp[2]

f = open(filepath+"/shotsInfo.json")

data = json.load(f)
f.close()

target = data["target"]

target = target.replace(" ", "_")
print(target)

if os.path.isdir(filepath+"/lights"):
    print("directories exist")
else:
    os.mkdir(filepath+"/lights")
    os.mkdir(filepath+"/darks")
    os.mkdir(filepath+"/biases")
    os.mkdir(filepath+"/flats")
files = os.listdir(filepath)
for f in files:
    if os.path.isfile(filepath+"/"+f):
        if f.endswith(".fits"):
            os.rename(filepath+"/"+f,filepath+"/lights/"+filedate+"_"+f )

os.rename(filepath, filepath+"_"+target)
