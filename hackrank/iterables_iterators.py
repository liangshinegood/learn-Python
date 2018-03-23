# 思路：判断有多少种组合的可能，然后找出有a的组合的个数

from itertools import combinations

_,s,n = input(),input().split(),int(input())

t = list(combinations(s,n))
f = [i for i in t if 'a' in i]
print(len(f)/len(t))




