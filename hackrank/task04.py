# 这道题让我想起商务部时候的写的逻辑结构，不断的测试每一次以为是对了的时候，结果却是错的
# 所以这种情况之所以出现是因为在测试的时候根本就没有想清楚所有测试可能的值。所以穷尽所有的测试值
# 需要对业务有很深的了解，这也是编程的一种挑战。

import math
from cmath import phase
class task04:

	def compl(self,a,b):
		z = phase(complex(a, b))
		return z

	def rv(self,a,b):
		r=math.sqrt(self.pw(a)+self.pw(b))
		return r

	def pw(self,v):
		return math.pow(v,2)

	def valgood(self,v):
		vl = []
		firstval = w[0].isdigit()
		if (firstval):
			secondval = w[1]
			if (secondval == "+"):
				vl = [int(i) for i in w.split('+')]
			elif (secondval == "-"):
				vl = [int(i) for i in w.split('-')]
				vl[1] = (-1) * vl[1]
			else:
				vl = [int(i) for i in w.split()]
		else:
			theNum = w.count('-')
			if (theNum == 1):
				vl = [int(i) for i in w.split('+')]
			else:
				vl = [int(i) for i in w[1:].split('-')]
				vl[0] = (-1) * vl[0]
				vl[1] = (-1) * vl[1]
		return vl
w = input()
w = w[:len(w)-1]
tk = task04()
vl = tk.valgood(w)
print(tk.rv(vl[0],vl[1]))
print(tk.compl(vl[0],vl[1]))


