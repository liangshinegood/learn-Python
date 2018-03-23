# 思想：根据规则写逻辑判断
# 规则的方式用正则去判断

import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}',u)#至少两个大写字母
        assert re.search(r'\d\d\d',u)#至少三个数字
        assert not re.search(r'[^a-zA-Z0-9]',u)#只包含小写、大写、数字
        assert not re.search(r'(.)\1',u)#不可以重复
        assert len(u)==10 #字符长度为10
    except:
        print('Invalid')
    else:
        print('Valid')




