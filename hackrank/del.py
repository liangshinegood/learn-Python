
class readF:
    def __init__(self,path):
        self.fp = open(path,'r')
    def readfile(self):
        txt = self.fp.read()
        print(txt)
    def __del__(self):
        print("file have been closed")
        self.fp.close()

file = readF('01.txt')

file.readfile()






