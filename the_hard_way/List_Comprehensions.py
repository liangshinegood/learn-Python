X = int(input("请输入一个X的值："))
Y = int(input("请输入一个Y的值："))
Z = int(input("请输入一个Z的值："))
N = int(input("请输入一个N的值："))
listA = [[i,j,k] for i in range(X+1) for j in range(Y+1) for k in range(Z+1) if i+j+k != N]
print(listA)