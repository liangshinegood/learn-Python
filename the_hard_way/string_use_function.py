number = "-290"
number1 = "  abc   aefg"
number2 = 'abc'
number3 = '123'
print('zfill的使用：',number.zfill(8))
print('index方法的使用：',number.index('2'))
print('find方法使用：',number.find('9'))
print('find方法使用：',number.find('+'))
print('rfind方法使用：',number.rfind('9'))
print('rindex方法使用：',number.rindex('9'))
print('rsplit方法使用：',number.rsplit('9'))
print('正常情况下的：',number1)
print('strip方法使用：',number1.strip())


print('isdecimal方法使用：',number.isdecimal())
print(number3.isdecimal())
print('isdigit方法使用：',number.isdigit())
print(number3.isdigit())
print('count 方法使用：',number1.count('a'))
print('split 方法使用：',number1.split('a'))
print('endswith 方法使用：',number1.endswith('a'))
print('lstrip 方法使用：',number1.lstrip())
print('capitalize 方法使用：',number2.capitalize())


print('center方法的使用：',number3.center(20,'*'))
string = 'Python*Ψ'
print('正常字符为：',string)
print('encode方法的使用1：',string.encode('ascii','ignore'))
print('encode方法的使用2：',string.encode('ascii','replace'))
print('encode方法的使用2：',string.encode('gbk','replace'))
stringExpand = 'abc\t780'
print('expandtabs方法的使用：',stringExpand.expandtabs())
print('expandtabs方法的使用：',stringExpand.expandtabs(2))
print('expandtabs方法的使用：',stringExpand.expandtabs(20))


print('format方法使用1：',format(123,'d'))
print('format方法使用2：',format(123,'f'))
print('format方法使用3：',format(8,'b'))
print('format方法使用4：',format(1234,'*>+7,d'))
print('format方法使用5：',format(123.4,'^-09.3f'))
point = {'x':4,'y':-5,'z':0}
print('format_map方法1：{y} {x}'.format_map(point))
print('format_map方法2：{x} {y}'.format_map(point))
class coordinate(dict):
    def __missing__(self,key):  # 注意这个地方是两个下划线，要不然不反应
        return key
print('format_map方法3：{x},{y}'.format_map(coordinate(x='6')))
print('format_map方法4：{x},{y}'.format_map(coordinate(y='6')))
print('format_map方法5：{x},{y}'.format_map(coordinate(x='5',y='6')))



stringIs = 'Dabc123'
stringIs1 = '123'
stringIs2 = 'abc'
print('isalnum 方法是1：',stringIs.isalnum())
print('isalnum 方法是2：',stringIs1.isalnum())
print('isalpha 方法是1：',stringIs.isalpha())
print('isalpha 方法是2：',stringIs.isalpha())
print('isalpha 方法是3：',stringIs2.isalpha())
print('isidentifier 方法是：',stringIs.isidentifier())
print('islower 方法是1：',stringIs.islower())
print('islower 方法是2：',stringIs2.islower())
print('isnumeric 方法是1：',stringIs.isnumeric())
print('isnumeric 方法是2：',stringIs1.isnumeric())
print('isprintable 方法是1：',stringIs.isprintable())
stringIs3 = '\nferere'
print('isprintable 方法2：',stringIs3.isprintable())
stringIs4 = ' abc '
stringIs5='abc'
stringIs6 = '   \t\n'
print('isspace 方法1：',stringIs4.isspace())
print('isspace 方法2：',stringIs5.isspace())
print('isspace 方法3：',stringIs6.isspace())
stringIs7 = 'Is Title'
stringIs8 = 'is title'
print('istitle 方法1：',stringIs7.istitle())
print('istitle 方法2：',stringIs8.istitle())
stringIs9 = 'ABCDEFG'
stringIs10 = 'abcdefg'
stringIs11 = 'ABCdefg'
print('isupper 方法1：',stringIs9.isupper())
print('isupper 方法2：',stringIs10.isupper())
print('isupper 方法3：',stringIs11.isupper())




strFunc01 = 'data'
strFunc02 = 'Science'
print('join()方法is：',strFunc01.join(strFunc02))
print('ljust 方法is:',strFunc01.ljust(8,'*'))
print('rjust 方法is:',strFunc01.rjust(8,'*'))
print('lower 方法is:',strFunc02.lower())
print('partition 方法is:',strFunc01.partition('a'))
print('rpartition 方法is:',strFunc01.rpartition('a'))
print('title method is ',strFunc01.title())
print('startswith method is 1',strFunc01.startswith('d'))
print('startswith method is 2',strFunc01.startswith('d',2,5))
print('startswith method is 3',strFunc01.startswith('z'))
print('swapcase method is',strFunc01.swapcase())
print('replace method is 1',strFunc01.replace('a','e',1))
print('replace method is 2',strFunc01.replace('a','e',3))

dictA = {'a':'123','b':'456','c':'789'}
string = 'abc'
print('learn makestrans method is 1:',string.maketrans(dictA))
dictB = {97:'123',98:'456',99:'789'}
string = 'abc'
print('learn makestrans method is 2:',string.maketrans(dictB))
firstString = 'abc'
secondString = 'def'
string = 'www'
print('learn makestran method is 3:',string.maketrans(firstString,secondString)) # 似乎跟string之间的对应关系已经取消
''''# it wrong 
firstString = 'abc'
secondString = 'defg' #个数必须要对应
string = 'abc'
print('learn makestran method is 3:',string.maketrans(firstString,secondString)) '''
firstString = 'abc'
secondString = 'def'
thirdString = 'zzz'
string = 'www'
# thirdString resets the mapping to none and add the new z to it
print('learn makestrans method is 4:',string.maketrans(firstString,secondString,thirdString))

grocery = 'milk\nchicken\r\nbread\tButter'
print('the splitline method is 1:',grocery.splitlines())
print('the splitlines method is 2:',grocery.splitlines(True))
grocery1 = 'milk chicken bread Butter'
print('the splitlines method is 3:',grocery1.splitlines())


strBB = 'abc'
print('the method upper is :',strBB.upper())
print('the method zfill is :',strBB.zfill(8))

firstString = 'abc'
secondString = 'ghi'
thirdString ='ab'
string = 'abcdef'
print('the original string is:',string)

translation = string.maketrans(firstString,secondString,thirdString)
print('the translation value is :',translation)
#translate 是将maketrans的值再翻译回来
print('translated string is :',string.translate(translation))# a为none,b为none,c为i 剩下的def




