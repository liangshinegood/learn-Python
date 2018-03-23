# 思路：一般这种情况用正则

def fun(s):
    a = re.match(r'[a-zA-Z0-9_-]+@[A-Za-z0-9]+\.[a-zA-Z]{1,3}$',s)
    return(a)




