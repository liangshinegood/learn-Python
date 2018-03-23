# 进行多行操作的思路，士梢允褂胑val语句
# 或者getattr(L,command) 相当于 L.command

input()
L = set(input().split())

for _ in range(int(input())):
    command,*args = input().split()
    getattr(L,command)(set(input().split()))

print(sum(map(int,L)))


