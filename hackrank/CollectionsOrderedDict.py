#1. 输入值  int(num), for i in range(num): input()
#2. 计算逻辑 输入的同时就开始计算；核心的问题是：怎样把字典中重复的内容求和
#原有存储的值 + 现有的值，如果原有存储的值不存在则为0
#3. 输出内容
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input("输入数量:"))):
    item, space, quantity = input("值：").rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
    print(d.get(item,0))#可以获取之前已经input的数据值
    print(quantity)
    print(d[item])
    print(d)
for item, quantity in d.items():
    print(item, quantity)
