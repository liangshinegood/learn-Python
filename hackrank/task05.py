class task05:

	def aver(self,n,listA):
		return sum(listA)/n
inin = input()
inivalue = [int(item) for item in input().split()]
hei = set(inivalue)
n = len(hei)
tk = task05()
result = tk.aver(n,hei)
print(result)
		





