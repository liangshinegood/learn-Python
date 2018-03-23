class Email:
    username = 'zhangsan'
    password = None

    def __init__(self):
        self.myname = 'lisi'
    def setusername(self,value):
        self.myname = value

    def getusername(self):
#        print(self.username)#不可以打印出username
        result = self.myname[0] + '*' + self.myname[1]
        return result 

    def delusername(self):
        print("hi,delete is here")
        del self.myname
    #如果getusername,setusername,delusername位置替换为：set,get,del 则为none
    username = property(getusername,setusername,delusername)

em = Email()
print(em.username)

em.username = 'wangwu'
print(em.username)


del em.username
print(em.username)





