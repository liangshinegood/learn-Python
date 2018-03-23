from collections import deque
# 当做列表使用
# queue = deque(['jim','tom','jack'])
# queue.append('meery')
# queue.append('maya')
# print(queue.pop())
# print(queue.popleft())
# # 当做堆栈使用
# listA = ['Jim','Tom','Jack','Mode']
# listA.pop()
# print(listA)
# listA.append('mode')
# print(listA)
#
# # Test
# print(listA[0])
# listA = [['Jim','Mom'],['Jack','father'],['Mode','brother']]
# print(listA[0])
# # print(len(listA[0]))
# newList = [[li[i] for li in listA] for i in range(len(listA[0]))]
# print('the newlist is :',newList)
# newList2 = []
# newlist3 = ['Jim','Jack','Mode']
# newlist4 = ['Mom','father','brother']
# newList2.append(newlist3)
# newList2.append(newlist4)
# print('the newList2 is :',newList2)
# newListTest = []
# for i in range(len(listA[0])):
#     for li in listA:
#         # if len(newListTest) <= len(listA):
#
#         newListTest.append(li[i])
#             # break
#         print(newListTest)
#         print(len(newListTest))
#         if len(newListTest) >= 3:
#             break
#             # newListTest.clear()
#             # continue
#             # break
#         # print('the newListTest is :',newListTest)
#     newList2.append(newListTest)
#     print(newListTest)
#
# print('the newList2 is:',newList2)
# a = 1
# b = 2
# print(a>b)



#当做列表推导式使用



# vec = [2,4,6]
# newVec1 = [3*x for x in vec]
# print('将列表中的元素都乘以3的结果是：',newVec1)
# newVec2 = [ [x,3*x]for x in vec]
# newVec3 = [(2*x,3*x) for x in vec]
# newVec4 = [{x:4*x} for x in vec]
# print("the new list2 is:",newVec2)
# print("the new list3 is:",newVec3)
# print("the new list4 is:",newVec4)
#
# freshfruit = [' banana',' loganberry','passion fruit ']
# newFruit = [ weapon.strip() for weapon in freshfruit]
# print('the newFruit is:',newFruit)
#
# newVec5 = (3*x for x in vec if x>3)
# print('the new tuple is :',newVec5)
# newVec6 = [3*x for x in vec if x>3]
# print('the new if_list is :',newVec6)
# newVec7 = {3*x for x in vec if x>3}
# print('the new if_dict is :',newVec7)
# print('the new dic is :',newVec7)
# dictA = {'A':6,'B':6}
# dictA.update(c = 7)
# print(dictA)
#

# vec1 = [2,4,9]
# vec2 = [4,3,-6]
# vec3 = [x*y for x in vec1 for y in vec2]
# vec4 = [x+y for x in vec1 for y in vec2]
# print('the len about vec1 is:',len(vec1))
# vec5 = [vec1[i] + vec2[i] for i in range(len(vec1))]
# print('loop the list method1:',vec3)
# print('loop the list method2:',vec4)
# print('loop the list method3:',vec5)
# vec6 = [str(round(355/113,i)) for i in range(1,6)]
# print("the new vec6 is:",vec6)

# 嵌套列表解析
# matrix = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]]
# newMatrix = [[row[i] for row in matrix] for i in range(4)]
# print(newMatrix)
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print('the another method transposed value is :',transposed)
# # for row in matrix:
# #         print(row)
# # 1. 需要新的储存列表；2.及时清空transposed_row列表；（之前范的错误，问题在于对于计算机的执行模式从上之下不熟悉）
# transposed = []
# for i in range(4):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
# print('the third method transposed value is:',transposed)
#
# a = [-1,1,66,333,444,1234.5]
# print(a[-3:])
# del a[0]
# print('del a[0] and the newest a is :',a)
# # 删除一个切片
# del a[:4]
# print('del a[:4],the newest a is:',a)
#
# b = 'a',1,4,'z'
# print(b)
# u = b,('3',4,a)
# print(u)


# tel = {'jack':123,'tom':234}
# dictA = {x:x**2 for x in (2,4,6)}
# print(dictA)

knighs = {'gallahad':'the pure','robin':'the brave'}
for k,v in knighs.items():
    print("the key and values is :",k,":",v)
for i,v in enumerate(['tic','tac','toe']):
    print("the enumerate values is:",i,v)
questions = ['name','quest','favorite color']
answers = ['lancelot','the holy grail','blue']
for q,a in zip(questions,answers):
    print("what is your {0}? it is {1}.".format(q,a))
for i in reversed(range(1,10,2)):
    print(i,end=' ')
basket = ['apple','orange','apple','pear','orange','banana']
for f in sorted(set(basket)):
    print(f)



