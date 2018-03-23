# 思路：使用则正判断


import email.utils,re
for _ in range(int(input())):
    t = email.utils.parseaddr(input())
    if bool(re.match(r'[a-zA-Z](\w|-|\.)*@[a-zA-Z]*\.[a-zA-Z]{0,3}$',t[1])):
        print(email.utils.formataddr(t))




