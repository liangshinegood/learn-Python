# 从题意来看没太明白
# 从答案来看，需要先大后小
for t in range(int(input())):
    input()
    lst = [int(i) for i in input().split()]
    l = len(lst)
    i = 0
    while i < l-1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l-1 and lst[i] <= lst[i+1]:
        i += 1
    print("Yes" if i== l-1 else "No")



