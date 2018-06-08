import json

class JsonReader(object):

    def __init__(self,file_path):
        self.file_path = file_path
        self.data = list()

    def f_read(self):
        f = open(self.file_path,'r')
        self.data = json.loads(f.read())
        f.close()
        return self.data
