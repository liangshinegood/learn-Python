
#思路：输入对应的值，调用numpy.min,求得结果后再调用numpy.max

import numpy

N,M = map(int,input().split())
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.max(numpy.min(A,axis=1),axis=0))




