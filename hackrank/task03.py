# 先别着急一下子就把逻辑写对，一点一点的写，由简单到复杂
from itertools import combinations
class task03:
	def __init__(self):
		self.listB = []
	
	def allcomb(self,s,n):
		 
		listA=[]
		itemA=""
		for ev in range(1,n+1):
			listA = list(combinations(sorted(s),ev))
			for item in listA:
				for i in item:
					itemA += i
					if(len(itemA)==ev):
						self.listB.append(itemA)
						itemA=""
						break
		return self.listB
	
	def printlist(self,s,n):
		for item in self.allcomb(s,n):
			print(item)
	
inv = [it for it in input().split()]
s = inv[0]
n = int(inv[1])
tk = task03()
tk.printlist(s,n)

