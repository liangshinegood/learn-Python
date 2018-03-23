
# 从对方提供的，group,groups,groupdic考虑

# 导入正则模块，用正则判断

import re
#m = re.search(r'(a-zA-Z0-9)\1+',input().strip())
#print(m.group(1) if m else -1)
m = re.findall(r"([A-Za-z0-9])\1+",input())
print(m[1])



