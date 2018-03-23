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
    def __repr__(self):
        return "this is my pure dream"
    __str__ = __repr__
hh = Human()
print(str(hh))
print(hh)
print(repr(hh))

