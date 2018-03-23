# 思路：比较简单就是求行列式

import numpy as np

n = int(input())

my = np.array([input().split() for _ in range(n)],float)

print(np.linalg.det(my))


