import os

"Download exercism for all python"

cPath = os.getcwd()

dirs = os.listdir(cPath)

with open(".gitignore", "r") as f:
    lines = [line.strip() for line in f.readlines()
             if line[0] != "#" and line != ""]
    rDir = []
    for d in dirs:
        if d in lines or d in [".gitignore", ".git", "README.md"]:
            rDir.append(d)

    for d in rDir:
        dirs.remove(d)

for d in dirs:
    os.system("exercism download --exercise={} --track=python".format(d))
