import os.path

def create(name, path):
    projectFolder = os.path.abspath(os.path.join(__file__ ,"../.."))
    fileAddress = projectFolder + path + name
    return open(fileAddress, 'w+')
