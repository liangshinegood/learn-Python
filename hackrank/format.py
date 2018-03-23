class Human:
    age = 18
    hair = 20
    name = 'zhangsan'
    def eat(self):
        print('hao chi , zhen hao chi ')
    def dream(self):
        print('my dream is data scientist!!!!')
#    def __str__(self):
#        return 'my dream'
#    def __repr__(self):
#        return "this is my pure dream"
#    __str__ = __repr__
#    def __bool__(self):
#        print("the bool method is ")
#        if self.age == 19:
#            return True
#        else:
#            return False
    def __format__(self,flag):
        print(flag)
        return self.name
        
hh = Human()
# print(bool(hh))
str1 = "lalala,{:center-6-#},large"
w = str1.format(hh)
print(w)










