import os
import time
class SearchFiles():
    def __init__(self):
        pass
    def search(self,dir,filename):
        self.filename=filename
        self.dir =dir
        self.files=[]
        for root,dir,file in os.walk(self.dir):
            if self.filename in file:
                self.files.append(os.path.join(root,filename))
        return self.files


