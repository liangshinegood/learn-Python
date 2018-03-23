# 1. 学习资料 #

	1.个人购买的学习教程
	[http://www.ydma.com/classroom/14/task](http://www.ydma.com/classroom/14/task)
	
	2.learn Python the hard way


# 2. 学习总结 #
	
	1.对于语言本身的理解和感悟：语言是工具，而真正厉害的是思想和思维，这就好比语言是一支笔，而真正让别人吃惊和惊叹的是用笔书写的文章。

----------

	2.语言特性：所有的语言都一样，都是有一个从陌生到熟练的过程，而这个过程中，基本的规律是：模仿，熟练，再思考，再熟练。这一点从做hankrank深有体会，自己想了半天想不出解决的思路，看看别人写的代码思路，恍然大悟，其核心的原因是对语言本身不熟悉，这样就思考不到那一层面，随着语言用的多了，见的多了，自然也就会解决了。

----------

	3.python 是这样，我们学习英语，其他语种，小孩子刚开始学语言也是这样（通过模仿，先一个单词，然后两个单词，然后一个句子，最后表达思想），而我们学习的过程中，其最重要的便是耐心，同时不要怕出错，错误是一种常态


----------
Python语言
	

	**1.环境搭建**
	这里资源很多，基本按照网上的流程走即可，没什么难点。
	总体而言，系统包括：windows,linux,MaC

----------

	**2.基本语法**
	语法构成：
	1.定义变量，根据运算符，逻辑判断分支来实现想要实现的功能；
	2.注意格式和缩进问题；
	3.用注释，来解释想要表达的想法；
	4.为了提高代码的使用率，通过导入已有模块、使用已有函数、面向对象方法，来简化操作，提高代码的复用率
	
----------
	**3.变量类型**

----------

- 	数字（int\long\float\bool\complex）

	- 	注意数字的长度限制
	- 	数字之间的转化
	- 	import math
	
	知识点1：常见的数学函数（abs,ceil,floor,round,cmp,exp,log,log10,max,min,modf,pow,sqrt）

	知识点2：随机函数random
	
	知识点3：三角函数（cos,acos,sin,asin,tan,atan,hypot,degrees,radians）

	知识点4：进制转换（%d,%o,%x）

----------

- 	字符
	- 	代码样例：
		str = 'Hello World!'
		print（ str)   # 输出完整字符串
		print（ str[0])# 输出字符串中的第一个字符
		print（ str[2:5])  # 输出字符串中第三个至第五个之间的字符串
		print（str[2:])   # 输出从第三个字符开始的字符串
		print（ str * 2)   # 输出字符串两次
		print（ str + "TEST")  # 输出连接的字符串

	知识点1：使用反斜杠()转义特殊字符,如果不用反斜杠可用r

	知识点2：系统自带的一些字符，不可以作为变量，可以通过keyword模块中的kwlist来查看

	知识点3：常用的函数（zfill,index,find,split,strip,isdigit,isalpha,islower,isnumeric,issupper,istitle,endswith,startswith,count,capitalize,center,encode,expandtabs,format,join,ljust,partition,title,swapcase,replace,maketrans,upper）
	

----------

	
- 	列表
	- 	代码样例
	list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
	tinylist = [123, 'john']
	 
	print( list )              # 输出完整列表
	print( list[0]   )         # 输出列表的第一个元素
	print( list[1:3]  )        # 输出第二个至第三个元素 
	print( list[2:]  )         # 输出从第三个开始至列表末尾的所有元素
	print( tinylist * 2 )      # 输出列表两次
	print( list + tinylist)    # 打印组合的列表

	知识点1：常见函数（append,insert,pop,remove，count,copy,,reverse,sort，index,list）

	知识点2：列表推导式，[3*x for x in listA],[3*x for x in listA if x > 3]当然也可以更复杂的表现方式

	知识点3：注意比较 list中的append 和 extend 区别
	
	

----------

- 	元祖
	- 	代码样例
	tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
	tinytuple = (123, 'john')
	print( tuple )              # 输出完整元组
	print( tuple[0]    )        # 输出元组的第一个元素
	print( tuple[1:3]   )       # 输出第二个至第三个的元素 
	print( tuple[2:]    )       # 输出从第三个开始至列表末尾的所有元素
	print( tinytuple * 2 )      # 输出元组两次
	print( tuple + tinytuple )  # 打印组合的元组

	知识点1：string、list和tuple都属于sequence（序列）
	
	知识点2：tup1 = () # 空元组，tup2 = (20,) # 一个元素，需要在元素后添加逗号

	知识点3：虽然tuple的元素不可改变，但它可以包含可变的对象，tupleA + tupleB

	知识点4：常见函数：del,+,*,in,len,切片，tuple

	

----------

- 	字典
	- 	代码样例
	tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
	print(dict['one'])          # 输出键为'one' 的值
	print(dict[2] )             # 输出键为 2 的值
	print( tinydict )            # 输出完整的字典
	print( tinydict.keys() )     # 输出所有键
	print( tinydict.values()  )  # 输出所有值


	知识点1：常见函数：keys,values,items,pop,clear,get,update,setdefault,

	知识点2：在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来

	知识点3：在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到

	知识点4：同时遍历两个或更多的序列，可以使用 zip() 组合

	知识点5：要反向遍历一个序列，首先指定这个序列，然后调用 reversesd() 函数

	知识点6：要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值


----------

- 	集合
	- 	知识点1：集合（set）是一个无序不重复元素的集
	- 	知识点2：创建一个空集合必须用 set()
	- 	知识点3：比较两个集合的差（-）、并（|）、交（&）

----------

	**4.运算符**

- 	算术
	- 	+，-，*，/，%，**，//


- 	比较
	- 	==,!=,<>,>,>=,<,<=


- 	赋值
	- 	=,+=,-=,*=,/=,%=,**=,//=

- 	逻辑
	- 	and , or , not
	
- 	位
	- 	a = 0011 1100，b = 0000 1101
	
	&,按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0。(a & b) 输出结果 12 ，二进制解释： 0000 1100

	|,按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。(a | b) 输出结果 61 ，二进制解释： 0011 1101

	^,按位异或运算符：当两对应的二进位相异时，结果为1。(a ^ b) 输出结果 49 ，二进制解释： 0011 0001

	~,按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1。(~a ) 输出结果 -61 ，二进制解释： 1100 0011，在一个有符号二进制数的补码形式。

	<<,左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。a << 2 输出结果 240 ，二进制解释： 1111 0000

	>>右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>右边的数字指定了移动的位数。a >2 输出结果 15 ，二进制解释： 0000 1111
	

- 	成员
	- 	in , not in
	
	
- 	身份
	- 	is ,is not


- 	优先级比较
	- 	指数，加减乘除优先 > 比较> 赋值运算 > 身份、成员、逻辑运算

----------

	**5.条件语句**

----------

	样例：
	num = 5     
	if num == 3:            # 判断num的值
	    print 'boss'        
	elif num == 2:
	    print('user')
	elif num == 1:
	    print('worker')
	elif num < 0:           # 值小于零时输出
	    print 'error'
	else:
	    print('roadman' )    # 条件均不成立时输出，不支持 switch 语句，所以多个条件判断，只能用 elif 来实现
	

----------
	**6.循环语句**
	样例：while,for

----------

	i = 1
	while i < 10:   
	    i += 1
	    if i%2 > 0:     # 非双数时跳过输出
	        continue
	    print i         # 输出双数2、4、6、8、10
	 
	i = 1
	while 1:            # 循环条件为1必定成立
	    print i         # 输出1~10
	    i += 1
	    if i > 10:     # 当i大于10时跳出循环
	        break
	

----------

	count = 0
	while count < 5:
	   print count, " is  less than 5"
	   count = count + 1
	else:				#循环中使用else
	   print(count, " is not less than 5")

----------

	fruits = ['banana', 'apple',  'mango']
	for index in range(len(fruits)):
	   print('当前水果 :', fruits[index])
	 
	print "Good bye!"

----------

	fruits = ['banana', 'apple',  'mango']
	for fruit in fruits:        # 第二个实例
	   print('当前水果 :', fruit)

----------

	for num in range(10,20):  # 迭代 10 到 20 之间的数字
	   for i in range(2,num): # 根据因子迭代
	      if num%i == 0:      # 确定第一个因子
	         j=num/i          # 计算第二个因子
	         print '%d 等于 %d * %d' % (num,i,j)
	         break            # 跳出当前循环
	   else:                  # 循环的 else 部分
	      print(num, '是一个质数')

----------
	for letter in 'Python':
	   if letter == 'h':
	      pass
	      print('这是 pass 块')
	   print('当前字母 :', letter)
	
	print("Good bye!")

	知识点1：注意break,continue
	

----------
	**7.函数**
	样例：
	# 定义函数（一个参数，或者没有参数）
	def printme( str ):
	   "打印任何传入的字符串"
	   print（str）;
	   return;
	 
	# 调用函数
	printme("我要调用用户自定义函数!");
	printme("再次调用同一函数");

----------

	#可写函数说明（多个参数）
	def printinfo( name, age ):
	   "打印任何传入的字符串"
	   print "Name: ", name;
	   print "Age ", age;
	   return;
	 
	#调用printinfo函数
	printinfo( age=50, name="miki" );

----------
	# 可写函数说明 （不定长参数）
	def printinfo( arg1, *vartuple ):
	   "打印任何传入的参数"
	   print "输出: "
	   print arg1
	   for var in vartuple:
	      print var
	   return;
	 
	# 调用printinfo 函数
	printinfo( 10 );
	printinfo( 70, 60, 50 );

----------
	# 可写函数说明 （lambda 表达式函数）
	sum = lambda arg1, arg2: arg1 + arg2;

----------

	知识点1：函数中需要注意：全局和局部变量
	知识点2：常用的内置函数（zip,map,getattr,divmod,enumerate,ord,all,any,isinstance,type,execfile,superiter,property，filter,frozenset,eval）

----------

	代码样例：zip
	>>>a = [1,2,3]
	>>> b = [4,5,6]
	>>> c = [4,5,6,7,8]
	>>> zipped = zip(a,b)     # 打包为元组的列表
	[(1, 4), (2, 5), (3, 6)]
	>>> zip(a,c)              # 元素个数与最短的列表一致
	[(1, 4), (2, 5), (3, 6)]
	>>> zip(*zipped)          # 与 zip 相反，可理解为解压，返回二维矩阵式
	[(1, 2, 3), (4, 5, 6)]

----------
	代码样例：map
	>>>def square(x) :            # 计算平方数
	...     return x ** 2
	... 
	>>> map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
	[1, 4, 9, 16, 25]
	>>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
	[1, 4, 9, 16, 25]
	 
	# 提供了两个列表，对相同位置的列表数据进行相加
	>>> map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
	[3, 7, 11, 15, 19]

----------
	代码样例：getattr
	>>>class A(object):
	...     bar = 1
	... 
	>>> a = A()
	>>> getattr(a, 'bar')        # 获取属性 bar 值
	1
	>>> getattr(a, 'bar2')       # 属性 bar2 不存在，触发异常
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	AttributeError: 'A' object has no attribute 'bar2'
	>>> getattr(a, 'bar2', 3)    # 属性 bar2 不存在，但设置了默认值
	3
	>>>

----------
	代码样例：divmod
	>>>divmod(7, 2)
	(3, 1)
	>>> divmod(8, 2)
	(4, 0)
	>>> divmod(1+2j,1+0.5j)
	((1+0j), 1.5j)


----------
	代码样例：all
	>>>all(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0
	True
	>>> all(['a', 'b', '', 'd'])   # 列表list，存在一个为空的元素
	False
	>>> all([0, 1，2, 3])          # 列表list，存在一个为0的元素
	False
	   
	>>> all(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0
	True
	>>> all(('a', 'b', '', 'd'))   # 元组tuple，存在一个为空的元素
	False
	>>> all((0, 1，2, 3))          # 元组tuple，存在一个为0的元素
	False
	   
	>>> all([])             # 空列表
	True
	>>> all(())             # 空元组
	True


----------
	代码样例：any
	>>>any(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0
	True
	 
	>>> any(['a', 'b', '', 'd'])   # 列表list，存在一个为空的元素
	True
	 
	>>> any([0, '', False])        # 列表list,元素全为0,'',false
	False
	 
	>>> any(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0
	True
	 
	>>> any(('a', 'b', '', 'd'))   # 元组tuple，存在一个为空的元素
	True
	 
	>>> any((0, '', False))        # 元组tuple，元素全为0,'',false
	False
	  
	>>> any([]) # 空列表
	False
	 
	>>> any(()) # 空元组
	False

----------
	代码样例：enumerate
	>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
	>>> list(enumerate(seasons))
	[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
	>>> list(enumerate(seasons, start=1))       # 小标从 1 开始
	[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

----------
	代码样例：ord
	>>>ord('a')
	97
	>>> ord('b')
	98
	>>> ord('c')
	99
	

----------
	代码样例：execfile
	>>>execfile('hello.py')


----------
	代码样例：super
	class FooParent(object):
	    def __init__(self):
	        self.parent = 'I\'m the parent.'
	        print ('Parent')
	    
	    def bar(self,message):
	        print ("%s from Parent" % message)
	 
	class FooChild(FooParent):
	    def __init__(self):
	        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
	        super(FooChild,self).__init__()    
	        print ('Child')
	        
	    def bar(self,message):
	        super(FooChild, self).bar(message)
	        print ('Child bar fuction')
	        print (self.parent)
	 
	if __name__ == '__main__':
	    fooChild = FooChild()
	    fooChild.bar('HelloWorld')
	
	Parent
	Child
	HelloWorld from Parent
	Child bar fuction
	I'm the parent.

----------

	iter() 函数用来生成迭代器。

	>>>lst = [1, 2, 3]
	>>> for i in iter(lst):
	...     print(i)
	... 
	1
	2
	3

----------
	样例：property
	class C(object):
	    def __init__(self):
	        self._x = None
	 
	    def getx(self):
	        return self._x
	 
	    def setx(self, value):
	        self._x = value
	 
	    def delx(self):
	        del self._x
	 
	    x = property(getx, setx, delx, "I'm the 'x' property.")

	class Parrot(object):
	    def __init__(self):
	        self._voltage = 100000
	 
	    @property
	    def voltage(self):
	        """Get the current voltage."""
	        return self._voltage

	class C(object):
	    def __init__(self):
	        self._x = None
	 
	    @property
	    def x(self):
	        """I'm the 'x' property."""
	        return self._x
	 
	    @x.setter
	    def x(self, value):
	        self._x = value
	 
	    @x.deleter
	    def x(self):
	        del self._x


----------
	样例：filter
	def is_odd(n):
	    return n % 2 == 1
	 
	newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
	print(newlist)

----------
	样例：eval
	>>>x = 7
	>>> eval( '3 * x' )
	21
	>>> eval('pow(2,2)')
	4
	>>> eval('2 + 2')
	4
	>>> n=81
	>>> eval("n + 4")

----------

	**8.模块（调用各种常见模块）**
	import os,from collections import deque
	
----------

	- collections模块
	- deque 
		-from collections import deque 使用堆栈效率会比较高
	from collections import deque
	# 从尾部进入，从头部弹出，保证长度为5
	dq1 = deque('abcdefg', maxlen=5)
	print(dq1)  # ['c', 'd', 'e', 'f', 'g']
	print(dq1.maxlen)  # 5
	# 从左端入列
	dq1.appendleft('q')
	print(dq1)  # ['q', 'c', 'd', 'e', 'f']
	# 从左端入列
	dq1.extendleft('abc')
	print(dq1)  # ['c', 'b', 'a', 'q', 'c']
	# 从左端出列并且返回
	dq1.popleft()  # c
	print(dq1)  # ['b', 'a', 'q', 'c']
	# 将队头n个元素进行右旋
	dq1.rotate(2)
	print(dq1)  # ['q', 'c', 'b', 'a']

----------

	ChainMap(这是一个为多个映射创建单一视图的类字典类型，也就是说，它同样具有字典类型的方法，它比基础数据结构中的字典的创建和多次更新要快，需要注意的是，增删改的操作都只会针对该对象的第一个字典，其余字典不会发生改变，但是如果是查找，则会在多个字典中查找，直到找到第一个出现的key为止)
	
	import collections
	a = {1: 2, 2: 3}
	b = {1: 3, 3: 4, 4: 5}
	chains = collections.ChainMap(a, b)
	# maps
	# 注意maps是个属性，不是一个方法，其改变
	print(chains.maps)  # [{1: 2, 2: 3}, {1: 3, 3: 4, 4: 5}]
	# get
	assert chains.get(1, -1) == 2

----------
	Counter,这是一个继承dict的子类，专门用来做计数器，dict中的方法这里同样适用
	from collections import Counter
	# init
	# 可迭代
	counter = Counter("accab")  # Counter({'a': 2, 'c': 2, 'b': 1})
	counter2 = Counter([1,2,3,4])  # Counter({1: 1, 2: 1, 3: 1, 4: 1})
	counter5 = Counter([('a',3),('b', 2)])  # Counter({('a', 3): 1, ('b', 2): 1})
	# 字典
	counter3 = Counter({'a': 1, 'b': 2, 'a': 3})  # Counter({'a': 3, 'b': 2})
	counter4 = Counter(a=1, b=2, c=1)  # Counter({'b': 2, 'a': 1, 'c': 1})
	# elements
	# 键值以无序的方式返回，并且只返回值大于等于1的键值对
	elememts = counter.elements()
	print([x for x in elememts])  # ['a', 'a', 'c', 'c', 'b']
	

----------
	OrderedDict,OrderedDict提供了一个有序字典，可以使用在遍历的时候根据相应的顺序进行输出，因为在dict中它的item是以任意顺序进行输出的。注意初始化的时候和在插入的话都根据插入顺序进行排序，而不是根据key进行排序

	from collections import OrderedDict
	items = {'c': 3, 'b': 2, 'a': 1}
	regular_dict = dict(items)
	ordered_dict = OrderedDict(items)
	print(regular_dict)  # {'c': 3, 'b': 2, 'a': 1}
	print(ordered_dict)  # [('c', 3), ('b', 2), ('a', 1)]
	# 按照插入顺序进行排序而不是
	ordered_dict['f'] = 4
	ordered_dict['e'] = 5
	print(ordered_dict)  # [('c', 3), ('b', 2), ('a', 1), ('f', 4), ('e', 5)]
	# 把最近加入的删除
	print(ordered_dict.popitem(last=True))  # ('e', 5)
	# 按照加入的顺序删除
	print(ordered_dict.popitem(last=False))  # ('c', 3)
	print(ordered_dict)  # [('b', 2), ('a', 1), ('f', 4)]
	# 移动到末尾
	ordered_dict.move_to_end('b', last=True)
	print(ordered_dict)  # [('a', 1), ('f', 4), ('b', 2)]

----------
	namedtuple,如果我们想要在tuple中使用名字的参数，而不是位置，namedtuple提供这么一个创建名称tuple的机会。
	from collections import namedtuple
	Point = namedtuple('Point', ['x', 'y'])
	p = Point(10, y=20)
	print(p)  # Point(x=10, y=20)
	print(p.x + p.y)  # 30

----------

- 	datetime 模块
	- 	datetime.date：表示日期的类
	- 	datetime.datetime：表示日期时间的类
	- 	datetime.time：表示时间的类
	- 	datetime.timedelta：表示时间间隔，即两个时间点的间隔
	- 	datetime.tzinfo：时区的相关信息

%y-%m-%d,%y,%b简写月份，%A星期几，%B月份全写

----------
- 	os 模块
	os.environ 一个dictionary 包含环境变量的映射关系   
	os.environ["HOME"] 可以得到环境变量HOME的值     
	os.chdir(dir) 改变当前目录 os.chdir('d:\\outlook')   
	注意windows下用到转义     
	os.getcwd() 得到当前目录     
	os.getegid() 得到有效组id os.getgid() 得到组id     
	os.getuid() 得到用户id os.geteuid() 得到有效用户id     
	os.setegid os.setegid() os.seteuid() os.setuid()     
	os.getgruops() 得到用户组名称列表     
	os.getlogin() 得到用户登录名称     
	os.getenv 得到环境变量     
	os.putenv 设置环境变量     
	os.umask 设置umask     
	os.system(cmd) 利用系统调用，运行cmd命令  
	os.rename(current_file_name, new_file_name) 重命名
	os.remove(file_name) 删除文件
	os.mkdir("newdir")创建目录
	os.chdir("newdir") 改变目录
	os.rmdir('dirname') 删除目录
	
----------

- 	unittest 模块
	import unittest
	执行测试的类
	class WidgetTestCase(unittest.TestCase):
	    def test_A(self):
	        self.widget = Widget()
	    def test_B(self):
	        self.widget.dispose()
	        self.widget = None

----------

- 	logging 模块
	- 	
	import logging
	import sys
	 
	获取logger实例，如果参数为空则返回root logger
	logger = logging.getLogger("AppName")
	 
	指定logger输出格式
	formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
	 
	文件日志
	file_handler = logging.FileHandler("test.log")
	file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
	 
	控制台日志
	console_handler = logging.StreamHandler(sys.stdout)
	console_handler.formatter = formatter  # 也可以直接给formatter赋值
	 
	为logger添加的日志处理器
	logger.addHandler(file_handler)
	logger.addHandler(console_handler)
	 
	指定日志的最低输出级别，默认为WARN级别
	logger.setLevel(logging.INFO)
	 
	输出不同级别的log
	logger.debug('this is debug info')
	logger.info('this is information')
	logger.warn('this is warning message')
	logger.error('this is error message')
	logger.fatal('this is fatal message, it is same as logger.critical')
	logger.critical('this is critical message')
	 
	移除一些日志处理器
	logger.removeHandler(file_handler)

----------

	# 格式化输出
	 
	service_name = "Booking"
	logger.error('%s service is down!' % service_name)  # 使用python自带的字符串格式化，不推荐
	logger.error('%s service is down!', service_name)  # 使用logger的格式化，推荐
	logger.error('%s service is %s!', service_name, 'down')  # 多参数格式化
	logger.error('{} service is {}'.format(service_name, 'down')) # 使用format函数，推荐


----------
	
	记录异常信息
	try:
	    1 / 0
	except:
	    # 等同于error级别，但是会额外记录当前抛出的异常堆栈信息
	    logger.exception('this is an exception message')
 
----------
- 	file i/o 模块
	print,input，format
	
	代码样例：
	with open('路径+文件名'，'r/r+/w/w+/a/a+') as f:
		f.read(),f.write(),f.readline(),f.readlines()

----------
	文件光标定位：
	# 打开一个文件
	fo = open("foo.txt", "r+")
	str = fo.read(10)
	print "读取的字符串是 : ", str
	 
	# 查找当前位置
	position = fo.tell()
	print "当前文件位置 : ", position
	 
	# 把指针再次重新定位到文件开头
	position = fo.seek(0, 0)
	str = fo.read(10)
	print "重新读取字符串 : ", str
	# 关闭打开的文件
	fo.close()

----------

	知识点1：r只读，r+读写，不创建
	w新建只写，w+新建读写，二者都会将文件内容清零
	r+：可读可写，若文件不存在，报错；w+: 可读可写，若文件不存在，创建
	r+与a+区别：一个读写，还有一个追加，说明r+进行了覆盖写

----------
- 	数据压缩 zlib(zlib.compress(),zlib.decompress())，互联网(urlib.request)，性能度量（from timeit import Timer）

	知识点1：name属性，说明： 每个模块都有一个name属性，当其值是'main'时，表明该模块自身在运行，否则是被引入
	if __name__ == __main__:
		执行语句
	
	知识点2：内置的函数 dir() 可以找到模块内定义的所有名称

	知识点3：reload() 函数，当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。

	知识点4：函数locals()，globals()；如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。

	知识点5：简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。__int__.py用于标识当前文件夹是一个包
	
----------

	**9.面向对象**
	
	class 类名（继承A,继承B）：
	class 类名：
	init() 的特殊方法,__init__:

----------

	样例：
	class Employee:
	   '所有员工的基类'
	   empCount = 0
	 
	   def __init__(self, name, salary):
	      self.name = name
	      self.salary = salary
	      Employee.empCount += 1
	   
	   def displayCount(self):
	     print "Total Employee %d" % Employee.empCount
	 
	   def displayEmployee(self):
	      print "Name : ", self.name,  ", Salary: ", self.salary
 
	"创建 Employee 类的第一个对象"
	emp1 = Employee("Zara", 2000)
	"创建 Employee 类的第二个对象"
	emp2 = Employee("Manni", 5000)
	emp1.displayEmployee()
	emp2.displayEmployee()
	print "Total Employee %d" % Employee.empCount

----------

	hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
	getattr(emp1, 'age')    # 返回 'age' 属性的值
	setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
	delattr(emp1, 'age')    # 删除属性 'age'

----------

	Python内置类属性
	__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
	__doc__ :类的文档字符串
	__name__: 类名
	__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
	__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）

----------

	python对象销毁(垃圾回收)

	析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行
	class Point:
	   def __init__( self, x=0, y=0):
	      self.x = x
	      self.y = y
	   def __del__(self):
	      class_name = self.__class__.__name__
	      print class_name, "销毁"
	 
	pt1 = Point()
	pt2 = pt1
	pt3 = pt1
	print id(pt1), id(pt2), id(pt3) # 打印对象的id
	del pt1
	del pt2
	del pt3

----------
	类的继承

	class Parent:        # 定义父类
	   parentAttr = 100
	   def __init__(self):
	      print "调用父类构造函数"
	 
	   def parentMethod(self):
	      print '调用父类方法'
	 
	   def setAttr(self, attr):
	      Parent.parentAttr = attr
	 
	   def getAttr(self):
	      print "父类属性 :", Parent.parentAttr
	 
	class Child(Parent): # 定义子类
	   def __init__(self):
	      print "调用子类构造方法"
	 
	   def childMethod(self):
	      print '调用子类方法'
	 
	c = Child()          # 实例化子类
	c.childMethod()      # 调用子类的方法
	c.parentMethod()     # 调用父类方法
	c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
	c.getAttr()          # 再次调用父类的方法 - 获取属性值

	调用子类构造方法
	调用子类方法
	调用父类方法
	父类属性 : 200

----------
	方法重写
	class Parent:        # 定义父类
	   def myMethod(self):
	      print '调用父类方法'
	 
	class Child(Parent): # 定义子类
	   def myMethod(self):
	      print '调用子类方法'
	 
	c = Child()          # 子类实例
	c.myMethod()         # 子类调用重写方法
	
	
	调用子类方法

----------
	类的属性，私有还是公有
	class JustCounter:
	    __secretCount = 0  # 私有变量
	    publicCount = 0    # 公开变量
	 
	    def count(self):
	        self.__secretCount += 1
	        self.publicCount += 1
	        print self.__secretCount
	 
	counter = JustCounter()
	counter.count()
	counter.count()
	print counter.publicCount
	print counter.__secretCount  # 报错，实例不能访问私有变量

----------
	运算符重载
	class Vector:
	   def __init__(self, a, b):
	      self.a = a
	      self.b = b
	 
	   def __str__(self):
	      return 'Vector (%d, %d)' % (self.a, self.b)
	   
	   def __add__(self,other):
	      return Vector(self.a + other.a, self.b + other.b)
	 
	v1 = Vector(2,10)
	v2 = Vector(5,-2)
	print v1 + v2

----------
	知识点1：__init__,__new__,__del__,单例设计，__cal__,__len__,__str__,__repr__,__bool__,__format__,__dict__,__name__,__doc__,__get__,__set__,__delete__,@property.setter,@property.deleter,__getattr__,__setattr__,__delattr__,__add__,__dir__,__sub__,__mul__,__truediv__,__gt__,__lt__,__ge__,__eq__,装饰器,

----------

	**10.正则表达式**

----------

	re.match函数
	re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
	import re
	print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
	print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配
	(0, 3)
	None

----------

	import re
	 
	line = "Cats are smarter than dogs"
	 
	matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
	 
	if matchObj:
	   print "matchObj.group() : ", matchObj.group()
	   print "matchObj.group(1) : ", matchObj.group(1)
	   print "matchObj.group(2) : ", matchObj.group(2)
	else:
	   print "No match!!"
	matchObj.group() :  Cats are smarter than dogs
	matchObj.group(1) :  Cats
	matchObj.group(2) :  smarter

----------

	re.search 扫描整个字符串并返回第一个成功的匹配。
	import re
	print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
	print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配
	(0, 3)
	(11, 14)


----------
	
	import re
	 
	line = "Cats are smarter than dogs";
	 
	searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
	 
	if searchObj:
	   print "searchObj.group() : ", searchObj.group()
	   print "searchObj.group(1) : ", searchObj.group(1)
	   print "searchObj.group(2) : ", searchObj.group(2)
	else:
	   print "Nothing found!!"
	
	searchObj.group() :  Cats are smarter than dogs
	searchObj.group(1) :  Cats
	searchObj.group(2) :  smarter

----------

	import re
	 
	phone = "2004-959-559 # 这是一个国外电话号码"
	 
	# 删除字符串中的 Python注释 
	num = re.sub(r'#.*$', "", phone)
	print "电话号码是: ", num
	 
	# 删除非数字(-)的字符串 
	num = re.sub(r'\D', "", phone)
	print "电话号码是 : ", num

	电话号码是:  2004-959-559 
	电话号码是 :  2004959559

----------

	import re
	 
	# 将匹配的数字乘于 2
	def double(matched):
	    value = int(matched.group('value'))
	    return str(value * 2)
	 
	s = 'A23G4HFD567'
	print(re.sub('(?P<value>\d+)', double, s))
	
	A46G8HFD1134


----------
	>>>import re
	>>> pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
	>>> m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
	>>> print m
	None
	>>> m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
	>>> print m
	None
	>>> m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
	>>> print m                                         # 返回一个 Match 对象
	<_sre.SRE_Match object at 0x10a42aac0>
	>>> m.group(0)   # 可省略 0
	'12'
	>>> m.start(0)   # 可省略 0
	3
	>>> m.end(0)     # 可省略 0
	5
	>>> m.span(0)    # 可省略 0
	(3, 5)

----------
	>>>import re
	>>> pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
	>>> m = pattern.match('Hello World Wide Web')
	>>> print m                               # 匹配成功，返回一个 Match 对象
	<_sre.SRE_Match object at 0x10bea83e8>
	>>> m.group(0)                            # 返回匹配成功的整个子串
	'Hello World'
	>>> m.span(0)                             # 返回匹配成功的整个子串的索引
	(0, 11)
	>>> m.group(1)                            # 返回第一个分组匹配成功的子串
	'Hello'
	>>> m.span(1)                             # 返回第一个分组匹配成功的子串的索引
	(0, 5)
	>>> m.group(2)                            # 返回第二个分组匹配成功的子串
	'World'
	>>> m.span(2)                             # 返回第二个分组匹配成功的子串
	(6, 11)
	>>> m.groups()                            # 等价于 (m.group(1), m.group(2), ...)
	('Hello', 'World')
	>>> m.group(3)                            # 不存在第三个分组
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	IndexError: no such group

----------
	re.I 忽略大小写
	re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
	re.M 多行模式
	re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
	re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
	re.X 为了增加可读性，忽略空格和 # 后面的注释

----------

	import re
	 
	pattern = re.compile(r'\d+')   # 查找数字
	result1 = pattern.findall('runoob 123 google 456')
	result2 = pattern.findall('run88oob123google456', 0, 10)
	 
	print(result1)
	print(result2)
	
	['123', '456']
	['88', '12']

----------

	import re
	 
	it = re.finditer(r"\d+","12a32bc43jf3") 
	for match in it: 
	    print (match.group() )
	12 
	32 
	43 
	3

----------
	>>>import re
	>>> re.split('\W+', 'runoob, runoob, runoob.')
	['runoob', 'runoob', 'runoob', '']
	>>> re.split('(\W+)', ' runoob, runoob, runoob.') 
	['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']
	>>> re.split('\W+', ' runoob, runoob, runoob.', 1) 
	['', 'runoob, runoob, runoob.']
	 
	>>> re.split('a*', 'hello world')   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
	['hello world']

----------
	^,$,\w\s\d\b\z\W\S\D\B\Z\A,(),*,+,.,?,{n,m},[],[^][0-9a-zA-Z]


----------
	**11.CUI编程(TKinter)**
	import Tkinter
	top = Tkinter.Tk()
	# 进入消息循环
	top.mainloop()

----------
	from Tkinter import *           # 导入 Tkinter 库
	root = Tk()                     # 创建窗口对象的背景色
	                                # 创建两个列表
	li     = ['C','python','php','html','SQL','java']
	movie  = ['CSS','jQuery','Bootstrap']
	listb  = Listbox(root)          #  创建两个列表组件
	listb2 = Listbox(root)
	for item in li:                 # 第一个小部件插入数据
	    listb.insert(0,item)
	
	for item in movie:              # 第二个小部件插入数据
	    listb2.insert(0,item)
	
	listb.pack()                    # 将小部件放置到主窗口中
	listb2.pack()
	root.mainloop()                 # 进入消息循环


----------
	具体参照手册，组件，属性，几何

----------

	**12.网络编程**

----------

	-服务器端

	import socket               # 导入 socket 模块
	
	s = socket.socket()         # 创建 socket 对象
	host = socket.gethostname() # 获取本地主机名
	port = 12345                # 设置端口
	s.bind((host, port))        # 绑定端口
	
	s.listen(5)                 # 等待客户端连接
	while True:
	    c, addr = s.accept()     # 建立客户端连接。
	    print '连接地址：', addr
	    c.send('欢迎访问菜鸟教程！')
	    c.close()                # 关闭连接

----------

	-客户端
	import socket               # 导入 socket 模块
	
	s = socket.socket()         # 创建 socket 对象
	host = socket.gethostname() # 获取本地主机名
	port = 12345                # 设置端口好
	
	s.connect((host, port))
	print s.recv(1024)
	s.close()  


----------

	**13.线程管理**
	
	import thread
	import time
	 
	# 为线程定义一个函数
	def print_time( threadName, delay):
	   count = 0
	   while count < 5:
	      time.sleep(delay)
	      count += 1
	      print "%s: %s" % ( threadName, time.ctime(time.time()) )
	 
	# 创建两个线程
	try:
	   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
	   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
	except:
	   print "Error: unable to start thread"
	 
	while 1:
	   pass

----------
	使用Threading模块创建线程

	import threading
	import time
	 
	exitFlag = 0
	 
	class myThread (threading.Thread):   #继承父类threading.Thread
	    def __init__(self, threadID, name, counter):
	        threading.Thread.__init__(self)
	        self.threadID = threadID
	        self.name = name
	        self.counter = counter
	    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
	        print "Starting " + self.name
	        print_time(self.name, self.counter, 5)
	        print "Exiting " + self.name
	 
	def print_time(threadName, delay, counter):
	    while counter:
	        if exitFlag:
	            (threading.Thread).exit()
	        time.sleep(delay)
	        print "%s: %s" % (threadName, time.ctime(time.time()))
	        counter -= 1
	 
	# 创建新线程
	thread1 = myThread(1, "Thread-1", 1)
	thread2 = myThread(2, "Thread-2", 2)
	 
	# 开启线程
	thread1.start()
	thread2.start()
	 
	print "Exiting Main Thread"


----------
	线程同步
	import threading
	import time
	 
	class myThread (threading.Thread):
	    def __init__(self, threadID, name, counter):
	        threading.Thread.__init__(self)
	        self.threadID = threadID
	        self.name = name
	        self.counter = counter
	    def run(self):
	        print "Starting " + self.name
	       # 获得锁，成功获得锁定后返回True
	       # 可选的timeout参数不填时将一直阻塞直到获得锁定
	       # 否则超时后将返回False
	        threadLock.acquire()
	        print_time(self.name, self.counter, 3)
	        # 释放锁
	        threadLock.release()
	 
	def print_time(threadName, delay, counter):
	    while counter:
	        time.sleep(delay)
	        print "%s: %s" % (threadName, time.ctime(time.time()))
	        counter -= 1
	 
	threadLock = threading.Lock()
	threads = []
	 
	# 创建新线程
	thread1 = myThread(1, "Thread-1", 1)
	thread2 = myThread(2, "Thread-2", 2)
	 
	# 开启新线程
	thread1.start()
	thread2.start()
	 
	# 添加线程到线程列表
	threads.append(thread1)
	threads.append(thread2)
	 
	# 等待所有线程完成
	for t in threads:
	    t.join()
	print "Exiting Main Thread"


----------
	线程优先级队列（ Queue）
	import Queue
	import threading
	import time
	 
	exitFlag = 0
	 
	class myThread (threading.Thread):
	    def __init__(self, threadID, name, q):
	        threading.Thread.__init__(self)
	        self.threadID = threadID
	        self.name = name
	        self.q = q
	    def run(self):
	        print "Starting " + self.name
	        process_data(self.name, self.q)
	        print "Exiting " + self.name
	 
	def process_data(threadName, q):
	    while not exitFlag:
	        queueLock.acquire()
	        if not workQueue.empty():
	            data = q.get()
	            queueLock.release()
	            print "%s processing %s" % (threadName, data)
	        else:
	            queueLock.release()
	        time.sleep(1)
	 
	threadList = ["Thread-1", "Thread-2", "Thread-3"]
	nameList = ["One", "Two", "Three", "Four", "Five"]
	queueLock = threading.Lock()
	workQueue = Queue.Queue(10)
	threads = []
	threadID = 1
	 
	# 创建新线程
	for tName in threadList:
	    thread = myThread(threadID, tName, workQueue)
	    thread.start()
	    threads.append(thread)
	    threadID += 1
	 
	# 填充队列
	queueLock.acquire()
	for word in nameList:
	    workQueue.put(word)
	queueLock.release()
	 
	# 等待队列清空
	while not workQueue.empty():
	    pass
	 
	# 通知线程是时候退出
	exitFlag = 1
	 
	# 等待所有线程完成
	for t in threads:
	    t.join()
	print "Exiting Main Thread"

----------

	**14.数据库的链接**
	数据库链接
	import MySQLdb
	
	# 打开数据库连接
	db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
	
	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()
	
	# 使用execute方法执行SQL语句
	cursor.execute("SELECT VERSION()")
	
	# 使用 fetchone() 方法获取一条数据
	data = cursor.fetchone()
	
	print "Database version : %s " % data
	
	# 关闭数据库连接
	db.close()

----------

	创建数据库表
	
	import MySQLdb
	
	# 打开数据库连接
	db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
	
	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()
	
	# 如果数据表已经存在使用 execute() 方法删除表。
	cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
	
	# 创建数据表SQL语句
	sql = """CREATE TABLE EMPLOYEE (
	         FIRST_NAME  CHAR(20) NOT NULL,
	         LAST_NAME  CHAR(20),
	         AGE INT,  
	         SEX CHAR(1),
	         INCOME FLOAT )"""
	
	cursor.execute(sql)
	
	# 关闭数据库连接
	db.close()

----------
	数据库插入操作
	import MySQLdb
	
	# 打开数据库连接
	db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
	
	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()
	
	# SQL 插入语句
	sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
	         LAST_NAME, AGE, SEX, INCOME)
	         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
	try:
	   # 执行sql语句
	   cursor.execute(sql)
	   # 提交到数据库执行
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()
	
	# 关闭数据库连接
	db.close()

----------

	数据库的查询操作
	import MySQLdb
	
	# 打开数据库连接
	db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
	
	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()
	
	# SQL 查询语句
	sql = "SELECT * FROM EMPLOYEE \
	       WHERE INCOME > '%d'" % (1000)
	try:
	   # 执行SQL语句
	   cursor.execute(sql)
	   # 获取所有记录列表
	   results = cursor.fetchall()
	   for row in results:
	      fname = row[0]
	      lname = row[1]
	      age = row[2]
	      sex = row[3]
	      income = row[4]
	      # 打印结果
	      print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
	             (fname, lname, age, sex, income )
	except:
	   print "Error: unable to fecth data"
	
	# 关闭数据库连接
	db.close()

----------

	数据库的更新操作
	import MySQLdb
	
	# 打开数据库连接
	db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
	
	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()
	
	# SQL 更新语句
	sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
	try:
	   # 执行SQL语句
	   cursor.execute(sql)
	   # 提交到数据库执行
	   db.commit()
	except:
	   # 发生错误时回滚
	   db.rollback()
	
	# 关闭数据库连接
	db.close()


----------
	数据库的删除操作
	import MySQLdb
	
	# 打开数据库连接
	db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
	
	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()
	
	# SQL 删除语句
	sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
	try:
	   # 执行SQL语句
	   cursor.execute(sql)
	   # 提交修改
	   db.commit()
	except:
	   # 发生错误时回滚
	   db.rollback()
	
	# 关闭连接
	db.close()


----------
	执行事务操作
	# SQL删除记录语句
	sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
	try:
	   # 执行SQL语句
	   cursor.execute(sql)
	   # 向数据库提交
	   db.commit()
	except:
	   # 发生错误时回滚
	   db.rollback()

----------

	**15.异常处理**

	import ipdb,ipdb.set_trace()
	n,s,j,restart,q
	
	
	代码样例
	try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
	except IOError:
	    print "Error: 没有找到文件或读取文件失败"
	else:
	    print "内容写入文件成功"
	    fh.close()

----------

	try:
	    正常的操作
	   ......................
	except(Exception1[, Exception2[,...ExceptionN]]]):
	   发生以上多个异常中的一个，执行这块代码
	   ......................
	else:
	    如果没有异常执行这块代码

----------

	try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
	finally:
	    print "Error: 没有找到文件或读取文件失败"

----------

	try:
    fh = open("testfile", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print "关闭文件"
        fh.close()
	except IOError:
	    print "Error: 没有找到文件或读取文件失败"

----------

	# 定义函数
	def temp_convert(var):
	    try:
	        return int(var)
	    except ValueError, Argument:
	        print "参数没有包含数字\n", Argument
	
	# 调用函数
	temp_convert("xyz");

----------
	def functionName( level ):
	    if level < 1:
	        raise Exception("Invalid level!", level)
	        # 触发异常后，后面的代码就不会再执行

----------

	# 定义函数
	def mye( level ):
	    if level < 1:
	        raise Exception,"Invalid level!"
	        # 触发异常后，后面的代码就不会再执行
	try:
	    mye(0)            # 触发异常
	except Exception,err:
	    print 1,err
	else:
	    print 2

----------
	class Networkerror(RuntimeError):
	    def __init__(self, arg):
	        self.args = arg
	try:
    raise Networkerror("Bad hostname")
	except Networkerror,e:
    print e.args


# 3. 累积问题及解决 #

	问题1：长整型也可以使用小写"L"，但是还是建议使用大写"L"，避免与数字"1"混淆
	

----------
	问题2：Isdigit,isdecimal,isnumeric区别（整数、小数判断）
	[https://stackoverflow.com/questions/22789392/str-isdecimal-and-str-isdigit-difference-example](https://stackoverflow.com/questions/22789392/str-isdecimal-and-str-isdigit-difference-example)

----------

	问题3：6 demos of Python split string (split, rsplit and splitlines)
	[https://www.jquery-az.com/python-split-string-methods-split-rsplit-and-splitlines-6-examples/](https://www.jquery-az.com/python-split-string-methods-split-rsplit-and-splitlines-6-examples/)


----------
	问题4：The different about pop\ remove \del\
	总结一句话：pop返回值，pop\del 是索引，remove 是值，error mode 也不同
	[https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists](https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists)

----------

	问题5：从99乘法表看for
	9*9乘法表看编写代码的思维方式
	# 错误1，用列的方式来思考是错误的
	# for j in range(1,10):
	#     for i in range(1,10):
	#         if (i >= j):
	#             print(i,"*",j,"=",i*j)
	# 1. 横向看计算机的输出方式；2.如何打印出2*1,2*2的方式 表达；3.i的值决定了j的循环方式；4.i打印完就会换行；5.同时解决print 换行问题
	for i in range(1,10):
	    for j in range(1,i+1):
	        print(i,"*",j,"=",i*j,end='\t')
	    print('\r')
	# 解决取消print 回车问题
	# for i in range(1,5):
	#     print(i,end=' ')

----------

	问题6：parchar调试程序的方法
	[http://blog.csdn.net/u013088062/article/details/50130991](http://blog.csdn.net/u013088062/article/details/50130991)
	
	
----------



	
	