
import os

filepath = 'C:\\Users\\blake\\Documents\\GitHub\\Python-Coding-Projects\\OS module drill\\files\\'

directory = os.listdir(filepath)


for filename in directory:
    if filename.endswith('.txt'):
        abPath = os.path.join(filepath,filename)
        mTime = os.path.getmtime(abPath)
        print(abPath)
        print(mTime)


