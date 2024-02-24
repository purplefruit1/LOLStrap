from tkinter import *
import os
import time
import shutil
import subprocess

master = Tk()

#LOLStrap code
def clone_file(original_file, new_file):
    try:
        with open(original_file, 'rb') as f:
            content = f.read()
        with open(new_file, 'wb') as f:
            f.write(content)
        print(f"File {original_file} cloned successfully as {new_file}")
    except IOError as e:
        print(f"Error: {e}")

def bootls():
    script_path = os.path.realpath(__file__)
    parent_dir = os.path.dirname(script_path)
    os.chdir(parent_dir)
    path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\1v1.LOL\\" #.lf
    getdir = os.getcwd()
    print("Working dir %s" % getdir) #bootls
    os.chdir(path)
    cpath = getdir
    getdir = os.getcwd()
    print("Working dir %s" % getdir) #.lf
    if os.path.exists(cpath+"\\boot.config"):
        print("f")
    else:
        print("nf ERR: 001. Please check error.txt")
        errtxt = open(cpath+"\\error.txt", "w")
        errtxt.write("ERR CODE: 001. boot.config cannot be found. Re-run the script.")
        errtxt.close()
        LOLexe = getdir+"\\1v1_LOL.exe"
        subprocess.run(LOLexe)
        
    print(cpath+"\\boot.config")
    np = getdir+"\\1v1_LOL_Data"
    print(np)
    cn = os.path.basename(cpath)
    nep = os.path.join(np, cn)

    if os.path.exists(np+"\\boot.config"):
        print("a")
       # os.remove(np+"\\boot.config")
        time.sleep(1)
        bootconf = cpath+"\\CONFIG_file_BACKUP\\boot.config"
        bootlsFOLD = cpath+"\\boot.config"
        LOLDATFOLD = path+"\\boot.config"
        clone_file(bootconf, LOLDATFOLD)
        LOLexe = getdir+"\\1v1_LOL.exe"
        subprocess.run(LOLexe)
    else:
        print("b")
        bootconf = cpath+"\\CONFIG_file_BACKUP\boot.config"
        bootlsFOLD = cpath+"\\boot.config"
        LOLDATFOLD = path+"\\boot.config"
        clone_file(bootconf, LOLDATFOLD)
        LOLexe = getdir+"\\1v1_LOL.exe"
        subprocess.run(LOLexe)

def launchLOL():
    script_path = os.path.realpath(__file__)
    parent_dir = os.path.dirname(script_path)
    os.chdir(parent_dir)
    path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\1v1.LOL\\" #.lf
    getdir = os.getcwd()
    print("Working dir %s" % getdir) #bootls
    os.chdir(path)
    time.sleep(0.2)
    getdir = os.getcwd()
    LOLexe = getdir+"\\1v1_LOL.exe"
    print(LOLexe)
    subprocess.run(LOLexe)

def remls():
    script_path = os.path.realpath(__file__)
    parent_dir = os.path.dirname(script_path)
    os.chdir(parent_dir)
    path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\1v1.LOL\\1v1_LOL_Data" #.lf
    getdir = os.getcwd()
    print("Working dir %s" % getdir) #bootls
    os.chdir(path)
    cpath = getdir
    getdir = os.getcwd()
    print("Working dir %s" % getdir) #.lf

    if os.path.exists(path+"\\boot.config"):
        #os.remove(path+"\\boot.config")
        bootconf = cpath+"\\CONFIG_file_BACKUP\\boot.config"
        bootlsFOLD = cpath+"\\boot.config"
        LOLDATFOLD = path+"\\boot.config"
        clone_file(bootconf, bootlsFOLD)
        clone_file(bootconf, LOLDATFOLD)
    else:
        bootconf = cpath+"\\CONFIG_file_BACKUP\\boot.config"
        bootlsFOLD = cpath+"\\boot.config"
        LOLDATFOLD = path+"\\boot.config"
        clone_file(bootconf, bootlsFOLD)
        clone_file(bootconf, LOLDATFOLD)

    bootls()


title = Label(master, text="LOLStrap: Debug bootstrapper for 1v1.LOL")
title.pack()
title['background']='#b8f1f2'

blank1 = Label(master, text="")
blank1.pack()
blank1['background']='#b8f1f2'

mainClickButton = Button(master, text="Run LOLStrap", command = remls)
mainClickButton.pack()
mainClickButton['background']='#b8f1f2'

zeroBS = Button(master, text="Run 1v1.LOL (without LOLStrap)", command = launchLOL)
zeroBS.pack()
zeroBS['background']='#b8f1f2'

master.title("LOLStrap B_M-7_2_24")
master.geometry("%sx%s+%s+%s" % (550,150,512,512))
master['background']='#67d3d6'

b = input("Press enter to exit LOLStrap")
