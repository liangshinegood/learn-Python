#思路：输入对应的值，调用numpy.sum,求得结果后再调用numpy.prob

import numpy

N,M = map(int,input().split())
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.prob(numpy.sum(A,axis=0),axis=0))



