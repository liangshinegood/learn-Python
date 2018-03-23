from collections import deque
# 列出所有deque可能的操作 pop append appendleft appendright clear
# extend extendleft count popleft remove reverse rotate maxlen

# listA = [input("输入操作信息").split() for _ in range(int(input("循环次数：")))]
tupleA = (input("输入操作信息").split() for _ in range(int(input("循环次数："))))
# print(listA)
print(tupleA)