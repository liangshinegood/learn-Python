
class Email:
    password = None
    
    def __init__(self):
        self.myname = 'zhangsan'


    @property
    def username(self):
        result = self.myname[0] + '*' + self.myname[-1]
        return result
    
#    @property.setter # 这里以及不是property 而是username
    @username.setter
    def username(self,value):
        self.myname = value
        
    
#    @property.deleter
    @username.deleter
    def username(self):
        del self.myname

em = Email()
print(em.username)

em.username = 'wangwu'
print(em.username)

del em.username
print(em.username)
