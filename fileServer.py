import os
from xmlrpc.server import SimpleXMLRPCServer
from fileManager import fileManager

class fileServer:
    def __init__(self) -> None:
        self.manager = fileManager(os.path.join(os.getcwd(), "archive"))