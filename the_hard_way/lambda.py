mylam = lambda x,y:x+y
returnValu = mylam(3,4)
print(returnValu)

mylam1 = lambda sex:'有jj'if sex == 'man' else '没有jj'
returnValu1 = mylam1('women')
print(returnValu1)

mylam2 = lambda x:type(x)
returnValu2 = mylam2(4)
print(returnValu2)


def myfunc():
    x = 8
    def innerf():
        nonlocal  x
        x += 10
        return x
    return innerf()
print(myfunc())