import os

class fileManager:
    def __init__(self, path):
        self.path = path
    
    def listFiles(self):
        return os.listdir(self.path)

    def getArchive(self, name):
        filePath = os.path.join(self.path, name)
        if os.path.exists(filePath):
            contents = open(filePath, "rt").read()
            return bytearray(contents, 'utf-8')
        else: return False

    def deleteArchive(self, name):
       filePath = os.path.join(self.path, name)
       if os.path.exists(filePath):
            os.remove(filePath)
            return True 
       else: return False