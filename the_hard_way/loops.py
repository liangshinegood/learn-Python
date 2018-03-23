N = int(input("请输入一个整数："))
for i in range (0,N):
    print(i**2,end='\t')
sumA = 0
n = 1
while n <=100:
    sumA += n
    n += 1
print('1..100的和为：',sumA)

print('使用function sum can do this:',sum(range(1,101),0)) # 从什么 0 ， 1,2 开始就要加上后面的这个数

# 注意break 的使用
for n in range(2,6):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break # 跳出 x 循环
        else:
            print(n,'is a prime number')

# 注意continue 的使用
for n in range(2,6):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            continue #  继续 x 的下一个循环
        else:
            print(n,'is a prime number')

# pass 的使用他会一直在执行
while True:
    pass