# 取函数pow(),并取mod
# 通过sep方法将pow(a,b),pow(a,b,m)隔开，是不错的思路，并且减少了代码生成
a,b,m = [int(input()) for _ in range(3)]
print(pow(a,b),pow(a,b,m),sep='\n')






