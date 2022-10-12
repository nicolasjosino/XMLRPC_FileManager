import os
from xmlrpc.server import SimpleXMLRPCServer
from fileManager import fileManager

class fileServer:
    def __init__(self) -> None:
        self.server = SimpleXMLRPCServer(("localhost", 8000))
        self.manager = fileManager(os.path.join(os.getcwd(), "archive"))
        self.server.register_function(self.manager.listFiles, "listFiles")
        self.server.register_function(self.manager.getArchive, "getArchive")
        self.server.register_function(self.manager.deleteArchive, "deleteArchive")
        print("server up...")
        self.server.serve_forever()

server = fileServer()