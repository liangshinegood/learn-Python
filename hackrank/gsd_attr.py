class Human:
    age = 18
    name = 'zhangsan'
    
    def run(self):
        print("lallalallal")
    
    def __getattr__(self,attrname):
        print(attrname)
        if attrname == 'height':
            print("this is getattr")
            return 120
        else:
            return 110
        pass

    def __setattr__(self,attrname,value):
        if attrname == 'age':
#            self.age = 20
             object.__setattr__(self,self.age,value)
#            return self.age
        elif attrname == 'name':
            object.__setattr__(self,attrname,value)
            
        else:
            pass
    def __delattr__(self,attrname):
        if attrname == 'aage':
            pass
        else:
            object.__delattr__(self,attrname)
        
        pass
hh = Human()
print(hh.height)
hh.name = 'wangwu'
print(hh.name)
del hh.age
print('the age is ',hh.age)










