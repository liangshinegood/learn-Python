# 思路：统计字符连续出现的次数

from itertools import groupby
for k,g in groupby(input()):
    print("({},{})".format(len(list(g)),k),end=" ")


