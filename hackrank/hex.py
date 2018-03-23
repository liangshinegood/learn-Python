#思路：问题：取css中的颜色数据，要排除那些非颜色#开头的内容
# 用正则表达式的方式

import re
for i in range(int(input())):
    matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})',input())
    if matches:
        print(*matches,sep='\n')


