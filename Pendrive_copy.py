import os
import shutil
import psutil

#Detecting Pendrive
def detect_pendrive():
    #partitions all available drives
    drives = psutil.disk_partitions()

    #detecting the removable one and return the path
    for drive in drives:
        if 'removable' in drive.opts:
            return drive.mountpoint

    return None

#Detecting the files and returns a list of files
def findfile(src, a):

    dir = src
    entries = os.listdir(dir)

    for entry in entries:

        entry_path = os.path.join(dir, entry)

        if os.path.isfile(entry_path):
            a.append(entry_path)
        elif os.path.isdir(entry_path):
            findfile(entry_path,a)

    return a    


#While loop to continue with the simultaneous detection of pendrive in every second
while True:
    pendrive_path = detect_pendrive()
    if pendrive_path == None:
        print("No Pendrive detected!")
    else:
        print("Pendrive detected at: ", pendrive_path)
        break

entry = []
forCopy = []

result = findfile(pendrive_path, entry)

#Finding the .png files
for ent in result:
    if ent.endswith(".png"):
        forCopy.append(ent)


#Loop fro copying the files to new destination
for item in forCopy:
    shutil.copy(item, "C:\\Users\\HP\\Desktop\\deep ler\\try\\pendrive_copy\\Test\\" )