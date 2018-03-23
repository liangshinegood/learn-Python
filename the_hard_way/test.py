import keyword
# a = 20
# b = 20
# c = id(a)
# print( a is b) # is是判断两个标识符是不是引用自一个对象
#
# print( a is not b ) #is not是判断两个标识符是不是引用自不同对象
# print( a is c)
# print( a is not c)
# print(keyword.kwlist)
# 按位运算符
# a = 10  # 0000 1010
# b = 20  # 0001 0100
# c = 0
# c = a & b # 0000 0000
# print('位与运算符 & ：',c) # 相同则同
# c = a | b # 0001 1110 # 不同、相同都同
# print('位或运算 | ：',c)
# c = a ^ b # 0001 1110 # 不同则同，同则不同
# print('位异或运算:',c)
# c = ~a # 00001011  = 将二进制数+1之后乘以-1,x的按位翻转 = -(a+1) = -(00001011)
# print('按位取反 ~:',c)
# c = a << 2 # 0010 1000 = 40 # 左边去掉 两个 0 ， 后面补齐 两个 0
# print('按位向左移动两位的结果：',c)
# c = a >> 2 # 0000 0010 = 2
# print('按位向右移动两位的结果为：',c)



## 字符串操作
# array = "我要成为\t数据科学家"
# print(array.expandtabs())
# s = 'ilovepython'
# print(s[1:4])
# print(s[:4])
# print(s[4:])
# print(s[:])
# print(s[0])
# b = 'data'
# print(s+b)
# print(b*2)
# # for i in range(1,N+1):

# listA = [1,2,3,4]
# listB = [5,6,7]
# print(listA + listB)
# print(listA*2)
# print(listA.index(2))
# print(listA.count('1'))
# listA.append()
# listA.clear()
# listA.copy()
# listA.extend()
# listA.insert()
# listA.pop()
# listA.remove()
# listA.reverse()
# listA.sort()


# # 集合set变量的一些操作
# a = set({'jack','tom','jack','maya'})
# a1 = set('abcd')
# b1 = set('cdf')
# print(a)
# print('a1的值：',a1)
# print('b1的值：',b1)
# print('a 和 b 之间的差集:',a1-b1) # a 和 b 之间的差集
# print('a 和 b 之间的并集:',a1 | b1) # a 和 b 之间的并集
# print('a 和 b  之间的交集:',a1 & b1) # a 和 b  之间的交集
# print('a 和 b 中不同时存在的元素:',a1 ^ b1) # a 和 b 中不同时存在的元素


# 字典操作
# dicA = {'zhangsan':98,'lisi':80,'wangwu':65}
# dicB = {}
# print(dicA)
# print('查询key 为 zhangsan对应的值：',dicA['zhangsan'])
# del dicA['lisi']
# print('del dicA 为 删除key 为 lisi的值：',dicA)
# dicA['liangliu'] = 77
# print('添加 key 为 liangliu 的 值为 77：',dicA)
# print('返回所有的keys组成成员',list(dicA.keys()))
# print('sorted 为 让 keys 进行排序：',sorted(dicA.keys()))
# print('判断 对应的 key 值是否在: ','wangwu' in dicA)
# print('判断 对应的 key 值是否在: ','wangwu'  not in dicA)
# dicC = dict( jack = 40 ,tom = 60 , merry = 70)
# print('创建dicC 方法is:',dicC)
# dicD = dict([('a',1),('b',2),('c',3)])
# print('创建dicD 方法is:',dicD)
# dicA.keys()
# dicA.pop()
# dicA.copy()
# dicA.clear()
# dicA.fromkeys()
# dicA.get()
# dicA.items()
# dicA.popitem()
# dicA.setdefault()
# dicA.update()
# dicA.values()


# ## 元祖操作
# tupleA = ('math','statistic','compu','data struct')
# tupleB = ('liter','english')
# print(tupleA)
# print(tupleA + tupleB)

