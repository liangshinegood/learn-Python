#思路：核心是当它进行10次操作时，就要进行10次操作
#输入完数据后，进行输入操作时，将输入的操作做对应＃ǎ所谓对应就是之前的思路已经OK了
#s.{0}({1}) 通过格式化的方式进行表达式而已，如s.remove(9)
#*input().split 是取到输入元素的值

n = int(input())
s = set(map(int,input().split()))
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))



