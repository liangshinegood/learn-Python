# 思路：k,len(input())-1 再除以k
# 然后统计数字出现的次数
# 最后找到 k != num次数的 数字


k,arr = int(input()),list(map(int,input().split()))
myset = set(arr)
print(((sum(myset)*k)-(sum(arr)))//(k-1))
