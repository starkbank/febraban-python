import os.path


class FileUtils:

    @classmethod
    def create(cls, name, path):
        projectFolder = os.path.abspath(os.path.join(__file__, "../.."))
        fileAddress = projectFolder + path + name
        return open(fileAddress, 'w+')