import os

def absPath():
    path1 = os.path.abspath('.')
    print(path1)

def realPath():
    path2 = os.path.realpath(__file__)
    print(path2)

def cwdPath():
    path3 = os.getcwd()
    print(path3)

absPath()
realPath()
cwdPath()
