# 准确的说也是属于知道规则判断是否正确的一类
# 通常判断这一类基本用re,正则方法

import re
test = re.compile(r"^"
        r"(?!.*(\d)(-?\1){3})"
        r"[456]"#以4，5or 6开头
        r"\d{3}"
        r"(?:-?\d{4}){3}"
        r"$")
for _ in range(int(input().strip())):
    print("Valid" if test.search(input().strip()) else "Invalid")




