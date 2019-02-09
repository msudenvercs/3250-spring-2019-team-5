#this class is used to read binary files
class FileReader:
#constructor
    def __init__(self,name):
        self.name = name
#method to read the file specified by name. Returns a bytes object containing the bytes read.
    def read(self):
        with open(self.name, "rb") as binary_file:
            return binary_file.read()
