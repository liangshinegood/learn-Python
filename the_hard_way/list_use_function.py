listA = ['a','b','c','d','a']
listB = ['e','f']
print('list index method is:',listA.index('b')) # 这里面应该添加的事列表中的元素
print('list count method is:',listA.count('a'))
listA.append('f') # 直接执行append 函数
print('use append method  and the new listA is:',listA)
listC = listA.copy()
print('use the copy method ,the listC is:',listC)
listA.extend(listB)# 感觉等同于listA + listB
print('use the extend method and the new is :',listA)
print('the listA + listB is:',listA+listB)
# print('the listA - listB is:',listA-listB) # 错误 unsupported
listA.clear()
print('use clear method and the new is:',listA)

listC = ['A','B','c']
listC.insert(0,'a')
print('use the insert method and the new listC is:',listC)
listC.pop(3)
print('use the pop method i want to del the c so the new result is :',listC)
listC.remove('B')
print('use the remove method and the new result is :',listC)
# listC.remove('b')
# print('use the remove method and i want remove a b but the b is not in listC,so the result is: ',listC)
listC.reverse()
print('use the reverse and the new result is :',listC)
listD = [2,3,1,9,0]
listD.sort() # 从小到大
print('use the sort and the new result is :',listD)
# 如果想从大到小的话，在reverse一下就好了
listD.reverse()
print('reverse the sorted result',listD)