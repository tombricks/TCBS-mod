import os
thing = {}
for file in os.listdir('.'):
    with open(file, 'r') as dafile:
        newfile = ""
        for x in dafile.readlines():
            if not x.lstrip().startswith("owner") and not x.lstrip().startswith("add_core_of"):
                newfile += x
        thing[file] = newfile
    with open(file, 'w') as dafile:
        dafile.write(thing[file])