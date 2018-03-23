# 思路：
# 首先要知道元音、辅音的字母区别
# 然后再看有多少种不同的组合
s = input()
vowels = 'AEIOU'
kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)#???
    else:
        stusc += (len(s)-i)
if kevsc > stusc:
    print("Kevin",kevsc)
elif kevsc < stusc:
    print("Stuart",stusc)
else:
    print("Draw")
