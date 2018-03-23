#使用datetime.strptime 转化日期类型，将其统一
#相减，用total_seconds计算秒数


import sys
from datetime import datetime


def time_delta(t1,t2):
    ta = datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    tb = datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    return int(abs((ta-tb).total_seconds()))


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1,t2)
        print(delta)


