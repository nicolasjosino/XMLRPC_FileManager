import os

class fileManager:
    def __init__(self, path):
        self.path = path
    
    def listFiles(self):
        return os.listdir(self.path)

    def getArchive(self, name):
        archivePath = os.path.join(self.path, name)
        contents = open(archivePath, "rt").read()
        return bytearray(contents, 'utf-8')

    def deleteArchive(self, name):
       archivePath = os.path.join(self.path, name)
       if os.path.exists(archivePath):
            os.remove(archivePath)