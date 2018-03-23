import unittest
class Human:
    age = 18
    sex = 'man'
    name = 'zhangsan'
    def __new__(cls,name):
        print(cls)
        print(name)
        print("new method is done")
#        return object.__new__(Monkey)
    def say(self):
        print("girl,please say love me ")
    def cry(self):
        print("girl cry 555555~")
yzf = Human('zhangsan')
print(yzf)

class Monkey:
    pass


















