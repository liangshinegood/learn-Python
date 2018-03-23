#思路：输入数据，然后调用floor,ceil,rint,最后输出


import numpy as np
A = np.array((input().split()),float)
print(np.floor(A),np.ceil(A),np.rint(A),sep='\n')
