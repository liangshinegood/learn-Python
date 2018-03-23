
class Human:
    age = 18
    name = "zhangsan"
    sex = "man"
    def say(self):
        print("lalalallalaaa")
    def cry(self):
        print("girl don't go away")
    def __call__(self):
        self.say()
        self.cry()

hh = Human()

hh()





