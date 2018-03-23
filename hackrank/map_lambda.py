# 思路：首先要了解fibonacci逻辑
# 根据map\lambda返回对应数据

cube = lambda x:pow(x,3)
def fibonacci(n):
    lis = [0,1]
    for i in range(2,n):
        lis.append(lis[i-2] + lis[i-1])
    return(lis[0:n])



