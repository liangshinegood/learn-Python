# 1. 如果存在，达到目标A = ('a',[1,2,3,5]) ('b',[4])，B = [a,b]
# 2. 根据B组中的数据，判断在A中是否存在，如果存在返回值，如果不存在返回-1
# 3. 测试所有的可能性，11 10 01 00
# 自己的
# from collections import defaultdict
#
# class task07:
#
# 	def __init__(self):
# 		d = defaultdict(list)
# 		inVal = [int(i) for i in input('请输入值：').split()]
# 		for i in range(inVal[0]):
# 			sa = input('请输入A组元素：')
# 			d['listA'].append(sa)
# 		for j in range(inVal[1]):
# 			sb = input("请输入B组元素：")
# 			d['listB'].append(sb)
# 		self.listA = d['listA']
# 		self.listB = d['listB']
#
#
# 	def isinA(self,A,B):
# 		attemp = defaultdict(list)
# 		for itemB in B:
# 				for i in range(1, len(A) + 1):
# 					if A[i-1] == itemB:
# 						attemp[itemB].append(i)
# 		return attemp
#
# 	def printResul(self):
# 		result = tk.isinA(self.listA,self.listB)
# 		s = ''
# 		for ib in self.listB:
# 			if result.get(ib)!= None:
# 				for key,value in result.items():
# 					if ib == key:
# 						for i in value:
# 							print(i,end=' ')
# 				print('')
# 			else:
# 				print(-1)
#
# tk = task07()
# tk.printResul()

from collections import defaultdict
d = defaultdict(list)
list1=[]
n, m = map(int,input().split()) #没有想到的原因是自己对map不熟悉

for i in range(0,n):
    d[input()].append(i+1)

for i in range(0,m):
    list1=list1+[input()]

for i in list1:
    if i in d:
        print( " ".join( map(str,d[i]) ))#把一个数组变为了字符串输出
    else:
        print(-1)


