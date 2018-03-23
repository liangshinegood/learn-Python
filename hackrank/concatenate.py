import numpy as np
n,m,_ = [int(x) for x in input().strip().split()]
a,b = map(lambda x:np.array([input().strip().split() for i in range(int(x))],int),[n,m])
print(np.concatenate((a,b),axis = 0))


