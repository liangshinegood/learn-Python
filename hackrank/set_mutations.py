# ���ж��в�����˼·��ʿ���ʹ��eval���
# ����getattr(L,command) �൱�� L.command

input()
L = set(input().split())

for _ in range(int(input())):
    command,*args = input().split()
    getattr(L,command)(set(input().split()))

print(sum(map(int,L)))


