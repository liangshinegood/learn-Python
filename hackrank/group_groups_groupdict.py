
# �ӶԷ��ṩ�ģ�group,groups,groupdic����

# ��������ģ�飬�������ж�

import re
#m = re.search(r'(a-zA-Z0-9)\1+',input().strip())
#print(m.group(1) if m else -1)
m = re.findall(r"([A-Za-z0-9])\1+",input())
print(m[1])



