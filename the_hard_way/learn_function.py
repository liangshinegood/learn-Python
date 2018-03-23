def loves():
    print('i love data ')

print(loves())

def loves1(w):
    return 'i love '+ w
print(loves1('data'))
print(loves1('5'))

def loves2(w,l):
    return w + " love " + l
print(loves2('i','data'))

# 全局变量和局部变量的部分
a= 4
def print_func1():
    a = 17
    print('in print_func1 a = ',a)
def print_func2():
    print('in print_func2 a = ',a)

print_func1()
print_func2()
print('a = ',a)

def parrot(voltage,state='a stiff',action='voom',type='Norwegian Blue'):
    print("-- this parrot wouldn't",action,end = ' ')
    print('if you put',voltage,'volts through it.')
    print('-- lovely plumage,the',type)
    print("--it's",state,"!")
parrot(1100) # 自动将 voltage = 1100
parrot(voltage= 1100)
parrot(voltage= 1100,action = 'VOOM')
parrot(action= 'VOOMM',voltage = 11001)
parrot('a million','bereft of life','jump') # 自动赋值给前三个参数
parrot("-- it's",state='',action = '!')
# ----error operator
parrot() # parrot() missing 1 required positional argument: 'voltage
parrot(voltage=5,a='dead') #parrot() got an unexpected keyword argument 'a'
parrot(110,voltage= 220) # got multiple values for argument 'voltage


def arithmetic_mean(*args):
    sum = 0
    for x in args:
        sum += x
    return  sum
print(arithmetic_mean(1,2,3,4))
# print(arithmetic_mean((1,2))) #unsupported operand type(s) for +=: 'int' and 'tuple' 注意这是书写错误
print(arithmetic_mean(1,2))
print(arithmetic_mean(1,2,3,4,5,6,7))
print(arithmetic_mean())

#注意 in (a,b)  == a and == b
for x in (1,10):
    print(x)

