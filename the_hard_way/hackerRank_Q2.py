num = int(input("请输入一个正整数:"))
num1 = num%2
if num < 1 or num > 100:
    print("你输入的数字有问题")
else:
    if num1 != 0:
        print("Weird")
    else:
        if num >= 2 and num <=5:
            print("Not Weird")
        elif num >=6 and num <=20:
            print("Weird")
        else:
            print("Not Weird")
