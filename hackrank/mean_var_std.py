# 公式的使用，mean,var,std

import numpy as np
n = np.array([input().split() for _ in range(int(input().split()[0]))],int)
print(np.mean(n,axis=1),np.var(n,axis=0),np.std(n),sep='\n')



