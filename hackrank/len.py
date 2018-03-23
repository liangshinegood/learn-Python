class Human:
    size = '360d'
    hair = 30
    def __init__(self):
        self.height = 2
        self.sex = 'na'
    def __len__(self):
        result = len(self.__dict__)
        return result

hh = Human()
print(len(hh))





