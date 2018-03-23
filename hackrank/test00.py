from collections import Counter, OrderedDict
c = Counter(input('请输入信息：') for i in range(3))
print(c)
print(OrderedDict(c))