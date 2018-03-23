# 在输入列表的时候，求列表最大值
# 最后再将所有最大值进行平方 取摸

from itertools import product

K,M = map(int,input().split())
N = (list(map(int,input().split()))[1:] for _ in range(K))
results = map(lambda x:sum(i**2 for i in x)%M,product(*N))
print(max(results))



