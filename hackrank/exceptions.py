#处理方式的重点思想：
#处理多行输入，range(input方式)
#用map做映射，将输入的值转化为int
for i in range(int(input())):
    try:
        a,b = map(int,input().split())
        print(a/b)
    except BaseException as e:
        print("Error Code:",e)


