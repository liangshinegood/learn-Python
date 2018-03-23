# 思路：总体来说还是比较简单

a = set(input().split())
print(all(a > set(input().split())for _ in range(int(input()))))




