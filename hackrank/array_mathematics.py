# 思路：使用 eval 或者 getattr()

import numpy as np

n,m = list(map(int,input().split()))

a1 = np.array([input().split() for _ in range(n)],int)
a2 = np.array([input().split() for _ in range(n)],int)
print(*[eval('a1'+i+'a2') for i in ['+','-','*','//','%','**']],sep='\n')




