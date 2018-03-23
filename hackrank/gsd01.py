
class Description:
    
    
    def __init__(self):
        self.firstname = 'zhang'
        self.secondname = 'san'
    def __set__(self,obj,valu):
        self.firstname = valu
    def __get__(self,obj,cls):
        result = self.firstname[0] + '***' + self.firstname[1]
        
        return result

    def __delete__(self,obj):
        del self.firstname





class Email:
    username = Description()
    password = None

    pass

em = Email()
print(em.username)

em.username = "lisi"

print(em.username)

del em.username
print(em.username)
