
class yuzhengfeng:
    obj = None
    def __new__(cls):
        if cls.obj == None:
            cls.obj = object.__new__(cls)
            return cls.obj
        else:
            return cls.obj
    

one = yuzhengfeng()
print(one)

two = yuzhengfeng()
print(two)

three = yuzhengfeng()
print(three)










