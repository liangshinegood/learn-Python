# 将矩阵按列的方式读取，如果遇到两个特殊字符用空格隔开
# 正则表达式
# 将输入的值存入列表，通过列表转变为字符串，然后用正则判断和替换
import re 

n,m = map(int,input().split())
a,b = [],""
for _ in range(n):
    a.append(input())

for z in zip(*a):
    b += "".join(z)

print(re.sub(r'(?<=\w)([^\w]+)(?=\w)'," ",b))




