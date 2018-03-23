#输入 4  for _ in range(4):input
#处理逻辑 1.怎样判断是否重复并统计
#输出
#该方法能够记录重复的元素，以及统计重复元素的个数
from collections import Counter, OrderedDict
#此方法相当于OrderedDict(Counter(input()for_ in range()))
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())#通过*的方式输出