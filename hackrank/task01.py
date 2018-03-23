


from collections import Counter
X = input("请输入鞋子的数量：")
myList = [ int(i) for i in input("输入鞋子的尺寸：").split()]
N = input("客户的数量：")
custom = []
for i in range(int(N)):
    custom.extend([int(i) for i in input("客户想要的尺寸及价格：").split() ])
arr = Counter(myList)
num = 0
sumA = 0
for i in range(0,len(custom),2):
    for keys,values in arr.items():
        if(custom[i] == keys):
            num = values
            if(num != 0):
                sumA = sumA + custom[i+1]
                arr[keys] = num-1
                break
            else:
                break
print(sumA)




