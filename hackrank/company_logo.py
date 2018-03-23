# 本质上也是根据条件进行筛选
# 统计每一个字母出现的次数，并排序
# 选择排名前三位的字符
# 如果出现相同则根据字母排序进行，最后输出


from collections import Counter,OrderedDict

# 从新继承Counter,OrderedDict,Counter 计数，OrderedDict 排序
# .most_common(3) 为前3个值
class OrderedCounter(Counter,OrderedDict):
    pass

[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]


