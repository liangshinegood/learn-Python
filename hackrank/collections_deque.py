# 思路：与之前的一些操作类似，可以用eval 进行实时操作

# 或者用getattr

from collections import deque
d = deque()
for _ in range(int(input())):
    cmd , *args = input().split()
    getattr(d,cmd)(*args)
[print(x,end=' ')for x in d]


