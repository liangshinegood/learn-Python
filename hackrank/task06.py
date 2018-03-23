# 首先是基于calendar 本身函数的使用，然后将具体日期转化为week数字，将数字转化为大写字母，最后将input数据进行转化
import calendar

class task06:
	
	def inputValue(self,year,month,day):
		resul = calendar.weekday(year,month,day)
		return resul
	
	def weekday(self,year,month,day):
		weeknum = self.inputValue(year,month,day)
		if weeknum==0:
			return 'MONDAY'
		elif weeknum==1:
			return 'TUESDAY'
		elif weeknum==2:
			return 'WEDNESDAY'
		elif weeknum==3:
			return 'THURSDAY'
		elif weeknum==4:
			return 'FRIDAY'
		elif weeknum==5:
			return 'SATURDAY'
		else:
			return 'SUNDAY'

data = [int(i) for i in input("请输入日期 mm dd yyyy:").split()]
tk = task06()
resul = tk.weekday(data[2],data[0],data[1])
print(resul)





