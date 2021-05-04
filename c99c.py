import os
import shutil
source=input('enter the source folder')
destination = input ('enter the destination folder')
source=source+'/'
destination=destination+'/'
listOfFiles=os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file),destination)