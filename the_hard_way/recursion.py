def recursionFun(x):
    #1. 打印x
    print(x)
    #2. 增加条件
    if x > 0:
        recursionFun(x-1)
    else:
        print('======================')
    #3. 打印x
    print(x)
m = recursionFun(3)
print(m)
'''分析如下：
    def recursionFun(3):
    #1. 打印x
    print(3)
    #2. 增加条件
    if x > 0:
        recursionFun(3-1)  执行recursionFun(2)继续执行
    #3. 打印x
    print(3)   等待操作
    
    
    def recursionFun(2):
    #1. 打印x
    print(2)
    #2. 增加条件
    if x > 0:
        recursionFun(2-1)  执行recursionFun(1)继续执行
    #3. 打印x
    print(2)   等待操作
    
      def recursionFun(1):
    #1. 打印x
    print(1)
    #2. 增加条件
    if x > 0:
        recursionFun(1-1)  执行recursionFun(0)继续执行
    #3. 打印x
    print(1)   等待操作
    
    
      def recursionFun(0):
    #1. 打印x
    print(0)
    #2. 增加条件
        print('======================')
    #3. 打印x
    print(0)   等待操作
    
    '''
