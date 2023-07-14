import os

# List files and folders in dir
dirlist = os.listdir(os.getcwd())
print(dirlist)

# List only files in dir
for f in dirlist:
    if os.path.isfile(f):
        print(f)

# Filter files by type
pptx = []
docx = []
txt = []
xlsx = []
python = []
dirs = []
other = []

for f in dirlist:
    if ('.' in f):
        ftype = f.split('.')[1]
        if ftype == "pptx":
            pptx.append(f)
        elif ftype == "docx":
            docx.append(f)
        elif ftype == "txt":
            txt.append(f)
        elif ftype == "xlsx":
            xlsx.append(f)
        elif ftype == "py":
            python.append(f)
        else:
            other.append(f)
    else:
        dirs.append(f)

print(f"PPTX: {pptx}\nDOCX: {docx}\nTXT: {txt}\nXLSX: {xlsx}\nPYTHON: {python}\nDIRS: {dirs}\nOTHER: {other}")
