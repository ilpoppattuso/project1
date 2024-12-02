import os
import shutil


path0 = r"C:\Users\matte\Pictures\Screenshots"
path1 = r"C:\Users\matte\AppData\Local\Temp"
path2 = r"C:\Users\matte\Pictures\Camera Roll\scuola"
path3 = r"C:\Users\matte\Downloads"



def binc():
    os.system('rd /s /q C:\$Recycle.bin')
    print("The bin is now empty!\n")
    
def screen():
    shutil.rmtree(path0)
    os.mkdir(path0)
    print("Screenshots are now deleted!\n")

def dns():
    os.system('ipconfig /flushdns')
    print("DNS cache is now empty!\n")

def temp():
    shutil.rmtree(path1)
    os.mkdir(path1)
    print("Temporary files are now deleted!\n")

def imgsch():
    shutil.rmtree(path2)
    os.mkdir(path2)
    print("Schoool images deleted!\n")

def down():
    shutil.rmtree(path3)
    os.mkdir(path3)
    print("All download files deleted!\n")



#print("Hello, what can I delete for you today?")

#while True:
commands = """Commands:
1 = Bin
2 = Screenshots
3 = DNS cache
4 = Temporary files
5 = School images
6 = Download files"""
    #if a == '1':
    #    binc()
    #elif a == '2':
    #    screen()
    #elif a == '3':
    #    dns()
    #elif a == '4':
    #    temp()
    #elif a == '5':
    #    imgsch()
    #elif a == '6':
    #    down()
    #else:
    #    print("Please insert a valid number")
