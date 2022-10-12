import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:

    print("File Manager operations: listFiles, getArchive and deleteArchive.")
    print("Type 'exit' to leave.")
    
    while (True):
        operation = input("Type the desired operation: ")

        match operation:
            case "listFiles": 
                print("listing files: %s" % str(proxy.listFiles()))
            case "getArchive":
                file_ = input("Type the file name (with extension): ")
                print(str(proxy.getArchive(file_)))
            case "deleteArchive":
                file_ = input("Type the file name to be deleted (with extension): ")
                print(str(proxy.deleteArchive(file_)))
            case "exit":
                print('bye...')
                break
            case _:
                print("ERROR: Please type a valid command")
