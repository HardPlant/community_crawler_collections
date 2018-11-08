import os

parentdir = ""

def ready_parent_dir(parent):
    global parentdir
    parentdir = parent
    if not os.path.exists(parent):
        os.mkdir(parent)
        return True

    if os.path.isdir(parent):
        return True

    else:
        return False

def write(content, filename = "", isDB=False):
    global parentdir
    with open(parentdir+'/'+filename,'w') as f:
        f.write(content)
    

def read(filename, isDB=False):
    global parentdir
    with open(parentdir+'/'+filename,'r') as f:
        text = f.read()
    return text