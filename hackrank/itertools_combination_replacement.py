# 思路：combinations_with_replacement应用

from itertools import combinations_with_replacement,combinations

word,k = input().split()
k = int(k)

for segment in combinations_with_replacement(sorted(word),k):
    print(''.join(segment))




