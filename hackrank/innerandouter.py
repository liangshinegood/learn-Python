# inner 对应元素x1*y1+x2*y2
# outer x1*(y1,y2),x2*(y1,y2)
# 计算这个就是调用对应的值即可
import numpy
A,B = [numpy.array(input().split,int) for _ in range(2)]
print('\n'.join(str(op(A,B))for op in (numpy.inner,numpy.outer)))



