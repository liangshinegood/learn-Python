# /* tdd 思想，先想测试，再写代码，再优化代码 */
from itertools import permutations
s = [i for i in input("请输入一个值：").split()]
listS = list(permutations(s[0],int(s[1])))
string = ''
listB=[]
for item in listS:
    for i in item:
        string += i
        if(len(string)==int(s[1])):
            listB.append(string)
            string=''
            break

print(listB)
listB.sort()
for item in listB:
    print(item)
