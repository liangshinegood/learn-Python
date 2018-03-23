# 本质上也是数字的判断，可以用re模块

import re

print(bool(re.match(r'^'
    r'(?!.*(.).\1.*(.).\2)'
    r'(?!.*(.)(.)\3\4)'
    r'[1-9]\d{5}'
    r'$',input())))



