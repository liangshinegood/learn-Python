# 思路：首先知道角ABC = 90，AB,BC
# m 是ac中重点
# 通过ab,bc 求ac ,然后求am
# amb = 90 所以求mbc度数用三角函数即可

import math
ab = int(input())
bc = int(input())

print(str(int(round(math.degrees(math.atan2(ab,bc)))))+'°')


