result=[]
for _ in range(int(input())):
    na = int(input())
    A = set(input().split())
    nb = int(input())
    B = set(input().split())
    if len(A.difference(B)) == 0:
        result.append('True')
    else:
        result.append('False')
for i in result:
    print(i)



